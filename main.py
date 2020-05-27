from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import date
import os, json, time, sys

today = str(date.today())

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self,event):
        for filename in os.listdir(folder):
            subject = filename.split("_")
            subject = subject[0]
            print(subject)
            ext = filename.split(".")
            ext = ext[1]

            if subject == "ALG":
                alg_folder = destination+"/FAE/Algoritmos de Programação/"
                path_base = alg_folder + today 
                
                if ext == "c" or ext == "cpp" or ext == "exe" or ext == "zip":
                    path = path_base + "/Códigos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

                else:
                    path = path_base + "/Documentos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

            if subject == "INT":
                int_folder = destination+"/FAE/Introdução a Tecnologias/"
                path_base = int_folder + today 
                
                if ext == "css" or ext == "html" or ext == "exe" or ext == "zip":
                    path = path_base + "/Códigos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

                else:
                    path = path_base + "/Documentos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

            if subject == "LOG":
                log_folder = destination+"/FAE/Lógica/"
                path_base = log_folder + today 
                
                if ext == "c" or ext == "cpp" or ext == "exe" or ext == "zip":
                    path = path_base + "/Códigos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

                else:
                    path = path_base + "/Documentos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

            if subject == "PRD":
                parag_folder = destination+"/FAE/Paradigmas de Programação/"
                path_base = parag_folder + today 
                
                if ext == "c" or ext == "cpp" or ext == "exe" or ext == "zip" or ext == "pas":
                    path = path_base + "/Códigos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

                else:
                    path = path_base + "/Documentos/"

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    src = folder + filename
                    new_destination = path + filename
                    os.rename(src, new_destination)

folder = "/Users/costa/Desktop/FolderMatic/"
destination = "/Users/costa/Desktop/Projetos Atuais"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

