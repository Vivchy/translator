from selenium import webdriver
import time
import os


def get_translate(driver, text):
    """
    :param driver: url
    :param text: текст для перевода
    :return: перевод
    """
    time.sleep(3)
    original_text_input = driver.find_element_by_xpath('//textarea[@aria-label="Исходный текст"]')
    original_text_input.clear()
    original_text_input.send_keys(text)
    time.sleep(3)
    translate_text = driver.find_element_by_class_name('J0lOec').text
    return translate_text


def main(parent_folder):
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
        folders = os.listdir(parent_folder)
        format_text = ['.txt', '.doc', '.docx']
        for folder in folders:
            print(folder)
            path = f'{parent_folder}\{folder}'

            files = os.listdir(path)
            num = 0
            for file in files:
                num += 1
                path_2 = f'{parent_folder}\{folder}\{file}'

                if os.path.isfile(path_2):
                    for i in format_text:

                        text = ''
                        new_text = ''
                        if i in file:
                            with open(path_2, 'r', encoding='utf-8') as fl:
                                print('файл открыт для перевода ', path_2)
                                text = fl.read()
                            try:
                                new_text = get_translate(driver, text)
                                print('файл переведен ', path_2)
                            except Exception as e:
                                print(e)
                            save_file = f'{path}\\translate_{num}.txt'

                            with open(save_file, 'w', encoding='utf-8') as fl:
                                fl.write(new_text)
                                print(f'записан перевод в нов файл {save_file}')
                                print('\n')
                else:
                    # еще вложеная папка
                    print('else folder')

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main(parent_folder='texts')
