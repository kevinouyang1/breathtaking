## Backend for Breathtaking

# Setup

Virtual environments need to be setup. Ensure you have venv and Python 3.9 installed. Setup the virtual environment and packages using:

python3.9 -m venv env

Activate Python virtual environment when developing using:

*NAVIGATE TO THE BACKEND DIRECTORY FIRST*

source env/bin/activate


# Functionality

We will use backend to handle route calculations and creation. Pass origin coordinates and destination coordinates to the endpoint, and we generate the path taken. Pass this back to the frontend in some sort of XML or JSON format, specifying all details for creating the route. Then, use frontend to handle the route configurations on the google maps screen.
