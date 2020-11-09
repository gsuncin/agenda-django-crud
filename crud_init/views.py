from django.shortcuts import render, redirect, reverse
from django.core.files.storage import FileSystemStorage
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


def add_contact(request):
    form = PersonForm()
    context = {
        'page_title': 'Novo contato',
        'header_title': 'Aumente sua rede e conheça novas pessoas',
        'form': form,
    }
    # if request.POST and request.FILES['photo']:
    #     form = PersonForm(request.POST and request.FILES)
    #     photo = request.FILES['photo']
    #     fs = FileSystemStorage()
    #     fs.save(photo.name, photo)
    #     form.save()
    #     context['message'] = 'Adicionado com sucesso'
    #     return redirect(reverse('home'))
    if request.POST:
        form = PersonForm(request.POST)
        form.save()
        context['message'] = 'Adicionado com sucesso'
        return redirect(reverse('home'))
    return render(request, 'add_contact.html', context)


def modal_delete(request):
    return render(request, 'modal_delete.html')
