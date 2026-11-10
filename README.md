# SQL Contact Book: Object-Oriented Database Manager

## Overview
So this is basically a backend Python app that manages a contact directory, but instead of dumping everything into a static file, it stores all the contacts in a persistent MySQL database. The whole point of the project is to show how Object-Oriented Programming (OOP) and relational databases work together — you get a dynamic, secure, and fully interactive data access layer instead of some flat file sitting on disk.

## Technical Architecture
* **Language:** Python 3
* **Database:** MySQL
* **Driver:** `mysql-connector-python`
* **Interface:** Interactive Command-Line Interface (CLI)

## Key Features
* **Object-Oriented Design:** Everything related to the database — connection lifecycles, cursors, transactions — is wrapped inside a solid DatabaseManager class. That way the main execution loop stays clean and modular instead of being one giant mess of SQL calls.
* **Automated Initialization:** On startup, the app sets up its own environment with CREATE TABLE IF NOT EXISTS, so the schema is always ready before any data gets thrown at it — no manual setup needed.
* **Security & Parameterization:** Built with security in mind. Every insertion uses parameterized SQL queries (tuple bindings via %s), which strictly prevents SQL injection vulnerabilities. 
* **Stateful CLI Engine:** It runs an interactive while-loop menu that keeps taking user input, routes each command to the database engine, and safely closes any active connections when you exit.   


## Setup & Installation
1. Ensure you have a MySQL server running locally.
2. Install the required MySQL connector for Python:
   pip install mysql-connector-python
3. Update the database credentials (host, user, password, database) in the __init__ method of the DatabaseManager class to match your local MySQL environment.