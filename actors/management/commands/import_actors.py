from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from actors.models import Actor
import pandas as pd
from tqdm import tqdm


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores'
        )
    

    def handle(self, *args, **options):
        file_name = options['file_name']

        df = pd.read_csv(file_name)
        
        for index, row in tqdm(df.iterrows(), total=df.shape[0]):
            name = row['name']
            birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
            nationality = row['nationality']

            Actor.objects.create(
                name=name,
                birthday=birthday,
                nationality=nationality,
                )   
        
        self.stdout.write(self.style.SUCCESS('ATORES ADICIONADOS COM SUCESSO!'))