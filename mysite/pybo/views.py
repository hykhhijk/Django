from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm


def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')   #-가 붙어있으므로 작성일시의 역순임
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context)      #context를 html파일에 적용하여 코드로 변환시킴
                                                                    #pybo/question_list -> 템플릿 = 장고의 태그가 사용 가능한 html파일
def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)          #urls.py에서 매핑해준 question_id
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)          #음... 각 함수별로 question_id의 매개변수로 들어오는 값의 형태가 다르다 아마 다른 url에서 들어오기 때문일텐데......
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id = question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """
    pybo 질문 등록
    """

    #POST와 GET방식을 조건문으로 나눠 처리했다

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
            form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
