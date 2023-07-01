from django.shortcuts import render
from tensorflow import keras
from keras.models import load_model
import os
import numpy as np
from PIL import Image
import base64
import io

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def removal(request):
    return render(request, 'object_removal_page.html')

def splicing(request):
    return render(request, 'splicing_page.html')

def copymove(request):
    return render(request, 'copy-move_page.html')

def quiz(request):
    return render(request, 'quiz_page.html')

def prepare_image(image_path):
    image_size = (128, 128)
    return np.array(image_path.convert('RGB').resize(image_size)).flatten() / 255.0

def result(request):
    if request.method == 'POST':
        img_file = request.FILES['upload']
        img_file = Image.open(img_file)

        img = prepare_image(img_file)
        #print("image shape"+img.shape)
        img = img.reshape(1, 128, 128, 3)

        filepath = os.path.join('myApp', 'static', 'model.h5')
        model = load_model(filepath)
        predicted = model.predict(img)
        print(predicted)
        data = io.BytesIO()
        img_file.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())

        res = np.argmax(predicted)
        if res == 1:
            return render(request,'index.html',{'val': 1, 'res':"Authentic Image", 'img': encoded_img_data.decode('utf-8')})  
        else:
            return render(request,'index.html',{'val': 0, 'res':"Tampered Image", 'img': encoded_img_data.decode('utf-8')})