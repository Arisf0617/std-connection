from selenium import webdriver
import os

def read():
    i = 0
    try:
        f = open("STD.ini", encoding='utf-8')
        line = f.readline()
        list = ['', '', '']
        while line:
            list[i] = line.split('=')[1].replace('\n', '')
            line = f.readline()
            i = i + 1
        f.close()
    except Exception as e:
        print("配置文件错误")
        print("except:", e)
    return list


list = read()
try:
    browser = webdriver.Edge(executable_path=list[0],capabilities={"ms:edgeOptions": {
                                                                            'args': ['--headless',
                                                                                        '--disable-gpu'
                                                                                        ]}})
except Exception as e:
    print("驱动错误", format(e))
    os._exit(0)


try:
    browser.get("http://1.1.1.1")
    name = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[1]/div/div[2]/input')
    password = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[1]/div/div[3]/input')
except Exception as e:
    print("已经连接到网络")
    print("except:", e)
    browser.quit()
    os._exit(0)
else:
    name.send_keys(list[1])
    password.send_keys(list[2])
    browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[1]/div/div[5]/button').click()
finally:
    try:
        alert = browser.find_elements_by_xpath('/html/body/div[4]/div[4]/button')
    except Exception as e:
        print('登录失败', format(e))
    try:
        messages = browser.find_element_by_xpath('/html/body/div[3]/div[2]')
        try:
            for message in messages:
                assert '账号或密码不正确' in message.text
                print('登录失败')
        except Exception as e:
            print('账号或密码不正确', format(e))
    except Exception as e:
        print('登录成功', format(e))
    finally:
        browser.quit()
        os._exit(0)

