from keras.models import load_model
import numpy as np
from PIL import Image
modelloaded = load_model('C:/Users/Vishwas/myproject/CNN_model_image_localization1- M1 High Acc.h5')
image_size = (128, 128)
def prepare_image(image_path):
    return np.array(Image.open(image_path).convert('RGB').resize(image_size)).flatten() / 255.0
imgnew=prepare_image("C:/Users/Vishwas/Pictures/sun.jpg")
# imgnew=np.array(imgnew)
imgnew=imgnew.reshape(1,128,128,3)
print(np.argmax(modelloaded.predict(imgnew)))
# Create your tests here.
