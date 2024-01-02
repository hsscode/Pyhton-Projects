import os.path
import io
import requests
from PIL import Image



class Character:
    def __init__(self, name, gender, species, origin, status, image_url, number_of_episodes):

        self.name= name
        self.gender=gender
        self.species= species
        self.origin= origin
        self.status= status
        self.image_url= image_url
        self.number_of_episodes= number_of_episodes
        self.image_name=self.name.replace(' ', '')+'.png'
        self.image_path ='./images/'+self.image_name
        self.download_image()  #it will check if imager is downloaded or not 


    def show_character(self):
        print(self.name, self.gender, self.status)   ## created new method to store images

    def download_image(self): 

        # check if image doesnt exit then download
        if not os.path.exists(self.image_path):

            response= requests.get(self.image_url)
            image_data= response.content
            image= Image.open(io.BytesIO(image_data))
            #resize of image 

            image=image.resize((200,200),Image.LANCZOS)
            image.save(self.image_path)

            print(self.name, 'Is downloaded')

    def get_image(self):
        return Image.open(self.image_path)
