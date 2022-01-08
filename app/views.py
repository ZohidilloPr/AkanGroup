from django.shortcuts import redirect, render
from .forms import AloqaForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def Web_hizmat(request):
    if request.method == 'POST':
        form = AloqaForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'Yangi Habar {form.cleaned_data["name"]} dan {form.cleaned_data["subject"]}'
            message = f"Ismi: {form.cleaned_data['name']} \n Email manzili: {form.cleaned_data['email']} dan \n Xabari {form.cleaned_data['message']}"
            send_mail(email_subject, message, settings.CONTACT_EMAIL, [settings.ADMIN_EMAILS], fail_silently=False)
            messages.success(request, 'Xabaringiz yetkazildi tez orada javob beriladi!')
            return redirect('app:Home')
        messages.error(request, "xabar yetkazilmadi :( qaytadan urinib ko'ring")
    # messages.error(request, "xabar yetkazilmadi :( qaytadan urinib ko'ring")
    form = AloqaForm()
    context = {'form': form}
    return render(request, 'index.html', context)

