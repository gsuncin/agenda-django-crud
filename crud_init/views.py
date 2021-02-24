from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Person
from .forms import PersonForm


def home(request):
    form = PersonForm()
    context = {
        'page_title': 'Agenda',
        'header_title': 'Organize sua agenda adicionando, editando e excluindo contatos existentes!',
        'persons': Person.objects.all(),
        'form': form,
    }
    return render(request, 'homepage.html', context)


def modal_add_contact(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    context = {
        'page_title': 'Novo contato',
        'header_title': 'Aumente sua rede e conheça novas pessoas',
        'form': form,
    }
    return render(request, 'add_contact.html', context)


def add_contact(request):
    form = PersonForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))


def modal_edit_contact(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    context = {
        'person': Person.objects.get(id=id),
        'page_title': 'Edite o contato',
        'header_title': 'Aumente sua rede e conheça novas pessoas',
        'form': form,
    }
    return render(request, 'edit_contact.html', context)


def edit_contact(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    context = {
        'person': Person.objects.get(id=id),
        'page_title': 'Edite o contato',
        'header_title': 'Aumente sua rede e conheça novas pessoas',
        'form': form,
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Alterado com sucesso'
        return redirect(reverse('home'))
    return render(request, 'edit_contact.html', context)


def modal_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    context = {
        'person': person,
    }
    return render(request, 'modal_delete.html', context)


def delete_contact(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect(reverse('home'))
