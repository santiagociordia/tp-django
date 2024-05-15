from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question
from django.template import loader

# Create your views here.
def index(request):
    questions = Question.objects.order_by("-date")
    context = {
        "questions": questions
    }
    
    return render(request, "index.html", context)

def detail(request,  question_id):
    return HttpResponse("This is question: " + str(question_id))
