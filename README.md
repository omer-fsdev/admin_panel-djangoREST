# Admin Panel - Django REST Framework

Admin Panel Django RestFramework is a backend website that provides a comprehensive admin panel with detailed features for managing your web application. It is designed specifically for backend tasks and leverages the capabilities of Django Rest Framework. The project includes the integration of Grappelli, a modern theme that enhances the admin interface, and also incorporates import-export functionality for seamless data management.

## Key Features

- Detailed Admin Panel: Access an extensive set of features to manage your web application, including user permissions, content management, and system settings.
- Django Rest Framework Integration: Benefit from the powerful Django Rest Framework to create a robust and flexible API backend for seamless data management and interaction.
- Grappelli Integration: Enhance the admin interface with Grappelli, a sleek and modern theme that improves the visual appeal and usability of the admin panel.
- Import-Export Functionality: Simplify data management with the ability to import and export data in various formats such as CSV, JSON, and Excel.

## Installation

To run the Blog App locally, please follow these steps:

1. Clone the repository:

```
git clone https://github.com/omer-fsdev/admin_panel-django_REST.git
```

2. Navigate to the project directory:

```
cd admin_panel-django_REST
```

3. Create a virtual environment:

```
python3 -m venv env
```

4. Activate the virtual environment:

- For Windows:
  ```
  .env\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source env/bin/activate
  ```

5. Install the project dependencies:

```
pip install -r requirements.txt
```

6. Set up the database:

- Modify the database settings in the `settings.py` file to match your environment.
- Run the following command to migrate the database:
  ```
  python manage.py migrate
  ```

7. Start the development server:

```
python manage.py runserver
```

8. Access the application in your web browser at `http://localhost:8000/admin`.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
