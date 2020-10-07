from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://yandex.ru')

u = browser.find_element_by_xpath('//*[@id="wd-_topnews"]/div/div[3]/div/div/div[1]')
e = browser.find_element_by_xpath('//*[@id="wd-_topnews"]/div/div[3]/div/div/div[2]')

print(u.text) 
print(e.text)


