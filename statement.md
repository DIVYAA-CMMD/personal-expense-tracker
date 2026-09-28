

## Name

Personal Expense Tracker

## Problem Statement

Managing daily expenses manually can be difficult. It can be hard to keep track of money on daily basis.

This project is a simple Expense Tracker made using Python. It allows the user to add, view, search, calculate total expenses, find the highest expense, delete expenses, and see expenses category-wise.

## Features

* Add a new expense
* View all expenses
* Search expenses by category
* Calculate total expenses
* Find the highest expense
* Delete an expense
* View category-wise expense summary


## Technologies Used

* Python
* Text file (`exp.txt`) for storing data

## How It Works

The program stores expenses in a list of dictionaries. Each expense contains a name, amt, and category.

The `load()` function reads previously saved expenses from the file when the program starts. The `save()` function saves the current expenses to the file after adding or deleting an expense.

The program displays a menu where the user can select different operations.

## Expected Outcome

The project provides a simple way to record and manage daily expenses using basic Python concepts such as functions, lists, dictionaries, loops, conditions, file handling, and user input.
