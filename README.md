#  Expense Tracker

A simple Python-based Expense Tracker that helps users record and manage their daily expenses.

The project uses a text file to store expenses, so the saved data can be loaded again when the program is started.

---

##  Project Overview

Managing daily expenses can become difficult when there are many small transactions.

This project provides a simple command-line solution where users can:

 Add expenses
 View all expenses
 Search expenses by category
 Calculate total expenses
 Find the highest expense
 Delete an expense
 View category-wise expense summaries

---

##  Features

| Option              | Function                                         |
| ------------------- | ------------------------------------------------ |
|  Add Expense       | Add a new expense with name, amount and category |
|  View Expenses    | Display all saved expenses                       |
|  Search Category  | Find expenses belonging to a category            |
|  Total Expenses   | Calculate the total amount spent                 |
|  Highest Expense  | Find the expense with the highest amount         |
|  Delete Expense  | Remove an expense from the list                  |
|  Category Summary | Display total spending for each category         |
|  Exit             | Close the program                                |

---

##  Technologies Used

**Python**
 **Text File Handling**
 Lists
 Dictionaries
Functions
 Loops
 Conditional Statements
 User Input

No external Python libraries are required.

---

##  Project Structure


Expense_tracker/
│
├── main.py
├── exp.txt
├── README.md
└── statement.md


### Files

**`main.py`**
Contains the main Python program and all expense-tracking functions.

**`exp.txt`**
Stores the expenses entered by the user.

**`README.md`**
Contains information about the project.

**`statement.md`**
Contains the project statement and objectives.

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version using:

```bash
python --version
```

### 2. Open the project folder

Open the `Expense_tracker` folder in VS Code or a terminal.

### 3. Run the program

```bash
python main.py
```

The expense tracker menu will appear in the terminal.

---

## 🖥️ Example Menu

```text
///// EXPENSE TRACKER /////

1.Add exp
2.View exp
3.Search category
4.Total exp
5.Highest exp
6.Delete
7.category Summary
8.Exit

Choice:
```

---

##  Data Storage

The program stores expense information in `exp.txt`.

Each expense contains:

 Expense name
 Amount
 Category

Example:

```text
Food,150.0,Food
Notebook,80.0,Education
Bus Ticket,40.0,Travel
```

The program loads previously saved expenses when it starts.

---

##  Learning Objectives

This project demonstrate a python based outcome thats useful.
