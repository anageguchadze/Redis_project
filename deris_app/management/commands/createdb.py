import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'Create a PostgreSQL database'
    def handle(self, *args, **kwargs):
        database_name = connections['default'].settings_dict['NAME']
        database_user = connections['default'].settings_dict['USER']
        database_password = connections['default'].settings_dict['PASSWORD']
        database_host = connections['default'].settings_dict['HOST']
        database_port = connections['default'].settings_dict['PORT']

        try: 
            conn = psycopg2.connect(
                dbname='postgres',
                user=database_user,
                password=database_password,
                host=database_host,
                port=database_port
            )
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            cursor.execute(f'SELECT 1 FROM pg_database WHERE datname = \'{database_name}\'')
            if not cursor.fetchone():
                cursor.execute(f'CREATE DATABASE {database_name}')
                self.stdout.write(self.style.SUCCESS(f'Database {database_name} created successfully'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Database {database_name} already exists'))
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            self.stdout.write(self.style.ERROR(f'Error creating database: {e}'))