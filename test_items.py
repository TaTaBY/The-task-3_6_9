import time

def test_access_to_button_for_adding_item_to_bucket(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207"
    browser.get(link)
    browser.implicitly_wait(10)
    if(browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")):
    	button1 = "True"
    else:
    	button1 = "False"
    assert button1 == "True", "Test 1 failed"
    time.sleep(3)
    
    
