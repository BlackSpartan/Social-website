from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image

# Create your views here.
@login_required # login_required decorator is used to prevent access for unauthenticated users
def image_create(request):
    if request.method =='POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # If the form data is valid create a new Image instance, 
            # but prevent the object from being saved to the database,
            # yet by passing commit=False to the form's save() method. 
            cd = form.cleaned_data 
            new_item = form.save(commit=False)

            # assign the current user to the new image object. 
            # This is how you can know who uploaded each image
            new_item.user = request.user
            new_item.save() # save the image object to the database. 
            messages.success(request, 'Image added successfully') # create a success message using the Django messaging framework 

            # redirect to new created item detail view 
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


# view to display an image
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html',{'section': 'images', 'image': image})