import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_personal_blog.settings')

django.setup()

##Faker pop scripts, fill random data
import random
from sergiu_website.models import User

from faker import Faker
fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first = fake_name[0]
        fake_last = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_first, last_name = fake_last,
                                          email = fake_email)[0]
        
if __name__ == '__main__':
    print("populatinr script!")
    populate(20)
    print("Done")

