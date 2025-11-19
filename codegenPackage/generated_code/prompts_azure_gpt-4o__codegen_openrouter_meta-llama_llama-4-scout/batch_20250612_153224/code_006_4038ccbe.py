"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Create code for a seasonal cleaning checklist generator that includes tasks like opening windows, moving furniture, and deep cleaning steps. Allow customization based on user preferences.
Generated: DETERMINISTIC_4038ccbebc2149e9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# seasonal_cleaning_checklist_generator.py

class SeasonalCleaningChecklistGenerator:
    def __init__(self):
        self.tasks = {
            "spring": [
                "Open windows and doors for ventilation",
                "Dust and vacuum furniture and floors",
                "Deep clean refrigerator and oven",
                "Wash windows",
                "Organize closets and cluttered areas"
            ],
            "summer": [
                "Clean outdoor furniture and grill",
                "Vacuum and clean pool and surrounding areas",
                "Deep clean carpets and upholstered furniture",
                "Clean out and organize garage or storage areas",
                "Power wash deck or patio"
            ],
            "autumn": [
                "Rake leaves and clean up yard",
                "Clean and inspect gutters",
                "Deep clean fireplace and chimney",
                "Prepare and store summer furniture and equipment",
                "Organize and switch out seasonal clothing"
            ],
            "winter": [
                "Insulate pipes and prevent freezing",
                "Deep clean and inspect HVAC system",
                "Clean and store outdoor furniture and equipment",
                "Organize and switch out seasonal clothing",
                "Check and replace air filters"
            ]
        }
        self.custom_tasks = {}

    def get_seasonal_tasks(self, season):
        """Returns a list of tasks for the given season"""
        if season in self.tasks:
            return self.tasks[season]
        else:
            raise ValueError("Invalid season. Please choose from: {}".format(", ".join(self.tasks.keys())))

    def add_custom_task(self, season, task):
        """Adds a custom task for the given season"""
        if season in self.tasks:
            if season not in self.custom_tasks:
                self.custom_tasks[season] = []
            self.custom_tasks[season].append(task)
        else:
            raise ValueError("Invalid season. Please choose from: {}".format(", ".join(self.tasks.keys())))

    def generate_checklist(self, season):
        """Generates a checklist for the given season, including custom tasks"""
        try:
            seasonal_tasks = self.get_seasonal_tasks(season)
            if season in self.custom_tasks:
                seasonal_tasks += self.custom_tasks[season]
            return seasonal_tasks
        except ValueError as e:
            print("Error: {}".format(e))
            return []

    def print_checklist(self, season):
        """Prints a checklist for the given season"""
        checklist = self.generate_checklist(season)
        if checklist:
            print("Seasonal Cleaning Checklist for {}:".format(season))
            for i, task in enumerate(checklist, start=1):
                print("{}. {}".format(i, task))
        else:
            print("No tasks available for {}".format(season))


def main():
    generator = SeasonalCleaningChecklistGenerator()

    while True:
        print("\nSeasonal Cleaning Checklist Generator")
        print("1. Generate Checklist")
        print("2. Add Custom Task")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nChoose a season:")
            print("1. Spring")
            print("2. Summer")
            print("3. Autumn")
            print("4. Winter")

            season_choice = input("Enter the number of your choice: ")
            seasons = ["spring", "summer", "autumn", "winter"]

            if season_choice.isdigit() and 1 <= int(season_choice) <= 4:
                season = seasons[int(season_choice) - 1]
                generator.print_checklist(season)
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print("\nChoose a season:")
            print("1. Spring")
            print("2. Summer")
            print("3. Autumn")
            print("4. Winter")

            season_choice = input("Enter the number of your choice: ")
            seasons = ["spring", "summer", "autumn", "winter"]

            if season_choice.isdigit() and 1 <= int(season_choice) <= 4:
                season = seasons[int(season_choice) - 1]
                task = input("Enter a custom task: ")
                generator.add_custom_task(season, task)
                print("Custom task added successfully!")
            else:
                print("Invalid choice. Please try again.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
