import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

try:
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD'), 
        database=os.getenv('DB_NAME', 'chuka_electronics')
    )
    cursor = connection.cursor()
    print("1. Connection successful!")

    # --- PART A: FETCH CUSTOMERS ---
    cursor.execute("SELECT customer_name, phone_number FROM Customers")
    records = cursor.fetchall()
    for row in records:
        print(f"Customer: {row[0]} | Phone: {row[1]}")

    # --- PART B: THE CALCULATION (Keep it inside the try block!) ---
    cursor.execute("""
        SELECT SUM(p.unit_price) 
        FROM Sales s 
        JOIN Products p ON s.product_id = p.product_id
    """)
    total_revenue = cursor.fetchone()[0]
    
    # Check if revenue is None (if no sales exist yet)
    revenue_display = total_revenue if total_revenue is not None else 0
    print(f"\n--- BUSINESS REPORT ---")
    print(f"Total Money Made: {revenue_display} KES")

except Exception as e:
    print(f"❌ Error occurred: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("4. Connection closed safely.")
        
