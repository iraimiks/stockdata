# stockdata
Tasks for work with stock API data

API for stock I use from AlphaVantage https://www.alphavantage.co/documentation/

Scripts were developed on Win10 
To test this script I use
Python virtual environment: https://docs.python.org/3/library/venv.html guide for preparation.

For database I use Oracle 19c:
I use this guide to install Oracle DB https://www.youtube.com/watch?v=Fe3y-QstF0w
And hear is prepared done action https://github.com/icyb3r-code/DBAdmin/tree/main/Oracle/Install_Oracle19c_SingleInstance

This script was cheked on:
OS Oracle Linux 8 
Oracle DB 19c


TODO Anisble:
Use Ansible

a. to install database client (driver) on additional Linux server
b. to execute created scripts
c. to retrieve the file

Create separate script:

1. Create a script which will create a table and generate sample data
2. Create a script to retrieve subset of generated data in CSV format.
