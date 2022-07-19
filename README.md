# Instructions:
you will find here how to create and the virtual environment either through Pycharm Projects or in the Terminal and how to install the requirements for your Django and Django Rest Api Framework
finally you will create your project with the Django-admin and create an app in it.
## A. creating virtual environment through Pycharm projects:
1- click on File--> new project in the window which will open give the project name `Django_tutorial` as in th image and make sure that there is virtual env there.


<img height="250" src="[/home/user/PycharmProjects/Django_tutorial/images/create_new_project.png](https://github.com/Lama-DCIpython/DjangoRest_tutorial/blob/main/images/create_new_project.png)" width="250"/>\
2- open a terminal in Pycharm and double check that you are in the right directory and your  virtual env is activated as in image\
<img height="250" src="/home/user/PycharmProjects/Django_tutorial/images/active_venv.png" width="250"/>\

## B. creating virtual environment in the terminal:
1- Navigate to the directory in which you want to put your project (e.g` ~ `for your home or `~/PycharmProjects`)\
2- `mkdir Django_tutorial`\
3- `cd Django_tutorial`\
4- make sure that you are not in an activated virtual environment, if this is the case deactivate it.
  _(This depends on your default project settings in Pycharm and whether you are working in an existing terminal of an old project or after you have deleted some project, ask the writer for more explanation if you need)_\
5- create the virtual environment by running this command: `python3 -m venv env`\
6- activate it by: `source env/bin/activate`\
7- If the virtual environment appears only in the terminal as active, but you don't see it in the project section in Pycharm then go to the right-down corner of pycharm and click on the python interpreter settings there this will open a window for you where you can delete the invalid interpreter if any and add a new correct one inside your venv\
<img height="250" src="/home/user/PycharmProjects/Django_tutorial/images/interpreter_1.png" width="250"/>\
<img height="250" src="/home/user/PycharmProjects/Django_tutorial/images/interpreter-2.png" width="250"/>\
8- your project window should be now like this: \
<img height="250" src="/home/user/PycharmProjects/TDjango_tutorialut/images/Project_window.png" width="250"/>


## Installing the requirements

```
# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

 ```
Your terminal will look like this
```commandline
(venv) user@user-ThinkPad-L15-Gen-1:~/PycharmProjects/Django_tutorial$ pip freeze
asgiref==3.5.2
backports.zoneinfo==0.2.1
Django==4.0.6
djangorestframework==3.13.1
pytz==2022.1
sqlparse==0.4.2

```
and your interpreter settings will look like the image.


## Set up a new project with a single application
```commandline
django-admin startproject tutorial .  # Note the trailing "." character
cd tutorial
django-admin startapp quickstart
cd ..
```
your Directory Tree will look like ![](/home/user/PycharmProjects/Django_tutorial/images/filetree.png)

## creating the tables of your database 
Now sync your database for the first time:

`python manage.py migrate`

We'll also create an initial user named `admin` with a password of `password123`. We'll authenticate as that user later in our example.

`python manage.py createsuperuser --email admin@example.com --username admin`

Once you've set up a database and the initial user is created and ready to go, open up the app's directory and we'll get coding...

Now in the `tutorial/quickstart/apps.py` change the app name into `'tutorial.quickstart'`

## Serializers
First up we're going to define some serializers. Let's create a new module named `tutorial/quickstart/serializers.py` that we'll use for our data representations.\
```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

```
## Views
Right, we'd better write some views then. Open `tutorial/quickstart/views.py` and get typing.
Make sure not to overwrite the existing code
```python
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

## URLs

Okay, now let's wire up the API URLs. On to `tutorial/urls.py`

