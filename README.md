# Customer_Interaction_Analysis_API
A Django Project for setting up data for user interactions in the database and retrieving analysis through an API

# Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    
- [Usage](#usage)
  - [Endpoints](#endpoints)
    
- [Examples](#examples)

- [Testing](#testing)
  
- [License](#license)

# Getting Started

## Prerequisites

Before you begin, ensure you have met the following requirements:

Python 3.8 or higher installed on your system.
Virtualenv installed to manage Python virtual environments (optional but recommended)

## Installation
1. Clone the project repository:
   run these commands:

git clone https://github.com/ducminh02/Customer_Interaction_Analysis_API.git

cd Customer_Interaction_Analysis_API

  
2. (Optional) Create a virtual environment for the project:

   run these commands:

virtualenv venv
source venv/bin/activate

You need to install the virtual environment if you haven't already done that

sudo apt install python3-virtualenv

pip install virtualenvwrapper

After done using:

deactivate


3. Install project dependencies:

   run this command:

pip install -r requirements.txt



5. Migrate the database and store user_interactions.log into the database:

   run these commands:

python manage.py migrate

python3 manage.py load_user_interactions



6. Start the development server:

   run this command:

python manage.py runserver



Now Customer_Interaction_Analysis_API is up and running locally

# Usage


## Endpoints
The API provides the following endpoint:

'/customer-analysis/{customer_id}/': Customer interaction analysis for a specific customer.

You can make HTTP GET requests to this endpoint to retrieve data.

# Examples


## Retrieve Customer Analysis
To retrieve customer interaction analysis for a specific customer (replace {customer_id} with the actual customer ID), make a GET request to:

http://localhost:8000/customer-analysis/{customer_id}/

# Testing
You can run tests to make sure everything works as intended


python3 manage.py test











