# importing required modules

from bs4 import BeautifulSoup
import requests
import csv

# Base URL of the website ({} will be replaced with page numbers)
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

all_books = []

# The website contains 50 pages of books
for page in range(1, 51):
    
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all book containers on the page
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.replace("£","")
        
        all_books.append([title, price])

    print(f"Page {page} scraped")

# Create and write data into CSV file
with open("books_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title","Price"])
    writer.writerows(all_books)


print(f"Done! Saved {len(all_books)} books to CSV")

