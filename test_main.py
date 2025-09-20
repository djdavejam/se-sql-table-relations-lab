import sqlite3
import pandas as pd
from main import *

def test_join_and_filter():
    # Test Step 1 - Boston employees
    assert(df_boston.shape == (2, 3))
    assert(list(df_boston['firstName']) == ['Julie', 'Steve'])
    
    # Test Step 2 - Offices with zero employees
    assert(df_zero_emp.shape[0] == 0)

def test_type_of_join():
    # Test Step 3 - All employees with office info
    assert(df_employee.shape == (23, 4))
    assert(df_employee.iloc[0]['firstName'] == 'Andy')
    
    # Test Step 4 - Customers with no orders
    assert(df_contacts.shape == (24, 4))
    assert(list(df_contacts['contactLastName'])[0:3] == ['Altagar,G M', 'Andersen', 'Anton'])

def test_builtin_function():
    # Test Step 5 - Payment information with proper sorting
    assert(df_payment.shape == (273, 4))
    assert(df_payment.iloc[0]['contactFirstName'] == 'Diego ')

def test_joining_and_grouping():
    # Test Step 6 - Employees with high credit limit customers
    assert(df_credit.shape == (4, 4))
    assert(df_credit.iloc[0]['firstName'] == 'Larry')
    
    # Test Step 7 - Product sales information
    assert(df_product_sold.shape == (109, 3))
    assert(df_product_sold.iloc[0]['totalunits'] == 1808)

def test_multiple_joins():
    # Test Step 8 - Products and their customer reach
    assert(df_total_customers.shape == (109, 3))
    assert(df_total_customers.iloc[0]['numpurchasers'] == 40)
    
    # Test Step 9 - Customers per office
    assert(df_customers.iloc[0]['n_customers'] == 29)
    assert('n_customers' in list(df_customers.columns))

def test_subquery():
    # Test Step 10 - Employees who sold underperforming products
    assert(df_under_20.shape == (15, 5))
    assert(df_under_20.iloc[0]['firstName'] == 'Leslie')