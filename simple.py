# According to the specified task I would use simplest possible solution - just one liner bash script with wget / grep
# But as position is for UI QA, I did this smallest code sample to solve it.
# If it's required to show proper usage of patterns, abstractions, waits, setting framework structure etc., it should be
# stated somewhere in the requirements.
from selenium import webdriver


class SimpleSearch:

    @staticmethod
    def search():
        driver = webdriver.Chrome()
        driver.get("https://www.finder.com.au/?s=home+loan")
        results = driver.find_element_by_xpath('//p[@class="search-results-count"]')
        print(results.text)
        driver.close()


if __name__ == "__main__":
    SimpleSearch.search()
