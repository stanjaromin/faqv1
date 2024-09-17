from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm

def faq_list(request):
    questions = Question.objects.all()
    return render(request, 'faq/faq_list.html', {'questions': questions})

def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = QuestionForm()
    return render(request, 'faq/question_form.html', {'form': form})

def edit_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'faq/question_form.html', {'form': form})

def delete_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        question.delete()
        return redirect('faq_list')
    return render(request, 'faq/confirm_delete.html', {'question': question})

def faq_script(request):
    questions = Question.objects.all()
    return render(request, 'faq/faq_script.html', {'questions': questions})