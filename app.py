from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_customer_data():
    conn = sqlite3.connect('customer_data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    data = cursor.fetchall()
    # Convert data to list of dictionaries
    data = [dict(row) for row in data]

    conn.close()

    if data:
        first_row = data[0]
        print("first_row: ", first_row)

    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_customers', methods=['GET'])
def get_customers():
    try:
        customers = get_customer_data()
        return jsonify(customers)
    except Exception as e:
        app.logger.error(f"Error getting customers: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)