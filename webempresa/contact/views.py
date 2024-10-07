from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get("name", "")
            email_from = contact_form.cleaned_data.get("email", "")
            content = contact_form.cleaned_data.get("content", "")
            
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de Contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email_from, content),
                "no-contestar@inbox.mailtrap.io",
                ["davidsuchiapa@gmail.com"],
                reply_to=[email_from]
            )
            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail")
    
    return render(request, "contact/contact.html", {'form': contact_form})
