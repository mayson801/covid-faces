from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
@app.route("/")
def pass_to_index():
    total_count = get_total_faces()
    faces=get_faces(total_count)
    return render_template('index.html', faces=faces, message=str(total_count))
def get_total_faces():
    plz=(os.getcwd())
    #for testing on local machine use the line below and comment out img_folder_path
    # this is because file scructure is slightly diffrent on heroku
    #img_folder_path = plz + '/static/people'
    img_folder_path = plz + '/serving_static/static/people'
    dirListing = os.listdir(img_folder_path)
    return len(dirListing)
def get_faces(covidcases):
    i=1
    while i<covidcases:
        if i == 1:
            faces="<img src = /static/people/person" + str(i) + ".jpg alt = helo>"
        else:
            faces = faces + "<img src = /static/people/person" + str(i) + ".jpg alt =" + str(i) +">"
        i = i + 1
    return faces
if __name__ == "__main__":
    app.run(debug=True)