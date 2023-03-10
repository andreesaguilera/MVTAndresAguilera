"""desafio_c18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from desafio_c18.views import hola_mundo
from desafio_c18.views import saludo_nombre
from desafio_c18.views import vista_con_template
from familiares.views import create_familiar
from familiares.views import list_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo ),
    path('nombre/<str:nombre>/', saludo_nombre ),
    path('inicio/', vista_con_template ),

    path('crear-familiar/', create_familiar),
    path('listar-familiar/', list_familiar),

]
