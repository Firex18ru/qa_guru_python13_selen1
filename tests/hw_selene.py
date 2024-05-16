from selene import browser, have, be


def test_demoqa():

    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Yakimenko")
    browser.element("#userEmail-wrapper").type("Firex1@yandex.ru")

    browser.element("#genterWrapper").all("label[for^=gender-radio]").element_by(
        have.text("male")
    ).click()
