from django.urls import path, include
from socialize_app import views

urlpatterns = [
    path('',views.signIn, name='signin'),
    path('signup/', views.signUp, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('showpost/', views.showPost, name='showpost'),
    path('uploadpost/', views.uploadPost, name='uploadpost'),
    path('home/', views.home, name='home'),
    path('likepost/<slug:pk>', views.likePost, name='likepost'),
    path('unlike/<slug:pk>', views.unlike, name='unlike'),
    path('commentpost/<slug:pk>', views.commentPost, name='commentpost')
]