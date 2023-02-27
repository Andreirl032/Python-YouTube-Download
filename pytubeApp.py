import pytube
import urllib.request
import PySimpleGUI as sg

def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

layout = [
    [sg.Text("DOWNLOAD DE COMPONENTES DO YOUTUBE")], 
    [sg.Combo(["Vídeo","Áudio","Thumbnail"],default_value="",key="-COMBO-",readonly=True)],
    [sg.Text("Insira link para baixar vídeo do youtube")], 
    [sg.In(size=(25, 1), enable_events=True, key="-INPUTLINK-")],
    [sg.Text("Insira o nome do arquivo")], 
    [sg.In(size=(25, 1), enable_events=True, key="-INPUTFILENAME-",disabled=True)],
    [sg.Checkbox('Baixar o arquivo com o nome sendo o título do vídeo', default=True,key="-CHECKBOX-",enable_events=True)],
    [sg.Button("OK",key="-BUTTON-")],
    [sg.Text("",key="-ERRORTEXT-")]
    ]

# Create the window
window = sg.Window(title="Python YouTube downloader - By Andrei", layout=layout,margins=(500,300))
flag=True
# Create an event loop
while True:
    event, values = window.read()

    # print(event)

    if event == sg.WIN_CLOSED:
        break
    if values["-CHECKBOX-"]==True:
        window["-INPUTFILENAME-"].update(disabled=True,text_color="gray")
    elif values["-CHECKBOX-"]==False:
        window["-INPUTFILENAME-"].update(disabled=False,text_color="black")
    if event=="-BUTTON-" and values["-COMBO-"]!="":
        try:
            defaultfilename=None
            if values["-CHECKBOX-"]==False:
                if values["-COMBO-"]=="Vídeo":
                    defaultfilename=values["-INPUTFILENAME-"]+'.mp4'
                elif values["-COMBO-"]=="Áudio":
                    defaultfilename=values["-INPUTFILENAME-"]+'.mp3'
                elif values["-COMBO-"]=="Thumbnail":
                    defaultfilename=values["-INPUTFILENAME-"]
            link=values["-INPUTLINK-"]
            yt=pytube.YouTube(link)
            imglink=yt.thumbnail_url.replace("sddefault","maxresdefault")
            action=""
            if values["-COMBO-"]=="Vídeo":
                yt.streams.get_highest_resolution().download(filename=defaultfilename)
                action="vídeo MP4 de"
            elif values["-COMBO-"]=="Áudio":
                if defaultfilename==None:
                    defaultfilename=yt.title+'.mp3'
                yt.streams.filter(only_audio=True).first().download(filename=defaultfilename)
                action="áudio MP3 de"
            elif values["-COMBO-"]=="Thumbnail":
                if defaultfilename==None:
                    defaultfilename=yt.title
                filepath="C:/Users/andre/Downloads/Python YT Download/"
                download_image(imglink,filepath,defaultfilename)
                action="thumbnail JPG de"
        except Exception as err:
            window["-ERRORTEXT-"].update("Ocorreu um erro, possivelmente um link inválido. Tente novamente.")
            print(err)
        else:
            window["-ERRORTEXT-"].update(f'Você baixou {action} {link}')

window.close()