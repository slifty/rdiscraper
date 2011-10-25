from BeautifulSoup import BeautifulSoup          # For processing HTML

# Get access to the the HTML that we're looking to parse
# For now it is stored in a file, but eventually we'll pull from a web site
f = open('chicago_sample.html', 'r')
html_data = f.read()

# Now we have the HTML string, let's make soup
soup = BeautifulSoup(html_data)

# Get the section of our document that has the search results
result_uls = soup.findAll('ul', attrs={'class': 'adv-results-list'})

# Set up storage for our result urls
urls = []

# We only expect to have one section containing results, but loop just in case
for result_ul in result_uls: 
	# Get the individual search result items and iterate through them
	result_lis = result_ul.findAll('li')
	for result_li in result_lis:
		# Find the first link in each item
		result_as = result_li.findAll('a', limit=1)
		for result_a in result_as:
			# Store the href attribute (i.e. the actual url) in our list of result urls
			urls.append(result_a['href'])