from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = ""
endpoint = ""

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
'''
END - Quickstart variables
'''
'''
Detect Faces - local
This example detects faces in a local image, gets their gender and age, 
and marks them with a bounding box.
'''
print("===== Detect Faces - local =====")
# Open local image
local_image_path = os.path.join (images_folder, "Tipos-de-estudiantes-cual-eres-tu.jpg")
local_image = open(local_image_path, "rb")

# Select visual features(s) you want
local_image_features = ["faces"]
# Call API with local image and features
detect_faces_results_local = computervision_client.analyze_image_in_stream(local_image, local_image_features)

# Print results with confidence score
print("Faces in the local image: ")
if (len(detect_faces_results_local.faces) == 0):
    print("No faces detected.")
else:
    for face in detect_faces_results_local.faces:
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))
print()
'''
END - Detect Faces - local
'''