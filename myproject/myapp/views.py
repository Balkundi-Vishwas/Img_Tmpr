from django.http import HttpResponse
from django.shortcuts import render
from keras.models import load_model
import numpy as np
from PIL import Image
# Create your views here.
def welcome(request):
    return render(request,'takeimg.html')

def result(request):
    imgpath=request.GET['myfile']
    modelloaded = load_model('C:/Users/Vishwas/myproject/CNN_model_image_localization1- M1 High Acc.h5')
    image_size = (128, 128)
    def prepare_image(image_path):
        return np.array(Image.open(image_path).convert('RGB').resize(image_size)).flatten() / 255.0
    imgnew=prepare_image("c:/Users/Vishwas/Pictures/"+imgpath)
# imgnew=np.array(imgnew)
    imgnew=imgnew.reshape(1,128,128,3)
    predicted=modelloaded.predict(imgnew)
    print(predicted)
    ress=np.argmax(predicted)
    if(ress==1):
        return render(request,'takeimg.html',{'ress':"Image is authentic"})   
    else:
        return render(request,'takeimg.html',{'ress':"Image had been tampered"})