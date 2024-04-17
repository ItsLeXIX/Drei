import csv
import sqlite3

def import_data(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY,
                        customer_id TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        company TEXT,
                        city TEXT,
                        country TEXT,
                        phone1 TEXT,
                        phone2 TEXT,
                        email TEXT,
                        subscription_date TEXT,
                        website TEXT,
                        sales_2021 INTEGER,
                        sales_2022 INTEGER
                    )''')
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            cursor.execute('''INSERT INTO customers (
                                customer_id, first_name, last_name, company, city, country,
                                phone1, phone2, email, subscription_date, website,
                                sales_2021, sales_2022
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (
                                row['Customer Id'], row['First Name'], row['Last Name'],
                                row['Company'], row['City'], row['Country'],
                                row['Phone 1'], row['Phone 2'], row['Email'],
                                row['Subscription Date'], row['Website'],
                                int(row['SALES 2021']), int(row['SALES 2022'])
                            ))
    
    conn.commit()
    conn.close()

import_data('customers_sales_2021_2022.csv', 'customer_data.db')
