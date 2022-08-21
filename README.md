# walmart_scarper

Step-by-step tutorial: [Product Review Scraper](https://youtu.be/yuVGiVKbz9I)
Scrape Walmart product reviews using Selenium &amp; BeautifulSoup
WALMART SCRAPER - PREET SHAH

(a) How you have implemented the scraper, what challenges you faced and how did you solve them?

• I have implemented the scraper using Selenium on Chrome along with Beautiful Soup.
The first challenge I faced was the code showed an error to find the see all review buttons as it took time to load. I tried the errorexception to wait till the element loads and also implicitly set the element as tyhe condition but to no good. Finally, I explicitly set the timer to 5 seconds and it works well.

• The titles of the reviews were a task to scrape as there were missing values. I tried alot of things but finally, I used the length of the list containing the tags for the titles under the review header as a boolean to whether append our tile list by the title or a nan value.

• The page had more review ratings than the number of reviews(average rating, etc) so pandas would show a size mismatch error. I implemented a match on the parent class to just get the actual rating values.

• I had problems running the chromedriver on brave; My IDE would sometimes crash after certain iterations of the next page(maybe because my RAM would bottleneck); the Xpath format was really tricky to figure out.

(b) What else you could do to improve your scraper?

• OOPS.

• Instead of parsing the website, we can just pass the product name and create an action chain to type it in the search bar.

• We can integrate multiple online shopping platforms.

(c) How would you design it to make it work on other retailers as well?

• For other retailers, simply changing the url would work as each product has a unique id.

• For other platforms, the tags and class names of the buttons would be different. So, we can add them in the script and make them work by querying the string of the url.
