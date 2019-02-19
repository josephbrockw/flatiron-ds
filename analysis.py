from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

class Analysis:
		def __init__(self, term):
				self.term = term
				self.sentiment = 0
				self.subjectivity = 0
				self.url = 'https://wwww.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)

		def run(self):
				response = requests.get(self.url)
				#soup = BeautifulSoup(response.text, 'html.parser')
				print(response.text)

test = Analysis('orthondtist')
test.run()
