# For processing HTML
from BeautifulSoup import BeautifulSoup

# Fetch the Post's Advanced Search results for 'the.' urllib allows passing of HTML data
# The Post uses the Lucene Java search library to construct URLs
import urllib
import urllib2

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

data = {
	'st': 'the',
	'sd': '10/01/2011-10/20/2011',
	'target': 'adv_article',
	'srchType': 'advSearch',
	'range': 'cust'
}
headers = { 'User-Agent' : user_agent }
url_values = urllib.urlencode(data)

url = 'http://www.washingtonpost.com/newssearch/search.html'
full_url = url + '?' + url_values
data = urllib2.urlopen(full_url)
print(full_url)

# Get access to the HTML we're looking to parse
f = urllib2.urlopen(data)
html_data = f.read()

# Now we have the HTML string. Let's make soup
soup = BeautifulSoup(html_data)

# Get the section of our document that has the search results
result_uls = soup.findAll('ul', attrs={'class': 'adv-results-list'})

# Set up storage for our result urls
urls = []

# We only expect to have one section here but will loop just in case
for result_ul in result_uls:
# Get the individual search results items and iterate through them
	result_lis = result_ul.findAll('li')
	for result_lis in result_lis:
# Find the first link in each item
		result_as = result_lis.findAll('a', limit=1)
		for result_a in result_as:
		# Store the href attribute (i.e. the actual URL in our list of result URLs)
			urls.append(result_a['href'])
			
## NEXT STEPS
# build in paging to go through multiple pages of search results (reconstruct advacned search URL
# plug it into mediacloud via an API wrapper http://webpy.org/
# The urllib module has been split into parts and renamed in Python 3.0 to urllib.request, urllib.parse, and urllib.error. 
# Update remainder to Python 3.0 with 2to3 tool: http://docs.python.org/library/2to3.html#to3-reference