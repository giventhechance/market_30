from .views import index
from django.urls import path

app_name = 'new_app'

urlpatterns = [
    path('index/', index, name='index'),
    # path('form_1', form_save, name='form_save')
]