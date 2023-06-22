from django.shortcuts import render
from keras.models import load_model
import numpy as np
from PIL import Image
import base64
import io

# Create your views here.
def homepage(request):
    return render(request, 'uploadImage.html')

def prepare_image(image_path):
    image_size = (128, 128)
    return np.array(image_path.convert('RGB').resize(image_size)).flatten() / 255.0

def result(request):
    if request.method == 'POST':
        img_file = request.FILES['upload']
        img_file = Image.open(img_file)

        img = prepare_image(img_file)
        img = img.reshape(1, 128, 128, 3)

        model = load_model('G:/DSCE notes/Minor Project 6th Sem/Image_Tamper_Detect/myApp/static/UNet Model.h5')
        predicted = model.predict(img)
        data = io.BytesIO()
        img_file.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())

        res = np.argmax(predicted)
        if res == 1:
            return render(request,'uploadImage.html',{'val': 1, 'res':"Authentic Image", 'img': encoded_img_data.decode('utf-8')})  
        else:
            return render(request,'uploadImage.html',{'val': 0, 'res':"Tampered Image", 'img': encoded_img_data.decode('utf-8')})


