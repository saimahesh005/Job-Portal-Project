import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobproject.settings')

import django
django.setup()



from jobapp.models import *
from faker import Faker
from random import randint

fake = Faker()
def phonenumbergen():
    d1 = randint(7, 9)
    num = str(d1)
    
    for i in range(9):
        num = num + str(randint(0, 9))
    
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Teamlead', 'Software Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()

        hyderabad_record = HyderabadJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phone_number=fphonenumber
        )

        chennai_record = ChennaiJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phone_number=fphonenumber
        )

        Bangalore_record = BangaloreJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phone_number=fphonenumber
        )

        PuneJobs_record = PuneJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phone_number=fphonenumber
        )

populate(20)
print("Records inserted successfully")