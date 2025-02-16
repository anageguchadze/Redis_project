# Redis_project

This project is a Django-based REST API for managing animal categories and animal details. It includes filtering, pagination, and RESTful endpoints using Django REST Framework (DRF) and Django Filters.

## Features
- Django 5.1.6
- REST API with Django REST Framework
- Redis support (to be configured)
- Animal and Category models
- Filtering, searching, and pagination

## Installation

### 1. Clone the Repository
git clone https://github.com/anageguchadze/Redis_project.git
cd Redis_project


### 2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Apply Migrations
python manage.py migrate


### 5. Run the Server
python manage.py runserver


### 6. Redis Setup (Optional)
- Install Redis on your machine.
- Start Redis server.
- Add Redis configurations in `settings.py`.

## API Endpoints
- **Categories:**
  - `GET /categories/` - List all categories
  - `POST /categories/` - Create a new category
  - `GET /categories/{id}/` - Retrieve a specific category
  - `PUT/PATCH /categories/{id}/` - Update a category
  - `DELETE /categories/{id}/` - Delete a category

- **Animals:**
  - `GET /animals/` - List all animals
  - `POST /animals/` - Create a new animal
  - `GET /animals/{id}/` - Retrieve a specific animal
  - `PUT/PATCH /animals/{id}/` - Update an animal
  - `DELETE /animals/{id}/` - Delete an animal

## Configuration for Redis Cache (Optional)
Add the following to your `settings.py`:
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

## License
This project is licensed under the MIT License.