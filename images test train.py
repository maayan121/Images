# -*- coding: utf-8 -*-
"""
A Script that creates two directories named test and train in a particular directory.
Then inserts images into one of the directories (test or train).
@author: Maayan Eliya
"""

import os, shutil
from matplotlib import image
import matplotlib.pyplot as plt


def create_directories():
    """Asks from the user to input a path to the directory.If the input is enter then the path is Desktop.
    Then asks for a directory name, if it doesn't exists then make new directory in path.
    Make two subdirectories named: train, test.
    :param:None
    :return: path train,test
    """
    #path
    first_path=input("Please enter a string represents a path. ")
    if first_path=="": #default = Desktop
        print("אם המחשב שלך בעברית הקלד t")
        print("אם המחשב שלך באנגלית הקלד f")
        flag=input()
        if (flag=='t'): #אם המחשב בעברית
            first_path=os.path.expanduser("~\שולחן העבודה") #Defines the path to be desktop
        else: #אם המחשב באנגלית
            first_path=os.path.expanduser("~/Desktop") #Defines the path to be desktop
        print(first_path)
    
    # Directory 
    directory = input("Please enter a string represents a directory name. ")
    path_directory = create_directory(first_path, directory) # Create directory named 'directory' in first_path 
        
    # Directorys train,test 
    directory_train = "train"
    directory_test = "test"
    path_train=create_directory(path_directory,directory_train) # train - Create the 'train' in 'directory'
    path_test=create_directory(path_directory,directory_test) # test - Create the 'test' in 'directory'
    return(path_train, path_test)


def create_directory (path, directory_name):
    """
    :param: path in which the directory should be, and a string describing the directory name.
    If the directory isn't already exist then make a new directory in the path.
    :return: path of the created directory.
    """
    path1 = os.path.join(path, directory_name) #join the directory_name to the directory path
    # Create directory: directory_name in path1
    try:
        os.makedirs(path1) #make new directory according to path1
        print("Directory '%s' created" %directory_name) 
        print(path1)
    except OSError as error:  
        print(error)   
        print("the directory already exists")
    return path1
        

def transfer_images (sub_path, images_path, pathes):
    """
    :param: the path of the subdirectory (train or test), a string describing the path of a directory with images (jpg).
    If the subdirectory path is the train then 70% of the images in the directory are transferred to train directory.
    If the subdirectory path is the test then all the images are transferred to test.
    :return: None
    """
    images_dirs = os.listdir(images_path) #מכיל רשימה של שמות הקבצים בספרייה שנמצאת במסלול
    if (sub_path==pathes[0]): #if train
        c=0
        images_number=int(0.7*len(images_dirs)) #צריך להעביר 70 אחוז מהתמונות
        for dr in images_dirs:
            if c!=images_number:
                shutil.move(f"{images_path}/{dr}", sub_path) #מעביר את התמונה מהספרייה של התמונות לספרייה של טריין
                c=c+1
    else: #if test
        for dr in images_dirs: #צריך להעביר את כל התמונות
            shutil.move(f"{images_path}/{dr}", sub_path) #מעביר את התמונה מהספרייה של התמונות לספרייה של טסט


def show_images (path):
    """
    :param: the path of the subdirectory in which there are images (jpg).
    Print the image name and shape.
    Show the image in Plots.
    Make a list of all the images' data.
    :return: None
    """
    loaded_images = list() #רשימה שתכיל את המידע של התמונות
    for filename in os.listdir(path): #לכל קובץ ברשימה של הקבצים הנמצאים בספרייה שבמסלול
        # load image
        img_data  =  image.imread (path + '/' + filename) #מכיל את המידע של התמונה
        # store loaded image 
        loaded_images.append(img_data)
        print('>  loaded  %s  %s' %  (filename,  img_data.shape)) #הדפסת שם התמונה והגודל שלה
        plt.imshow(img_data) #display the array of pixels as an image
        plt.show() #מציג את התמונה בפלוטס
    
    
def main():
    pathes=create_directories() #מכיל מסלול של הספרייה טריין ושל הספרייה טסט
    flag=input("train or test? ")
    if flag=="train":
        sub_path=pathes[0]  #sub_path_test => r"C:\Users\maaya\שולחן העבודה\me\train"
    else:
        sub_path=pathes[1]  #sub_path_train=> r"C:\Users\maaya\שולחן העבודה\me\test"
    images_path=r"C:\Users\maaya\OneDrive\שולחן העבודה\images" #נתיב של ספרייה שמכילה תמונות
    transfer_images (sub_path, images_path, pathes) #מעביר את התמונות לספרייה טריין או טסט
    show_images (sub_path) #מציג את התמונות ומדפיס את המידע עליהן

if __name__ == "__main__": 
    main()
    
