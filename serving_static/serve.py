from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
@app.route("/")

#def get_total_faces():
   # cwd = os.getcwd()
  #  img_folder_path = cwd + '\serving_static\static\people'
 #   dirListing = os.listdir(img_folder_path)
#    return len(dirListing)
def get_faces(covidcases):
    i=1
    while i<covidcases:
        if i == 1:
            faces="<img src = /static/people/person" + str(i) + ".jpg alt = helo>"
        else:
            faces = faces + "<img src = /static/people/person" + str(i) + ".jpg alt =" + str(i) +">"
        i = i + 1
    return faces

def pass_to_index():
    total_count = 10
    faces=get_faces(total_count)
    return render_template('index.html', faces=faces, message=str(total_count))
if __name__ == "__main__":
    app.run(debug=True)