import os
import time
def tomp3():
    # Open a file
    path = r'C:/Users/edgar/Desktop/Proyects Juanma/Python Proyects/Others/VideoDownload/Musics'

    with os.scandir(path) as dirs:
        for entry in dirs:
            base = os.path.splitext(entry.name)[0]
            if not entry.name.endswith('.mp3'):
                os.rename(path + '/' + entry.name, path + '/' + base + '.mp3',)


    print('Renombracion finalizada.\n')
    time.sleep(3)