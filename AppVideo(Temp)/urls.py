from django.urls import path

from . import views

app_name= 'AppVideo'

urlpatterns = [
    # path('', views.videolist, name='videolist'),
    path('', views.VideoList.as_view(), name='videolist'),
    path('upload-video/', views.UploadVideo.as_view(), name='uploadvideo'),
    path('details/<slug:slug>', views.VideoDetails, name='videodetails'),
    # path('liked/<pk>/', views.liked, name='liked_video'),
    # path('unliked/<pk>/', views.unliked, name='unliked_video'),
    # path('my-videos/', views.MyVideos.as_view(), name='myvideo'),
    # path('edit/<pk>/', views.UpdateVideo.as_view(), name='editvideo'),
]