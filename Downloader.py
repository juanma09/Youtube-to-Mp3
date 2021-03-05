import Tomp3
import pafy
import time
import urllib.request
import os
import re
import tkinter


def confirm(text, mensajedespedida):
    siono = input(text+'\n')
    if siono.lower() == 'sí' or siono.lower() == 'si':
        print('Ok\n')
    elif siono.lower() == 'no':
        print(mensajedespedida)
        time.sleep(3)
        quit()
    else:
        print('Si desea continuar inserte "sí" y si no inserte "no"')
        confirm('', mensajedespedida)

def insertIndex(audiostreams):
    downloadFolder = os.getcwd() + '/Musics'
    m = input('Inserte Aqui:')
    try:
        int(m)
    except:
        print('Por favor inserte un nro valido')
        insertIndex(audiostreams)
    try:
        if int(m) in range(len(audiostreams) + 1):
            print('Descargando...')
            audiostreams[int(m) - 1].download(filepath=downloadFolder)
        elif int(m) == 0:
            print('Descargando...')
            bestaudio = video.getbestaudio()
            bestaudio.download(filepath=downloadFolder)
        else:
            print('Inserte un nro valido')
            insertIndex(audiostreams)
    except:
        pass
    try:
        Tomp3.tomp3()
    except:
        os.remove(downloadFolder + '/' + audiostreams[0].title + '.' + 'mp3')
        Tomp3.tomp3()

def getVidID(search):
    text = str(search).split()
    url = ''
    for i in text:
        url = url + i + '+'
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+ url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(video_ids[0])
    return video_ids[0]

def download(ID):
    url = 'https://www.youtube.com/watch?v=' + str(ID)
    video = pafy.new(url)
    audiostreams = video.audiostreams
    downloadFolder = 'C:/Users/edgar/Desktop/Proyects Juanma/Python Proyects/Others/VideoDownload/Musics'

    for i in audiostreams:
        print('%s bitrate: %s, ext: %s, size %0.2fMb' % (audiostreams.index(i)+1, i.bitrate, i.extension, i.get_filesize()/1024/1024))

    #print('\nInserte el indice del video que quiera descargar:\n'
    #          'O inserte "0" si quiere descargar el mejor audio posible(Recomendado)\n'
    #          '(En caso de no funcionar o el archivo se corrompa pruebe la opcion 1)\n')

    bestaudio = video.getbestaudio()
    bestaudio.download(filepath=downloadFolder)
    descargaCompleta = tkinter.Label(tab, text = "Descarga Completa")
    descargaCompleta.pack()
    #var = insertIndex(audiostreams= audiostreams)
    print('Descarga completada')

def getTitle(entry):
    ID = getVidID(entry)
    url = 'https://www.youtube.com/watch?v=' + str(ID)
    video = pafy.new(url)
    audiostreams = video.audiostreams
    x = tkinter.Label(tab, text = audiostreams[0].title)
    x.pack()
    downloadButton = tkinter.Button(tab, text = "Descargar", command = lambda :download(ID))
    downloadButton.pack()




tab = tkinter.Tk()

tab.geometry("400x300")

label = tkinter.Label(tab, text = "Inserte el nombre o URL del video que desee descargar")
label.pack()

Entry = tkinter.Entry(tab)
Entry.pack()

label1 = tkinter.Label(tab)
label1.pack()

boton1 = tkinter.Button(tab, text="Buscar", command=lambda: getTitle(Entry.get()),padx = 20, pady = 10)
boton1.pack()



tab.mainloop()
