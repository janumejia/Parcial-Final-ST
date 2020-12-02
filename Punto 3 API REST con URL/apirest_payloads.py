# coding=utf-8
#import time
import requests
#import math
#import random


# MÉTODO PARA CONSULTAR LIBROS
def get_request(): 
    url = "http://192.168.60.3:5000/books"

    req = requests.get(url=url)
    # Processes results
    status = req.status_code
    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    print(req.text)
    return True

# MÉTODO PARA AGREGAR LIBRO NUEVO
def post_request(): #Nuevo
    # Creates the headers for the HTTP requests
    url = "http://192.168.60.3:5000/books"
    headers = {"Content-Type": "application/json"}

    # Makes the HTTP requests
    #while status >= 400 and attempts <= 5: #Original
    #while status >= 400:
    
    identificador = raw_input('Ingrese ID ')
    title = raw_input('Ingrese Titulo ')
    description = raw_input('Ingrese Descripción ')
    author = raw_input('Ingrese Autor ')

    payload = {
        "description": description,
        "author": author,
        "title": title
    }

    req = requests.post(url=url, headers=headers, json=payload)
    status = req.status_code
        #attempts += 1
        #time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    return True


# MÉTODO PARA MODIFICAR LIBRO EXISTENTE
def put_request():
    identificador = raw_input('Ingrese ID del libro modificar: ')
    url = "http://192.168.60.3:5000/books/" + str(identificador)

    headers = {"Content-Type": "application/json"}
    
    title = raw_input('Ingrese Titulo ')
    description = raw_input('Ingrese Descripción ')
    author = raw_input('Ingrese Autor ')

    payload = {
        "author": author,
        "description": description,
        "title": title
    }

    req = requests.put(url=url, headers=headers, json=payload)

    # Processes results
    status = req.status_code
    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    return True


# MÉTODO PARA BORRAR UN LIBRO
def delete_request():
    identificador = raw_input('Ingrese ID de libro a borrar: ')
    url = "http://192.168.60.3:5000/books/" + str(identificador)
    
    headers = {"Content-Type": "application/json"}
    req = requests.delete(url=url)

    # Processes results
    status = req.status_code
    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    return True



def main():
    #El usuario digita el método a realizar 
    metodo = raw_input('Método: ').upper()

    if metodo == "POST":
        print("Método POST")
        post_request()
        #print("Método post_request finalizado")
    elif metodo == "GET":
        print("Método GET")
        get_request()
        #print("Método get_request finalizado")
    elif metodo == "PUT":
        print("Método PUT")
        put_request()
        #print("Método put_request finalizado")
    elif metodo == "DELETE":
        print("Método DELETE")
        delete_request()
        #print("Método delete_request finalizado")
    else:
        print("¡El método digitado no es valido!")

if __name__ == '__main__':
    i=0
    while (i<5):
        main()
        i = i+1