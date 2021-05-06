import time

import selenium

import capabilities
import utilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.config_utils import get_My_Config


class MyBrowser:
    def __init__(self):
        pass


    def get_browser_selection(self):
        try:
            os = get_My_Config().my_config(my_test_config_key="os", key_id=None)
            main_webdriver = get_My_Config().my_config(my_test_config_key="main_webdriver", key_id=None)
            
            #print("\n", os)
            #print("\n", main_webdriver)
            
            key_id = 0
            if(os == "mac"):
                key_id = 0
            elif(os == "win"):
                key_id = 1
            elif(os == "linux"):
                key_id = 2
            
            
            var0 = get_My_Config().my_config(my_test_config_key="test_host_environment", key_id=key_id)
            #print("\nvar0 = ", var0)



            var1 = get_My_Config().my_config_json(json_data=var0, my_test_config_key=os, key_id=None)
            #print("\nvar1 = ", var1)


            key_id = 0
            if (main_webdriver == "webdriver1"):
                key_id = 0
            elif (main_webdriver == "webdriver2"):
                key_id = 1
            elif (main_webdriver == "webdriver3"):
                key_id = 2
            elif (main_webdriver == "webdriver4"):
                key_id = 3

            webdriver_selection = get_My_Config().my_config_json(json_data=var1, my_test_config_key="", key_id=key_id)
            #print(webdriver_selection)

            webdriver_selection = get_My_Config().my_config_json(json_data=webdriver_selection, my_test_config_key=main_webdriver, key_id=None)
            print("\nWebDriver Selected = ", webdriver_selection)

            return(webdriver_selection)            

        except Exception as e:
            print(str(e))

    def get_browser(self):
        try:
            import selenium.webdriver.chrome.webdriver
            import selenium.webdriver.firefox.webdriver
            webdriver_selection = self.get_browser_selection()
            mystep = capabilities.remote_capabilities.MyRemoteWebDriver()
            print(webdriver_selection)

            if("chrome" in webdriver_selection):
                if("win" in webdriver_selection):
                    driver = mystep.remote_windows_chrome_driver()
                elif("mac" in webdriver_selection):
                    driver = mystep.remote_mac_os_chrome_browser_driver()
                return driver

            elif("gecko" in webdriver_selection):
                if("win" in webdriver_selection):
                    driver = mystep.remote_windows_firefox_driver()
                if("mac" in webdriver_selection):
                    driver = mystep.remote_mac_os_firefox_browser_driver()
                return driver

            elif ("safari" in webdriver_selection):
                if ("mac" in webdriver_selection):
                    driver = mystep.remote_mac_os_safari_browser_driver()
                return driver

            elif ("edge" in webdriver_selection):
                if ("win" in webdriver_selection):
                    driver = mystep.remote_windows_edge_driver()
                return driver

            elif ("ie11" in webdriver_selection):
                if ("win" in webdriver_selection):
                    driver = mystep.remote_windows_ie11_driver()
                return driver

        except Exception as e:
            print(str(e))
            pass


    def set_browser_view_dimensions(self, driver):
        dimension_x = utilities.config_utils.get_My_Config().my_config(my_test_config_key="main_dimension_x")
        dimension_y = utilities.config_utils.get_My_Config().my_config(my_test_config_key="main_dimension_y")
        driver.implicitly_wait(14)
        #driver.set_window_size(int(dimension_x), int(dimension_y))
        driver.set_window_rect(x=0, y=0, width=int(dimension_x), height=int(dimension_y))
        return driver


    def navigate_to_url(self, driver):
        try:
            url_selection = utilities.config_utils.get_My_Config().my_config("main_url")
            url_selected = utilities.data_utils.get_My_Data().my_data(my_test_data_key=url_selection, key_id=None)
            driver.get(url_selected)
            return driver
        except Exception as e0:
            try:
                print("URL Navigation Failed")
                assert False
            except Exception as e1:
                return driver

    def hover_and_click_on_web_element(self, driver, myxpath, index_location=None):
        xElements = None
        xElement = None
        mystep = utilities.action_utils.Driver_Actions()
        if(index_location!=None):
            try:
                driver, xElement = mystep.move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=index_location)
            except Exception as e00:
                try:
                    driver, xElement = mystep.scroll_and_search_into_view_and_click_element(driver, myxpath=myxpath, index_location=index_location)
                except Exception as e01:
                    pass
            """
            xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
            try:
                driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElements[int(index_location)])
            except Exception as e0:
                pass
            try:
                xElement = xElements[int(index_location)]
            except Exception as e1:
                pass
            """
        else:
            try:
                driver, xElement = mystep.move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=0)
            except Exception as e02:
                try:
                    driver, xElement = mystep.scroll_and_search_into_view_and_click_element(driver, myxpath=myxpath, index_location=0)
                except Exception as e03:
                    pass
            """
            xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath)
            try:
                driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElement)
            except Exception as e2:
                pass
            """
        return driver


    def hover_and_send_keys_to_web_element(self, driver, myxpath, index_location=None, mytext=None):
        xElements = None
        xElement = None
        #flag = False
        #mystep = utilities.driver_utils.Common_Actions()
        if(index_location!=None):
            try:
                #xElements, flag = mystep.check_webelement_existence_using_xpath(driver, myxpath=myxpath, index_location=index_location)
                xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
            except Exception as e0:
                pass

            try:
                xElement = xElements[int(index_location)]
            except Exception as e1:
                pass

        elif(index_location==None):
            try:
                #xElement, flag = mystep.check_webelement_existence_using_xpath(driver, myxpath=myxpath, index_location=0)
                xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath)
            except Exception as e0:
                pass
        try:
            driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElement)
        except Exception as e2:
            pass

        try:
            xElement.click()
        except Exception as e:
            pass

        try:
            xElement.clear()
        except Exception as e:
            pass

        try:
            xElement.send_keys(mytext)
            return driver
        except Exception as e3:
            try:
                print("Hover and send keys to web element failed")
                assert False
            except Exception as ee:
                return driver

        return driver


    def hover_and_get_text_from_web_element(self, driver, myxpath, index_location=None):
        xElements = None
        xElement = None
        mytext = None

        try:
            #driver, xElement = utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_element(driver, myxpath=myxpath, index_location=index_location)
            driver, xElement = utilities.action_utils.Driver_Actions().move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=index_location)
        except Exception as e00:
            pass

        try:
            mytext = xElement.get_attribute('innerText')
        except Exception as e01:
            pass

        return driver, mytext


    def navigate_to_page_end(self, driver):
        try:
            utilities.action_utils.Driver_Actions().driver_page_end_action(driver)
        except Exception as e0:
            pass
        return driver


    def navigate_to_end_of_the_page(self, driver, myxpath, index_location=None):
        xElements = None
        xElement = None

        if(index_location!=None):
            try:
                xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
            except Exception as e0:
                pass

            try:
                xElement = xElements[int(index_location)]
            except Exception as e1:
                pass

        elif(index_location==None):
            try:
                xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
            except Exception as e1:
                pass
            try:
                #xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath)
                xElement = xElements[0]
            except Exception as e2:
                pass
        try:
            utilities.action_utils.Driver_Actions().driver_page_end_action(driver)
        except Exception as e3:
            pass

        try:
            driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElement)
        except Exception as e4:
            try:
                print("Navigating to End of the Page Failed")
                assert False
            except Exception as e5:
                return driver
        return driver



