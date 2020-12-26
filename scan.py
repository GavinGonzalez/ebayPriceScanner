import requests
from bs4 import BeautifulSoup
import smtplib

print('==========Ebay Price Scanner==========\n')
URL = input('Input your Input \n')
email = input('Input your Email \n')
password = input('Input your Password \n')
desired_price = input('Input your desired \n')

headers = {
	'User-Agent': 'Mozilla/5.0BeautifulSoup (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

print(requests.get(URL))

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id='itemTitle').get_text()

	try:
		price = soup.find(id='prcIsum').get_text()

	except Exception:		
		price = soup.find(id='mm-saleDscPrc').get_text()


	converted_price = float(price[4:10])
	#if(converted_price == desired_price):
	send_email()


def send_email():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login(email, password)

	subject = 'Price fell down!!!!!!'

	msg = f'Subect: {subject}\n{URL} The Price went down'

	server.sendmail(
		email,
		email,
		msg
	)
	print('Email has been sent')
	server.quit()



check_price()
