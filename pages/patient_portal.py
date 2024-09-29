import streamlit as st
import requests

# Get the public IP address of the user
ip_request = requests.get('https://api64.ipify.org?format=json')
ip_address = ip_request.json()['ip']

# Get the location information based on the IP address using ipinfo.io
ipinfo_url = f'https://ipinfo.io/{ip_address}/json'
location_request = requests.get(ipinfo_url)
location_data = location_request.json()

# Extract latitude and longitude from the 'loc' field
loc = location_data['loc'].split(',')
latitude = loc[0]
longitude = loc[1]

# Extract the city, region, and country
city = location_data.get('city', 'N/A')
region = location_data.get('region', 'N/A')
country = location_data.get('country', 'N/A')

# Format the address
address = f"{city}, {region}, {country}"

st.write(f"User's location: {address}")