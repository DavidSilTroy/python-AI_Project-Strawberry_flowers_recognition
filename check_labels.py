import os
import sys
cwd = os.getcwd()

foldersName = [
    './yolo/data',
    './yolo/data/train',
    './yolo/data/val',
    './yolo/data/train/images',
    './yolo/data/train/labels',
    './yolo/data/val/images',
    './yolo/data/val/labels',
]

files_extensions = [
    '.jpg',
    '.png',
    '.JPG',
    '.PNG',
]

#Checking all the folder existes
for folder in foldersName:
    if not os.path.isdir(folder):
        print(f'Folder {folder} not exist')
        sys.exit()

#getting the list of files from the folders
train_imgs = os.listdir(foldersName[3])
train_lbls = os.listdir(foldersName[4])
val_imgs = os.listdir(foldersName[5])
val_lbls = os.listdir(foldersName[6])




#Checking if the image has its label
def checkImageWithLabel(images_list, labels_list):

    #removing extension from images to compare them with the labels
    for fileExt in files_extensions:
        images_list = [img.replace(fileExt,'') for img in images_list]
    
    #to count how many labels from images are found
    img_c = 0
    good_lbls = [] #To be sure the labels are from the current images

    for img in images_list:
        count = 0
        for lbl in labels_list:
            if img == lbl.replace('.txt',''):
                count+=1
        
        if count == 1:
            img_c = img_c +1
            good_lbls.append(img+'.txt')

        if count <1:
            path = './yolo/data/removed'
            print(f'not label for {img}')
            if not os.path.exists('./yolo/data/removed'):
                os.makedirs(path)

            for fileExt in files_extensions: 
                if os.path.exists(foldersName[3]+'/'+img+fileExt):
                    print('Train image removed since there is not label for it')
                    os.replace(foldersName[3]+'/'+img+fileExt, './yolo/data/removed/'+img+fileExt)
                if os.path.exists(foldersName[5]+'/'+img+fileExt):
                    os.replace(foldersName[5]+'/'+img+fileExt, './yolo/data/removed/'+img+fileExt)
                    print('Validation image removed since there is not label for it')
            
        if count >1:
            print(f'more than 1 label for {img}, why?')
        
    if len(good_lbls) != len(labels_list):
        print('Some labels need to be remove')
        for lbl in labels_list:
            count = 0
            for g_lbl in good_lbls:
                if lbl == g_lbl:
                    count+=1

            if count <1:
                path = './yolo/data/removed'
                print(f'not image for {lbl}')
                if not os.path.exists('./yolo/data/removed'):
                    os.makedirs(path)
                if os.path.exists(foldersName[4]+'/'+lbl):
                    os.replace(foldersName[4]+'/'+lbl, './yolo/data/removed/'+lbl)
                    print('One train label removed since there is not image for it')
                if os.path.exists(foldersName[6]+'/'+lbl):
                    os.replace(foldersName[6]+'/'+lbl, './data/removed/'+lbl)
                    print('One validation label removed since there is not image for it')

    print(f'Images {img_c}/{len(images_list)} ')

print('Checking train data')
checkImageWithLabel(train_imgs, train_lbls)
print('Checking validation data')
checkImageWithLabel(val_imgs, val_lbls)
