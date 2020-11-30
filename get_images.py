import requests
from PIL import Image
import time
import os
import shutil


def get_total_faces():
   img_folder_path = file_directory + '/serving_static/static/people'
   dirListing = os.listdir(img_folder_path)
   return len(dirListing)

def get_total_faces_temp():
   img_folder_path = file_directory + '/serving_static/static/people'
   dirListing = os.listdir(img_folder_path)
   return len(dirListing)-1

def get_images_from_website(newcases,images_generated):

   i=0
   while i!=newcases:
      i=i+1
      images_generated = images_generated + 1

      print(images_generated)
      img_data = requests.get("https://thispersondoesnotexist.com/image").content
      with open(file_directory + '/serving_static/static/-temp/person'+str(images_generated)+'.jpg', 'wb') as handler:
         handler.write(img_data)
      foo = Image.open(file_directory + "/serving_static/static/-temp/person" + str(images_generated) + ".jpg")
      foo = foo.resize((120,120),Image.ANTIALIAS)
      foo.save(file_directory + "/serving_static/static/-temp/person" + str(images_generated) + ".jpg",optimize=True,quality=80)
      time.sleep(2)
def move_images(image_number):
   shutil.move(file_directory + "/serving_static/static/-temp/person" + str(image_number) + ".jpg", file_directory + "/serving_static/static/people/person" + str(image_number) + ".jpg")
def newcases():
   newcase_number=10
   return newcase_number


def main():
   total_faces = get_total_faces()
   total_to_move = get_total_faces_temp()
   i= 1
   get_images_from_website(newcases(),total_faces)
   while i <= total_to_move:
      move_images(total_faces+i)
      i=i+1
   print()

if __name__ == "__main__":
   file_directory = (os.getcwd())
   main()
