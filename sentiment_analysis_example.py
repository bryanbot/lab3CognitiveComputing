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

    documents = ["La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea. Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de exopositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos. El país sufre la campaña con mayor polarización del periodo democrático de los últimos 20 años. Pero la tensión fundamental que nos separa no está en relación a “el comunismo versus la democracia”. Está en la relación de quienes votan con la inclusión en el modelo económico y político, más aún tras los estragos que ha generado la pandemia. No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública."]
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