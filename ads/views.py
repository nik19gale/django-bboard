from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from ads.models import Category, Advertisement

class CategoriesList(ListView):
    template_name = 'ads/categories_list.html'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = self.get_queryset()
        return context


class CategoryAdd(TemplateView):
    template_name = 'ads/category_add.html'


class CategoryEdit(TemplateView):
    template_name = 'ads/category_edit.html'


class AdvertisementsList(ListView):
    template_name = 'ads/advertisements_list.html'
    paginate_by = 5
    page_kwarg = 'page'

    def get_queryset(self):
        cat_name = Category.objects.get(name=self.kwargs['cat_name'])
        return Advertisement.objects.filter(category=cat_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = self.get_queryset()
        context['cat_name'] = self.kwargs['cat_name']
        return context


class AdvertisementDetail(DetailView):
    model = Advertisement
    slug_url_kwarg = 'ad_id'
    slug_field = 'id'
    query_pk_and_slug = True
    template_name = 'ads/advertisement_detail.html'


class AdvertisementAdd(TemplateView):
    template_name = 'ads/advertisement_add.html'


class AdvertisementEdit(TemplateView):
    template_name = 'ads/advertisement_edit.html'