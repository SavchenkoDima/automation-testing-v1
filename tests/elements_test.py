import random
import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
from conftest import driver


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.agree_personal_data()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.agree_personal_data()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button.open()
            radio_button.agree_personal_data()
            radio_button.click_on_the_radio_button('yes')
            output_yes = radio_button.get_output_result()
            radio_button.click_on_the_radio_button('impressive')
            output_impressive = radio_button.get_output_result()
            radio_button.click_on_the_radio_button('no')
            output_no = radio_button.get_output_result()
            assert output_yes == 'Yes', 'Yes have not been selected'
            assert output_impressive == 'Impressive', 'Impressive have not been selected'
            assert output_no == 'No', 'No have not been selected'

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.agree_personal_data()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.agree_personal_data()
            key_world = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_same_person(key_world)
            table_result = web_table_page.check_search_person()
            assert key_world in table_result, 'the peron was not found in the table'
