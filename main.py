from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class TestFooterOnPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_footer_on_pages(self):
        driver = self.driver
        pages = [
            "https://only.digital/",
            "https://only.digital/projects",
            "https://only.digital/job",
            "https://only.digital/contacts",
            "https://only.digital/company"
        ]

        for page in pages:
            driver.get(page)

            # Проверка наличия футера
            footer = driver.find_element(By.TAG_NAME, "footer")
            self.assertIsNotNone(footer, f"Footer not found on page: {page}")

            # Поиск ссылок в футере
            social_links = footer.find_elements(By.CSS_SELECTOR, "a")

            # Проверка, что есть хотя бы одна ссылка
            self.assertGreater(len(social_links), 0, f"No links found in footer on page: {page}")

            # Вывод всех найденных ссылок
            print(f"Footer and links found on {page}:")
            for link in social_links:
                href = link.get_attribute("href")
                text = link.text
                print(f"Link: {text} -> {href}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
