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

1) Django Rest Framework - download these dependecies to work with DRF
 ```
pip install djangorestframework
pip install markdown       
pip install django-filter 
```
#### Calculations:
After indivisually calculating matching of every field, I'm then merging them according to the provided weightage:
```
DISTANCE_WEIGHT = 0.3
BUDGET_WEIGHT = 0.3
BATHROOM_WEIGHT = 0.2
BEDROOM_WEIGHT = 0.2

Result(in %age)  = distance_match * DISTANCE_WEIGHT
        + budget_match * BUDGET_WEIGHT
        + bedroom_match * BEDROOM_WEIGHT
        + bathroom_match * BATHROOM_WEIGHT
