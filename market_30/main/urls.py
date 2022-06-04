from django.urls import path


from main.views import main_page

from .views import category_sort, product_detail, less_forms, category_form, form_category, form_model

app_name = 'main'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('<int:id>/', category_sort, name='category_sort'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('less_forms/', less_forms, name='less_forms'),
    path('category_form/', category_form, name='category_form'),
    # path('form_product/', form_product, name='form_product'),
    path('form_category/', form_category, name='form_category'),
    path('form_model/', form_model, name='form_model'),
    # path('form_shop/', form_shop, name='form_shop'),
]
