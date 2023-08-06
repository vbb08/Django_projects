# Web Development Project with Django
## Introduction
This repository contains the source code for a web development project built with Django framework. It is part of the assignments and projects completed during the Web Development with Django courses on Coursera.org
- [Web Application Technologies and Django](https://www.coursera.org/learn/django-database-web-apps?specialization=django)
- [Building Web Applications in Django](https://www.coursera.org/learn/django-build-web-apps?specialization=django)
- [Django Features and Libraries](https://www.coursera.org/learn/django-features-libraries?specialization=django)


## Project Description
### My working project can be visited at https://thewhiteowl.pythonanywhere.com/
Some applications require a log in, in this case a guest account can be used:
username : Guest
password : Pass123!

### Folder ***'batch'*** :
Subfolders needed to create a **One-To-Many Data Model**.
Task: Develop a data model from a file of un-normalized data and then build a script to load data in to that model. The data is a simplified extraction of the [UNESCO World Heritage Sites](https://whc.unesco.org/en/list/) registry. The un-normalized data is provided as CSV file [whc-sites-2018-clean.csv](https://github.com/vbb08/django_projects/blob/main/batch/unesco/whc-sites-2018-clean.csv)

### Folder ***'mysite'*** :
Various subfolders corresponding to their 'app name':
- 'ads' : Classified ad web site. People can view ads without logging in and if they log in, they can create their own ads.
- 'autos' : Fully working **CRUD** (Create, Read, Update, and Delete) **app** to manage automobiles and their makes (i.e. Ford, Hyundai, etc.). Log in required
- 'cats' : **CRUD app** with CRISPY implementation. Log in required
- 'hello' : Return the **sessions count**
- 'home' : Main page creation
- 'polls' : **Poll app** composed by two parts 1) A [public site](https://thewhiteowl.pythonanywhere.com/polls/) that lets people view polls and vote in them ; 2) An [admin site](https://thewhiteowl.pythonanywhere.com/admin/) that lets you add, change, and delete polls. Log in required just in the admin site

## Setup Instructions

To set up the project, go into your virtual environment if needed, and follow the steps below:

    git clone https://github.com/vbb08/django_projects.git
    cd django_projects
    pip3 install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runscript gview_load
    python manage.py runscript many_load


### Running Locally
If you have Django installed on your local computer you can test any of the sample
applications by going into the folder and starting the server:

    cd django_projects
    python manage.py runserver

And visit `http://localhost:8000`.

### Running on PythonAnywhere
Once you have checked out the code under `django_projects`, and
ran the migrations and load scripts,
go under the Web tab, update the config files to point to your new application:

    Source code:                /home/--your-account--/django_projects/mysite
    Working Directory:          /home/--your-account--/django_projects/mysite

Use this as your `WGSI configuration file`:

    import os
    import sys

    path = os.path.expanduser('~/django_projects/mysite')
    if path not in sys.path:
        sys.path.insert(0, path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    from django.core.wsgi import get_wsgi_application
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(get_wsgi_application())

You can edit these files and settings in the Web tab to switch between
 various projects on PythonAnywhere.  Make sure to reload under the Web tab after
every file or configuration change.