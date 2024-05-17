from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contactmodel

# Create your views here.
def home(request):
    contacts = Contactmodel.objects.all()  
    return render(request, 'home.html', {'contacts': contacts})

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def search_contacts(request):
    query = request.GET.get('query', '')
    contacts = Contactmodel.objects.filter(name__icontains=query)
    return render(request, 'home.html', {'contacts': contacts, 'query': query})

def edit(request, contact_id):
    contact = Contactmodel.objects.get(id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit.html', {'form': form, 'contact': contact})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contactmodel, id=contact_id)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'delete.html', {'contact': contact})

