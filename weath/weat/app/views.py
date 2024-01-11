from django.shortcuts import render
from .forms import Todo_form
from .models import Todo 
# Create your views here.
def index(request):

    context={}
    todo_form=Todo_form()
    todo=Todo.objects.all()

    if request.method == 'POST':
        if 'save' in request.POST:
            key=request.POST.get('save')

            
            if not key:
               todo_form=Todo_form(request.POST)
            else:
               todo_edit=Todo.objects.get(id=key)
               todo_form=Todo_form(request.POST,instance=todo_edit)
            
            
            
            todo_form.save()
            todo_form=Todo_form()
        
        
        elif 'delete' in request.POST:
            key=request.POST.get('delete')
            todo_del=Todo.objects.get(id=key)
            todo_del.delete()

        elif 'edit' in request.POST:
             key=request.POST.get('delete')
             todo_edit=Todo.objects.get(id=key)
             todo_form=Todo_form(instance=todo_edit)

    context['todo_form']=todo_form
    context['todo']=todo
    return render(request,'index.html',context)



