# from selenium import webdriver
# #实例化浏览器
# driver= webdriver.Chrome()
# driver.get ()
# driver.find_element_by_xpath('//*[@id="autocomplete-listbox-desktop-site-header-"]').send_keys('oranges')
# driver.find_element_by_xpath('//*[@id="site-layout"]/div[1]/div[3]/div/header/div[1]/div[2]/form/button').click()

from selenium import webdriver
import time

class Supermarket:
	def __init__(self,name):
		self.name = name
		self.item = None
		self.itemNames = []
		self.itemPrices = []
		self.website = None
		self.searchbar = None
		self.searchbutton = None
		self.getname = None
		self.getprice = None
	def printItemPrice(self):
		for index in range(len(self.itemNames)):
			print(self.itemNames[index]+ ":" + self.itemPrices[index])
	def itemPrice(self):
		itemPrice = []
		for index in range(len(self.itemNames)):
			itemPrice.append({self.itemNames[index], self.itemPrices[index]})
		return itemPrice

Loblaws = Supermarket("Loblaws")
Loblaws.website = 'https://www.loblaws.ca/'
Loblaws.searchbar = '//*[@id="autocomplete-listbox-desktop-site-header-"]'
Loblaws.searchbutton = '//*[@id="site-layout"]/div[1]/div[3]/div/header/div[1]/div[2]/form/button'
Loblaws.getname = "product-name__item--name"
Loblaws.getprice = "selling-price-list__item__price--now-price__value"
# Costco = Supermarket()
# Costco.website = 'https://www.costco.ca/'
# Costco.searchbar = '//*[@id="search-field"]]'
# Costco.searchbutton = '//*[@id="formcatsearch"]/div[2]/button'
# Costco.getname = "your-price row no-gutter"
# Costco.getprice = "your-price row no-gutter" ##this need to be change
Metro = Supermarket("Metro")
Metro.website = 'https://www.metro.ca/en'
Metro.searchbar = '//*[@id="header--search--input"]'
Metro.searchbutton = '//*[@id="header--search--button"]'
Metro.getname = "pt-title"
Metro.getprice = "pi-sale-price"

allMarkets = [Loblaws, Metro]
	

def demo_test(searchItem):
	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver= webdriver.Chrome()
	Loblaws.item = searchItem
	Metro.item = searchItem
	for market in allMarkets:
		website = market.website
		driver.get (website)
		time.sleep(5)
		# Name = 'input'
		#last = driver.find_element_by_xpath('//*[@id="kw"]')
		driver.find_element("xpath", market.searchbar).send_keys(searchItem)
		driver.find_element("xpath", market.searchbutton).click();
		time.sleep(5)

		#get the value
		#driver.find_element(By.CLASS_NAME, "product-tracking")
		element = driver.find_elements_by_class_name(market.getname)
		itemNames = []
		for item in element:
			itemNames.append(item.text)
		market.itemNames = itemNames

		element = driver.find_elements_by_class_name(market.getprice)
		itemPrices = []
		for item in element:
			itemPrices.append(item.text)
		market.itemPrices = itemPrices

		if(len(itemNames) == len(itemPrices)):
			print("good!")

	allStoreResults = []
	for market in allMarkets:
		print(market.name)
		market.printItemPrice()
		for index in range(len(market.itemPrice())):
			allStoreResults.append((market.item ,market.name, market.itemNames[index], float((((market.itemPrices[index])[1:]).split(' ',1))[0])))
			print(float((((market.itemPrices[index])[1:]).split(' ',1))[0]))
			
	#allStoreResults.sort(key= lambda x: (x[0],x[1]),reverse=False)
	allStoreResults.sort(key= lambda x: (x[3]),reverse=False)
	return allStoreResults

#demo_test('orange')

# clickable = driver.find_element(By.id("clickable"));
# clickable.click()
#driver.click()
#actions.contextClick(btnElement).perform();
## hold time?
#<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">

