# Create your views here.# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Post, Comment 


def post_list(request):
    posts = Post.objects.all()
    """html=''
    for i in posts:
       html+= str(i) + '<br/>'
    return HttpResponse(html )
    """
    t=loader.get_template('blog/post_list.html')
    c=Context ({'posts':posts})
    return HttpResponse(t.render(c))

def post_detail(request, id, showComments=False):
    """post=Post.objects.get(pk=id)
    if (showComments):
	out='<h1>'+post.title+'</h1>'+'<br>'+post.body
    else:
	out=post.title+'<br>'
    return HttpResponse(out)"""
    posts=Post.objects.all()
    return render_to_response('blog/post_detail.html',{'post':posts, 'comments':comments})
    	

 def post_search(request, term):
	posts=Post.objects.filter(title__contains=term)
	return render_to_response('blog/post_search.html',{'post':posts, 'term':term})
	

def home(request):
    """print 'it works'
    return HttpResponse('hello world. Ete zene?')"""
    return render_to_response('blog/base.html',{}) 


