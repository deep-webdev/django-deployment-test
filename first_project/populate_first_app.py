import email
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, WebPage, Topic, Users
from faker import Faker

fakegen = Faker()
topics = ['Social', 'Search', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):
        #get the topic 
        top = add_topic()

        #create Fake data 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()
        
        #create Fake Webpage
        webpg = WebPage.objects.get_or_create(topic= top, url=fake_url, name=fake_name)[0]
        
        #create Fake Access Record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        
        #create Fake Users Records
        Users.objects.get_or_create(first_name= fake_fname, last_name= fake_lname, email= fake_email)[0]
        
if __name__ == '__main__':
    print("Populating Scriptssss!!!!")
    populate(20)
    print("Population Complete....")




