# Little Lemon Restaurant API

A Django REST API for managing a restaurant's menu, orders, cart, and user management system. This project provides a complete backend solution for restaurant operations with authentication, authorization, and role-based access control.

## Features

- **Menu Management**: CRUD operations for menu items and categories
- **Shopping Cart**: Add, update, and remove items from cart
- **Order Management**: Create and manage orders with delivery crew assignment
- **User Authentication**: Token-based authentication using Djoser
- **Role-Based Access Control**: Manager and Delivery Crew user groups
- **Rate Limiting**: Throttling to prevent API abuse
- **Pagination**: Efficient data retrieval with paginated responses
- **Search & Filtering**: Search and filter capabilities for menu items and orders

## Tech Stack

- **Django 6.0.1**: Web framework
- **Django REST Framework**: REST API toolkit
- **Djoser**: Authentication library for Django REST Framework
- **SQLite**: Database (default, can be configured for production)
- **Python 3.14**: Programming language

## Prerequisites

- Python 3.14 or higher
- pipenv (for dependency management)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-api-project
   ```

2. **Install dependencies using pipenv**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication Endpoints (Djoser)
- `POST /auth/users/` - Register a new user
- `POST /auth/token/login/` - Login and get authentication token
- `POST /auth/token/logout/` - Logout (requires authentication)

### Menu Items
- `GET /api/menu-items` - List all menu items (paginated)
- `POST /api/menu-items` - Create a new menu item (requires authentication)
- `GET /api/menu-items/<id>` - Get a specific menu item
- `PUT /api/menu-items/<id>` - Update a menu item (requires authentication)
- `PATCH /api/menu-items/<id>` - Partially update a menu item (requires authentication)
- `DELETE /api/menu-items/<id>` - Delete a menu item (requires authentication)

### Categories
- `GET /api/categories` - List all categories
- `POST /api/categories` - Create a new category (requires authentication)

### Cart
- `GET /api/cart/menu-items` - Get current user's cart items
- `POST /api/cart/menu-items` - Add item to cart
- `DELETE /api/cart/menu-items` - Delete all items from cart
- `GET /api/cart/menu-items/<id>` - Get a specific cart item
- `PATCH /api/cart/menu-items/<id>` - Update cart item quantity
- `DELETE /api/cart/menu-items/<id>` - Remove item from cart

### Orders
- `GET /api/orders` - List orders (paginated)
- `POST /api/orders` - Create a new order from cart items
- `GET /api/orders/<id>` - Get a specific order
- `PUT /api/orders/<id>` - Update an order (requires authentication)
- `PATCH /api/orders/<id>` - Partially update an order (requires authentication)
- `DELETE /api/orders/<id>` - Delete an order (requires authentication)

### User Management
- `GET /api/groups/manager/users` - List all manager users
- `POST /api/groups/manager/users` - Assign user to manager group
- `DELETE /api/groups/manager/users/<id>` - Remove user from manager group
- `GET /api/groups/delivery-crew/users` - List all delivery crew users
- `POST /api/groups/delivery-crew/users` - Assign user to delivery crew group
- `DELETE /api/groups/delivery-crew/users/<id>` - Remove user from delivery crew group

## Authentication

The API uses token-based authentication. To authenticate requests:

1. **Register a new user:**
   ```bash
   POST /auth/users/
   {
     "username": "john_doe",
     "email": "john@example.com",
     "password": "securepassword123"
   }
   ```

2. **Login to get a token:**
   ```bash
   POST /auth/token/login/
   {
     "username": "john_doe",
     "password": "securepassword123"
   }
   ```

3. **Use the token in subsequent requests:**
   ```bash
   Authorization: Token <your-token-here>
   ```

## Rate Limiting

The API implements rate limiting to prevent abuse:
- **Anonymous users**: 10 requests per hour
- **Authenticated users**: 5 requests per minute

## Pagination

List endpoints support pagination:
- Default page size: 10 items
- Menu items and orders are paginated
- Use `?page=<number>` to navigate through pages

## Search and Filtering

Menu items support search and filtering:
- **Search**: `?search=<term>` - Search by title or category title
- **Filter**: `?category=<category_id>` - Filter by category

## Project Structure

```
django-api-project/
├── Littlelemon/              # Django project settings
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Root URL configuration
│   └── ...
├── LittlelemonAPI/          # Main application
│   ├── models.py            # Database models
│   ├── views.py             # API view classes
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # API URL patterns
│   └── migrations/          # Database migrations
├── manage.py                # Django management script
├── db.sqlite3               # SQLite database
├── Pipfile                  # Python dependencies
└── README.md                # This file
```

## Database Models

- **Category**: Menu item categories (slug, title)
- **MenuItem**: Individual menu items (title, price, featured, category)
- **Cart**: User shopping cart items (user, menuitem, quantity, prices)
- **Order**: Customer orders (user, delivery_crew, status, total, date)
- **OrderItem**: Items within an order (order, menuitem, quantity, prices)

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Django Admin
Navigate to `http://127.0.0.1:8000/admin/` and login with your superuser credentials.

## License

This project is part of a Coursera Django API course.

## Contributing

This is an educational project. Feel free to fork and modify for learning purposes.
