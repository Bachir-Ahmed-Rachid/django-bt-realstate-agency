# django-bt-realstate-agency
This is a Django-based real estate listings web application that allows users to browse and search for properties along with the owner's contact information.



![7](https://github.com/Bachir-Ahmed-Rachid/django-bt-realstate-agency/assets/99692801/58b8c260-82eb-45c9-a4db-681f0bdfbb60)
![2](https://github.com/Bachir-Ahmed-Rachid/django-bt-realstate-agency/assets/99692801/e5df282c-1bc3-4592-b871-05007344fece)
![3](https://github.com/Bachir-Ahmed-Rachid/django-bt-realstate-agency/assets/99692801/f9395bf0-8a8a-4fa8-b6cf-87740ce4aaad)
![4](https://github.com/Bachir-Ahmed-Rachid/django-bt-realstate-agency/assets/99692801/5400fbc1-f4c5-42a4-bf9d-a01b44bc7389)
![5](https://github.com/Bachir-Ahmed-Rachid/django-bt-realstate-agency/assets/99692801/fff1e202-2d86-4b69-8000-69864e944f43)
![6](https://github.com/Bachir-Ahmed-Rachid/django-bt-realstate-agency/assets/99692801/f52e758c-215e-48bd-8c57-e7d4f6d7f909)

## Overview
The Django-based real estate listings web application allows users to browse and search for properties along with the owner's contact information. The site includes features such as user authentication, property listing, search functionalities, contact information, and pagination. 

## Features
### User Authentication
The application includes user authentication to ensure that only registered users can post properties and contact owners.

### Property Listing
The web application allows property owners to list their properties along with their details such as property type, location, price, and images.

### Search Functionalities
Users can search for properties using keywords, location, and price ranges. The search results are displayed with relevant details such as the property type, location, and price.

### Contact Information
The contact information of the property owners is displayed alongside the property details, allowing users to easily contact the owners for further information.

### Pagination
The web application implements pagination for search results and property listings, allowing users to navigate easily through large sets of data.

## Technologies Used
The application is built using the Model-View-Template (MVT) architecture and uses a PostgreSQL database to store data. The front-end is designed using Bootstrap and jQuery, and the back-end includes various Django packages such as django-crispy-forms and django-pagination. The site is deployed on Heroku and uses Git for version control.

## Installation
Sure, here's a detailed installation guide for the Django real estate listings web application:

1. Clone the repository:
   ```
   git clone https://github.com/Bachir-Ahmed-Rachid/django-bt-realstate-agency.git
   ```

2. Navigate to the project directory:
   ```
   cd django-bt-realstate-agency
   ```

3. Create a virtual environment for the project:
   ```
   python3 -m venv env
   ```

4. Activate the virtual environment:
   ```
   source env/bin/activate  # for Linux/Mac
   env\Scripts\activate    # for Windows
   ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. Create a PostgreSQL database and update the database credentials in the `settings.py` file.

7. Run database migrations:
   ```
   python manage.py migrate
   ```
9. Start the development server:
   ```
   python manage.py runserver
   ```

10. Open a web browser and go to http://localhost:3000 to access the real estate listings web application.

Note: For production deployment, make sure to update the `SECRET_KEY`, `DEBUG`, and other settings in `settings.py`. Also, consider using a web server like Apache or Nginx to serve the application.

## Conclusion
The Django-based real estate listings web application is an easy-to-use and effective way to browse and search for properties, and contact property owners. With its user authentication, search functionalities, and pagination, it provides a seamless experience for users.
