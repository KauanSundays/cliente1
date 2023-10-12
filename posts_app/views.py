from django.shortcuts import render
from posts_app.models import Posts

# Create your views here.
def post_list(request):
    template_name = 'post-list.html' # template
    posts = Posts.objects.all() # query com todas as postagens
    context = { # cria context para chamar no template
        'posts': posts
        }
    return render(request, template_name, context) # render

