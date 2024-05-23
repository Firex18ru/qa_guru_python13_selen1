from selene import browser, have, be, by


def test_demoqa_form():
    # открываю регистрационную форму
    browser.open("/automation-practice-form")
    # заполняю ФИО
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Yakimenko")
    # указываю адрес электронной почты
    browser.element("#userEmail").type("Def11@def.ru")
    # указываю пол
    browser.element('[for="gender-radio-1"]').click()
    # указываю номер контактного телефона
    browser.element("#userNumber").type("+79997776019")
    # указываю дату рождения
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(
        "[value = '1']"
    ).click()
    browser.element(".react-datepicker__year-select").click().element(
        "[value = '1989']"
    ).click()
    browser.all(".react-datepicker__day--001").second.click()

    browser.element("#subjectsInput").type("other")
