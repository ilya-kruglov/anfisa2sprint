# from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import Category, IceCream


def index(request):
    template_name = 'homepage/index.html'
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'description'
    # ).filter(
    #     Q(is_on_main=True)
    #     | (Q(title__contains='пломбир') & Q(is_published=True))
    # )
    categories = Category.objects.values(
        'id', 'output_order', 'title'
    ).order_by(
        'output_order', 'title'
    )
    # context = {
    #     'ice_cream_list': ice_cream_list,
    # }
    context = {
        'categories': categories
    }
    return render(request, template_name, context)
