# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# The company would like to let Boston employees go remote but need to know more information about who is working in that office. 
# Return the first and last names and the job titles for all employees in Boston.
df_boston = pd.read_sql("""
    SELECT e.firstName, e.lastName, e.jobTitle
    FROM employees e
    JOIN offices o ON e.officeCode = o.officeCode
    WHERE o.city = 'Boston'
""", conn)

# STEP 2
# Recent downsizing and employee attrition have caused some mixups in office tracking and the company is worried they are supporting a 'ghost' location. 
# Are there any offices that have zero employees?
df_zero_emp = pd.read_sql("""
    SELECT o.officeCode, o.city, o.country
    FROM offices o
    LEFT JOIN employees e ON o.officeCode = e.officeCode
    WHERE e.employeeNumber IS NULL
""", conn)

# STEP 3
# As a part of this larger analysis project the HR department is taking the time to audit employee records to make sure nothing is out of place 
# and have asked you to produce a report of all employees. Return the employees first name and last name along with the city and state of the office 
# that they work out of (if they have one). Include all employees and order them by their first name, then their last name.
df_employee = pd.read_sql("""
    SELECT e.firstName, e.lastName, o.city, o.state
    FROM employees e
    LEFT JOIN offices o ON e.officeCode = o.officeCode
    ORDER BY e.firstName, e.lastName
""", conn)

# STEP 4
# The customer management and sales rep team know that they have several 'customers' in the system that have not placed any orders. 
# They want to reach out to these customers with updated product catalogs to try and get them to place initial orders. 
# Return all of the customer's contact information (first name, last name, and phone number) as well as their sales rep's employee number 
# for any customer that has not placed an order. Sort the results alphabetically based on the contact's last name
df_contacts = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
    FROM customers c
    LEFT JOIN orders o ON c.customerNumber = o.customerNumber
    WHERE o.orderNumber IS NULL
    ORDER BY c.contactLastName
""", conn)

# STEP 5
# The accounting team is auditing their figures and wants to make sure all customer payments are in alignment, 
# they have asked you to produce a report of all the customer contacts (first and last names) along with details for each of the customers' 
# payment amounts and date of payment. They have asked that these results be sorted in descending order by the payment amount.
df_payment = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, CAST(p.amount AS REAL) as amount, p.paymentDate
    FROM customers c
    JOIN payments p ON c.customerNumber = p.customerNumber
    ORDER BY CAST(p.amount AS REAL) DESC
""", conn)

# STEP 6
# The sales rep team has noticed several key team members that stand out as having trustworthy business relations with their customers, 
# reflected by high credit limits indicating more potential for orders. The team wants you to identify these 4 individuals. 
# Return the employee number, first name, last name, and number of customers for employees whose customers have an average credit limit over 90k. 
# Sort by number of customers from high to low.
df_credit = pd.read_sql("""
    SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) as numCustomers
    FROM employees e
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY e.employeeNumber, e.firstName, e.lastName
    HAVING AVG(c.creditLimit) > 90000
    ORDER BY numCustomers DESC
""", conn)

# STEP 7
# The product team is looking to create new model kits and wants to know which current products are selling the most in order to get an idea of what is popular. 
# Return the product name and count the number of orders for each product as a column named 'numorders'. 
# Also return a new column, 'totalunits', that sums up the total quantity of product sold (use the quantityOrdered column). 
# Sort the results by the totalunits column, highest to lowest, to showcase the top selling products.
df_product_sold = pd.read_sql("""
    SELECT p.productName, COUNT(DISTINCT od.orderNumber) as numorders, SUM(od.quantityOrdered) as totalunits
    FROM products p
    JOIN orderdetails od ON p.productCode = od.productCode
    GROUP BY p.productCode, p.productName
    ORDER BY totalunits DESC
""", conn)

# STEP 8
# As a follow-up to the above question, the product team also wants to know how many different customers ordered each product to get an idea of market reach. 
# Return the product name, code, and the total number of customers who have ordered each product, aliased as 'numpurchasers'. 
# Sort the results by the highest number of purchasers.
df_total_customers = pd.read_sql("""
    SELECT p.productName, p.productCode, COUNT(DISTINCT o.customerNumber) as numpurchasers
    FROM products p
    JOIN orderdetails od ON p.productCode = od.productCode
    JOIN orders o ON od.orderNumber = o.orderNumber
    GROUP BY p.productCode, p.productName
    ORDER BY numpurchasers DESC
""", conn)

# STEP 9
# The custom relations team is worried they are not staffing locations properly to account for customer volume. 
# They want to know how many customers there are per office. Return the count as a column named 'n_customers'. 
# Also return the office code and city.
df_customers = pd.read_sql("""
    SELECT o.officeCode, o.city, COUNT(c.customerNumber) as n_customers
    FROM offices o
    JOIN employees e ON o.officeCode = e.officeCode
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY o.officeCode, o.city
    ORDER BY n_customers DESC
""", conn)

# STEP 10
# Having looked at the results from above, the product team is curious to dig into the underperforming products. 
# They want to ask members of the team who have sold these products about what kind of messaging was successful in getting a customer to buy these specific products. 
# Using a subquery or common table expression (CTE), select the employee number, first name, last name, city of the office, and the office code 
# for employees who sold products that have been ordered by fewer than 20 customers.
df_under_20 = pd.read_sql("""
    SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode
    FROM employees e
    JOIN offices o ON e.officeCode = o.officeCode
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    JOIN orders ord ON c.customerNumber = ord.customerNumber
    JOIN orderdetails od ON ord.orderNumber = od.orderNumber
    WHERE od.productCode IN (
        SELECT p.productCode
        FROM products p
        JOIN orderdetails od ON p.productCode = od.productCode
        JOIN orders o ON od.orderNumber = o.orderNumber
        GROUP BY p.productCode
        HAVING COUNT(DISTINCT o.customerNumber) < 20
    )
    ORDER BY e.employeeNumber
""", conn)

# Close the connection
conn.close()