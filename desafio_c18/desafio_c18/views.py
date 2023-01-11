from django.http   import   HttpResponse
from django.shortcuts   import   render

def hola_mundo ( request ): 
    return   HttpResponse ( 'Viva Cristo' )

def saludo_nombre ( request ,   nombre ):
    return   HttpResponse ( 'Hola {}' . format ( nombre ))

def vista_con_template ( request ): 
    return   render ( request ,   'inicio.html' )