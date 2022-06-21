
#from django.conf.urls import url
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.urls import path
from django.contrib import admin
from todolist.views import todo
from todolist.views import category
from todolist.views import redirect_view

urlpatterns = [

    path('', redirect_view),
    path('admin/', admin.site.urls),
    path('todo/', todo, name="TodoList"),
    path('category/', category, name="Category"),
]