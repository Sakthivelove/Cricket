"""worldcup URL Configuration

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
from ODI import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name="lndex"),
    path("booking",views.booking,name="booking"),
    path("addrecord",views.addrecord,name="addrecord"),
    path("booklist",views.booklist,name="booklist"),
    path('delete/<int:id>', views.delete, name='delete'),
    path("final1",views.final1,name="final1"),
    path("final2",views.final2,name="final2"),
    path("final3",views.final3,name="final3"),  
    path("final4",views.final4,name="final4"),
    path("final5",views.final5,name="final5"),
    path("final6",views.final6,name="final6"),
    path("final7",views.final7,name="final7"),
    path("final8",views.final8,name="final8"),
    path("final9",views.final9,name="final9"), 
    path("final10",views.final10,name="final10"),
    path("final11",views.final11,name="final11"),
    path("final12",views.final12,name="final12"),
    path('get-topics-ajax/',views.get_topics_ajax, name="get_topics_ajax"),
    ]
