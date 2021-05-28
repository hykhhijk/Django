from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),           #question_id가 매핑되어 views.detail실행
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
]

#MTV + 이 부분을 좀 더 파보아야할듯 -> <int: ~ >이런 문법은 어디서 나온건지  등등