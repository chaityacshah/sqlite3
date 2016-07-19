import sqlite3
import time
import datetime
import random
from dateutil import parser
import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549217,'2016-01-11 13:53:39','Python',6)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()


def read_from_db():
    c.execute('''SELECT * FROM stuffToPlot WHERE value = 9 AND keyword = 'Python' ''')
    # data = c.fetchall()
    # print(data)
    for row in c.fetchall():
        print row
#        print row[0]

def graph_data():
    c.execute('SELECT datestamp, value FROM stuffToPlot')
    data = c.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values,'-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    for row in data:
        print row
#    print len(c.fetchall())
    c.execute('UPDATE stuffToPlot SET value = 11 WHERE value = 1')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print 'After UPDATE'
    for row in data:
        print row
#    print len(c.fetchall())

    c.execute('DELETE FROM stuffToPlot WHERE value = 11')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print 'After DELETE'
    for row in data:
        print row
#    print len(c.fetchall())

# create_table()
# data_entry()
#
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

# read_from_db()

# graph_data()

del_and_update()

c.close
conn.close()
