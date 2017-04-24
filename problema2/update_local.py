import psycopg2, sqlite3, sys

try:
    print("Attempting to connect to pheno_db...")
    pg_conn = psycopg2.connect(
            database="dfu5v18hea0jro",
            user="puxsikmrnjnnml",
            password="fpqWwIT73lFClOn23I1MMYpjP3",
            host="ec2-107-22-175-206.compute-1.amazonaws.com",
            port="5432")
    print("Sucessfully connected to pheno_db!")
except:
    sys.exit("Unable to connect to pheno_db.")

try:
    print("Attempting to connect to local database...")
    sqlite_conn = sqlite3.connect('local_phenodb.db')
    print("Sucessfully connected to local database!")
except:
    sys.exit("Unable to connect to local database.\n")

pg_cursor = pg_conn.cursor()
sqlite_cursor = sqlite_conn.cursor()


print("Collecting data from pheno_db..")
pg_cursor.execute("SELECT * FROM pheno_db")
rows = pg_cursor.fetchall()
print("Data collected!")

print("Cleaning local database...")
sqlite_cursor.execute("DELETE FROM pheno_db")
sqlite_conn.commit()
print("Local data deleted!")

print("Updating local database..")
for row in rows:
    sqlite_cursor.execute("INSERT INTO pheno_db (id, gene, disease) VALUES (:id, :gene, :disease)", {"id": row[0], "gene": row[1], "disease": row[2]})
    sqlite_conn.commit()
print("Local database updated!")

pg_conn.close()
sqlite_conn.close()

