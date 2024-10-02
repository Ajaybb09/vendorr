# Vendor Management System API

This project is a RESTful API built with **Django** and **Django REST Framework** to manage vendors, track purchase orders, and calculate performance metrics such as on-time delivery rates and quality ratings.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Example API Requests](#example-api-requests)

---

## Features

- **Vendor Management**: Create, update, delete, and retrieve vendor information.
- **Purchase Order Management**: Create, update, delete, and retrieve purchase orders.
- **Performance Metrics Calculation**: Automatically calculates vendor performance metrics based on completed purchase orders.

---

## Technologies Used

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **SQLite** (default database)
- **Postman** or **cURL** for API testing

---

## Setup Instructions

Follow the steps below to set up and run the project locally.

### Prerequisites

Ensure that you have the following installed:

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional but recommended)

### 1. Clone the Repository

Open your terminal and run the following commands:

```bash
git clone https://github.com/Ajaybb09/Vendor
cd vendor_management



# Clone the Repository
git clone https://github.com/Ajaybb09/Vendor
cd vendor_management


# Create and Activate a Virtual Environment

# For Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# For Windows
# python -m venv venv
# venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Set Up the Database
python manage.py migrate

# Create a Superuser (optional)
python manage.py createsuperuser

# Run the Development Server
python manage.py runserver



API 
API Endpoints
1. Vendor Profile Management
HTTP Method	Endpoint	Description
POST	/api/vendors/	     Create a new vendor
GET	/api/vendors/	     List all vendors
GET	/api/vendors/{vendor_id}/	Retrieve a specific vendor
PUT	/api/vendors/{vendor_id}/	Update a vendor's details
DELETE	/api/vendors/{vendor_id}/	Delete a vendor
2. Purchase Order Tracking
HTTP Method	Endpoint	Description
POST	/api/purchase_orders/	Create a purchase order
GET	/api/purchase_orders/	List all purchase orders
GET	/api/purchase_orders/{po_id}/	Retrieve details of a specific purchase order
PUT	/api/purchase_orders/{po_id}/	Update a purchase order
DELETE	/api/purchase_orders/{po_id}/	Delete a purchase order
3. Vendor Performance
HTTP Method	Endpoint	Description
GET	/api/vendors/{vendor_id}/performance/	Retrieve performance metrics for a vendor
