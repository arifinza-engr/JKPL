import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Pengujian 1: Login


class Test1Login():
    @pytest.fixture(autouse=True)
    def setup_teardown(self, chrome_driver):
        self.driver = chrome_driver
        self.vars = {}

    def test_1Login(self):
        self.driver.get("http://localhost:8889/wp-login.php")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.ID, "user_login").send_keys("admin")
        self.driver.find_element(By.ID, "user_pass").send_keys("password")
        self.driver.find_element(By.ID, "wp-submit").click()

# Pengujian 2: Add User


class Test2AddUser():
    @pytest.fixture(autouse=True)
    def setup_teardown(self, chrome_driver):
        self.driver = chrome_driver
        self.vars = {}

    def test_2AddUser(self):
        self.driver.get("http://localhost:8889/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.LINK_TEXT, "WordPress Develop").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".menu-icon-users > .wp-menu-name").click()
        self.driver.find_element(By.LINK_TEXT, "Add New User").click()
        self.driver.find_element(By.ID, "user_login").click()
        self.driver.find_element(By.ID, "user_login").send_keys("maman")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("maman@gmail.com")
        self.driver.find_element(By.ID, "first_name").click()
        self.driver.find_element(By.ID, "first_name").send_keys("Maman")
        self.driver.find_element(By.ID, "last_name").click()
        self.driver.find_element(By.ID, "last_name").send_keys("Suparman")
        self.driver.find_element(By.ID, "url").click()
        self.driver.find_element(By.ID, "url").send_keys("localhost:1717")
        self.driver.find_element(By.ID, "url").send_keys("localhost:8888")
        self.driver.find_element(By.ID, "createusersub").click()

# Pengujian 3: Edit Komen


class Test3EditKomen():
    @pytest.fixture(autouse=True)
    def setup_teardown(self, chrome_driver):
        self.driver = chrome_driver
        self.vars = {}

    def test_3EditKomen(self):
        self.driver.get("http://localhost:8889/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.LINK_TEXT, "WordPress Develop").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".menu-icon-comments > .wp-menu-name").click()
        self.driver.find_element(By.CSS_SELECTOR, ".has-row-actions").click()
        # Perbaiki URL di bawah ini dengan menambahkan tanda "/" setelah "localhost:8889"
        self.driver.get(
            "http://localhost:8889/wp-admin/comment.php?action=editcomment&c=1")
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Hendra Kumbara")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("testes@gmail.com")
        self.driver.find_element(By.ID, "content").click()
        self.driver.find_element(By.ID, "content").send_keys(
            "Halo saya telah mengedit komen")
        self.driver.find_element(By.ID, "save").click()

# Pengujian 4: Ubah Tema


class Test4UbahTema():
    @pytest.fixture(autouse=True)
    def setup_teardown(self, chrome_driver):
        self.driver = chrome_driver
        self.vars = {}

    def test_4UbahTema(self):
        self.driver.get("http://localhost:8889/wp-admin/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(
            By.CSS_SELECTOR, ".menu-icon-appearance > .wp-menu-name").click()
        # Pastikan Anda memilih elemen yang benar sesuai dengan tema yang digunakan.
        # Misalnya, jika ingin mengklik elemen dengan teks "Activate", pastikan elemen tersebut ada dalam tema yang digunakan.
        # Jika tidak, sesuaikan dengan elemen yang benar.
        # self.driver.find_element(By.LINK_TEXT, "Activate").click()

# Pengujian 5: Install Plugin


class Test5InstallPlugin():
    @pytest.fixture(autouse=True)
    def setup_teardown(self, chrome_driver):
        self.driver = chrome_driver
        self.vars = {}

    def test_5InstallPlugin(self):
        self.driver.get("http://localhost:8889/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.LINK_TEXT, "WordPress Develop").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".menu-icon-plugins > .wp-menu-name").click()
        self.driver.find_element(By.CSS_SELECTOR, ".page-title-action").click()
        self.driver.find_element(By.LINK_TEXT, "Popular").click()
        self.driver.find_element(By.LINK_TEXT, "Install Now").click()
        self.driver.find_element(By.LINK_TEXT, "Activate").click()


# Menjalankan semua pengujian dalam satu kali pembukaan Chrome
if __name__ == "__main__":
    pytest.main(["-v", "e2e_tests.py"])
