from selenium import webdriver
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import lxml
import re
from PIL import ImageOps
from PIL import Image
from selenium import webdriver
from time import sleep
from random import choice, uniform
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
import html5lib
import pymysql.cursors





class Bot:



	def __init__(self):
		# options = Options()
		# # options.headless = True
		# profile = FirefoxProfile("C:\\Users\\Дмитрий\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\kl5gzaww.default-release")
		# self.driver = webdriver.Firefox(options=options, firefox_profile=profile)
		# self.driver.set_page_load_timeout(10)
		options = webdriver.ChromeOptions()
		options.add_argument("user-data-dir=C:\\Users\\Дмитрий\\AppData\\Local\\Google\\Chrome\\User Data")
		self.driver = webdriver.Chrome(chrome_options=options) 
		self.driver.set_page_load_timeout(10)
		# self.data = row
		self.navigate()

	def navigate(self):
		f = open('ids.txt', 'a')
		ids = []
		i = 0
		urls  = []
		url =   'https://arenda-piter.ru/workpage.php?page=firmi'
		self.driver.get(url) #ЗАХОДИМ НА СТРАНИЦУ С КОНТАКТАМИ ФИРМ
		sleep(3)
		requiredHtml = self.driver.page_source
		soup = BeautifulSoup(requiredHtml, 'html5lib')
		# trs = soup.find_all('div', class_='bukva-block')
		firma_tbl = soup.find_all('table' ,class_='firma_tbl')
		firma_link = soup.find_all('a', class_='company-name-link')
		# print(firma_link[0].get('href'))
		for firm in firma_link:
			# try:
			url = 'https://arenda-piter.ru' + firm.get('href')
			# print(url)
			self.driver.get(url)
			r = self.driver.page_source
			soup = BeautifulSoup(r, 'lxml')
			agent_table = soup.find('table', class_='tarif_tbl').find_all('tr', valign='middle')
			for agent in agent_table:
				agent_data = agent.find_all('td')[-1].find('span').find('span').get('id')
				ids.append(agent_data)
				f.write(agent_data+'\n')
			# except:
			# 	try:
			# 		url = 'https://arenda-piter.ru' + firm.get('href')
			# 		# print(url)
			# 		self.driver.get(url)
			# 		r = self.driver.page_source
			# 		soup = BeautifulSoup(r, 'lxml')
			# 		agent_table = soup.find('table', class_='tarif_tbl').find_all('tr', valign='middle')
			# 		for agent in agent_table:
			# 			agent_data = agent.find_all('td')[-1].find('span').find('span').get('id')
			# 			ids.append(agent_data)
			# 			f.write(agent_data+'\n')
			# 	except:
			# 		print('Somthing wrong')

		f.close()
		print(ids)





			




def main():


	b = Bot()
	

main()