from automation.page_objects.search_page import SearchPage
from automation.conftest import validate_window

def test_filter_book(eyes, driver):
    page = SearchPage(driver)
    page.filter_books('Agile')
    validate_window(driver, eyes, tag='filter_text')