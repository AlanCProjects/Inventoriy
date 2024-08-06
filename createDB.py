import sqlite3

conn = sqlite3.connect('./static/db/officeinsight.db')

c = conn.cursor()

c.execute("""CREATE TABLE users(
                name TEXT,
                lastname TEXT,
                user TEXT PRIMARY KEY,
                passwd TEXT
);""")

c.execute("""CREATE TABLE agents(
                
                name TEXT,
                lastname TEXT,
                team TEXT,
                charge TEXT,
                wuser TEXT PRIMARY KEY,
                mail TEXT,
                phone TEXT
            ); """)

c.execute("""CREATE TABLE laptops(
            brand TEXT,
            sn TEXT PRIMARY KEY,
            name TEXT NOT NULL
            );""")

c.execute("""CREATE TABLE have(
                status TEXT,
                wuser TEXT,
                sn TEXT,
                FOREIGN KEY (wuser) REFERENCES agents(wuser)
                FOREIGN KEY (sn) REFERENCES laptop(sn)
            );""")

'''c.execute("""CREATE TABLE monitors(
            brand TEXT,
            size INTEGER,
            sn TEXT PRIMARY KEY
            );""")
'''



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

conn.commit()

conn.close()

