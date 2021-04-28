from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from django.views.generic import View
from .models import Entry, Person

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context = {},
    )
    
class EntryView(generic.ListView):
    """Generic class-based view for Entry Maintenance."""
    model = Entry
    
    def get_context_data(self, **kwargs):
        person_list = Person.objects.all().order_by('name')
        # Call the base implementation first to get the context
        context = super(EntryView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['action'] = self.kwargs['action']
        context['person_list'] = person_list
        return context
        
class AddEntryView(generic.ListView):
    """Generic class-based view for Entry Maintenance."""
    model = Entry
    template_name = 'trackapp/addentry.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AddEntryView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        idcheck = Person.objects.get(name=name)
        id = idcheck.id
        date = self.request.GET.get('date')
        weight = self.request.GET.get('weight')
        try:
            checkname = Entry.objects.get(name_id=id, date=date)
        except Entry.DoesNotExist:
            newEntry = Entry.objects.create(name_id=id, date=date, weight=weight)
            msg = 'Entry added successfully'
        else:
            msg = 'Duplicate Entry found'
        context['name'] = name
        context['date'] = date 
        context['weight'] = weight
        context['msg'] = msg
        return context
    
class UpdEntryView(generic.ListView):
    """Generic class-based view for Entry Maintenance."""
    model = Entry
    template_name = 'trackapp/updentry.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(UpdEntryView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        idcheck = Person.objects.get(name=name)
        id = idcheck.id
        date = self.request.GET.get('date')
        weight = self.request.GET.get('weight')
        updatename = Entry.objects.filter(name_id=id).update(date=date, weight=weight)
        msg = 'Entry updated successfully'
        context['name'] = name
        context['date'] = date
        context['weight'] = weight
        context['msg'] = msg
        return context

class UpdEntryDescView(generic.ListView):
    """Generic class-based view for Person Maintenance."""
    model = Person
    template_name = 'trackapp/updentrydesc.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(UpdEntryDescView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        idcheck = Person.objects.get(name=name)
        id = idcheck.id
        date = self.request.GET.get('date')
        checkname = Entry.objects.get(name_id=id, date=date)
        context['name'] = checkname.name
        context['date'] = checkname.date
        context['weight'] = checkname.weight
        context['action'] = 'u'
        return context
    
    
class DelEntryView(generic.ListView):
    """Generic class-based view for Entry Maintenance."""
    model = Entry
    template_name = 'trackapp/delentry.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(DelEntryView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        idcheck = Person.objects.get(name=name)
        id = idcheck.id
        date = self.request.GET.get('date')
        deletename = Entry.objects.filter(name_id=id, date=date).delete()
        msg = ' was deleted successfully'
        context['name'] = name
        context['date'] = date
        context['msg'] = msg
        return context
    
class PersonView(generic.ListView):
    """Generic class-based view for Person Maintenance."""
    model = Person
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PersonView, self).get_context_data(**kwargs)
        person_list = Person.objects.all().order_by('name')
        # Create any data and add it to the context
        context['action'] = self.kwargs['action']
        context['person_list'] = person_list
        return context
        
class AddPersonView(generic.ListView):
    """Generic class-based view for Person Maintenance."""
    model = Person
    template_name = 'trackapp/addperson.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AddPersonView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        description = self.request.GET.get('description')
        try:
            checkname = Person.objects.get(name=name)
        except Person.DoesNotExist:
            newPerson = Person.objects.create(name=name, description=description)
            msg = 'Person added successfully'
        else:
            msg = 'Duplicate Person found'
        context['msg'] = msg
        return context

class UpdPersonDescView(generic.ListView):
    """Generic class-based view for Person Maintenance."""
    model = Person
    template_name = 'trackapp/updpersondesc.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(UpdPersonDescView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        checkname = Person.objects.get(name=name)
        description = checkname.description
        context['name'] = name
        context['description'] = description
        context['action'] = 'u'
        return context
    
class UpdPersonView(generic.ListView):
    """Generic class-based view for Person Maintenance."""
    model = Person
    template_name = 'trackapp/updperson.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(UpdPersonView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        description = self.request.GET.get('description')
        updatename = Person.objects.filter(name=name).update(description=description)
        msg = 'Person updated successfully'
        context['name'] = name
        context['description'] = description
        context['msg'] = msg
        return context
   
class DelPersonView(generic.ListView):
    """Generic class-based view for Person Maintenance."""
    model = Person
    template_name = 'trackapp/delperson.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(DelPersonView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        deletename = Person.objects.filter(name=name).delete()
        msg = ' was deleted successfully'
        context['name'] = name
        context['msg'] = msg
        return context

class ChartNameView(generic.ListView):
    model = Person
    template_name = 'trackapp/chartname.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ChartNameView, self).get_context_data(**kwargs)
        person_list = Person.objects.all().order_by('name')
        # Create any data and add it to the context
        context['person_list'] = person_list
        return context
        

def barpage(request):
    context = {}
    name = request.GET.get('name')
    request.session['name'] = name
    context['name'] = name
    return render(request, 'barpage.html', context)
    
def barchart(request):
    name = request.session.get('name')
    idcheck = Person.objects.get(name=name)
    id = idcheck.id
    qs=Entry.objects.filter(name_id=id).all().order_by('date')
    labels = []
    chartdata = []

    for item in qs:
        labels.append(item.date)
        chartdata.append(item.weight)

    chartLabel = "Weight Graph"
    return JsonResponse(data={
        'name': name,
        'labels': labels,
        'data': chartdata,
    })