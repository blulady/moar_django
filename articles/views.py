from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article
# Create your views here.
def article_detail_view(request, id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)

def article_search_view(request):
    print(request.GET)
    query_dict = request.GET #this is a dictionary produced by the get request created by this function
    query = query_dict.get("query") # <input type="text" name="query"/>
    try:
        query = int(query_dict.get("query"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query) #using the query as ide instead
    context = {
        "object": article_obj
    } #this is the object we have in search.html
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    #print(request.POST)
    form = ArticleForm(request.POST or None) #here we render the form
    #print(dir(form))
    context = {
        "form": form
    }
    # if request.method == "POST": #once we do a post method that method needs to handle the data
    #     form = ArticleForm(request.POST) #here we pass in the unclean data
    #     context['form'] = form
    if form.is_valid(): #we run this if statement to make sure our form data is cleaned
        article_object = form.save()
        #context['form'] = ArticleForm() #supposed to clear the form but doesn't

        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # print(title, content)
        # article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True

    return render(request, "articles/create.html", context=context)
