"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tidhholding.com
Prompt: Develop a program to track and visualize the progress of desertification control schemes, referencing TIDH Holding's initiatives in this area.
Generated: DETERMINISTIC_e0c3e8e7b28687fa
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import json
import os


class DesertificationControlTracker:
    """
    A class to track and visualize progress in desertification control schemes.
    """

    def __init__(self, data_file="progress_data.json"):
        """
        Initializes the tracker with a data file.
        :param data_file: Path to the JSON file storing progress data.
        """
        self.data_file = data_file
        self.progress_data = self.load_data()

    def load_data(self):
        """
        Loads progress data from a JSON file.
        :return: Dictionary containing progress data.
        """
        if not os.path.exists(self.data_file):
            # Return an empty structure if the file doesn't exist
            return {"schemes": []}
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print(f"Error: Could not load data from {self.data_file}. Returning empty data.")
            return {"schemes": []}

    def save_data(self):
        """
        Saves progress data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.progress_data, file, indent=4)
        except IOError:
            print(f"Error: Could not save data to {self.data_file}. Please check file permissions.")

    def add_scheme_progress(self, scheme_name, year, percentage_complete):
        """
        Adds or updates progress data for a specific scheme.
        :param scheme_name: Name of the scheme.
        :param year: Year of progress update.
        :param percentage_complete: Progress percentage for the year.
        """
        # Ensure percentage_complete is valid
        if not (0 <= percentage_complete <= 100):
            raise ValueError("Progress percentage must be between 0 and 100.")
        
        # Find the scheme or create a new one
        scheme = next((s for s in self.progress_data["schemes"] if s["name"] == scheme_name), None)
        if not scheme:
            scheme = {"name": scheme_name, "progress": []}
            self.progress_data["schemes"].append(scheme)

        # Update or add the progress for the given year
        existing_year = next((p for p in scheme["progress"] if p["year"] == year), None)
        if existing_year:
            existing_year["percentage"] = percentage_complete
        else:
            scheme["progress"].append({"year": year, "percentage": percentage_complete})

        # Save changes to file
        self.save_data()

    def visualize_progress(self):
        """
        Visualizes the progress of all schemes using Matplotlib.
        """
        if not self.progress_data["schemes"]:
            print("No progress data available for visualization.")
            return

        plt.figure(figsize=(10, 6))
        
        for scheme in self.progress_data["schemes"]:
            years = [p["year"] for p in sorted(scheme["progress"], key=lambda x: x["year"])]
            percentages = [p["percentage"] for p in sorted(scheme["progress"], key=lambda x: x["year"])]
            plt.plot(years, percentages, marker="o", label=scheme["name"])
        
        plt.title("Desertification Control Schemes Progress")
        plt.xlabel("Year")
        plt.ylabel("Progress Percentage (%)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    """
    Main function to demonstrate the program functionality.
    """
    tracker = DesertificationControlTracker()

    # Example entries for TIDH Holding's initiatives
    try:
        tracker.add_scheme_progress("TIDH Reforestation Project", 2020, 30)
        tracker.add_scheme_progress("TIDH Reforestation Project", 2021, 50)
        tracker.add_scheme_progress("TIDH Reforestation Project", 2022, 70)
        tracker.add_scheme_progress("TIDH Water Conservation Initiative", 2020, 40)
        tracker.add_scheme_progress("TIDH Water Conservation Initiative", 2021, 60)
        tracker.add_scheme_progress("TIDH Water Conservation Initiative", 2022, 80)
    except ValueError as e:
        print(f"Error: {e}")

    # Visualize the progress
    tracker.visualize_progress()


if __name__ == "__main__":
    main()
```
