from django.urls import path
from review import views

app_name = 'review'

urlpatterns = [
    path('', views.review_list, name='review_list'), #홈  http://127.0.0.1:8000/board
    path('<int:review_id>/', views.review_detail, name='review_detail'),    #리뷰상세  http://127.0.0.1:8000/board/?숫자
    path('review/create/', views.review_create, name='review_create'),      #리뷰생성
    path('answer/create/<int:review_id>/', views.answer_create, name='answer_create'),  #리뷰 답변
]