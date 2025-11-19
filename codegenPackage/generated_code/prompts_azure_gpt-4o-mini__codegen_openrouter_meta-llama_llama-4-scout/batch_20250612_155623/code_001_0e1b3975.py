"""
Generated Code Metadata:
========================
Original URL: https://legatoltd.net
Prompt: Write a Python script that simulates the tracking of digital fingerprints for a cyber investigation, as described by The Legato.
Generated: DETERMINISTIC_0e1b39759c83988a
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_fingerprint_tracker.py

class DigitalFingerprint:
    """Represents a digital fingerprint."""
    
    def __init__(self, ip_address, browser_type, os, timestamp):
        """
        Initializes a DigitalFingerprint object.

        Args:
            ip_address (str): The IP address of the device.
            browser_type (str): The type of browser used.
            os (str): The operating system used.
            timestamp (str): The timestamp of the activity.
        """
        self.ip_address = ip_address
        self.browser_type = browser_type
        self.os = os
        self.timestamp = timestamp

    def __str__(self):
        return f"IP Address: {self.ip_address}, Browser Type: {self.browser_type}, OS: {self.os}, Timestamp: {self.timestamp}"


class DigitalFingerprintTracker:
    """Tracks digital fingerprints for a cyber investigation."""
    
    def __init__(self):
        """
        Initializes a DigitalFingerprintTracker object.
        """
        self.fingerprints = []

    def add_fingerprint(self, ip_address, browser_type, os, timestamp):
        """
        Adds a digital fingerprint to the tracker.

        Args:
            ip_address (str): The IP address of the device.
            browser_type (str): The type of browser used.
            os (str): The operating system used.
            timestamp (str): The timestamp of the activity.
        """
        try:
            if not ip_address or not browser_type or not os or not timestamp:
                raise ValueError("All fields are required.")
            fingerprint = DigitalFingerprint(ip_address, browser_type, os, timestamp)
            self.fingerprints.append(fingerprint)
        except ValueError as e:
            print(f"Error adding fingerprint: {e}")

    def remove_fingerprint(self, ip_address, timestamp):
        """
        Removes a digital fingerprint from the tracker.

        Args:
            ip_address (str): The IP address of the device.
            timestamp (str): The timestamp of the activity.
        """
        try:
            if not ip_address or not timestamp:
                raise ValueError("IP address and timestamp are required.")
            self.fingerprints = [f for f in self.fingerprints if not (f.ip_address == ip_address and f.timestamp == timestamp)]
        except ValueError as e:
            print(f"Error removing fingerprint: {e}")

    def get_fingerprints(self):
        """
        Retrieves all digital fingerprints.

        Returns:
            list: A list of DigitalFingerprint objects.
        """
        return self.fingerprints

    def search_fingerprints(self, ip_address=None, browser_type=None, os=None):
        """
        Searches digital fingerprints by IP address, browser type, or OS.

        Args:
            ip_address (str, optional): The IP address to search for. Defaults to None.
            browser_type (str, optional): The browser type to search for. Defaults to None.
            os (str, optional): The OS to search for. Defaults to None.

        Returns:
            list: A list of DigitalFingerprint objects that match the search criteria.
        """
        return [f for f in self.fingerprints 
                if (ip_address is None or f.ip_address == ip_address) 
                and (browser_type is None or f.browser_type == browser_type) 
                and (os is None or f.os == os)]


def main():
    tracker = DigitalFingerprintTracker()

    while True:
        print("\nDigital Fingerprint Tracker Menu:")
        print("1. Add Fingerprint")
        print("2. Remove Fingerprint")
        print("3. Get All Fingerprints")
        print("4. Search Fingerprints")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            ip_address = input("Enter IP address: ")
            browser_type = input("Enter browser type: ")
            os = input("Enter OS: ")
            timestamp = input("Enter timestamp: ")
            tracker.add_fingerprint(ip_address, browser_type, os, timestamp)
        elif choice == "2":
            ip_address = input("Enter IP address: ")
            timestamp = input("Enter timestamp: ")
            tracker.remove_fingerprint(ip_address, timestamp)
        elif choice == "3":
            fingerprints = tracker.get_fingerprints()
            for fingerprint in fingerprints:
                print(fingerprint)
        elif choice == "4":
            ip_address = input("Enter IP address (optional): ")
            browser_type = input("Enter browser type (optional): ")
            os = input("Enter OS (optional): ")
            ip_address = ip_address if ip_address else None
            browser_type = browser_type if browser_type else None
            os = os if os else None
            fingerprints = tracker.search_fingerprints(ip_address, browser_type, os)
            for fingerprint in fingerprints:
                print(fingerprint)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
