from django.core.management.base import BaseCommand

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


class Command(BaseCommand):
    help = "Populate Job Tables"

    def handle(self, *args, **kwargs):

        for i in range(20):
            fdate = fake.date()
            fcompany = fake.company()
            ftitle = fake.random_element(elements=('Project Manager','Teamlead','Software Engineer'))
            feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
            faddress = fake.address()
            femail = fake.email()
            fphonenumber = phonenumbergen()

            HyderabadJobs.objects.get_or_create(
                date=fdate,
                company=fcompany,
                title=ftitle,
                eligibility=feligibility,
                address=faddress,
                email=femail,
                phone_number=fphonenumber
            )

            ChennaiJobs.objects.get_or_create(
                date=fdate,
                company=fcompany,
                title=ftitle,
                eligibility=feligibility,
                address=faddress,
                email=femail,
                phone_number=fphonenumber
            )

            BangaloreJobs.objects.get_or_create(
                date=fdate,
                company=fcompany,
                title=ftitle,
                eligibility=feligibility,
                address=faddress,
                email=femail,
                phone_number=fphonenumber
            )

            PuneJobs.objects.get_or_create(
                date=fdate,
                company=fcompany,
                title=ftitle,
                eligibility=feligibility,
                address=faddress,
                email=femail,
                phone_number=fphonenumber
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Records inserted successfully'
            )
        )