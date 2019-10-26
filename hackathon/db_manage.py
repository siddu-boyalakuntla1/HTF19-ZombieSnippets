import sqlite3
def get_event_data():
    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute('SELECT * from event')
    return (c.fetchall())


