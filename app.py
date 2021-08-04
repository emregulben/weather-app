from flask import Flask, render_template, request, url_for
import weather_test as mymodel

#import weather_vgg_test as vgg
#import weather_mobilenet_test as mobilenet


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def weather():
    #predi = "None"
    if request.method == "POST":
        image = request.files['img']
        image_path = "./images/" + image.filename
        image.save(image_path)
        (ind, percentage) = mymodel.predict_weather(image_path)
        percentage = round(percentage, 2)
        if ind == 0:
            pred = "Cloudy"
        elif ind == 1:
            pred = "Rainy"
        elif ind == 2:
            pred = "Shiny"
        elif ind == 3:
            pred = "Sunrise"

        return render_template("index.html", pred=pred, percentage=percentage)
    else: 
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)