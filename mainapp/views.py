from django.shortcuts import render
import stackexchange
from django.core.paginator import Paginator

# Create your views here.
def Index(request):
    return render(request, template_name='mainapp/index.html')


def SearchUser(request):
    if request.method == "POST":
        if request.POST["userterm"] is not None:
            so = stackexchange.Site(stackexchange.StackOverflow)
            search_user = request.POST["userterm"]
            u = so.user(search_user)
            reputation = u.reputation.format()
            totalanswers = u.answers.count
            display_name = u.display_name,
            creation_date = u.creation_date,
            context = {
                'reputation': reputation,
                'totalanswers': totalanswers,
                'creation_date': creation_date,
                'display_name': display_name,
            }
            return render(request, template_name='mainapp/user_result.html', context=context)


def SearchQuery(request):
    if request.method == "POST":
        if request.POST["term"] is not None:
            so = stackexchange.Site(stackexchange.StackOverflow, impose_throttling=True)
            search_term = request.POST["term"]
            qs = so.search(intitle=search_term)
            order = request.POST["order"]
            count = 0
            response = []
            for q in qs:
                count += 1
                if count <= 3*qs.pagesize:
                    response.append(q)
                else:
                    break
            if order == "desc":
                response.reverse()
            context = {
                'response': response,
            }
            return render(request, template_name='mainapp/search_result.html', context=context)
