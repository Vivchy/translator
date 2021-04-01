from selenium import webdriver
import time


def main():
    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        executable_path='G:\\Project_Python\\translator google\\chromedriver\\chromedriver.exe',
        options=options
    )
    text = 'The Internet was invented in the late 1960s by the US Defense Department’s Advanced Research Projects Agency. In 1969, there was a network of just four mainframe computers. A mainframe computer is a large, powerful computer, shared by many users. The idea of the electronic mailbox was born when users looked for a way to talk to each other electronically. '
    try:
        driver.get("https://translate.google.com/?hl=ru&sl=auto&tl=ru&op=translate")
        time.sleep(3)
        original_text_input = driver.find_element_by_xpath('//textarea[@aria-label="Исходный текст"]')
        original_text_input.clear()
        original_text_input.send_keys(text)
        time.sleep(5)
        translate_text = driver.find_element_by_class_name('J0lOec').text
        print(translate_text)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
