from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('ciscoapp',views.RouterView)

urlpatterns = [
    #path('router/', router_list),
    path('',include(router.urls))
]
