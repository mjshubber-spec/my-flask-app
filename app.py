from flask import Flask
import psycopg2

app = Flask(__name__)

# Your DB connection string (hardcoded for now)
DB_URL = "postgresql://mj_db_user:JRN1n8r59pv81A61MKWQtSDgdp2BNwYM@dpg-d2fjk2be5dus73ard6sg-a/mj_db"

def init_db():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    return "Hello from MJ + Postgres"

@app.route("/add/<name>")
def add_name(name):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("INSERT INTO test_table (name) VALUES (%s);", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return f"Added {name}!"

@app.route("/list")
def list_names():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM test_table;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"rows": rows}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=10000)
