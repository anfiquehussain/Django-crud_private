# Django CRUD Application

A simple CRUD (Create, Read, Update, Delete) application built using the Django framework. This project demonstrates basic CRUD operations on a database using Django's ORM (Object-Relational Mapping).

## Features

- Create new records
- Retrieve and display existing records
- Update existing records
- Delete records

## Installation

### Clone the Repository
```bash
git clone https://github.com/anfiquehussain/Django-crud.git
cd Django-crud
```

### Create and Activate a Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Migrations
```bash
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- **Home Page:** View all records.
- **Add Record:** Use the form to create a new record.
- **Edit Record:** Click on a record to update its details.
- **Delete Record:** Click on a record to delete it.

## Project Structure

```
├───crud_app
│   ├───migrations
│   │   └───__pycache__
│   ├───templates
│   │   └───crud_app
│   └───__pycache__
├───crud_project
│   └───__pycache__
├───media
│   └───products
```

- `crud_app/`: Main Django application directory.
  - `migrations/`: Database migrations.
  - `templates/`: HTML templates for the application.
    - `crud_app/`: Templates specific to `crud_app`.
  - `__pycache__/`: Compiled Python files.
- `crud_project/`: Project configuration directory.
  - `__pycache__/`: Compiled Python files.
- `media/`: Directory for storing media files.
  - `products/`: Directory for product images and files.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Django Documentation: https://docs.djangoproject.com/

## Contact
For any queries or further assistance, please contact [Anfique Hussain V](mailto:anfiquehussain1@example.com).
<p align="left">
<a href="https://dev.to/anfiquehussain" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/devto.svg" alt="anfiquehussain" height="30" width="40" /></a>
<a href="https://twitter.com/anfique_hv" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="anfique_hv" height="30" width="40" /></a>
<a href="https://linkedin.com/in/anfique-hussain-v-aa8841290" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="anfique-hussain-v-aa8841290" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/16822116" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="16822116" height="30" width="40" /></a>
<a href="https://fb.com/100022489001636" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="100022489001636" height="30" width="40" /></a>
<a href="https://instagram.com/anfique_hv" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="anfique_hv" height="30" width="40" /></a>
<a href="https://www.hackerearth.com/@anfiquehussain1" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerearth.svg" alt="@anfiquehussain1" height="30" width="40" /></a>
</p>
