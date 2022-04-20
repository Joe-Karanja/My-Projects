import os
import tensorflow as tf
from django.apps import AppConfig
from django.conf import settings
import tensorflow_hub as hub
import torch



class DetectapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detectapi'
    #model = tf.keras.models.load_model('C:/Users/bkimathi/Desktop/Crop Disease/Models/20220125-14571643122660-trained-mobinetv5.h5',
     #                              custom_objects={'KerasLayer': hub.KerasLayer})
     
    path_hubconfig = "./app/app/Cropdetection/yolov5"
    path_weightfile = "./app/app/best_2.pt"
            
            
    model = torch.hub.load(path_hubconfig, 'custom',
                               path=path_weightfile, source='local') 

