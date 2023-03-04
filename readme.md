
# Parsing Maven Pizza Challenge Data with Python and Flask

## introduction

This is a program assignment for CS551P Advanced programming, focusing on use python and flask to parse data for a web application using Maven Pizza challenge tracking data.

The task at hand is to develop a Flask application that meets several criteria. Specifically, the application should be database-driven and contain three linked tables. Additionally, it should be based on a suitable open data source and utilize appropriate templates for the pages while employing proper error handling techniques. The codebase should make use of Git as part of the development process for source control, and suitable tests should be included. Finally, the application should be published on Render to make it accessible to users.


### Datebase

We'll use data on Maven Pizza Challenge to develop our application. Data is taken from [https://www.kaggle.com/datasets/neethimohan/maven-pizza-challenge-dataset](https://www.kaggle.com/datasets/neethimohan/maven-pizza-challenge-dataset).
Download the zip file and unpack it to a folder.

The dataset has 5 .csv files and 4 tables. We only use the orders, pizzas, and order_details tables.

- The order_details tables has 48621 rows containing order details regarding pizza type and order quantity. We need to reduce it to 4642 rows.
- The orders table record the datetime indicators of the 21351 orders.  We need
  to reduce it to 2501 rows.
- The pizzas table has 97 rows containing the pricing details of pizza based on the size and pizza type.


## Step1

### Table Relationships for the Data

We'll import data from two related tables. Each order is listed
in the orders.csv file and is identified in the order_id column. The details of
an order are recorded in the order_details.csv file. The order_details column
in the second file references the order_id column in the first file. Therefore
we end up with a one_to_many relationship between the two files. The pizza’s
information are recorded in the pizzas.csv. And the PizzaID colomn in the
pizzas.csv file references the PizzaID colomn in the order details file.

You can see the table structure in the setup_db.py file where we
create the tables.

We can start developing our application to
display the data. Create a new project folder called 'program_assignment' and
then cd into the folder via the terminal and execute these commands:

```
	  pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```

We will use Flask ([https://flask.palletsprojects.com/en/1.1.x/](https://flask.palletsprojects.com/en/1.1.x/)) as our web framework for the application. We install that with

```
pip install flask
```

And that will install flask with its associated dependencies. We can now start to build the application.


### We need to parse a csv file and add the data to a database

The goal is to have the order details on the website, which means we need to put the spreadsheet data into a database.

We'll start with reading the csv file, then, we need to connect to the database, and run a query to create our table. You can see all code in a  file called 'setup_db.py'.

You should be able to run this to confirm the path is correct, and you can read the file with

```
python3 parse_csv.py
```

### Building the web components

We need a landing page to show profile, This page can be linked to all orders.And we need another two pages to show the details of a order and pizzas.

We can now start our actual app file, 'MavenPizza.py', which needs to be in the main folder.

We can confirm this runs by setting a few variables in your environment via the terminal (this assumes you're either using Linux or MacOS)

```
    export FLASK_APP=MavenPizza.py
    export FLASK_ENV=development
    python3 -m flask run
```

## Step2

### Add test page

Tests go in a separate folder. ‘Features’ are test files, ‘driver’ hold files for browsers, ‘steps’ are directions for features

### Add features folder and files

Use ‘almost’ plain English to write something similar to acceptance tests, Given, when, then format sets the context, and what should happen
Given, when, then format sets the context, and what should happen

### Add a steps folder and files

We can now add the testing library Behave, along with Selenium for and the appropriate web drivers for your system, which you can find at [https://selenium-python.readthedocs.io/installation.html#drivers](https://selenium-python.readthedocs.io/installation.html#drivers)

You might want to look at the documentation for Behave [https://behave.readthedocs.io/en/latest/](https://behave.readthedocs.io/en/latest/) You should look at Selenium documentation for [navigating web pages]

```
pip install behave
```


### Check the tests

You can run the current tests to see that the customer pages load, with the command

```
behave
```

in the terminal.


### Use environment.py for context

You will need to download the same version of chromdriver as your current chrome browser on this page, go to this website to download and put it in ./driver directory：[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

If you're on a Mac, then you will need to remove the chrome driver from quarantine with the command

```
xattr -d com.apple.quarantine <name-of-executable>
```

To set imports，you need to：
（if you already have these module,you can skip these commands.）

```
pip install selenium
pip install threading
pip install wsgiref
pip install os
```

## Step3

### Use one Git repository for the project

Go to your git account and create a new Repositories.

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin  (https://)
git push -u origin main
```


Each time you update a file you need to do the following steps, repush to git：

```
git add --all
git commit -m 'Your records'
git push origin master
```

## Step4

### Deploy your program to render

- Start by creating a new account with Render (if you don't have one).

- Then, navigate to your dashboard, click on the "New +" button, and select "Web Service".

- Connect your Render account to either your GitHub account.

- Once connected, select the repository to deploy:

```
Name: (e.g.) shopping-test
Environment: Python3
Build command: $ pip install -r requirements.txt
Start command: $ gunicorn shopping:app
```

Click 'Create Web Service'

.....

until build successfully

