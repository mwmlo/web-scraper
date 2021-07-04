from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once"

# Retrieve web page
client = urlopen(my_url)
page_html = client.read()
client.close()

# Parse HTML
page_soup = soup(page_html, "html.parser")

# Extract books
containers = page_soup.findAll("tr", {"itemtype": "http://schema.org/Book"})

# Create CSV
filename = "goodreads.csv"
f = open(filename, "w")
headers = "title, author, image, rating\n"
f.write(headers)

# Extract attributes
for container in containers:
    title = container.find("a", {"class": "bookTitle"}).text.strip()
    title = title.replace(",", "")
    author = container.find("a", {"class": "authorName"}).text.strip()
    image = container.find("img", {"class": "bookCover"})["src"]
    rating = container.find("span", {"class": "minirating"}).text.strip()
    rating = rating.split()[0]

    f.write(title + "," + author + "," + image + "," + rating + "\n")

f.close()