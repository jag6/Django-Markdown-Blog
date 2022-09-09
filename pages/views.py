from django.views.generic import TemplateView

class AboutPage(TemplateView):  
    template_name = "about.html"
    
class ContactPage(TemplateView):  
    template_name = "contact.html"