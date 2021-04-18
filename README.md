# django-blog
It is a blog written in python using django it has many functionally
>
> - Home, About, Blog Home, Contact Page
> - Functional Contact Form
> - Functional Blog Home Page and Blog Post
> - Functional Contact From
> - More Comming (This Project is Under Development)
>

Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/Sadman-Sakib2234/django-blog.git
```
Install Dependencies 

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

After all these steps , you can start testing and developing this project. 

Run
```
python manage.py runserver
```
then checkout http://127.0.0.1:8000/ the project will be running

<hr/>
you can use the shell script to start fast i dont recommend that
```
bash run.sh
```