from polls import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail")
]
