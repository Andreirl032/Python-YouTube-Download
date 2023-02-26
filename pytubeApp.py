import pytube
import urllib.request
import cv2

def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

option=int(input("Digite 1 para baixar vídeo e 2 para baixar thumbnail:\n"))
link=str(input("Coloque uma URL de vídeo do Youtube:\n"))
yt=pytube.YouTube(link)
imglink=yt.thumbnail_url
action=""
if option==1:
    yt.streams.filter(file_extension='mp4',only_video=True,res="720p",progressive=True).first().download()
    action=" video from"
elif option==2:
    filename=str(input("Insira nome do arquivo:\n"))
    filepath="C:/Users/andre/Downloads/Python YT Download/"
    download_image(imglink,filepath,filename)
    image = cv2.imread(filepath+filename+'.jpg')
    crop_image = image[60:420, 0:640]
    cv2.imwrite(filename+'.jpg',crop_image)
    action="thumbnail from"
    

print(f'Downloaded{action}',link)