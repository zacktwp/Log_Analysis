## Log Analysis Project

This is the first project in the Udacity full stack nanodegree program where we will explore basic concepts regarding python, relational databases, queries, and views.

In this project, you are expected to write PostgreSQL queries that connect to the newsdata.sql database in a python file to answer the three questions below:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Dependencies:
python 3.6, PostgreSQL 9.5.16, Vagrant, VirtualBox, newsdata.sql

## How to run:
1. Install Dependencies: [python3](https://www.python.org/downloads/), [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Vagrant](https://www.vagrantup.com/downloads.html), [News DB](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. Download the files in [github repo](https://github.com/zacktwp/Log_Analysis) into a chosen directory.
3. Create virtual machine in that directory of choice by cd-ing into that directory and type 'vagrant up' in the command line.
4. You will need to unzip the newsdata.zip file downloaded earlier. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
5. Place all other files from the github repo into the vagrant directory.
5. type 'vagrant ssh' to ssh into the virtual machine.
5. Navigate to the /vagrant directory where you will find Logs_Analysis_project.py
6. type: python Logs_Analysis_project.py into the terminal and you will see your results
