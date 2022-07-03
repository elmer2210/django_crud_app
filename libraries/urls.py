from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.start, name='init'),
    path('nosotros', views.we, name='we'),
    path('libros', views.books, name="books"),
    path('libros/crear', views.create_book, name="create_book"),
    path('libros/editar', views.edit_book, name="edit_book"),
    path('libros/eliminar/<int:id>', views.delete, name="delete_book"),
    path('libros/editar/<int:id>', views.edit_book, name="edit_book"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
