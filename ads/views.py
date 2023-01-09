from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from ads.models import Category, Advertisement
from django.urls import reverse_lazy
from django.shortcuts import redirect

class CategoriesList(ListView):
    template_name = 'ads/categories_list.html'

    def get_queryset(self):
        return Category.objects.all().order_by('-updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = self.get_queryset()
        return context

    def post(self, request, *args, **kwargs):
        cat = Category.objects.get(id=request.POST['category'])
        cat.delete()
        return self.get(request, *args, **kwargs)


class AdvertisementsList(ListView):
    template_name = 'ads/advertisements_list.html'
    paginate_by = 4
    page_kwarg = 'page'

    def get_queryset(self):
        cat_name = Category.objects.get(name=self.kwargs['category'])
        return Advertisement.objects.filter(category=cat_name).order_by('-updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = self.get_queryset()
        context['current_category'] = self.kwargs['category']
        return context

    def post(self, request, *args, **kwargs):
        ad = Advertisement.objects.get(id=request.POST['ad_id'])
        ad.delete()
        return self.get(request, *args, **kwargs)


class AdvertisementDetail(DetailView):
    model = Advertisement
    slug_url_kwarg = 'ad_id'
    slug_field = 'id'
    query_pk_and_slug = True
    template_name = 'ads/advertisement_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = Advertisement.objects.get(id=self.kwargs['ad_id'])
        cat = Category.objects.get(name=ad.category)
        context['current_category'] = cat.name
        return context

    def post(self, request, *args, **kwargs):
        ad = Advertisement.objects.get(id=request.POST['ad_id'])
        cat = ad.category.name
        ad.delete()
        return redirect(reverse_lazy('ads:advertisements_list', kwargs={'category': cat}))


class HomePage(TemplateView):
    template_name = 'ads/home_page.html'


class AddCategoryForm(CreateView):
    template_name = 'ads/category_add.html'
    success_url = reverse_lazy('ads:categories_list')
    model = Category
    fields = [
        'name',
        'desc',
    ]


class EditCategoryForm(UpdateView):
    template_name = 'ads/category_edit.html'
    success_url = reverse_lazy('ads:categories_list')
    model = Category
    fields = [
        'name',
        'desc',
    ]
    slug_url_kwarg = 'category'
    slug_field = 'name'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.kwargs['category']
        return context


class AddAdvertisementForm(CreateView):
    template_name = 'ads/advertisement_add.html'
    model = Advertisement
    fields = [
        'subject',
        'text',
        'cost',
        'category',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(name=self.kwargs['category'])
        context['cat'] = cat
        context['current_category'] = cat.name
        return context

    def get_success_url(self):
        cat_name = self.kwargs['category']
        return reverse_lazy('ads:advertisements_list', kwargs={'category': cat_name})


class EditAdvertisementForm(UpdateView):
    template_name = 'ads/advertisement_edit.html'
    model = Advertisement
    fields = [
        'subject',
        'text',
        'cost',
        'category',
    ]
    slug_url_kwarg = 'ad_id'
    slug_field = 'id'
    query_pk_and_slug = True

    def get_success_url(self):
        ad_id = self.kwargs['ad_id']
        ad = Advertisement.objects.get(id=self.kwargs['ad_id'])
        cat_name = ad.category
        return reverse_lazy('ads:advertisement_detail', kwargs={'ad_id': ad_id, 'category':cat_name})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = Advertisement.objects.get(id=self.kwargs['ad_id'])
        cat = Category.objects.get(name=ad.category)
        context['current_category'] = cat.name
        return context