from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    latest_questions_list = models.Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list":latest_questions_list };
    return render(request, "polls/index.html", context);

def results(request, question_id):
    question = models.Question(pk=question_id);
    print(question_id)
    return render(request, "polls/results.html", {"question" : question}); 

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id);
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]);
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice", 
        })
    else:
        selected_choice.votes += 1;
        selected_choice.save();
        return redirect('polls:results', question.id)