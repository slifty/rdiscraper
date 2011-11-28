# For processing HTML
from BeautifulSoup import BeautifulSoup

# Fetch the Times's Advanced Search results for 'the.' urllib allows passing of HTML data
# The Times has several searches, including a Beta, an Archive from 1851-1980, and an archive since 1981

import urllib
import urllib2
import sys

def fetch_page(date, page): 
	# 
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	# unique
	query_args = {
		'Query': 'redskins',
		'mon1': start_month,
		'day1': start_day,
		'year1': start_year,
		'mon2': end_month,
		'day2': end_day,
		'year2': end_year,
		'daterange': 'period',
		# or change this to results_loop
		'frow': page * results_per_page,
		'n': results_per_page
		}
		
	headers = { 'User-Agent' : user_agent }
	# Turns the array into query arguments for the URL
	url_args = urllib.urlencode(query_args)
	# unique
	base_url = 'http://query.nytimes.com/search/alternate/query'
	full_url = base_url + '?' + url_args
	page_handle = urllib2.urlopen(full_url)
	print(full_url)
	
	# Get access to the HTML we're looking to parse
	html_data = page_handle.read()
	# print html_data
	
	# Have BeautifulSoup parse the HTML into a tree of objects we can use
	soup = BeautifulSoup(html_data)
	return soup
	
def get_links(soup):
	# Find all the story urls we care about
	# Get the unique section of our document that has the search results
	result_ols = soup.findAll('ol', attrs={'class': 'srchSearchResult'})
	# Set up storage for our result urls
	urls = []
	# We only expect to have one section here but will loop just in case
	for result_ol in result_ols:
	# Get the individual search results items and iterate through them
		result_lis = result_ol.findAll('li')
		for result_lis in result_lis:
	# Find the first link in each item
			result_as = result_lis.findAll('a', limit=1)
			for result_a in result_as:
			# Store the href attribute (i.e. the actual URL in our list of result URLs)
				urls.append(result_a['href'])
	return urls

current_page_number = 0
start_month = '01'
start_day = '01'
start_year = '2001'
end_month = '01'
end_day = '01'
end_year = '2002'
results_per_page = '50'

# need to define this
current_date = 0

# need to loop this?
# results_loop = '0' + results_per_page

all_urls = []


more_pages = True
while more_pages:
	# page contains Next >>
	# "Next chr(175)"
	page = fetch_page(current_date, current_page_number)
	page_links = get_links(page)
	if len(page_links)==0:
		more_pages = False
	else:
		all_urls = all_urls + page_links
		current_page_number = current_page_number + 1
print all_urls

## NEXT STEPS
# plug it into mediacloud via an API wrapper http://webpy.org/
# these results include non-NYT content, such as AP
# update paging to go through multiple pages of search results