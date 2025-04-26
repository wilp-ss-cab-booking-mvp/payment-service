import time
import psycopg2

while True:
    try:
        conn = psycopg2.connect(
            host="payment_db",
            port=5432,
            user="postgres",
            password="postgres",
            dbname="paymentdb1"
        )
        print("PostgreSQL is ready!")
        conn.close()
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL to start...")
        time.sleep(2)
