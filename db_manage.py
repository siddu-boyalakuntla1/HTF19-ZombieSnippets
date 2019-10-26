import sqlite3
def get_event_data():
    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute('SELECT * from event')
    return (c.fetchall())

def get_by_id(id):
    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute('SELECT event_name,event_start,event_end from event where evnt_id=?',(id,))
    return (c.fetchall())

print(get_by_id(1))
    
