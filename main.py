from bs4 import BeautifulSoup
import requests
import time
import psycopg2

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}


time.sleep(3)
# Create the URLs for each page in the 2010s Best of Decade List

url = 'https://www.goodreads.com/list/best_of_decade/2010?id=4093.Best_Books_of_the_Decade_2010s&page={}'

# Function to save the data to database
def savedata():

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Polopo00!",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="GR2010sBestBooks")
        cursor = connection.cursor()

        dbquery = "INSERT INTO books (title, author, rating, booklink, pages, bookformat, genre, language) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        datainsert = (title, author, rating, book_link2, numpages, bookformat, genre, language)
        cursor.execute(dbquery, datainsert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Data inserted successfully")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert data", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


for page in range(1, 2):
    urllinks = url.format(page)
    page = +1
    print(urllinks)

    # Sends a get request using Beautiful soup
    grmainpage = requests.get(urllinks)
    data = grmainpage.text
    soup = BeautifulSoup(data, "html.parser")
    books = soup.find_all("tr", {"itemtype": "http://schema.org/Book"})  # Pulls all the titles listed on the page

    # Pulls the title, author, rating and link of each book on the page
    for book in books:
        title = book.find("a", {"class": "bookTitle"}).text
        author = book.find("a", {"class": "authorName"}).text
        rating = book.find("span", {"class": "minirating"}).text
        book_link1 = book.find("a", {"itemprop": "url"}).get('href')
        book_link2 = "https://www.goodreads.com/" + book_link1

        # Sends a request to the book page and pulls the book format, # of pages, genre and language
        grbookpage = requests.get(book_link2)
        databookpage = grbookpage.text
        soupbookpage = BeautifulSoup(databookpage, "html.parser")
        bookformat = soupbookpage.find("span", {"itemprop": "bookFormat"}).text
        numpages = soupbookpage.find("span", {"itemprop": "numberOfPages"}).text
        genre = soupbookpage.find("a", {'class': 'actionLinkLite bookPageGenreLink'}).text
        language = soupbookpage.find("div", {"itemprop": "inLanguage"}).text

        print('Book Title:', title.strip(), '\nAuthor:', author, '\nRating:', rating, '\nLink:', book_link2,
              '\nNumber of Pages:', numpages, '\nBook Format:', bookformat, '\nGenre:', genre, '\nLanguage:',
              language,
              '\n---')
        savedata()

