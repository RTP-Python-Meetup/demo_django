from django.views.generic.base import TemplateView

from .forms import FileForm


class MainView(TemplateView):

    template_name = "read_docstring_main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foo'] = 'bar'
        context['form'] = self.file_form or FileForm()
        if self.file is None:
            context['file_id'] = 'New'
        else:
            context['file_id'] = self.file.id

        return context
