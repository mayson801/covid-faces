from flask import Flaskfrom flask import render_templatefrom get_images import get_images_from_website# creates a Flask application, named appapp = Flask(__name__)# a route where we will display a welcome message via an HTML template@app.route("/")def pass_to_index():    total_count = get_total_faces()    faces=get_faces(total_count)    return render_template('index.html', faces=faces, message=str(total_count))def get_total_faces():    import os    img_folder_path = 'D:\covid_faces\serving_static\static\people'    dirListing = os.listdir(img_folder_path)    return len(dirListing)def get_faces(covidcases):    i=1    while i<covidcases:        if i == 1:            faces="<img src = /static/people/person" + str(i) + ".jpg alt = helo>"        else:            faces = faces + "<img src = /static/people/person" + str(i) + ".jpg alt =" + str(i) +">"        i = i + 1    return faces# run the applicationif __name__ == "__main__":    app.run(debug=True)