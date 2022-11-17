from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from main.forms import ShortenerForm
from main.models import Shortener


class IndexPage(View):
    template_name = 'main/index.html'
    form_class = ShortenerForm
    context = {}

    def get(self, request):
        form = self.form_class()
        self.context['form'] = form
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        form = self.form_class(request.POST)
        self.context['form'] = form
        if form.is_valid():
            shortened = form.save()
            new_url = request.build_absolute_uri(shortened.short_url)
            self.context['full_url'] = shortened.full_url
            self.context['short_url'] = new_url
            return render(request, self.template_name, self.context)
        self.context['errors'] = form.errors
        return render(request, self.template_name, self.context)


class RedirectToLongAddressView(View):
    def get(self, request, short_url):
        shortened = get_object_or_404(Shortener, short_url=short_url)
        return redirect(shortened.full_url)
