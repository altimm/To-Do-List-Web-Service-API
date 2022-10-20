from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# relative import of forms
from .models import TaskModel
from .forms import TaskCreateForm, TaskUpdateForm


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = TaskCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)


def retrieve_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = TaskModel.objects.all()
		
	return render(request, "retrieve_view.html", context)

# update view for details
def update_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(TaskModel, id = request.GET.get('id'))
 
    # pass the object as instance in form
    form = TaskUpdateForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def delete_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(TaskModel, id = request.GET.get('id'))
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)