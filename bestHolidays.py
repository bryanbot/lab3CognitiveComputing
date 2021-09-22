from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential("")
    text_analytics_client = TextAnalyticsClient(
            endpoint="", 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def sentiment_analysis_example(client):

    documents = ['''
        En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer.
    ''']
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

'''
Opinion Mining - Sentimiento con la minería de opiniones
'''
def sentiment_analysis_with_opinion_mining_example(client):

    documents = [
        "En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer."
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
'''
END
'''

'''
Detección de idiomas
'''
def language_detection_example(client):
    try:
        documents = ["En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer."]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))
language_detection_example(client)
'''
END
'''
'''
Reconocimiento de entidades con nombre (NER)
'''
def entity_recognition_example(client):

    try:
        documents = ["En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer."]
        result = client.recognize_entities(documents = documents)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")

    except Exception as err:
        print("Encountered exception. {}".format(err))
entity_recognition_example(client)
'''
END
'''
'''
Reconocimiento de la información de identificación personal
'''
def pii_recognition_example(client):
    documents = [
        '''
        En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer.
        '''
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
'''
END
'''
'''
Vinculación de entidad
'''
def entity_linking_example(client):

    try:
        documents = ["""En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer."""]
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
'''
END
'''
'''
Extracción de la frase clave
'''
def key_phrase_extraction_example(client):

    try:
        documents = ["En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer."]

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
        En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer.
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
'''
'''
END
'''