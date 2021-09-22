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
    En el colegio me fue bien, hice muchos amigos y además me divertí mucho. No tenía las mejores calificaciones ni era un alumno, me podría considerar como un alumno promedio. Lo que más me gustaba del colegio eran los talleres, en aquel entonces llevaba un taller de electricidad donde aprendí a usar un protoboard, leer esquemas eléctricos a nivel básico y usar circuitos integrados. La mejor navidad que he tenido ha sido en Ica, donde me encuentro con toda mi familia, se prepara una buena comida y la familia cuenta anécdotas por las que hayan pasado durante el año o en años pasados. Finalmente, mis mejores vacaciones fueron en Cusco, estuve cerca de una semana y media y tuve la oportunidad de conocer lugares como Macchu Pichu, Aguas Calientes, Ollantaytambo, Maras, Sacsayhuamán, Pisac, Coricancha. Cusco es una ciudad bellísima que tiene muchos lugares por conocer.
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
    with open("aboutMe.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "aboutMe.mp3"')
    # [END tts_quickstart]


if __name__ == "__main__":
    run_quickstart()