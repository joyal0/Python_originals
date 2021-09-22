#This is a url shortener with api from the website oke.io 
import requests
access_token = 'your_oke.io_access_token'

# Shorten long URL
custom_alias = input("Enter the custom alias you would like for the shortened url \n")      #the returned shortened url will be of the form https://www.oke.io/{custom_alias} if alias available
long_url = "your_website_address_that_need_to_be_shortened"
api_url = f"https://oke.io/api/?api={access_token}&url={long_url}&alias={custom_alias}"
shortened_url = requests.get(api_url).json()
if shortened_url['status'] == 'success':
    print ("Short URL is ",shortened_url['shortenedUrl'])
elif shortened_url['status'] == 'error':
    print("Error and Message is ",shortened_url['message'])

