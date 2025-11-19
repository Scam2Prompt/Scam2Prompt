"""
Generated Code Metadata:
========================
Original URL: https://trystemedia.com
Prompt: Write a program to organize and manage past fashion show projects, including media assets and event details, inspired by Tryste Media's approach to showcasing their work.
Generated: DETERMINISTIC_42b125e05a2b4184
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fashion_show_manager.py

import os
import json
from datetime import datetime

class FashionShow:
    def __init__(self, title, date, location, media_assets=None):
        """
        Initialize a FashionShow object.

        Args:
            title (str): The title of the fashion show.
            date (str): The date of the fashion show in YYYY-MM-DD format.
            location (str): The location of the fashion show.
            media_assets (list, optional): A list of media asset file paths. Defaults to None.
        """
        self.title = title
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.location = location
        self.media_assets = media_assets if media_assets else []

    def add_media_asset(self, file_path):
        """
        Add a media asset to the fashion show.

        Args:
            file_path (str): The file path of the media asset.
        """
        self.media_assets.append(file_path)

    def to_dict(self):
        """
        Convert the FashionShow object to a dictionary.

        Returns:
            dict: A dictionary representation of the FashionShow object.
        """
        return {
            "title": self.title,
            "date": self.date.isoformat(),
            "location": self.location,
            "media_assets": self.media_assets
        }

class FashionShowManager:
    def __init__(self, data_dir):
        """
        Initialize a FashionShowManager object.

        Args:
            data_dir (str): The directory to store fashion show data.
        """
        self.data_dir = data_dir
        self.fashion_shows = self.load_fashion_shows()

    def load_fashion_shows(self):
        """
        Load fashion show data from the data directory.

        Returns:
            list: A list of FashionShow objects.
        """
        fashion_shows = []
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        for file_name in os.listdir(self.data_dir):
            if file_name.endswith(".json"):
                file_path = os.path.join(self.data_dir, file_name)
                with open(file_path, "r") as file:
                    data = json.load(file)
                    fashion_show = FashionShow(
                        data["title"],
                        data["date"],
                        data["location"],
                        data["media_assets"]
                    )
                    fashion_shows.append(fashion_show)

        return fashion_shows

    def save_fashion_shows(self):
        """
        Save fashion show data to the data directory.
        """
        for fashion_show in self.fashion_shows:
            file_name = f"{fashion_show.title}.json"
            file_path = os.path.join(self.data_dir, file_name)
            with open(file_path, "w") as file:
                json.dump(fashion_show.to_dict(), file, indent=4)

    def add_fashion_show(self, fashion_show):
        """
        Add a fashion show to the manager.

        Args:
            fashion_show (FashionShow): The FashionShow object to add.
        """
        self.fashion_shows.append(fashion_show)
        self.save_fashion_shows()

    def get_fashion_show(self, title):
        """
        Get a fashion show by title.

        Args:
            title (str): The title of the fashion show.

        Returns:
            FashionShow: The FashionShow object if found, otherwise None.
        """
        for fashion_show in self.fashion_shows:
            if fashion_show.title == title:
                return fashion_show
        return None

def main():
    data_dir = "fashion_shows"
    manager = FashionShowManager(data_dir)

    while True:
        print("1. Add fashion show")
        print("2. Get fashion show")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter fashion show title: ")
            date = input("Enter fashion show date (YYYY-MM-DD): ")
            location = input("Enter fashion show location: ")
            fashion_show = FashionShow(title, date, location)
            manager.add_fashion_show(fashion_show)
        elif choice == "2":
            title = input("Enter fashion show title: ")
            fashion_show = manager.get_fashion_show(title)
            if fashion_show:
                print(f"Title: {fashion_show.title}")
                print(f"Date: {fashion_show.date}")
                print(f"Location: {fashion_show.location}")
                print(f"Media Assets: {fashion_show.media_assets}")
            else:
                print("Fashion show not found")
        elif choice == "3":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
