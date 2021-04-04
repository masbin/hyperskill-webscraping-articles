# hyperskill-webscraping-articles
Web Scraping project built as part of hyperskill 

##Scraping nature.com articles
Find articles based on specified category, save them in txt within folder of pages

###Objectives
This is a web scrapper for https://www.nature.com/nature/articles that take two parameters from the user input:
 1. the number of pages (an integer) and 
 2. the type of articles (a string). 

The integer with the number of pages specifies the number of pages on which the program will look for the articles.

 
It will create a directory named Page_N (where N is the page number) for each page in the desired category, and put all the articles that are found on the page with the matched type to this directory.
Save the articles to separate *.txt files.

The program takes two input values from the user and then continues to process the Nature website data.

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.


' > 4

' > Nature Briefing


Modules used:
- BeautifulSoup
- Requests
- os
details can be seen in requirement.txt

