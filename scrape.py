# Coded by Praneeth as a part of an interview process.


#This module is to scrape draw analysis for the page http://myneta.info/ls2014/candidate.php?candidate_id=8000. 
#I am using BeautifulSoup which is a package for parsing html and extracting data.
# urllib is used to use the url functionalities.

import requests,json,csv,pymongo,sys,getopt,pprint
from pymongo import MongoClient
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
id = input('enter the candidate id:')


def scrape(id):
	url = 'http://myneta.info/ls2014/candidate.php?candidate_id={0}'.format(id)
	try:
		response = requests.get(url)
		if response.status_code!=200:#checking if url exists or not.
			return "Error: Unexpected response {}".format(response)
		page = urlopen(url).read()#It returns HTML tree and stores in page.
		soup = BeautifulSoup(page, 'html.parser')#parsing
		#print(soup)
		
		#fetching nae of the candidate
		name = soup.find('h2', attrs={'class': 'main-title'})
		name = name.text.strip()
		#print(name)
		
		#fetching election and year
		election = soup.find('h2', attrs={'class': 'title first'})
		election = election.text
		#print('\n',election)
		
		#fetching constituency
		const = soup.find('h5')
		const = const.text.strip()
		#print('\n',const)
		
		bt = soup.find_all('div', attrs={'class': 'grid_2 alpha'})
		sonof = bt[0].text
		sonof1=str(sonof).replace('S/o|D/o|W/o:','')
		#print(sonof1)
		
		party = bt[1].text
		party=str(party).replace('Party:','')
		#print(party)
		
		Age = bt[2].text
		Age=str(Age).replace('Age:','')
		#print(Age)
		
		Address = bt[3].text
		Address=str(Address).replace('Address:','')
		#print(Address)


		election=str(election).replace(' ','')#strip() function is not working, hence I used replace function.
		with open(election+'.csv', 'a') as csv_file:#storing csv file according to the election year
			elect = csv.writer(csv_file)
			elect.writerow(["name","election","const","Age","Address","datetime"])
			elect.writerow([name,election,const,Age,Address,datetime.now()])
		
		return 0
	except requests.exceptions.RequestException as e:
		return "Error: {}".format(e)
scrape(id)