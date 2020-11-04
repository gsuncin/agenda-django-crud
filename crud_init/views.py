from django.shortcuts import render, redirect, reverse
from .models import Agenda, Person
from .forms import PersonForm


# Create your views here.
def home(request):
    form = PersonForm()
    context = {
        'page_title': 'Agenda',
        'header_title': 'Organize sua agenda adicionando, editando e excluindo contatos existentes!',
        'persons': Person.objects.all(),
        'form': form,
    }
    if request.POST:
        form = PersonForm(request.POST)
        form.save()
        context['message'] = 'Adicionado com sucesso'
        return redirect(reverse('home'))
    return render(request, 'homepage.html', context)
