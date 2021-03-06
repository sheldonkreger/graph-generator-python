import names
import csv
from random import randint

def generate_users(num_users, users_file_path):
    with open(users_file_path, 'wb') as csv_file:
        wr = csv.writer(csv_file)
        # Add header to CSV.
        wr.writerow(('user_id', 'name'))
        i = 1
        while i in range (1, num_users + 1):
            user_item = []
            user_item.append(i)
            # Grab user name from 1990 Census data. Cool!
            user_item.append(names.get_full_name());
            wr.writerow(user_item)
            i = i + 1

def generate_pages(num_pages, node_type, pages_file_path):
    with open(pages_file_path, 'wb') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerow(('page_id', 'node_type'))
        i = 1
        while i in range (1, num_pages + 1):
            page_item = []
            page_item.append(i)
            page_item.append(node_type)
            wr.writerow(page_item)
            i = i + 1

def generate_connections(num_users, num_pages, max_edges, edges_file_path):
    with open(edges_file_path, 'wb') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerow(("user_id", "page_id"))
        i = 1
        while i in range (1, num_users + 1):
            # print "i: %i" % i
            i = i + 1
            rand = randint(0, max_edges)
            # print "rand: %r" % rand

            j = 0
            while j in range (0, rand):
                j = j + 1
                # print "j: %s" % j
                page_id = randint(1, num_pages)
                connection = []
                connection.append(i)
                connection.append(page_id)
                wr.writerow(connection)




num_users = 10
num_pages = 100
max_edges = 10
node_type = 'article'

generate_users(num_users, '/Users/skregerx/data/python_users.csv')
generate_pages(num_pages, node_type, '/Users/skregerx/data/python_pages.csv')
generate_connections(num_users, num_pages, max_edges, '/Users/skregerx/data/python_connections.csv')
