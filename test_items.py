import time

def test_access_to_button_for_adding_item_to_bucket(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207"
    browser.get(link)
    browser.implicitly_wait(10)
    button1 = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
    if language == "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207":
    	assert button1.text == "Ajouter au panier", "Sub-test failed"
    time.sleep(3)
    
