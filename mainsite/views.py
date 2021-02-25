from django.shortcuts import render
from .models import Plants
from .filters import plantsFilter
from .forms import SearchForm


# Create your views here.
def home(request):
    plantsByFamily = None
    # 請求方法為POST（使用者查詢）時，依據請求傳入的查詢條件篩選資料
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            plantsByFamily = plantsFilter(formdata=form.cleaned_data)
    else:
        form = SearchForm()
    context = {
        'form': form,
        'plantsByFamily': plantsByFamily
    }
    return render(request, 'home.html', context)
