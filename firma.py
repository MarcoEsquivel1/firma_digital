import base64
from hmac import digest
from inspect import signature
from msilib.schema import Signature
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

def firmar(mensaje):
    with open('ClavePrivada.txt') as f:
        key=f.read()
        rsakey=RSA.importKey(key)
        signer=Signature_pkcs1_v1_5.new(rsakey)

        digest=SHA.new()
        digest.update(mensaje)
        print("Contenido del documento", mensaje)
        print("Se genero el hash", digest.hexdigest())

        sign=signer.sign(digest)
        signature=base64.b64encode(sign)

    with open('firma.txt', 'wb') as fp1:
        fp1.write(signature)
        fp1.close()

    print("firma creada", signature)
    print("firma guardada en: firma.txt")

    return signature

""" Codigo agregado: se piden los datos a firmar y se guardan en datos.txt """

texto = input("Introduzca el texto a firmar: ")
with open("datos.txt", "w") as data:
    data.write(texto)


with open("datos.txt", "r") as f1:
    mensaje=f1.read()

mensaje=mensaje.encode()
signature=firmar(mensaje)