also make sure not to overwrite the existing code rather than integrate the codes.
```python
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```
## Pagination
Pagination allows you to control how many objects per page are returned. To enable it, add the following lines to `tutorial/settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

# Settings
Add `'rest_framework'` and `'tutorial.quickstart'` to `INSTALLED_APPS`. The settings module will be in `tutorial/settings.py`

# Running the server to test the API

In the terminal type:
`python manage.py runserver`
(this will run as long as you don't stop it by `cntr + C`, if you need to still use the terminal without stopping the server open another window
in the terminal)\
you can go to the localhost now and see the user List  at [//127.0.0.1:8000/users/](//127.0.0.1:8000/users/) and the group list at [//127.0.0.1:8000/groups/](//127.0.0.1:8000/groups/)

visit those urls (of the back end) and investigate the available methods (get,put, patch, post,delete)
check the options to see which fields are required and what is necessary for validation
## Admin view 
you can go to the html template site of the admin through: [//127.0.0.1:8000/admin]()

login with the username and password of the superuser from above.
The admin has the permission to manage the database and set user (default passwords)they need to be valid(strong)

[sourse and additional info](https://www.django-rest-framework.org/tutorial/quickstart/)

## adding other models and a html file for the homepage template
#TODo still under editing

Let's say you want to make a blog website where you add blog posts to your blog then you need to create Post model in the `tutorial/quickstart/views.py`
If you want to make a website to collect books you need to add a Book model there and so on.
In the following we will create a very simple Book model to our `tutorial/quickstart/views.py` file
We will develop this coe later

Add the following code there:

```python

from django.db import models

# Create your models here.


class Book(models.Model):
    objects = None
    name = models.CharField(max_length=50, null=True)
    pub_date = models.DateField()

    class Meta:
        ordering = ['pub_date']

```
## Create tables for models in your database

The last step here is to add our new model to our database. First we have to make Django know that we have some changes in our model. (We have just created it!) Go to your terminal(another window than where the server is running) and type
`python manage.py makemigrations quickstart`. It will look like this:

```commandline
(venv) user@user-ThinkPad-L15-Gen-1:~/PycharmProjects/Django_tutorial$ python manage.py makemigrations quickstart
Migrations for 'quickstart':
  tutorial/quickstart/migrations/0001_initial.py
    - Create model Book

```

Note: Remember to save the files you edit. Otherwise, your computer will execute the previous version which might give you unexpected error messages.

Django prepared a migration file for us that we now have to apply to our database. Type `python manage.py migrate quickstart` and the output should be as follows:

```commandline
(venv) user@user-ThinkPad-L15-Gen-1:~/PycharmProjects/Django_tutorial$ python manage.py migrate quickstart
Operations to perform:
  Apply all migrations: quickstart
Running migrations:
  Applying quickstart.0001_initial... OK

```

Our Book model is now in our database! It would be nice to see it, right? Therefore, we need to register it in the Admin Site.
## Django admin
To make the books appear on the admins site we need to register this model in the `tutorial/quickstart/admin.py`

Add the following to the existing code there

```python
from tutorial.quickstart.models import Book

admin.site.register(Book)
```
you can now go to the admin site and create some books there 

## add the Book list to the routers and the backend urls

we need to add the following code to the `tutorial/quickstart/serializers.py` \

```python
from tutorial.quickstart.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'name', 'pub_date']
```
And the following to `tutorial/quickstart/views.py` \

```python
from tutorial.quickstart.models import Book
from tutorial.quickstart.serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
```
Add also `router.register(r'books', views.BookViewSet)` to the `tutorials/urls.py`\

The  "books": "http://127.0.0.1:8000/books/" will appear now on your homepage //127.0.0.1:8000

## adding a html template with a books list to your homepage
to be continued
To the `tutorial/quickstart/views.py` file add:

```python
from django.shortcuts import render
def books_list(request):
    return render(request, 'quickstart/books_list.html', {})
```
Then add the new file urls.py to the `tutorials/quickstart` and paste the following inside it.

```python
from django.urls import path
from tutorial.quickstart import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
]

```

# ToDo 
you need to edit the tutorial/urls.py to add a base-hompage
you need also to create the 
