from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential("")
    text_analytics_client = TextAnalyticsClient(
            endpoint="", 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

print("----------------------------------------------------------------")
def sentiment_analysis_example(client):

    documents = ["La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."]
    response = client.analyze_sentiment(documents=documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))
          
sentiment_analysis_example(client)
print("----------------------------------------------------------------")
'''
Opinion Mining - Sentimiento con la minería de opiniones
'''
def sentiment_analysis_with_opinion_mining_example(client):

    documents = [
        "La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."
    ]

    result = client.analyze_sentiment(documents, show_opinion_mining=True)
    doc_result = [doc for doc in result if not doc.is_error]

    positive_reviews = [doc for doc in doc_result if doc.sentiment == "positive"]
    negative_reviews = [doc for doc in doc_result if doc.sentiment == "negative"]

    positive_mined_opinions = []
    mixed_mined_opinions = []
    negative_mined_opinions = []

    for document in doc_result:
        print("Document Sentiment: {}".format(document.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            document.confidence_scores.positive,
            document.confidence_scores.neutral,
            document.confidence_scores.negative,
        ))
        for sentence in document.sentences:
            print("Sentence: {}".format(sentence.text))
            print("Sentence sentiment: {}".format(sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))
            for mined_opinion in sentence.mined_opinions:
                target = mined_opinion.target
                print("......'{}' target '{}'".format(target.sentiment, target.text))
                print("......Target score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                    target.confidence_scores.positive,
                    target.confidence_scores.negative,
                ))
                for assessment in mined_opinion.assessments:
                    print("......'{}' assessment '{}'".format(assessment.sentiment, assessment.text))
                    print("......Assessment score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                        assessment.confidence_scores.positive,
                        assessment.confidence_scores.negative,
                    ))
            print("\n")
        print("\n")
          
sentiment_analysis_with_opinion_mining_example(client)
print("----------------------------------------------------------------")
'''
END
'''

'''
Detección de idiomas
'''
def language_detection_example(client):
    try:
        documents = ["La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))
language_detection_example(client)
print("----------------------------------------------------------------")
'''
END
'''
'''
Reconocimiento de entidades con nombre (NER)
'''
def entity_recognition_example(client):

    try:
        documents = ["La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."]
        result = client.recognize_entities(documents = documents)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")

    except Exception as err:
        print("Encountered exception. {}".format(err))
entity_recognition_example(client)
print("----------------------------------------------------------------")
'''
END
'''
'''
Reconocimiento de la información de identificación personal
'''
def pii_recognition_example(client):
    documents = [
        "La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."
    ]
    response = client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        print("Redacted Text: {}".format(doc.redacted_text))
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("\tCategory: {}".format(entity.category))
            print("\tConfidence Score: {}".format(entity.confidence_score))
            print("\tOffset: {}".format(entity.offset))
            print("\tLength: {}".format(entity.length))
pii_recognition_example(client)
print("----------------------------------------------------------------")
'''
END
'''
'''
Vinculación de entidad
'''
def entity_linking_example(client):

    try:
        documents = ["""La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."""]
        result = client.recognize_linked_entities(documents = documents)[0]

        print("Linked Entities:\n")
        for entity in result.entities:
            print("\tName: ", entity.name, "\tId: ", entity.data_source_entity_id, "\tUrl: ", entity.url,
            "\n\tData Source: ", entity.data_source)
            print("\tMatches:")
            for match in entity.matches:
                print("\t\tText:", match.text)
                print("\t\tConfidence Score: {0:.2f}".format(match.confidence_score))
                print("\t\tOffset: {}".format(match.offset))
                print("\t\tLength: {}".format(match.length))
            
    except Exception as err:
        print("Encountered exception. {}".format(err))
entity_linking_example(client)
print("----------------------------------------------------------------")
'''
END
'''
'''
Extracción de la frase clave
'''
def key_phrase_extraction_example(client):

    try:
        documents = ["La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        
key_phrase_extraction_example(client)
print("----------------------------------------------------------------")
'''
END
'''
'''
Extracción de entidades de mantenimiento
'''
'''

def health_example(client):
    documents = [
        """
        La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de exopositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. El país sufre la campaña con mayor polarización del periodo democrático de los últimos 20 años. Pero la tensión fundamental que nos separa no está en relación a “el comunismo versus la democracia”. Está en la relación de quienes votan con la inclusión en el modelo económico y político, más aún tras los estragos que ha generado la pandemia. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública.
        """
    ]

    poller = client.begin_analyze_healthcare_entities(documents)
    result = poller.result()

    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("...Normalized Text: {}".format(entity.normalized_text))
            print("...Category: {}".format(entity.category))
            print("...Subcategory: {}".format(entity.subcategory))
            print("...Offset: {}".format(entity.offset))
            print("...Confidence score: {}".format(entity.confidence_score))
        for relation in doc.entity_relations:
            print("Relation of type: {} has the following roles".format(relation.relation_type))
            for role in relation.roles:
                print("...Role '{}' with entity '{}'".format(role.name, role.entity.text))
        print("------------------------------------------")
health_example(client)
print("----------------------------------------------------------------")
'''
'''
END
'''