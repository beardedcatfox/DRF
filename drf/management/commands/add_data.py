from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from drf.models import Comment, Post

from faker import Faker


class Command(BaseCommand):
    help = 'Generate test data'

    def add_arguments(self, parser):
        parser.add_argument('users', type=int)
        parser.add_argument('posts', type=int)
        parser.add_argument('comments', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        num_users = options['users']
        num_posts = options['posts']
        num_comments = options['comments']

        users = []
        for i in range(num_users):
            username = fake.user_name()
            email = fake.email()
            user = User(username=username, email=email)
            user.set_password('password')
            user.save()
            users.append(user)

        for user in users:
            for i in range(num_posts):
                title = fake.sentence()
                content = fake.paragraph()
                post = Post(title=title, content=content, author=user)
                post.save()

                for j in range(num_comments):
                    text = fake.paragraph()
                    comment = Comment(text=text, post=post, author=user)
                    comment.save()
