# RentEasy

## Introduction
RentEasy is a web application designed to streamline the process of managing rental properties for landlords and finding rental properties for tenants. It provides a user-friendly platform for listing properties, searching for rentals, and facilitating communication between landlords and tenants.

- **Deployed Site**: [RentEasy](https://renteasy-1.onrender.com/)
- **Final Project Blog Article**: [RentEasy Blog Article](https://www.linkedin.com/pulse/welcome-renteasy-jefferson-trapkid-svcoe)
- **Author LinkedIn**: [Your LinkedIn Profile]( https://www.linkedin.com/in/jefferson-trapkid-2a5b07239/)


## Installation

To install and run the RentEasy application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jeffer-thebandit/renteasy.git
   cd renteasy
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database:**
   Create a PostgreSQL database and update the `DATABASES` setting in `renteasy/settings.py` with your database information.

5. **Run the migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

RentEasy allows users to:

- **For Landlords:**
  - Create and manage property listings
  - Upload property images
  - Set rental prices and specify property details
  - Communicate with potential tenants

- **For Tenants:**
  - Search for rental properties using various filters (location, price range, amenities, etc.)
  - View detailed property information and images
  - Contact landlords directly through the platform
  - Submit rental applications

## Contributing

We welcome contributions to RentEasy! To contribute:

1. **Fork the repository:**
   Click the "Fork" button at the top right corner of this page.

2. **Clone your forked repository:**
   ```bash
   git clone https://github.com/jeffer-thebandit/renteasy.git
   cd renteasy
   ```

3. **Create a new branch for your feature or bugfix:**
   ```bash
   git checkout -b feature-or-bugfix-name
   ```

4. **Make your changes and commit them:**
   ```bash
   git commit -am 'Add some feature or fix some bug'
   ```

5. **Push your changes to your forked repository:**
   ```bash
   git push origin feature-or-bugfix-name
   ```

6. **Create a pull request:**
   Go to the original repository and create a new pull request with a description of your changes.

## Related Projects

- [Awesome Property Management](https://github.com/awesome/property-management)
- [Rental Manager](https://github.com/rental/manager)

## Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Resources


Feel free to explore, use, and contribute to RentEasy. Your feedback and contributions are highly valued!
