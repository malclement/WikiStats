# AXONEPRO Python Test


## Title
Big word search

## Abstract
Create a django project analyse whether a particular wikipedia page includes alot of big words.

1. create new branch off of main
	- create django project (follow tutorial https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
	- create app called wiki_stats
	- create services.py file in wiki_stats app
	- In services.py, write a function to fetch summary section of a wikipedia page by passing title argument and using wikipedia api.
	- In services.py, write a second function to interpret the amount of 5+ letter words in the summary section.
	- Return an alert in the second function if more than 20% of words are 5+ letter words.
	- Send an email if an alert exists (https://docs.djangoproject.com/en/3.2/topics/email/)
	- create a function based view in wiki_stats/views (use api_view from django rest framework : https://www.django-rest-framework.org/api-guide/views/#api_view)
		- input request.GET.get('title') and return results of service in previous steps
	- add a unit test for whatever you think is a good idea to test
	- capture screenshot of browser with view response
	- add requirements.txt file with project dependencies
	- add README for how to run your project
13. create pull request of your branch pointing to branch:main with screenshot in PR description
14. email pflih@ooti.co once PR is ready

Goodluck !


Warning : 	
	To be able to send email using gmail you now need to generate a custom password for an application
	https://support.google.com/accounts/answer/185833
	You then need to replace fields in settings.py file with your personal values: 
		- EMAIL_HOST_USER: your email address
		- EMAIL_HOST_PASSWORD : your custom app password


To run the project you may:
	- install the requirements
	- locate yourself in the folder containing the manage.py file
	- run the command : python manage.py runserver

To run the tests you may use the following command line: python manage.py test wiki_stats.tests

This API uses three different endpoints:
	- /wikistats : for the Homepage
	- /wikistats/{wikipedia's page title} : to retrieve the page summary
	- /wikistats/{wikipedia's page title}/words : to check summary word lengh# WikiStats
