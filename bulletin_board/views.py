from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

from .forms import AdsForm, ReactionsForms

from .filters import ReactionsFilter


class AdsList(LoginRequiredMixin, ListView):
    model = Ads
    template_name = 'article.html'
    context_object_name = 'ads'
    form_class = AdsForm


class AdsCreate(CreateView):
    template_name = 'ads_create.html'
    form_class = AdsForm
    success_url = '/'


class AdsUpdate(UpdateView):
    template_name = 'ads_create.html'
    form_class = AdsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ads.objects.get(pk=id)


class AdsDetail(DetailView):
    template_name = 'ads_detail.html'
    queryset = Ads.objects.all()

    def post(self, request, pk):
        form = ReactionsForms(request.POST)
        ads = Ads.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.ads = ads
            form.authors = self.request.user
            print(request.POST)
            form.save()

            return redirect(ads.get_absolute_url())


class ReactionsList(ListView):
    template_name = 'reactions_list.html'
    context_object_name = 'reactions'

    def get_queryset(self, **kwargs):
        authors_id = self.request.user.id
        return Reactions.objects.filter(ads__authors=authors_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ReactionsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ReactionsAdd(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        reaction = Reactions.objects.get(id=pk)
        reaction.authentication = True
        reaction.save()
        return redirect('/reaction/')


class ReactionsDelete(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        reaction = Reactions.objects.get(pk=pk)
        reaction.authentication = False
        reaction.delete()
        return redirect('/reaction/')

