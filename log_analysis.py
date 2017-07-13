#! /usr/bin/env
#PROJECT:-LOG ANALYSIS
import psycopg2

DB_NAME = "news"

# 1. What are the most popular three articles of all time?
query_1 = "select title,views from articles_view limit 3"

# 2. Who are the most popular article authors of all time?
query_2 = """select authors.name,sum(articles_view.views) as views from
articles_view,authors where authors.id = articles_view.author
group by authors.name order by views desc"""

# 3. On which days did more than 1% of requests lead to errors?
query_3 = "select * from log_error_view where \"Error\" > 1"

#query data from tables
def get_query_results(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

#print title and results of first and second questions
def print_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' --> ' + str(result[1]) + ' views')

#print title and results of question3
def print_error_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' --> ' + str(result[1]) + ' %')

if __name__ == "__main__":
	# stores query result
	query_1_result = dict()
	query_1_result['title'] = "\n1.What are the most popular three articles of all time?\n"
	query_1_result['results'] = get_query_results(query_1)
	
	query_2_result = dict()
	query_2_result['title'] = "\n2.Who are the most popular article authors of all time?\n"
	query_2_result['results'] = get_query_results(query_2)
	
	query_3_result = dict()
	query_3_result['title'] = "\n3.On which days did more than 1% of requests lead to errors?\n"
	query_3_result['results'] = get_query_results(query_3)

	# print formatted output
	print_query_results(query_1_result)
	print_query_results(query_2_result)
	print_error_query_results(query_3_result)