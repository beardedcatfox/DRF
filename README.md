# DRF

## Add basic DRF authentification functions + by Token (djoser)
### Tested via Postman

```bash
    pip install -r requirements.txt
```
```
    python manage.py makemigrations
```
```
    python manage.py migrate
```
### Add 5 users, 5 posts for each user, 3 comments for each post

```
    python manage.py add_data 5 5 3
```
### Or download testdev fixtures from json file
```
    python manage.py loaddata fixtures.json
```

```
    python manage.py createsuperuser --username=admin --email=admin@example.com
```
```bash
    ./manage.py runserver
```

# LINKS
#### [Create User](http://127.0.0.1:8000/auth/users/) 
#### [Token Create](http://127.0.0.1:8000/auth/token/create/)
#### [Login](http://127.0.0.1:8000/api-auth/login/?next=/posts/)
#### [Post List](http://127.0.0.1:8000/posts/)
#### [Comments](http://127.0.0.1:8000/comments/)
