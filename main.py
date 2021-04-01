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
    try:
        driver.get("https://translate.google.com/?hl=ru&sl=auto&tl=ru&op=translate")
        time.sleep(3)


    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
