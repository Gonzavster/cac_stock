from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm

def home(request):
    #return HttpResponse("Hello world!")
    return render(request, 'inventory/index.html')

def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def inventory(request):
    return render(request, 'inventory/inventory_portal.html')

def tutorial(request):
    return render(request, 'inventory/tutorial.html')

def signin(request):
    return render(request, 'inventory/signin.html')

def signup(request):
    return render(request, 'inventory/signup.html')

def logout(request):
    return render(request, 'inventory/logout.html')

def new_item(request):
    if request.method == 'GET':
        return render(request, 'inventory/new_item.html', {
            'form': ItemForm
        })

"""     else:
        try:
            form = ItemForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            print(new_task)
            new_task = form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create.html', {
                'form': ItemForm,
                'error': 'Please provide valid data'
            })  """

def publishers(request):
    return render(request, 'inventory/publisher_mgmt.html')

def classifications(request):
    return render(request, 'inventory/classification_mgmt.html')