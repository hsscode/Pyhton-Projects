import requests
from tkinter import * ## used for app
from PIL import Image, ImageTk
from scrollablee import ScrollableFrame
from character import Character

def load_data():


    url= 'https://rickandmortyapi.com/api/character/?page=1'

    response=requests.get(url)

    json_res= response.json()

    ## now i want to print name only from json from result(it isin json)

    json_res_result= json_res['results']

    characters=[]

    for obj in json_res_result:
        name= obj['name']
        gender= obj['gender']
        species= obj['species']
        origin= obj['origin']['name']
        status= obj['status']
        image_url= obj['image']
        number_of_episodes= len(obj['episode'])
        character= Character(name,  gender,species, origin, status,image_url,number_of_episodes)
        characters.append(character)
    return characters


characters=load_data()


## Now creating UI 
root= Tk()  #this is going to be a main window 
root.title('Rick and marty')  #this is going to be a title

root.geometry('535x560')

root.resizable(0,0)   #to avoid resiable 

root.update()

scrollable= ScrollableFrame(root)

for char in characters:
##  main item frame for each characters 

    list_item_frame= Frame(scrollable.scrollable_frame, borderwidth= 4, relief= GROOVE )

    list_item_frame.pack(fill= X, padx= 7.5 )


    #left frame

    left_frame= Frame(list_item_frame)
    #load the image 
    photo= ImageTk.PhotoImage(char.get_image())
    img_lbl= Label(left_frame, image=photo)
    img_lbl.image= photo

    img_lbl.pack(fill= BOTH, expand=True)


    left_frame.grid(row=0, column=0, padx=7.5, pady= 15 )

    #right frame


    right_frame= Frame(list_item_frame)
    right_frame.grid(row=0, column=1,   sticky='we' )


    #labels 

    Label(right_frame, text='Name: '+ char.name,font= ("calibri", 12), padx= 7.5 ).pack(anchor=W, expand=True) #anchor =w for west side 
    Label(right_frame, text='Gender: ' + char.gender,font= ("calibri", 12), padx= 7.5 ).pack(anchor=W, expand=True) #anchor =w for west side 
    Label(right_frame, text='Species: '+ char.species,font= ("calibri", 12), padx= 7.5 ).pack(anchor=W, expand=True) #anchor =w for west side 
    Label(right_frame, text='Origin: '+ char.origin,font= ("calibri", 12), padx= 7.5 ).pack(anchor=W, expand=True) #anchor =w for west side 
    Label(right_frame, text='Status: '+ char.status,font= ("calibri", 12), padx= 7.5 ).pack(anchor=W, expand=True) #anchor =w for west side 
    Label(right_frame, text= str(char.number_of_episodes)+ ' Episodes',font= ("calibri", 12), padx= 7.5 ).pack(anchor=W, expand=True) #anchor =w for west side 


scrollable.pack(fill= BOTH, expand= True)
root.mainloop()  #differenct character will be downloaded first then ui will be open 

