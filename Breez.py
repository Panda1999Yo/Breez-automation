import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----------------------------
# Desired Capabilities
# -----------------------------
desired_caps = {
    "platformName": "Android",
    "deviceName": "Galaxy Tab A9+",
    "udid": "R52WA06RVNX",
    "platformVersion": "16",
    "appPackage": "com.cyntra.voicebreeze",
    "appActivity": "com.cyntra.voicebreeze.ui.screens.splash.SplashActivity",
    "automationName": "UiAutomator2",
    "noReset": False,
    "newCommandTimeout": 300,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "appium:unicodeKeyboard": True
}


class BreezAutomation(unittest.TestCase):

    driver = None

    # -----------------------------
    # Setup Appium Driver
    # -----------------------------
    @classmethod
    def setUpClass(cls):
        options = UiAutomator2Options()
        for key, value in desired_caps.items():
            options.set_capability(key, value)

        cls.driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            options=options
        )

        cls.wait = WebDriverWait(cls.driver, 20)
        print("✅ Appium driver started")

    # -----------------------------
    # Tear Down
    # -----------------------------
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
            print("🛑 Appium driver stopped")

    # -----------------------------
    # Helper Method
    # -----------------------------
    def wait_for_element(self, by, value, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except Exception:
            print(f"Element NOT found: {value}")
            return None
    


    # -----------------------------
    # Test Case 01
    # -----------------------------
    def test_01_Verify_User_Can_Allow_the_Permissions(self):
        print("Test Case 01: Verify user can allow permissions")

        Allow_btn = self.wait_for_element(
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_button"
        )

        self.assertIsNotNone(Allow_btn, "Allow button not found")
        Allow_btn.click()

        Allow1_btn = self.wait_for_element(
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_button"
        )
        self.assertIsNotNone(Allow1_btn, "Allow button not found")
        Allow1_btn.click()

        # Allow2_btn = self.wait_for_element(
            # AppiumBy.ID,
            # "android:id/switch_widget"
        # )

        # self.assertIsNotNone(Allow2_btn, "Allow button not found")
        # Allow2_btn.click()
        
        # Back = self.wait_for_element(
        #  //   AppiumBy.XPATH,
            # "//android.widget.ImageButton[@content-desc='Navigate up']"
        # )

        # self.assertIsNotNone(Back, "Back button not found")
        # Back.click()
    


    # -----------------------------
    # Test Case 02
    # -----------------------------
    def test_02_Verify_User_sucessfull_login_with_credentails(self):
        print("Test Case 02: Verify user can complete registration with valid credentials")

    
        User_id = self.wait_for_element(
            AppiumBy.ID,
            "com.cyntra.voicebreeze:id/etEmployeeId2"
        )
        self.assertIsNotNone(User_id, "User ID field not found")
        User_id.click()
        User_id.send_keys("4152")

        Password = self.wait_for_element(
            AppiumBy.ID,
            "com.cyntra.voicebreeze:id/etPassword2"
        )
        self.assertIsNotNone(Password, "Password field not found")
        Password.click()
        Password.send_keys("931839")
 
        Login = self.wait_for_element(
            AppiumBy.ID,
            "com.cyntra.voicebreeze:id/btnLogin"
        )
        self.assertIsNotNone(Login, "Login button not found")
        Login.click()
        time.sleep(2)
    
    # -----------------------------
    # Test Case 03
    # -----------------------------
    def test_03_Verify_User_can_complete_registration_and_closing_the_order(self):
        print("Test Case 03: Verify user can complete registration with valid credentials and closing the order")

        Touch_to_start = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[1]"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click()

        Dinein = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[2]"
        )
        self.assertIsNotNone(Dinein, "Dine in field not found")
        Dinein.click()

        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(2)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        Choose_different_Cat = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]"
        )
        self.assertIsNotNone(Choose_different_Cat, "Choose different category field not found")
        Choose_different_Cat.click()
        time.sleep(3)
    
        Veg_Man = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]"
        )
        self.assertIsNotNone(Veg_Man, "Veg Man field not found")
        Veg_Man.click()
        time.sleep(3)
 
        Checkout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(Checkout, "Checkout field not found")
        Checkout.click()
        time.sleep(3)


        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 04
    # -----------------------------
    def test_04_Verify_User_can_Select_different_order_type(self):
        print("Test Case 04: Verify user can select different order type")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 

        time.sleep(3)
        
        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(2)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        Choose_different_Cat = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]"
        )
        self.assertIsNotNone(Choose_different_Cat, "Choose different category field not found")
        Choose_different_Cat.click()
        time.sleep(3)
    
        Veg_Man = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]"
        )
        self.assertIsNotNone(Veg_Man, "Veg Man field not found")
        Veg_Man.click()
        time.sleep(3)
 
        Checkout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(Checkout, "Checkout field not found")
        Checkout.click()
        time.sleep(3)


        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 05
    # -----------------------------
    def test_05_Verify_User_can_Select_Continue_as_a_Guest(self):
        print("Test Case 05: Verify user can select Continue as a Guest")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 

        time.sleep(3)
        
        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Continue = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]"
        )
        self.assertIsNotNone(Continue, "Continue field not found")
        Continue.click()

        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        Choose_different_Cat = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]"
        )
        self.assertIsNotNone(Choose_different_Cat, "Choose different category field not found")
        Choose_different_Cat.click()
        time.sleep(3)
    
        Veg_Man = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]"
        )
        self.assertIsNotNone(Veg_Man, "Veg Man field not found")
        Veg_Man.click()
        time.sleep(3)
 
        Checkout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(Checkout, "Checkout field not found")
        Checkout.click()
        time.sleep(3)


        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()

    # -----------------------------
    # Test Case 06
    # -----------------------------
    def test_06_Verify_User_can_search_the_items(self):
        print("Test Case 06: Verify user can search the items")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Continue = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]"
        )
        self.assertIsNotNone(Continue, "Continue field not found")
        Continue.click()

        time.sleep(3)

        Search = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.ImageView[@content-desc='search']"
        )
        self.assertIsNotNone(Search, "Search field not found")
        Search.click()

        time.sleep(3)

        Search_field = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Search_field, "Search field not found")
        Search_field.click()
        Search_field.send_keys("Man")

        Veg_Man = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]"
        )
        self.assertIsNotNone(Veg_Man, "Veg Man field not found")
        Veg_Man.click()    

        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 07
    # -----------------------------
    def test_07_Verify_User_can_add_the_qunatity_of_the_items(self):
        print("Test Case 07: Verify user can add the quantity of the items")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Continue = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]"
        )
        self.assertIsNotNone(Continue, "Continue field not found")
        Continue.click()


        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        Qunatity = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Qunatity, "Quantity field not found")
        Qunatity.click()
        time.sleep(3)

        Repeat = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Repeat Last']"
        )
        self.assertIsNotNone(Repeat, "Repeat field not found")
        Repeat.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 08
    # -----------------------------
    def test_08_Verify_User_can_click_the_call_assistant(self):
        print("Test Case 08: Verify user can click the call assistant button")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Continue = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]"
        )
        self.assertIsNotNone(Continue, "Continue field not found")
        Continue.click()


        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        call_assistant = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.ImageView[@content-desc='help']"
        )
        self.assertIsNotNone(call_assistant, "Call assistant field not found")
        call_assistant.click()
        time.sleep(3)

        Close= self.wait_for_element(
            AppiumBy.XPATH,
            "//android.view.View[@content-desc='Back']"
        )
        self.assertIsNotNone(Close, "Close field not found")
        Close.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()
  

    # -----------------------------
    # Test Case 09
    # -----------------------------
    def test_09_Verify_User_can_applied_the_discount(self):
        print("Test Case 09: Verify user can apply the discount")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 
 
        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Continue = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]"
        )
        self.assertIsNotNone(Continue, "Continue field not found")
        Continue.click()


        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Discount = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]"
        )
        self.assertIsNotNone(Discount, "Discount field not found")
        Discount.click()

        Bacck = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[1]/android.view.View"
        )
        self.assertIsNotNone(Bacck, "Back field not found")
        Bacck.click()

        Bacck1 = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.view.View[@content-desc='Back']"
        )
        self.assertIsNotNone(Bacck1, "Back field not found")
        Bacck1.click()

        Qunatity = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Qunatity, "Quantity field not found")
        Qunatity.click()
        time.sleep(3)

        Repeat = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Repeat Last']"
        )
        self.assertIsNotNone(Repeat, "Repeat field not found")
        Repeat.click()
        time.sleep(3)

        Qunatity1 = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Qunatity1, "Quantity field not found")
        Qunatity1.click()
        time.sleep(3)

        Repeat1 = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Repeat Last']"
        )
        self.assertIsNotNone(Repeat1, "Repeat field not found")
        Repeat1.click()
        time.sleep(3)

        Qunatity2= self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Qunatity2, "Quantity field not found")
        Qunatity2.click()
        time.sleep(3)

        Repeat2 = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Repeat Last']"
        )
        self.assertIsNotNone(Repeat2, "Repeat field not found")
        Repeat2.click()
        time.sleep(3)

        Qunatity3 = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Qunatity3, "Quantity field not found")
        Qunatity3.click()
        time.sleep(3)

        Repeat3 = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Repeat Last']"
        )
        self.assertIsNotNone(Repeat3, "Repeat field not found")
        Repeat3.click()
        time.sleep(3)

        Qunatity4 = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Qunatity4, "Quantity field not found")
        Qunatity4.click()
        time.sleep(3)

        Repeat4 = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Repeat Last']"
        )
        self.assertIsNotNone(Repeat4, "Repeat field not found")
        Repeat4.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()


        Discount = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]"
        )
        self.assertIsNotNone(Discount, "Discount field not found")
        Discount.click()

        Apply = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Tap to apply']"
        )
        self.assertIsNotNone(Apply, "Apply field not found")
        Apply.click()
        time.sleep(3)

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 10
    # -----------------------------
    def test_10_Verify_User_can_reorder_your_Last_meal(self):
        print("Test Case 10: Verify user can reorder your last meal")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 
 
        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(2)

        Reorder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]"
        )
        self.assertIsNotNone(Reorder, "Reorder field not found")
        Reorder.click()
        
        Add_to_cart = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to cart']"
        )
        self.assertIsNotNone(Add_to_cart, "Add to cart field not found")
        Add_to_cart.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()
  

    # -----------------------------
    # Test Case 11
    # -----------------------------
    def test_11_Verify_User_can_use_the_veg_filter(self):
        print("Test Case 11: Verify user can use the veg filter")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 
 
        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(2)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Filter= self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Filters']"
        )
        self.assertIsNotNone(Filter, "Filter field not found")
        Filter.click()

        Veg= self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Veg']"
        )
        self.assertIsNotNone(Veg, "Veg field not found")
        Veg.click()

        Apply= self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Apply']"
        )
        self.assertIsNotNone(Apply, "Apply field not found")
        Apply.click()


        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        # Qunatity = self.wait_for_element(
            # AppiumBy.XPATH,
            # "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        # )
        # self.assertIsNotNone(Qunatity, "Quantity field not found")
        # Qunatity.click()
        # time.sleep(3)

        # Repeat = self.wait_for_element(
            # AppiumBy.XPATH,
            # "//android.widget.TextView[@text='Repeat Last']"
        # )
        # self.assertIsNotNone(Repeat, "Repeat field not found")
        # Repeat.click()
        # time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 12
    # -----------------------------
    def test_12_Verify_User_can_Logout_the_and_relogin_same_user(self):
        print("Test Case 12: Verify user can logout and relogin same user")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().className(\"android.view.View\").instance(3)"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click() 
 
        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()

        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(2)

        Logout = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[2]"
        )
        self.assertIsNotNone(Logout, "Logout field not found")
        Logout.click()
        time.sleep(2)

        Yes = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Yes']"
        )
        self.assertIsNotNone(Yes, "Yes field not found")
        Yes.click()

    # -----------------------------
    # Test Case 13
    # -----------------------------
    def test_13_Verify_User_can_Clear_the_cart(self):
        print("Test Case 13: Verify user can clear the cart")
 
        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(10)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        Clear_cart = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Clear all']"
        )
        self.assertIsNotNone(Clear_cart, "Clear cart field not found")
        Clear_cart.click()
        time.sleep(3)

        Yes = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Yes']"
        )
        self.assertIsNotNone(Yes, "Yes field not found")
        Yes.click()
        time.sleep(3)



    # -----------------------------
    # Test Case 14
    # -----------------------------
    def test_14_Verify_User_can_Apply_the_tip(self):
        print("Test Case 14: Verify user can apply the tip")

        time.sleep(3)

        
        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        Tip = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]"
        )
        self.assertIsNotNone(Tip, "Tip field not found")
        Tip.click()
        time.sleep(2)

        Cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(Cash, "Cash field not found")
        Cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()
  


    # -----------------------------
    # Test Case 15
    # -----------------------------
    def test_15_Verify_User_can_Chosses_different_category(self):
        print("Test Case 15: Verify user can choose different category")

        time.sleep(3)

        Touch_to_start = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[1]"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click()

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(10)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Special = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]"
        )
        self.assertIsNotNone(Special, "Special field not found")
        time.sleep(3)
        Special.click()

        Soups = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]"
        )
        self.assertIsNotNone(Soups, "Soups & Noodles field not found")
        time.sleep(3)
        Soups.click()   

        Curries = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[4]"
        )
        self.assertIsNotNone(Curries, "Curries field not found")
        time.sleep(3)
        Curries.click()  

        Green = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]"
        )
        self.assertIsNotNone(Green, "Green field not found")
        time.sleep(3)
        Green.click() 

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        Tip = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]"
        )
        self.assertIsNotNone(Tip, "Tip field not found")
        Tip.click()
        time.sleep(2)

        Cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View"
        )
        self.assertIsNotNone(Cash, "Cash field not found")
        Cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()    

    # -----------------------------
    # Test Case 16
    # -----------------------------
    def test_16_Verify_User_can_Enter_the_Item_level_Special_request(self):
        print("Test Case 16: Verify user can enter item level special request")

        time.sleep(2)

        Touch_to_start = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[1]"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click()

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(10)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)


        Note = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Note to Kitchen']"
        )
        self.assertIsNotNone(Note, "Note field not found")
        Note.click()
        time.sleep(3)


        Note = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Note, "Note field not found")
        Note.click()
        Note.send_keys("Please make it spicy")
        time.sleep(3)

        Submit = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Submit']"
        )
        self.assertIsNotNone(Submit, "Submit button not found")
        Submit.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        Tip = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]"
        )
        self.assertIsNotNone(Tip, "Tip field not found")
        Tip.click()
        time.sleep(2)

        Cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(Cash, "Cash field not found")
        Cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()
  

    # -----------------------------
    # Test Case 17
    # -----------------------------
    def test_17_Verify_User_can_Select_the_combo_items(self):
        print("Test Case 17: Verify user can select the combo items")

        time.sleep(2)

        Touch_to_start = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[1]"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click()

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(10)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Soups = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]"
        )
        self.assertIsNotNone(Soups, "Soups field not found")
        time.sleep(3)
        Soups.click()
  
        Yellow = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[5]"
        )
        self.assertIsNotNone(Yellow, "Yellow field not found")
        time.sleep(3)
        Yellow.click()
  
        Meal = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[2]"
        )
        self.assertIsNotNone(Meal, "Meal field not found")
        time.sleep(3)
        Meal.click()


        Combo = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[2]/android.view.View"
        )
        self.assertIsNotNone(Combo, "Combo field not found")
        time.sleep(3)
        Combo.click()

        Add = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart ₹372.00']"
        )
        self.assertIsNotNone(Add, "Add field not found")
        time.sleep(3)
        Add.click()

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 18
    # -----------------------------
    def test_18_Verify_User_can_Select_the_addons(self):
        print("Test Case 18: Verify user can select the addons")

        time.sleep(2)

        Touch_to_start = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[1]"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click()

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(10)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Soups = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]"
        )
        self.assertIsNotNone(Soups, "Soups field not found")
        time.sleep(3)
        Soups.click()
  
        Asian = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Asian, "Asian field not found")
        time.sleep(3)
        Asian.click() 

        Addons = self.wait_for_element(
            AppiumBy.XPATH,
            "(//android.widget.TextView[@text='Add'])[1]"
        )
        self.assertIsNotNone(Addons, "Addons field not found")
        time.sleep(3)
        Addons.click() 

        Add = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Add, "Add field not found")
        time.sleep(3)
        Add.click()
        
        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(cash, "Cash field not found")
        cash.click()
        time.sleep(2)

        Neworder = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View"
        )
        self.assertIsNotNone(Neworder, "New order field not found")
        Neworder.click()


    # -----------------------------
    # Test Case 19
    # -----------------------------
    def test_19_Verify_User_can_Select_the_Custom_tip(self):
        print("Test Case 19: Verify user can select the custom tip")

        time.sleep(2)

        Touch_to_start = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[1]"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click()

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(10)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        Customtip = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Customtip, "Custom tip field not found")
        Customtip.click()
        time.sleep(2)
        Customtip.send_keys("10")

        Cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(Cash, "Cash field not found")
        Cash.click()
        time.sleep(2)


    # -----------------------------
    # Test Case 20
    # -----------------------------
    def test_20_Verify_User_can_reselect_the_same_items(self):
        print("Test Case 20: Verify user can reselect the same items")

        time.sleep(2)

        Touch_to_start = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[1]"
        )
        self.assertIsNotNone(Touch_to_start, "Touch to start field not found")
        Touch_to_start.click()

        time.sleep(3)

        Takeaway = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View[2]/android.view.View[1]"
        )
        self.assertIsNotNone(Takeaway, "Takeaway field not found")
        Takeaway.click()


        Phone_Number = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Phone_Number, "Phone number field not found")
        Phone_Number.click()
        Phone_Number.send_keys("9318392530")
        time.sleep(10)

        New_order = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[4]"
        )
        self.assertIsNotNone(New_order, "New order field not found")
        time.sleep(3)
        New_order.click()

        Flat_noodles = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles, "Flat noodles field not found")
        Flat_noodles.click()
        time.sleep(3)

        Modifiers = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers, "Modifiers field not found")
        Modifiers.click()
        time.sleep(3)

        Flat_noodles1 = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]"
        )
        self.assertIsNotNone(Flat_noodles1, "Flat noodles field not found")
        Flat_noodles1.click()
        time.sleep(3)

        Choose = self.wait_for_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiSelector().text(\"I'll Choose\")"
        )
        self.assertIsNotNone(Choose, "Choose field not found")
        Choose.click()
        time.sleep(3)

        Modifiers1 = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Add to Cart']"
        )
        self.assertIsNotNone(Modifiers1, "Modifiers field not found")
        Modifiers1.click()
        time.sleep(3)

        CHeckout = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Checkout']"
        )
        self.assertIsNotNone(CHeckout, "Checkout field not found")
        CHeckout.click()

        Paynow = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Pay Now']"
        )
        self.assertIsNotNone(Paynow, "Pay now field not found")
        Paynow.click()
        time.sleep(2)

        Customtip = self.wait_for_element(
            AppiumBy.XPATH,
            "//android.widget.EditText"
        )
        self.assertIsNotNone(Customtip, "Custom tip field not found")
        Customtip.click()
        time.sleep(2)
        Customtip.send_keys("10")

        Cash = self.wait_for_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView[@resource-id='com.cyntra.voicebreeze:id/composeView']/android.view.View/android.view.View/android.view.View[5]/android.view.View"
        )
        self.assertIsNotNone(Cash, "Cash field not found")
        Cash.click()
        time.sleep(2)
















































# -----------------------------
# Run Tests
# -----------------------------
if __name__ == "__main__":
    unittest.main()
