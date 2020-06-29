# Python web stuff

### [Python web stuff 1 - creating a django project](https://github.com/RTP-Python-Meetup/demo_django/tree/creating_a_django_project)

#### Installing django

Links:
- [Google: django quick start](https://www.google.com/search?q=django+quick+start)
  - [Getting started with Django](https://www.djangoproject.com/start/)

Commands:
- ```pipenv shell```
- ```pipenv install django```

#### Starting a project

Links:
- [Writing your first Django app, part 1](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
  - [Creating a project](https://docs.djangoproject.com/en/3.0/intro/tutorial01/#creating-a-project)

Commands:
- ```django-admin startproject demo_django```
- ```cd demo_django```
- ```python manage.py runserver```

#### Adding the first and app to the django project

Links:
- [Writing your first Django app, part 1](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
  - [Creating the Polls app](https://docs.djangoproject.com/en/3.0/intro/tutorial01/#creating-the-polls-app)

Commands:
- ```python manage.py startapp read_docstring```
- ```python manage.py runserver```

Changes:
- Add read_docstring to INSTALLED_APPS in settings.py

#### Creating the first view and routing it to a URL

Links:
- [Writing your first Django app, part 1](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
  - [Write your first view](https://docs.djangoproject.com/en/3.0/intro/tutorial01/#write-your-first-view)

Changes:
- Add index function to read_docstring/views.py
- Create read_docstring/urls.py and add  "" route to it
- Add "read_docstring/" route to demo_django/urls.py

#### Starting with class based views

Links:
- [Google: django template view](https://www.google.com/search?q=django+template+view)
  - [TemplateView](https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#templateview)

Changes:
- Create MainView in read_docstring/views.py pointed to "read_docstring_main.html"
- Point the "" URL in read_docstring/urls.py to ```views.MainView.as_view()```

#### Creating and using a template

Links:
- [TemplateView](https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#templateview)

Changes:
- Create templates/main.html
- Add ```os.path.join(BASE_DIR, 'templates')``` to TEMPLATES['DIRS']
