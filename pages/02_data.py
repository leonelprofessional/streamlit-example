import streamlit as st
import psycopg2
import psycopg2.extras

DB_HOST = "ep-floral-snowflake-805891.us-west-2.retooldb.com"
DB_NAME = "retool"
DB_USER = "retool"
DB_PASS = "8ADj0SJrwGFe"



conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


    #cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    #cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

    #cur.execute("INSERT INTO student (name) VALUES(%s)", ("Cristina",))

    #cur.execute("SELECT * FROM student;")

    #print(cur.fetchall())
with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        #cur.execute("SELECT * FROM student WHERE id = %s;", (1,))

        cur.execute("SELECT * FROM users;")
        print(cur.fetchall())

        #print(cur.fetchone()['name'])

        #cur.execute("INSERT INTO student (name) VALUES(%s)", ("David",))

#conn.commit()

#cur.close()

conn.close()
