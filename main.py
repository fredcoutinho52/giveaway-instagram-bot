from selenium import webdriver
from time import sleep
import math

# path for the chromedriver
oper_sys = 'YOUR-OS-HERE'
driver_path = oper_sys.lower() + '/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)

# user data and draw's profile
username = "YOUR-USERNAME-HERE"
password = "YOUR-PASSWORD-HERE"
post_link = "POST-LINK-HERE"

# login on instagram
def access_account():
    driver.get("https://www.instagram.com")
    sleep(3)

    print('Logging on Instagram...')
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(4)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
    sleep(2)

    get_followers()

# capture the followers's usernames
def get_followers():
    print("Accessing follower's list...")

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    sleep(3)

    # get number of followers
    followers_number = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('textContent')
    
    if '.' in followers_number:
        followers_number = followers_number.replace('.', '')
    
    list_to_scroll = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div')
    sleep(2)

    # scroll the followers's list to the end
    print("Getting follower's names...")
    scroll_times = int(math.ceil(int(followers_number) / 8))
    for i in range(scroll_times):
        driver.execute_script('document.querySelector(".PZuss").scrollIntoView(false)')
        sleep(2)

    # get each username in the followers's list
    print("Putting names in a list...")
    usernames_elements = list_to_scroll.find_elements_by_tag_name('a')
    usernames_list = [user.text for user in usernames_elements if len(user.text) > 0]
    sleep(2)

    driver.refresh()
    sleep(2)

    search_profile(usernames_list)

# search the draw's profile and publication
def search_profile(usernames):
    driver.get(post_link)

    print("Commenting on post...")
    for i in range(0, len(usernames), 3):
        can_press = True

        while can_press:
            try:
                # click on comment area
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').click()
                sleep(4)
                can_press = False
            except:
                # press post button if comment is blocked
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
                sleep(4)
        
        # write follower's username
        message = '@' + usernames[i] + ' @' + usernames[i + 1] + ' @' + usernames[i + 2]
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').send_keys(message)
        sleep(2)
        
        # press post button
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
        sleep(2)


access_account()