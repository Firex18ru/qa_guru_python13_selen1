from selene import browser, have, be


def test_complete_todo():

    browser.open("/")
    browser.element("#firstName").type("Ivan").press_enter()
    browser.element("#lastName").type("Yakimenko").press_enter()
    browser.element("#userEmail-wrapper").tupe("Firex1@yandex.ru").press_enter()
