# Django_React__App
application created to learn django Rest framework 

## Project Setup

### Create Django Project

```sh
django-admin startproject "ProjectName"
cd "ProjectName"
```
### Create Django Application

```sh
django-admin startapp "AppName"
```

Running a django server

```sh
python3 manage.py runserver
```

application created to learn django Rest framework 

Django REST Framework
Views
Views in Django handle the logic for your web application. They receive HTTP requests, process them, interact with models, and return HTTP responses. In Django REST Framework, views can be used to create APIs that handle various HTTP methods (GET, POST, PUT, DELETE, etc.).

Models
Models are the single, definitive source of information about your data. They contain the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

Data Types Used in Models
CharField: For strings with a max length.
TextField: For longer text fields.
IntegerField: For integers.
BooleanField: For True/False values.
DateField and DateTimeField: For dates and times.
ForeignKey: For creating many-to-one relationships.
ManyToManyField: For many-to-many relationships.
OneToOneField: For one-to-one relationships.
Meta Class in Models
The Meta class inside a Django model is used to define metadata for the model. This can include options like ordering, database table name, and verbose names.

Serializers
Serializers are used to convert complex data types, such as Django model instances, into Python data types that can be easily rendered into JSON, XML, or other content types. They can also be used to validate and parse input data.

Templates
Templates in Django are used to define the structure and layout of your web pages. They allow you to dynamically generate HTML content using Django's template language.

Migrations
Migrations are Django’s way of propagating changes you make to your models into your database schema.

Making Migrations:


python3 manage.py makemigrations

Applying Migrations:

python3 manage.py migrate
Migrations are necessary to keep the database schema in sync with the current state of the models.

Primary Keys
A primary key is a field in a table which uniquely identifies each row/record in that table. By default, Django adds an id field as the primary key.

Foreign Keys
A foreign key is a field in a table that is a primary key in another table. It is used to link two tables together.

CreateAPIView and ListAPIView
CreateAPIView: A view that provides a method to handle POST requests for creating new model instances.
ListAPIView: A view that provides a method to handle GET requests for listing multiple model instances.




