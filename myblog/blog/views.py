# Create your views here.# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    items=[]
    for item in post_list:
	items.append(item.title)
    return HttpResponse(items)

def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    if (showComments):
	out='<h1>'+post.title+'</h1>'+'<br>'+post.body[:100]+'<br>'+post.body[100:200]
    else:
	out=post.title+'<br>'
    return HttpResponse(out)
    
def post_search(request, term):
    pass

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
