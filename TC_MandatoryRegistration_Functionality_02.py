import datetime
import requests


specific_time = datetime.datetime(2023,5,31,2,0,0)

datetime.datetime = classmethod(lambda cls: specific_time)

pages = [
    "post-insert",
    "post-insert-images",
    "post-insert/$idannuncio$/",
    "post-promote/i/",
    "feedback/post-publish-email/",
    "post-edit/"
]
for page in pages:
    url = "https://example.com/{}".format(page)  # Replace "example.com" with the actual domain
    
    # Send a GET request to the page
    response = requests.get(url, timeout=5)
    
    # Check if the response is a redirection
    if response.history:
        final_url = response.url
        print("Page {} got redirected to: {}".format(page, final_url))
    else: 
        print("Page {} is accessible".format(page))
