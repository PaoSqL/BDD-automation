from pages.login_page import LoginPage
from behave import *

login_page = LoginPage()

@when('login: I login with valid credential')
def step_impl(context):
    login_page.fill_user_input('pao.Sql')
    login_page.fill_pass_input('Comprehensiune25#')
    login_page.click_login_button()

