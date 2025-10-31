import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class TestLoginPage:
    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")  # Sauce Demo site
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_valid_login(self, setup):
        """Test login with valid credentials"""
        try:
            # Locate elements for Sauce Demo
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")
            
            # Enter credentials
            username_field.send_keys("standard_user")
            password_field.send_keys("secret_sauce")
            login_button.click()
            
            # Verify successful login
            success_element = self.wait.until(
                EC.presence_of_element_located((By.ID, "inventory_container"))
            )
            
            # Take screenshot
            self.driver.save_screenshot(os.path.join(BASE_DIR, "valid_login_success.png"))
            assert success_element.is_displayed()
            
        except Exception as e:
            self.driver.save_screenshot(os.path.join(BASE_DIR, "valid_login_failure.png"))
            pytest.fail(f"Valid login test failed: {str(e)}")

    def test_invalid_login(self, setup):
        """Test login with invalid credentials"""
        try:
            # Locate elements for Sauce Demo
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")
            
            # Enter invalid credentials
            username_field.send_keys("invalid_user")
            password_field.send_keys("wrong_password")
            login_button.click()
            
            # Verify error message
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
            )
            
            # Take screenshot
            self.driver.save_screenshot(os.path.join(BASE_DIR, "invalid_login_error.png"))
            assert error_message.is_displayed()
            
        except Exception as e:
            self.driver.save_screenshot(os.path.join(BASE_DIR, "invalid_login_unexpected.png"))
            pytest.fail(f"Invalid login test failed: {str(e)}")

if __name__ == "__main__":
    pytest.main([__file__, "-v", f"--html={os.path.join(BASE_DIR, 'report.html')}", "--self-contained-html"])