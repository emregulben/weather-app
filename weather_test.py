import numpy as np
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


from tensorflow.keras.models import load_model
model = load_model('models/weather_model.h5')


def prepare_image(file):
    img = image.load_img(file, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)

def predict_weather(image):
    preprocessed_image = prepare_image(image)
    predictions = model.predict(preprocessed_image)
    return (np.argmax(predictions), 100 * np.amax(predictions))

#p = predict_weather('images/cloudy5.jpg')
#print(p)


