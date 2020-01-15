from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . models import Product


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class TestModelListJson(BaseDatatableView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    template_name = 'create.html'
    fields = ['name', 'category', 'price']
    success_url = '/'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update.html'
    fields = ['name', 'category', 'price']
    success_url = '/'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = '/'
