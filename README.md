# News-App-Project

NEWSAPP PROJECT

A HTTP service that accepts an RSS URL and displays it out on a web page in a simple but visually appealing manner.
A Django based News WebApp. This WebApp basically renders the frontend which shows some details of the newsfeed like a headline, the main image and a small snippet of the article.

Requirements (Tested on):

Python 3:
Python is an interpreted, object oriented and high level programming language used for creating web applications and dynamic web content. 

django 2.1.12 (‘pip install django==2.1.12’ on cmd):

Django is a frame work which is used to create web based applications
Django uses MVC(Model View Controller) pattern as MVT(Model View Template) with minimal changes.

feedparser==5.2.1 (‘pip install feedparser’ on Shell):

STEPS TO PARSE WEBSITE CONTENTS
>>>python manage.py shell (To enter into shell on cmd)
>>>import feedparser (importing feedparse onto our project)
>>>parsed = feedparser.parse(‘website_link’)
>>>parsed (hit enter. This displays all the website content in the form of a dictionary).

Then we append dictionary to the articles list at the end of function to return those articles

Frontend: Used HTML, CSS, Bootstrap. Frontend shows some details of the newsfeed like a headline, the main image and a small
Backend: Python
API Endpoints: GET http://localhost:8000 This endpoint renders a news app in the browser.

Please refer the documents 'Deploying to GitHub doc.txt' and 'Deploying to Heroku doc.txt' for step by step procedure on deploying our project or app on GitHub account and Heroku Server.

Heroku subdomain name given: readnewsongo

Newsapppro is deployed on Heroku server with below link.
https://readnewsongo.herokuapp.com/

