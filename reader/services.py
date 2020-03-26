import csv

from reader.models import DataStore
import os
from dataRead.settings import BASE_DIR



def data_read_service(csv_path):
    csv_path = os.path.join(BASE_DIR, csv_path)
    print(csv_path)
    try:
        with open(csv_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                email = row.get('Email')
                f_name = row.get('firstName')
                address = row.get('Address')
                phone = row.get('phoneNumber')
                DataStore.objects.get_or_create(email=email, f_name=f_name, address=address, phone=phone)
        csvfile.close()
        return True
    except Exception as e:
        print(e)
        return False
