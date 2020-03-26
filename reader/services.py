import csv

from reader.models import DataStore
import os
from dataRead.settings import BASE_DIR

import csv
import requests




def data_read_service(csv_path, external_link):
    try:
        if external_link:
            with requests.Session() as s:
                download = s.get(csv_path)
                decoded_content = download.content.decode('utf-8')
                reader = csv.DictReader(decoded_content.splitlines(), delimiter=',')
                for row in reader:
                    email = row.get('Email')
                    f_name = row.get('firstName')
                    address = row.get('Address')
                    phone = row.get('phoneNumber')
                    if email and f_name:
                        DataStore.objects.get_or_create(email=email, f_name=f_name, address=address, phone=phone)
        else:
            csv_path = os.path.join(BASE_DIR, csv_path)
            print(csv_path)
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
