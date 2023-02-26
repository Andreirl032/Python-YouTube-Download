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
    [sg.Text("Insira nome para baixar thumbnail do youtube (SE FOR BAIXAR THUMBNAIL)")], 
    [sg.In(size=(25, 1), enable_events=True, key="-INPUTFILENAME-")],
    [sg.Button("OK",key="-BUTTON-")],
    [sg.Text("",key="-ERRORTEXT-")]
    ]

# Create the window
window = sg.Window(title="Python YouTube downloader - By Andrei", layout=layout,margins=(500,300))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event=="-BUTTON-" and values["-COMBO-"]!="":
        try:
            link=values["-INPUTLINK-"]
            yt=pytube.YouTube(link)
            imglink=yt.thumbnail_url.replace("sddefault","maxresdefault")
            action=""
            if values["-COMBO-"]=="Vídeo":
                yt.streams.get_highest_resolution().download()
                action="vídeo MP4 de"
            elif values["-COMBO-"]=="Áudio":
                yt.streams.filter(only_audio=True).first().download()
                action="áudio MP3 de"
            elif values["-COMBO-"]=="Thumbnail":
                filename=values["-INPUTFILENAME-"]
                filepath="C:/Users/andre/Downloads/Python YT Download/"
                download_image(imglink,filepath,filename)
                action="thumbnail JPG de"
            print(f'Você baixou {action}',link)
        except:
            window["-ERRORTEXT-"].update("ERRO. INSIRA UM LINK VÁLIDO")
        else:
            window["-ERRORTEXT-"].update("")

window.close()