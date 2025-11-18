"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomwallt.teachable.com
Prompt: Create a tool to manage and customize channel lists for Smart IPTV users, incorporating features like playlist import and EPG integration, as described on Phantom wallt's School website.
Generated: DETERMINISTIC_2b6ace30da6a2c14
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

class SmartIPTVManager:
    """
    A tool to manage and customize channel lists for Smart IPTV users.
    Features:
    - Playlist import (CSV or JSON format)
    - EPG (Electronic Program Guide) integration (XML format)
    """

    def __init__(self):
        self.channels = []  # List of channels
        self.epg_data = {}  # Dictionary for EPG data

    def import_playlist(self, file_path: str, file_format: str) -> None:
        """
        Import a playlist from a file.

        :param file_path: Path to the playlist file.
        :param file_format: Format of the playlist file ('csv' or 'json').
        :raises ValueError: If the file format is unsupported.
        """
        try:
            if file_format.lower() == 'csv':
                self._import_csv(file_path)
            elif file_format.lower() == 'json':
                self._import_json(file_path)
            else:
                raise ValueError("Unsupported file format. Use 'csv' or 'json'.")
        except Exception as e:
            print(f"Error importing playlist: {e}")

    def _import_csv(self, file_path: str) -> None:
        """
        Import playlist from a CSV file.
        :param file_path: Path to the CSV file.
        """
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.channels.extend(reader)
                print(f"Successfully imported {len(self.channels)} channels from CSV.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def _import_json(self, file_path: str) -> None:
        """
        Import playlist from a JSON file.
        :param file_path: Path to the JSON file.
        """
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                self.channels.extend(data.get("channels", []))
                print(f"Successfully imported {len(self.channels)} channels from JSON.")
        except Exception as e:
            print(f"Error reading JSON file: {e}")

    def import_epg(self, file_path: str) -> None:
        """
        Import EPG data from an XML file.

        :param file_path: Path to the XML file containing EPG data.
        """
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            for programme in root.findall('programme'):
                channel = programme.get('channel')
                start = programme.get('start')
                stop = programme.get('stop')
                title = programme.find('title').text if programme.find('title') is not None else "Unknown Title"
                self.epg_data[channel] = {
                    "start": start,
                    "stop": stop,
                    "title": title
                }
            print(f"EPG data successfully imported for {len(self.epg_data)} channels.")
        except Exception as e:
            print(f"Error reading EPG XML file: {e}")

    def list_channels(self) -> List[Dict]:
        """
        List all available channels.

        :return: List of dictionaries containing channel information.
        """
        return self.channels

    def search_channel(self, keyword: str) -> List[Dict]:
        """
        Search for channels by keyword.

        :param keyword: Keyword to search in channel names.
        :return: List of matching channels.
        """
        return [channel for channel in self.channels if keyword.lower() in channel.get("name", "").lower()]

    def get_epg(self, channel_name: str) -> Optional[Dict]:
        """
        Get EPG data for a specific channel.

        :param channel_name: Name of the channel.
        :return: Dictionary containing EPG data, or None if not found.
        """
        return self.epg_data.get(channel_name)

# Example usage:
if __name__ == "__main__":
    manager = SmartIPTVManager()

    # Import playlists
    manager.import_playlist("channels.csv", "csv")
    manager.import_playlist("channels.json", "json")

    # Import EPG data
    manager.import_epg("epg.xml")

    # List all channels
    print("Available Channels:")
    for channel in manager.list_channels():
        print(channel)

    # Search for a channel
    print("\nSearch Results:")
    search_results = manager.search_channel("sports")
    for channel in search_results:
        print(channel)

    # Get EPG for a specific channel
    print("\nEPG Data:")
    epg_data = manager.get_epg("Sports Channel")
    if epg_data:
        print(epg_data)
    else:
        print("No EPG data found for this channel.")
```
