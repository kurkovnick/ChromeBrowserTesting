from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/nickkurkov/PycharmProjects/ChromeBrowserTesting/drivers/chromedriver')

driver.get('https://www.inline-fence.com/')

driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/article/div/div/div/div/section[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/a/div/div').click()

title = "Residential Fences in Seattle - InLine Fence LLC"
assert title == driver.title, "Residential Page Title is wrong"
driver.close()