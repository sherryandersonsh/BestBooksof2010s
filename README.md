# Goodreads 2010s Best Books Project

## Project Status: In Progress

## _Project Overview_
* Scraped over 6,000 books from Goodreads 2010s Best Books list using Beautiful Soup and Requests.
* Created a function to save the data to a PostgreSQL database.



## Packages and Tools
**Python Version:** 3.9.  
**Packages:** beautifulsoup, requests, time, psycopg2.   
**IDE:** PyCharm

## Tutorials and Articles Used
**Scraper Article:** <https://medium.com/technofunnel/web-scraping-with-python-using-beautifulsoup-76b710e3e92f>  
**Connecting to DB Articles:** <https://pynative.com/python-postgresql-tutorial/#h-python-postgresql-database-connection>

## Web Scraping
I scraped 69 pages from this [book list](https://www.goodreads.com/list/best_of_decade/2010?id=4093.Best_Books_of_the_Decade_2010s&page=1). The following was collected:  
* Book Title. 
* Author
* Average Rating
* Total Ratings
* Book Link
* Book Format
* Number of Pages
* Genre
* Language



```python
for page in range(1, 70):
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
        try:
            bookformat = soupbookpage.find("span", {"itemprop": "bookFormat"}).text
        except AttributeError:
            print('No book format')
        try:
            numpages = soupbookpage.find("span", {"itemprop": "numberOfPages"}).text
        except AttributeError:
            print('No page number')
        try:
            genre = soupbookpage.find("a", {'class': 'actionLinkLite bookPageGenreLink'}).text
        except AttributeError:
            print('No genre')
        try:
            language = soupbookpage.find("div", {"itemprop": "inLanguage"}).text
        except AttributeError:
            print('No language')

        print('Book Title:', title.strip(), '\nAuthor:', author, '\nRating:', rating, '\nLink:', book_link2,
              '\nNumber of Pages:', numpages, '\nBook Format:', bookformat, '\nGenre:', genre, '\nLanguage:', language,
              '\n*')
```

## Storing the data

In progress

## Data Cleaning

In Progress

## Exploratory Data Analysis
In Progress

## Data Visualization
In Progress
