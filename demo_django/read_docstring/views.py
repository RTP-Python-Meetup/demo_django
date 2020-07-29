from django.views.generic.base import TemplateView


class MainView(TemplateView):

    template_name = "read_docstring_main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foo'] = 'bar'

        return context
