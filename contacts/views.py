from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Contact


@login_required(redirect_field_name='login')
def index(request):

    contacts = Contact.objects.order_by('-id').filter(
        visible=True
    )

    paginator = Paginator(contacts, 3)
    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def send_contacts(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.visible:
        raise Http404('Does not exist')

    return render(request, 'contacts/send_contacts.html', {
        'contact': contact
    })


def search(request):
    termo = request.GET.get('termo')
    camps = Concat('first_name', V(''), 'lastName')
    contacts = Contact.objects.annotate(
        full_name=camps
    ).filter(
        Q(full_name__icontains=termo) | Q(telephone=termo)
    )
    
    paginator = Paginator(contacts, 3)
    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/search.html', {
        'contacts': contacts}
    )
      
    qs = super().get_queryset()

    categoria = self.kwargs.get('categoria', None)

    if not categoria:
        return qs

    qs = qs.filter(categoria_post__nome_categoria__iexact=categoria)

    return qs
