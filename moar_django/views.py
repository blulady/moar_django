"""to render html web pages"""
#from django.shortcuts import redirect, render
from django.http import HttpResponse #, HttpResponseRedirect
from django.template.loader import render_to_string
from articles.models import Article
from random import randint
#from django.urls import reverse


HTML_STRING = """<h1>Hello World its your wild Girl</h1>"""

def home_view(request, *args, **kwargs):
    """take in a request (django sends request)
    return html as a responce (we pick to return the response"""
    print("args, kwargs", args, kwargs)
    print(id)
    random_id = randint(1,8)
    article_obj = Article.objects.get(id=random_id)
    article_list = Article.objects.all()
    object_list = article_list #[43, 69, 112, 38, 99]
    context = {
        "object_list": object_list,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = f"""
    #  <h1>{article_obj.title} id: {(article_obj.id)}</h1>
    #  <p>{article_obj.content}<p>
    #  """.format()
    return HttpResponse(HTML_STRING)

