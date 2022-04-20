from django.shortcuts import render
import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from .forms import ImageUploadForm
from PIL import Image as im
import base64
import tensorflow as tf
import tensorflow_hub as hub

class_labels ={ 0 : 'jute', 1 : 'maize', 2 : 'rice', 3 : 'sugarcane', 4 : 'tomato', 5 : 'wheat'}
tfmodel = tf.keras.models.load_model("./app/app/Cropdetection/Trained Models/2022-03-02-12_07-cropdetectionmodel.h5")
IMG_SIZE = 224

def getcrop(img):
    # turn image into numerical tensors
    image = tf.image.decode_jpeg(img, channels=3)
    # covert colour channel values
    image = tf.image.convert_image_dtype(image, tf.float32)
    # resize image
    image = tf.image.resize(image, size=[IMG_SIZE, IMG_SIZE])
    image = np.expand_dims(image, axis=0)
    pred = tfmodel.predict(image)
    pred_crop = class_labels[np.argmax(pred)]
    return pred_crop,pred


class deploy(APIView):
    

    @staticmethod
    def post(request):
    
        results = None
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
           image = request.FILES.get('image')
        
           img = image.file.read()
        
           #decode image from bytes
           encoded_img = im.open(image)       


           pred_crop , pred = getcrop(img)
           prob = np.max(pred)
           prob = round(prob,2)*100
           


        if pred_crop == 'tomato':
            path_hubconfig = "./app/app/Cropdetection/yolov5"
            path_weightfile = "./app/app/best_2.pt"
            
            
            model = torch.hub.load(path_hubconfig, 'custom',
                               path=path_weightfile, source='local')
            results = model(encoded_img, size=640)
            results.render()
            for img in results.imgs:
                img_base64 = im.fromarray(img)
                img_base64.save("media/yolo_out", format="JPEG")

            inference_img = "/media/yolo_out"
            #results = model(img, size=640)
            results = results.pandas().xyxy[0]
            name= results.name
            conf = round(results.confidence,2)*100
        else:
            return Response({'Crop':pred_crop,'prob':prob})
        

           
           
        return Response({'Crop':pred_crop,'pred':prob,'Disease':name,'Probablity':conf,'image':inference_img})
       