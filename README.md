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
