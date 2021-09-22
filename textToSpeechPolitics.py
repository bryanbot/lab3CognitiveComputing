#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python quickstart.py
"""

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'D:\Descargas\exalted-altar-326415-adb1aaf81af0.json'

def run_quickstart():
    # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech
    

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text='''
    La política peruana ha apostado todas sus monedas por la candidatura de Keiko Fujimori. Políticos con muchos minutos como entrevistados en televisión —pero escasos votos en las últimas contiendas— hablan de ella como si representara una esperanza similar a Barack Obama para Estados Unidos en 2008, y no estuviera siendo investigada por lavado de activos en el Caso Odebrecht y tuviera responsabilidad gravitante en la crisis política de los últimos años. “Keiko Fujimori representa la libertad y el progreso; y creo que el señor (Pedro) Castillo representa la dictadura”, dijo el escritor Mario Vargas Llosa en esa misma línea.

Fujimori ha recibido el respaldo de líderes empresariales, de la mayoría de los partidos políticos, de políticos sin partidos, de ex opositores, de los Vargas Llosa, todos defensores del modelo económico actual. Ninguno de ellos le ha exigido que desista de su intención de indultar a su padre, el expresidente Alberto Fujimori, condenado a prisión por corrupción y por ser autor mediato de homicidio calificado en las matanzas de La Cantuta y Barrios Altos.

No juzgo a los votantes de uno y otro candidato, pues tienen argumentos de peso, ya que ambos producen temores fundamentados. Lo que resulta criticable es la actitud y la argumentación de los líderes políticos que, debiendo comprender la crisis de representatividad que hay en el país, se han unido a causas con una ceguera que nos puede arrastrar a un peligroso escenario de política sin interlocutores. Pues en serio, ¿qué importancia le pueden dar los grandes perdedores de la crisis sanitaria a la vigilancia democrática de Álvaro Vargas Llosa? Este 6 de junio no solo se decidirá la continuidad del modelo económico, sino también será un referéndum sobre la vigencia de las élites políticas que dominan la opinión pública.

    ''')

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("politicsOpinion.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "politicsOpinion.mp3"')
    # [END tts_quickstart]


if __name__ == "__main__":
    run_quickstart()