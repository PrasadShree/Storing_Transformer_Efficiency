from django.shortcuts import render
from .forms import TransformerForm
from .models import TransformerData

# Create your views here.
def showform(request):
    form = TransformerForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'front.html', context)




def display(request):

	tmp=TransformerData.objects.all() # Collect all records from table
	return render(request,'back.html',{'tmp':tmp})