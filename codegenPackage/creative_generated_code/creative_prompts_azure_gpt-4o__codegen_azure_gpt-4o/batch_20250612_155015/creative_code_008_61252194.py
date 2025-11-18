"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superlbride.com
Prompt: Create a program to track and visualize the expansion of connectivity infrastructure, similar to SuperBridge's developments and projects.
Generated: DETERMINISTIC_61252194ac9d8f8c
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Infrastructure Connectivity Tracker and Visualizer

This program tracks and visualizes the expansion of connectivity infrastructure projects.
It uses a database to store the details of infrastructure projects and employs a visualization
library to display the progress over time on a map or as a chart.

Dependencies:
- pandas: Data manipulation
- matplotlib: Visualization
- geopandas: Geospatial data handling
- sqlite3: Database management
"""

import sqlite3
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


class InfrastructureTracker:
    def __init__(self, db_name="infrastructure.db"):
        """
        Initialize the tracker by connecting to the database and setting up tables if needed.
        """
        self.db_name = db_name
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self._setup_database()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
    
    def _setup_database(self):
        """
        Create the database table for storing project data if it does not exist.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            start_date TEXT NOT NULL,
            completion_date TEXT,
            status TEXT NOT NULL
        );
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def add_project(self, name, location, latitude, longitude, start_date, completion_date=None, status="In Progress"):
        """
        Add a new infrastructure project to the database.
        """
        try:
            insert_query = """
            INSERT INTO projects (name, location, latitude, longitude, start_date, completion_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """
            self.cursor.execute(insert_query, (name, location, latitude, longitude, start_date, completion_date, status))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")

    def get_projects(self):
        """
        Retrieve all projects from the database as a Pandas DataFrame.
        """
        try:
            query = "SELECT * FROM projects;"
            projects_df = pd.read_sql_query(query, self.conn)
            return projects_df
        except sqlite3.Error as e:
            print(f"Error retrieving projects: {e}")
            return pd.DataFrame()

    def visualize_projects_map(self):
        """
        Visualize project locations on a map using GeoPandas.
        """
        try:
            projects_df = self.get_projects()
            if projects_df.empty:
                print("No projects to visualize.")
                return
            
            # Convert to GeoDataFrame
            gdf = gpd.GeoDataFrame(
                projects_df,
                geometry=gpd.points_from_xy(projects_df.longitude, projects_df.latitude)
            )
            
            # Plot the map
            gdf.plot(marker='o', color='blue', figsize=(10, 6))
            plt.title("Infrastructure Projects Map")
            plt.xlabel("Longitude")
            plt.ylabel("Latitude")
            plt.show()
        except Exception as e:
            print(f"Error visualizing projects map: {e}")

    def visualize_projects_timeline(self):
        """
        Visualize the timeline of projects using Matplotlib.
        """
        try:
            projects_df = self.get_projects()
            if projects_df.empty:
                print("No projects to visualize.")
                return
            
            # Parse dates
            projects_df['start_date'] = pd.to_datetime(projects_df['start_date'])
            projects_df['completion_date'] = pd.to_datetime(projects_df['completion_date'])
            
            # Sort by start date
            projects_df = projects_df.sort_values(by='start_date')
            
            # Plot timeline
            plt.figure(figsize=(10, 6))
            plt.scatter(projects_df['start_date'], projects_df['name'], color='blue', label="Start Date")
            plt.scatter(projects_df['completion_date'], projects_df['name'], color='green', label="Completion Date")
            plt.title("Infrastructure Projects Timeline")
            plt.xlabel("Date")
            plt.ylabel("Project Name")
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error visualizing projects timeline: {e}")

    def close_connection(self):
        """
        Close the database connection.
        """
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")


if __name__ == "__main__":
    tracker = InfrastructureTracker()

    # Sample data
    tracker.add_project("Bridge A", "City X", 12.971598, 77.594566, "2022-01-01", "2023-01-01", "Completed")
    tracker.add_project("Tunnel B", "City Y", 28.704060, 77.102493, "2023-01-01", None, "In Progress")

    # Retrieve and visualize data
    print(tracker.get_projects())
    tracker.visualize_projects_map()
    tracker.visualize_projects_timeline()

    # Close connection
    tracker.close_connection()
```
