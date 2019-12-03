from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def page_list(request):

    pages = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'appsite/page_list.html', {'pages':pages})

# def new_page(request):
#     pass
#     # page = Post.
