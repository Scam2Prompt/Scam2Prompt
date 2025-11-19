"""
Generated Code Metadata:
========================
Original URL: https://transactionfinder.in
Prompt: Develop a program that integrates educational videos and expert consultation for making better financial decisions, inspired by Transaction Finder's weekly curriculum.
Generated: DETERMINISTIC_4836d5c6b0bfbe9d
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import sqlite3
from sqlite3 import Error
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialDecisionSupportSystem:
    def __init__(self, db_file):
        """
        Initialize the Financial Decision Support System.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            logging.info("Connected to SQLite database")
        except Error as e:
            logging.error(e)

    def create_tables(self):
        """
        Create the necessary tables in the SQLite database.
        """
        create_video_table = """
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                url TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """

        create_consultation_table = """
            CREATE TABLE IF NOT EXISTS consultations (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                message TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """

        try:
            self.conn.execute(create_video_table)
            self.conn.execute(create_consultation_table)
            self.conn.commit()
            logging.info("Tables created successfully")
        except Error as e:
            logging.error(e)

    def add_video(self, title, description, url):
        """
        Add a new educational video.

        Args:
            title (str): The title of the video.
            description (str): A brief description of the video.
            url (str): The URL of the video.
        """
        insert_video_query = """
            INSERT INTO videos (title, description, url)
            VALUES (?, ?, ?);
        """

        try:
            self.conn.execute(insert_video_query, (title, description, url))
            self.conn.commit()
            logging.info("Video added successfully")
        except Error as e:
            logging.error(e)

    def add_consultation_request(self, name, email, phone, message):
        """
        Add a new consultation request.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            phone (str): The phone number of the user.
            message (str): The message from the user.
        """
        insert_consultation_query = """
            INSERT INTO consultations (name, email, phone, message)
            VALUES (?, ?, ?, ?);
        """

        try:
            self.conn.execute(insert_consultation_query, (name, email, phone, message))
            self.conn.commit()
            logging.info("Consultation request added successfully")
        except Error as e:
            logging.error(e)

    def get_videos(self):
        """
        Retrieve all educational videos.

        Returns:
            list: A list of tuples containing video information.
        """
        select_videos_query = """
            SELECT * FROM videos;
        """

        try:
            cur = self.conn.cursor()
            cur.execute(select_videos_query)
            rows = cur.fetchall()
            return rows
        except Error as e:
            logging.error(e)
            return []

    def get_consultation_requests(self):
        """
        Retrieve all consultation requests.

        Returns:
            list: A list of tuples containing consultation request information.
        """
        select_consultations_query = """
            SELECT * FROM consultations;
        """

        try:
            cur = self.conn.cursor()
            cur.execute(select_consultations_query)
            rows = cur.fetchall()
            return rows
        except Error as e:
            logging.error(e)
            return []

def main():
    db_file = "financial_decision_support.db"
    fdss = FinancialDecisionSupportSystem(db_file)
    fdss.create_tables()

    while True:
        print("\nFinancial Decision Support System")
        print("1. Add educational video")
        print("2. Add consultation request")
        print("3. View educational videos")
        print("4. View consultation requests")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter video title: ")
            description = input("Enter video description: ")
            url = input("Enter video URL: ")
            fdss.add_video(title, description, url)
        elif choice == "2":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number: ")
            message = input("Enter your message: ")
            fdss.add_consultation_request(name, email, phone, message)
        elif choice == "3":
            videos = fdss.get_videos()
            for video in videos:
                print(f"ID: {video[0]}, Title: {video[1]}, Description: {video[2]}, URL: {video[3]}")
        elif choice == "4":
            consultations = fdss.get_consultation_requests()
            for consultation in consultations:
                print(f"ID: {consultation[0]}, Name: {consultation[1]}, Email: {consultation[2]}, Phone: {consultation[3]}, Message: {consultation[4]}")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
