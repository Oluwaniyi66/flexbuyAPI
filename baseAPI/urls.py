from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
]
