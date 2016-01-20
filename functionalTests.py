from selenium import webdriver as web

browser = web.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

