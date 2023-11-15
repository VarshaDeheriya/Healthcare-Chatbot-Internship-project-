import requests
from bs4 import BeautifulSoup

# Set the URL of the page to scrape
url = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z'

# Send a request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
anchors = soup.find_all('a')

# Extract the links that lead to illness pages
illness_links = set()
for link in anchors:
    href = link.get('href')
    if href and 'illnesses-and-conditions/a-to-z' in href:
        illness_links.add('https://www.nhsinform.scot' + href)

# Scrape the health topics for each illnessContinued from the previous message...


for illness_link in illness_links:
    # Send a request to the illness page
    response = requests.get(illness_link)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the list of health topics
    health_topics = soup.find('div', {'class': 'js-guide cf guide'})

    if health_topics:
        # Extract the health topics
        health_topic_items = health_topics.find_all(['p', 'h2'])
        for item in health_topic_items:
            print(item)