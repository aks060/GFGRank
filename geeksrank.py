import requests
from bs4 import BeautifulSoup

s=requests.session()
n=input('Enter name to search: ')
header={'Content-Type': 'application/x-www-form-urlencoded;'}
for i in range(0, 100):
	#print('Searching on page '+str(i))
	data={'slug':'lpu-jalandhar',
	'page':int(i)}
	req=s.post('https://auth.geeksforgeeks.org/ajax/instituteAjax.php', data=data, headers=header)
	req=req.content.decode()
	if n in req:
		print(n+' is also present on page number '+str(i+1))
		print("\n")