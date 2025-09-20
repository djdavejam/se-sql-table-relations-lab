# SQL Table Relations Lab

## Quick Setup
1. Fork and clone the repo
2. Install dependencies: `pipenv install && pipenv shell`
3. Run tests: `pytest`
4. Run your code: `python3 main.py`

## What You Need to Do
Complete 10 SQL queries in `main.py` that demonstrate joins, subqueries, and data analysis using the Northwind database.

## The Tasks

### Part 1: Basic Joins (Steps 1-2)
- **Step 1**: Find Boston employees (names and job titles)
- **Step 2**: Find offices with zero employees

### Part 2: Different Join Types (Steps 3-4)
- **Step 3**: List all employees with their office locations
- **Step 4**: Find customers who haven't placed any orders

### Part 3: Functions & Grouping (Steps 5-7)
- **Step 5**: Customer payment report (sorted by amount)
- **Step 6**: Employees with high-credit-limit customers (>$90k average)
- **Step 7**: Top-selling products by quantity

### Part 4: Multiple Joins (Steps 8-9)
- **Step 8**: Customer reach per product
- **Step 9**: Customer count per office

### Part 5: Subqueries (Step 10)
- **Step 10**: Employees who sold underperforming products (<20 customers)

## Key Database Tables
- `employees` - Employee information
- `offices` - Office locations
- `customers` - Customer data
- `orders` - Order records
- `orderdetails` - Order line items
- `products` - Product catalog
- `payments` - Payment transactions

## Tips
- Use the ERD diagram to understand table relationships
- Look for shared columns to create joins
- Test your queries incrementally
- Run `pytest -v` for detailed test output

## Expected Results
Each step has specific expected outputs tested by the test suite. Make sure your queries return the correct data types, column names, and sorting order.