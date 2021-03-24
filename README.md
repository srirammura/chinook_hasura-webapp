# Hasura Assignment


#### Problem Statement:

Build a web dashboard to look at data coming in from a database and a form to insert data back into the database. 
1. Setup a relational database:   
2. Load a sample dataset into your database (We recommend the chinook dataset) 
3. Write APIs to retrieve data from the database and insert back into db. Use any programming language or framework that you’re familiar with. One endpoint for “read” and one endpoint for “write”. 
4. Create a web app that pulls data from the API and 
a. shows data in a tabular format 
b. has a page with a form to create a new record. 

   


#### Framework and dependencies used:

Django Rest Framework - download these dependecies to work with DRF
 ```
pip install django
pip install djangorestframework
pip install markdown       
pip install django-filter 
```
instead just use the requirements.txt file that I have created to install all dependencies

```
pip install requirements.txt
```

#### Important files to check , to understand the codebase :

Backend

- [models.py](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/models.py)
- [serializers.py](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/serializers.py)
- [views.py] (https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/views.py)

Frontend

-[index.html](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/templates/index.html)
-[base.html](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/templates/base.html 

Note : base.html is actually kept in /var/www/html and is served through apache2 server running in cloud. For convenience I have copied the base.html in templates folder


