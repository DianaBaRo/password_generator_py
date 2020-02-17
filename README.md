Run the docker-compose up command from the top level directory for your project.
The app should be running at port 8000 on your Docker host.
Make migrations: sudo docker-compose run web python manage.py makemigrations
Run migrations: sudo docker-compose run web python manage.py migrate
Shell: sudo docker-compose run web python manage.py shell
Import your models to the shell: from supergenpy.models import Login
And then you can play with the data: 
Login.objects.all()
Login.objects.create(domain="fromshell")

SuperGenPy

Implementations / Python module (haslib)
Test Selenium (headless browser)
Hypothesis (Unit test)