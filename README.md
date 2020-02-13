# Bot for Instagram's draws
A tool for automatization of participation in instagram's draws

## Used tools
* [Pip](https://pypi.org/project/pip/)
* [Python 3](https://www.python.org/)
* [Selenium](https://selenium.dev/)
* [Visual Studio Code](https://code.visualstudio.com/)

## How to use

### Install dependencies

```
pip install selenium
```

### Change operational system

```python
oper_sys = 'YOUR-OPERATIONAL-SYSTEM'
```

### Put necessary data

```python
# user data and draw's profile
username = 'YOUR-USERNAME'
password = 'YOUR-PASSWORD'
profile = 'DRAW-PROFILE'
```

### Choose publication

```python
driver.find_element_by_xpath('PUBLICATION-XPATH').click()
```