import random
import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage
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

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.agree_personal_data()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_same_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'the person card has not been changed'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.agree_personal_data()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_same_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.agree_personal_data()
            count = web_table_page.select_up_to_same_rows()
            assert count == [5, 10, 10, 20, 25, 50, 100], 'the number of rows in the table has not been changed or ' \
                                                          'changed incorrectly'

    class TestButtonsPage:
        def test_different_click_on_the_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            button_page.agree_personal_data()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', "The double click button was not pressed"
            assert right == 'You have done a right click', "The right click button was not pressed"
            assert click == 'You have done a dynamic click', "The click button was not pressed"
