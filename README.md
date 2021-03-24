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
pip install djangp_table2
```
instead just use the requirements.txt file that I have created to install all dependencies

```
pip install requirements.txt
```

### Important files to check , to understand the codebase :

Backend

- [models.py](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/models.py)
- [serializers.py](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/serializers.py)
- [views.py](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/views.py)

Frontend

- [index.html](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/templates/index.html)
- [base.html](https://github.com/srirammura/chinook_hasura-webapp/blob/main/app/templates/base.html)

Note : base.html is actually kept in /var/www/html and is served through apache2 server running in cloud. For convenience I have copied the base.html in templates folder

### Explanation about the important files

1) models.py - Model contains the essential fields and behaviors of the data you’re storing. Each field of the model has a specific definition in the sense of the data it stores or the type of field it is. It can be a CharField or IntegerField, a ManytoManyField or a OneToManyField or just be a ForeignKey. We can also define the minimal validation requirements, used in Django’s admin and in automatically-generated forms. These fields are important as they will go on to define our database.

2) serializers.py - Serializers are not part of Django but instead of Django-REST (which works in conjunction with the main Django framework). The main function of serializers is to render the available information into formats that can be easily accessible and utilised by the frontend.

3) views.py -  In this project, views.py not only contain viewsets but also contains table views which are created with the help of **django_tables2**  

**Check this youtube video for detailed explanation of codebase and deployment : https://youtu.be/wl2OuTaosh **

### Screenshots of webapp

![alt_text](https://github.com/srirammura/chinook_hasura-webapp/blob/main/1.png)
![alt_text](https://github.com/srirammura/chinook_hasura-webapp/blob/main/2.PNG)
![alt_text](https://github.com/srirammura/chinook_hasura-webapp/blob/main/3.PNG)
