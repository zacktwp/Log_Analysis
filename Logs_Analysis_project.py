#!/usr/bin/env python3

import psycopg2

# queries
query1 = """SELECT title, count(title) AS views
            FROM articles, log
            WHERE log.path=CONCAT('/article/',articles.slug)
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;"""

query2 = """SELECT authors.name, count(*) as views
            FROM articles
            inner JOIN authors on articles.author = authors.id
            inner JOIN log on log.path LIKE concat('%', articles.slug, '%')
            WHERE log.status LIKE '%200%'
            GROUP BY authors.name
            ORDER BY views DESC;"""

query3 = """SELECT *
            FROM (SELECT date(time),round(100.0*sum(CASE log.status
            WHEN '200 OK'  THEN 0 ELSE 1 END)/count(log.status),2) AS error
            FROM log
            GROUP BY date(time)
            ORDER BY error DESC) AS subquery
            WHERE error > 1;"""

# connect to the database
db = psycopg2.connect(database='news')
cursor = db.cursor()
# Execute queries
cursor.execute(query1)
# Return result of the query
result1 = cursor.fetchall()
print('What are the most popular three articles of all time? \n')
print('{} with {} views \n').format(result1[0][0],result1[0][1])
print('{} with {} views \n').format(result1[1][0],result1[1][1])
print('{} with {} views \n').format(result1[2][0],result1[2][1])

cursor.execute(query2)
# Return result of the query
result2 = cursor.fetchall()
print('Who are the most popular article authors of all time? \n')
print('{} with {} views \n').format(result2[0][0],result2[0][1])
print('{} with {} views \n').format(result2[1][0],result2[1][1])
print('{} with {} views \n').format(result2[2][0],result2[2][1])

cursor.execute(query3)
# Return result of the query
result3 = cursor.fetchall()
print('On which days did more than 1% of requests lead to errors? \n')
print('{} with error of {} percent').format(result3[0][0],result3[0][1])

db.close()
