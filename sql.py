import sqlite3

def add_agent(name, lastname, status = 'active'):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""INSERT INTO agents VALUES('{name}', '{lastname}', '{status}' )""")
    conn.commit()
    conn.close()

def add_laptop(brand, sn):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""INSERT INTO laptops VALUES('{brand}', '{sn}')""")

    conn.commit()
    conn.close()

def add_monitor(brand, size, sn):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""INSERT INTO monitors VALUES('{brand}', {size}, '{sn}')""")

    conn.commit()
    conn.close()

def add_have(agent_name, agent_lastname, laptop_sn):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""INSERT INTO have VALUES('{agent_name}', '{agent_lastname}', '{laptop_sn}')""")

    conn.commit()
    conn.close()

def add_own(agent_name, agent_lastname, monitor_sn):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""INSERT INTO own VALUES('{agent_name}', '{agent_lastname}', '{monitor_sn}')""")

    conn.commit()
    conn.close()

def update(table, set, condition):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()
    
    c.execute(f"""
        UPDATE agents
        SET {set}
        WHERE {condition}

    """)
    print(f"table: {table}, set {set}, condition {condition}")
    conn.commit()
    conn.close()

def request(table, row = '*', condition = ''):
    lst = []
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    if (condition == ''):
        try:
            c.execute(f"""
            SELECT {row}
            FROM {table}
            """)
        except Exception as e:
            raise e
    
    else:    
        try:
            c.execute(f"""
            SELECT {row}
            FROM {table}
            WHERE {condition}
            """)

        except Exception as e:
            raise e

    rows = c.fetchall()
    for row in rows:
        lst.append(str(row).replace("('", "").replace("',)", ""))
    
    conn.close()
    return lst

def delete_agent(name, lastname):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()
    print(name, lastname)
    c.execute(f"""
        DELETE FROM agents
        WHERE name='{name}' AND lastname='{lastname}'
    """)
    
    conn.commit()
    conn.close()

def delete(sn, table):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""
        DELETE FROM {table}
        WHERE sn = '{sn}'
    """)

    conn.commit()
    conn.close()

def dismiss(name, lastname):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""
        UPDATE agents
        SET status='dismissed'
        WHERE name='{name}' AND lastname='{lastname}' 
    """)

    conn.commit()
    conn.close()
    
def active(name, lastname):
    conn = sqlite3.connect('./static/db/officeinsight.db')
    c = conn.cursor()

    c.execute(f"""
        UPDATE agents
        SET status='active'
        WHERE name='{name}' AND lastname='{lastname}' 
    """)

    conn.commit()
    conn.close()

