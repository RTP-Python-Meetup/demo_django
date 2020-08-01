from django.views.generic.base import TemplateView
from django.shortcuts import render

from .forms import FileForm


class MainView(TemplateView):

    template_name = "read_docstring_main.html"
    # Set up placeholders to be populated by either post() or get_context_data()
    file_form = None
    file = None

    def post(self, request, *args, **kwargs):
        # Initialize a form from the post data received
        self.file_form = FileForm(request.POST)

        # Validate and save the form
        if self.file_form.is_valid():
            self.file = self.file_form.save()

        # Collect the context data
        context = self.get_context_data(**kwargs)

        # Render the template
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foo'] = 'bar'

        # Use the self.file_form if it's been set, otherwise initialize an empty one.
        context['form'] = self.file_form or FileForm()

        # Indicate "New" file, or the if of the file in self.file if it's set.
        if self.file is None:
            context['file_id'] = 'New'
        else:
            context['file_id'] = self.file.id

        return context
