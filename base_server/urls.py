from django.contrib import admin
from django.urls import path

import iot_app.views

urlpatterns = [
    path('', iot_app.views.index),
    path('admin/', admin.site.urls),
]
