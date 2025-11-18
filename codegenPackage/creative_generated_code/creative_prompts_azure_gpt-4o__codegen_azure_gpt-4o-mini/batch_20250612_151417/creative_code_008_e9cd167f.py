"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Recommend libraries or frameworks to build a newsletter system that delivers updates on industry trends and tech news, as offered by SMART Training Resources.
Generated: DETERMINISTIC_e9cd167f0906f50d
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
from sqlite3 import Error

# Define a function to create a database connection
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection successful to database:", db_file)
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Define a function to create the subscribers table
def create_subscribers_table(conn):
    """ Create a subscribers table in the database """
    try:
        sql_create_subscribers_table = """ CREATE TABLE IF NOT EXISTS subscribers (
                                                id integer PRIMARY KEY,
                                                email text NOT NULL UNIQUE
                                            ); """
        cursor = conn.cursor()
        cursor.execute(sql_create_subscribers_table)
        print("Subscribers table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Define a function to add a subscriber
def add_subscriber(conn, email):
    """ Add a new subscriber to the database """
    try:
        sql = ''' INSERT INTO subscribers(email) VALUES(?) '''
        cursor = conn.cursor()
        cursor.execute(sql, (email,))
        conn.commit()
        print("Subscriber added successfully:", email)
    except Error as e:
        print(f"Error adding subscriber: {e}")

# Define a function to send newsletter
def send_newsletter(email_list, subject, body):
    """ Send newsletter to the list of subscribers """
    try:
        # Email configuration
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        
        # Create the email
        for recipient in email_list:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'html'))
            
            # Set up the server
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"Newsletter sent to: {recipient}")
    except Exception as e:
        print(f"Failed to send newsletter: {e}")

# Main function to manage the newsletter system
def main():
    # Define database file
    database = "newsletter.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create subscribers table
        create_subscribers_table(conn)
        
        # Add sample subscribers (could be replaced with user input)
        add_subscriber(conn, "example1@example.com")
        add_subscriber(conn, "example2@example.com")
        
        # Retrieve subscriber emails
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscribers")
        email_list = [row[0] for row in cursor.fetchall()]
        
        # Define newsletter content
        subject = "Weekly Industry Trends"
        body = "<h1>Latest Tech News</h1><p>Stay updated with the latest trends in the industry.</p>"
        
        # Send the newsletter
        send_newsletter(email_list, subject, body)
        
        # Close the database connection
        conn.close()

if __name__ == '__main__':
    main()
```
