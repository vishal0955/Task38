import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = 'https://indianexpress.com/article/cities/mumbai/plane-grounded-in-france-over-human-trafficking-lands-in-mumbai-9082765'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print the soup to see the HTML structure
    print(soup.prettify())

    # Adjust these based on actual HTML structure
    title_tag = soup.find('h1')
    content_tag = soup.find('div', {'class': 'article'})

    # Check if the elements are found before trying to access their attributes
    if title_tag:
        title = title_tag.text.strip()
    else:
        title = "Title not found"

    if content_tag:
        content = content_tag.text.strip()
    else:
        content = "Content not found"

    # Extracting images (optional)
    images = [img['src'] for img in soup.find_all('img', src=True)]

    return {
        'title': title,
        'content': content,
        'images': images
    }

if __name__ == "__main__":
    data = scrape_data()
    print(data)
