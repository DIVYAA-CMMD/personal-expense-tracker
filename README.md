# Personal Expense Tracker

## About the Project

Personal Expense Tracker is a simple Python command-line application used to record and manage daily expenses.

The program allows the user to:

* Add a new expense
* View all recorded expenses
* Search expenses by category
* Calculate total spending
* Find the highest expense
* Delete an expense
* View category-wise spending

The expense data is stored in a CSV file so that the records remain available even after closing the program.

## Features

* Menu-driven command-line interface
* Add, view, search, and delete expenses
* Total spending calculation
* Highest expense calculation
* Category-wise spending summary
* Input validation for basic user errors
* CSV-based data storage

## Technologies Used

* Python 3.x
* CSV file handling
* Visual Studio Code
* Git and GitHub

## Project Structure

```text
Expense_tracker/
│
├── main.py
├── file_handler.py
├── expenses.csv
├── statement.md
└── README.md
```

`main.py` contains the main program and user interaction.

`file_handler.py` contains functions used to read and save expense data.

`expenses.csv` stores the expense records.

`statement.md` contains the project statement and scope.

## Requirements

* Python 3.x
* No external Python libraries are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Make sure Python is installed by running:

```bash
python --version
```

4. Run the project using:

```bash
python main.py
```

5. Select an option from the menu and enter the required information.

## Testing

The project can be tested directly through the command line.

The following operations should be tested:

* Adding a valid expense
* Viewing saved expenses
* Searching for an existing category
* Calculating total spending
* Finding the highest expense
* Deleting an expense
* Viewing the category-wise summary
* Entering invalid amounts or menu choices

## Data Storage

Expense records are stored in `expenses.csv`. Each record contains:

* Expense name
* Amount
* Category

The CSV file is kept in the project folder so that saved records can be loaded when the program starts.
