from selene import browser, have
import os


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
    browser.element("#userNumber").type("0999777601")

    # указываю дату рождения
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(
        "[value = '0']"
    ).click()
    browser.element(".react-datepicker__year-select").click().element(
        "[value = '1989']"
    ).click()
    browser.all(".react-datepicker__day--001").second.click()

    # указываю увлечения
    browser.element("#subjectsInput").type("Computer Science").press_enter()
    browser.element("[for = hobbies-checkbox-1]").click()
    browser.element("[for = hobbies-checkbox-2]").click()

    # загружаю картинку
    browser.element("#uploadPicture").send_keys(os.path.abspath("./picture/094745.png"))

    # указываю текущий адрес
    browser.element("#currentAddress").type("Izhevsk")

    # указываю штат и город
    browser.element("#state").click().element("#react-select-3-option-0").click()
    browser.element("#city").click().element("#react-select-4-option-0").click()

    # отправляю анкету
    browser.element("#submit").press_enter()

    # проверка анкеты

    browser.element(".modal-content").element("table").all("tr").all("td").even.should(
        have.exact_texts(
            "Ivan Yakimenko",
            "Def11@def.ru",
            "Male",
            "0999777601",
            "01 February,1989",
            "Computer Science",
            "Sports, Reading",
            "094745.png",
            "Izhevsk",
            "NCR Delhi",
        )
    )

    browser.element("#closeLargeModal").click()
