import sqlite3

conn = sqlite3.connect('./static/db/inventory.db')

c = conn.cursor()

'''c.execute("""CREATE TABLE agents(
                
                name TEXT,
                lastname TEXT,
                PRIMARY KEY (name, lastname)
            ) """)

c.execute("""CREATE TABLE laptops(
            
            brand TEXT,
            sn TEXT PRIMARY KEY
            )""")

c.execute("""CREATE TABLE monitors(
            brand TEXT,
            size INTEGER,
            sn TEXT PRIMARY KEY
            )""")

c.execute("""CREATE TABLE have(
            
            agent_name TEXT,
            agent_lastname TEXT,
            laptop_sn TEXT PRIMARY KEY,
            FOREIGN KEY (agent_name) REFERENCES agents(name),
            FOREIGN KEY (agent_lastname) REFERENCES agents(lastname),
            FOREIGN KEY (laptop_sn) REFERENCES laptops(sn)
            ) """)

c.execute("""CREATE TABLE own(
            agent_name TEXT,
            agent_lastname TEXT,
            monitors_sn TEXT PRIMARY KEY,
            FOREIGN KEY (agent_name) REFERENCES agents(name),
            FOREIGN KEY (agent_lastname) REFERENCES agents(lastname),
            FOREIGN KEY (monitors_sn) REFERENCES monitors(sn)
            )""")'''


# c.execute("""

#     CREATE TABLE users(
#     user TEXT,
#     passwd TEXT PRIMARY KEY
#     )
#     """)

# c.execute("""
#         ALTER TABLE Agents
#         ADD status TEXT;
# """)

# c.execute("""
#         ALTER TABLE agents
#         DROP COLUMN state;
# """)


# c.execute("""
#     DROP TABLE own;
# """)
# c.execute("""
#     CREATE TABLE desks(
#         id TEXT NOT NULL PRIMARY KEY,
#         floor INTEGER
#     )
# """)

c.execute("""
    CREATE TABLE belong(
        desk_id TEXT NOT NULL,
        monitors_sn TEXT NOT NULL,
        PRIMARY KEY (desk_id), 
        FOREIGN KEY (desk_id) REFERENCES desks(id),
        FOREIGN KEY (monitors_sn) REFERENCES monitros(sn)
    )
""")
conn.commit()

conn.close()

