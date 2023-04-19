from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.get('http://practice.automationtesting.in/')
driver.maximize_window()

#Đăng kí trong email
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
passs = driver.find_element_by_id("reg_password")
passs.send_keys("3KVfE7BvLaTc@7E")
time.sleep(5)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]")).click()
time.sleep(3)

#Đăng kí trống mật khẩu
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
email = driver.find_element_by_id("reg_email")
email.send_keys("MayNhut@yahoo.com")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]")).click()
time.sleep(3)

#Đăng kí trống cả email cả mật khẩu
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]")).click()
time.sleep(3)

# Đăng kí thành công
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
email = driver.find_element_by_id("reg_email")
email.send_keys("MayNhut@yahoo.com")
time.sleep(3)
passs = driver.find_element_by_id("reg_password")
passs.send_keys("3KVfE7BvLaTc@7E")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]")).click()
time.sleep(3)

#Đăng nhập trống email
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
passs = driver.find_element_by_id("password")
passs.send_keys("3KVfE7BvLaTc@7E")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()
time.sleep(3)

# Đăng nhập trống mật khẩu
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
email = driver.find_element_by_id("username")
email.send_keys("MayNhut@yahoo.com")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()
time.sleep(3)

#Đăng nhập không có email và mật khẩu
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()

#Đăng nhập sai mật khẩu
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
email = driver.find_element_by_id("username")
email.send_keys("MayNhut@yahoo.com")
time.sleep(3)
passs = driver.find_element_by_id("password")
passs.send_keys("mayvanhut2001")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()
time.sleep(3)

#Đăng nhập thành công
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
email = driver.find_element_by_id("username")
email.send_keys("MayNhut@yahoo.com")
time.sleep(3)
passs = driver.find_element_by_id("password")
passs.send_keys("3KVfE7BvLaTc@7E")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()
time.sleep(3)

#Đăng xuất
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/p[1]/a")).click()
time.sleep(5)
driver.execute_script("window.history.go(-1)")

#Đăng nhập thành công
email = driver.find_element_by_id("username")
email.send_keys("MayNhut@yahoo.com")
time.sleep(3)
passs = driver.find_element_by_id("password")
passs.send_keys("3KVfE7BvLaTc@7E")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()
time.sleep(3)

#Xem chi tiết sp
driver.find_element_by_link_text("Shop").click()
time.sleep(5)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/ul/li[2]/a[1]/img")).click()

#Thêm sp vào giỏ hàng
add_product = driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div[2]/form/div/input"))
add_product.clear()
add_product.send_keys("2")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/form/button").click()
time.sleep(2)

#Xem chi tiết sp2
driver.find_element_by_link_text("Shop").click()
time.sleep(5)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/ul/li[1]/a[1]/img")).click()
time.sleep(2)

#Thêm sp2 vào giỏ hàng
add_product1 = driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div[2]/form/div/input"))
add_product1.clear()
add_product1.send_keys("2")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/form/button").click()
time.sleep(2)


#Tăng sp

driver.find_element_by_link_text("VIEW BASKET").click()
plus_product = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
plus_product.send_keys(Keys.UP)
time.sleep(5)

#Giảm sp
minus_product = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
minus_product.send_keys(Keys.DOWN)
time.sleep(5)


#Xoá sp
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[1]/a").click()
time.sleep(3)


#Thanh toán
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/a")).click()
time.sleep(3)
firstname = driver.find_element_by_id("billing_first_name")
firstname.send_keys("MayNhut")
lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Nguyen")

company = driver.find_element_by_id("billing_company")
company.send_keys("MayNhut")


phone = driver.find_element_by_id("billing_phone")
phone.send_keys("0123456789")

add = driver.find_element_by_id("billing_address_1")
add.send_keys("VietNam")

add2 = driver.find_element_by_id("billing_postcode")
add2.send_keys("12345")

city = driver.find_element_by_id("billing_city")
city.send_keys("DaNang")

note = driver.find_element_by_id("order_comments")
note.send_keys("do de vo, dong goi can than")

time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[2]/div/div/input[1]").click()
time.sleep(3)

