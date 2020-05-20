from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from polls.models import Question, Choice


def index(request):
    questions = Question.objects.order_by("-date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": questions
    }
    return HttpResponse(template.render(context, request))

def details(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("This ID does not exist")
    template = loader.get_template("polls/details.html")
    context = {
        "question": question
    }
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("This ID does not exist")
    template = loader.get_template("polls/results.html")
    context = { "question": question }
    return HttpResponse(template.render(context, request))

def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("This Question ID does not exist")
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        template = loader.get_template("polls/details.html")
        context = {
            "question": question,
            "error_message": "You didn't select a choice"
        }
        return HttpResponse(template.render(context, request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=( question_id, )))

