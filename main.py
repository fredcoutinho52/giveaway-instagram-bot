from selenium import webdriver
from time import sleep
import math

# path for the chromedriver
oper_sys = 'windows'
driver_path = oper_sys.lower() + '/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)

# user data and draw's profile
username = 'fredcoutinho52'
password = 'fredflor3414'
profile = 'igr.brc'

# login on instagram
def access_account():
    driver.get("https://instagram.com")
    sleep(3)

    driver.find_element_by_xpath("//a[contains(text(), 'Conecte-se')]").click()
    sleep(2)

    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(4)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
    sleep(2)

# capture the followers's usernames
def get_followers():
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    sleep(2)

    # get number of followers
    followers_number = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('textContent')
    
    list_to_scroll = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div')
    sleep(2)

    # scroll the followers's list to the end
    scroll_times = int(math.ceil(int(followers_number) / 8))
    for i in range(scroll_times):
        driver.execute_script('document.querySelector(".PZuss").scrollIntoView(false)')
        sleep(2)

    # get each username in the followers's list
    usernames_elements = list_to_scroll.find_elements_by_tag_name('a')
    usernames_list = [user.text for user in usernames_elements if len(user.text) > 0]
    sleep(1)

    search_profile(usernames_list)

# search the draw's profile and publication
def search_profile(usernames_list):
    driver.refresh()
    sleep(2)

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(profile)
    sleep(2)

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
    sleep(4)

    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a').click()
    sleep(4)

    for user in usernames_list:
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys('@' + user)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(Keys.ENTER)
        sleep(1)


access_account()
get_followers()