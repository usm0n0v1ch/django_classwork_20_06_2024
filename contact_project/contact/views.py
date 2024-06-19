


from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = ContactForm()
    ctx = {'form': form}
    return render(request, 'contact/contact_form.html', context=ctx)

def thanks_view(request):
    return render(request, 'contact/thanks.html')