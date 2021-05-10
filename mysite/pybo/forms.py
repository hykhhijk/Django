from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content': '답변내용'}


# 위와 같은 클래스의 형태를 장고 폼이라한다!

