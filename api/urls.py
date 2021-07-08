from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.Userlist.as_view()),
    path('users/<int:pk>/', views.Userdetail.as_view()),
    path('articles/', views.Articlelist.as_view()),
    path('articles/<int:pk>/', views.Articledetail.as_view()),
    path('articlesbyuser/<int:pk>/',views.ViewArticleByUserView.as_view()),
    path('usersbyviews/',views.UserViewList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
