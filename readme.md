***Data Science***

Data science involves four steps
	Data fetch: I was provided with a URL to crawl and get the desired data from html.
				URL:"http://myneta.info/ls2014/candidate.php?candidate_id=8000"
	Data clean: I used google's open refine to reove unwanted whitespaces,special characters etc.
	Data analysis: I have stored the data in mongodb for further analysis.
	Data analytics and visualization: Fetching the desired data from the database for the visualization. This step is not done in this project.

This project contains four files.
	1)core files
	2)csv file
	3)screenshot
	
""Technicalities""
	The two core files are written in python.
	Scrape.py file gets into the html elements of the web page, fetches the data and stores in csv.
	import.py file imports the csv file into mongodb(mongodb is running on localhost port 27017)
	
""Prerequisites""
	install pandas(for data analysis in python),pymongo(mongodb driver),beautifulsoup4.
	example pip install beautifulsoup4