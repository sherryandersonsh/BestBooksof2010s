CREATE TABLE books
(
    id         serial,
    title      varchar(200),
    author     varchar(200),
    rating     varchar(200),
    booklink   varchar(200),
    pages      varchar(50),
    bookformat varchar(50),
    genre      varchar(50),
    language   varchar(50)
);

--I extracted from the rating column the avg rating and the total ratings. Removed the word pages from the pages column
select title,
       author,
       right(substring(rating, 1, strpos(rating, 'avg') - 2), 4)      as AverageRating,
       split_part(substring(rating, strpos(rating, '—') + 2), ' ', 1) as TotalRatings,
       split_part(substring(pages, strpos(pages, '—')), ' ', 1)       as NumberofPages,
       genre,
       bookformat,
       language
from books;