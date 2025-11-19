"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Develop a size chart FAQ for christening gowns and outfits that caters to various age groups and sizes, including preemie christening wear.
Generated: DETERMINISTIC_88c265829d84d5a9
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# size_chart_faq.py

class SizeChartFAQ:
    def __init__(self):
        """
        Initialize the size chart FAQ with preemie and infant sizes.
        """
        self.size_chart = {
            "Preemie": {
                "Age": "0-3 months (premature)",
                "Weight": "2-4 lbs",
                "Chest": "8-10 inches",
                "Waist": "6-8 inches"
            },
            "Newborn": {
                "Age": "0-3 months",
                "Weight": "4-7 lbs",
                "Chest": "10-12 inches",
                "Waist": "8-10 inches"
            },
            "Infant": {
                "Age": "3-6 months",
                "Weight": "7-10 lbs",
                "Chest": "12-14 inches",
                "Waist": "10-12 inches"
            },
            "Baby": {
                "Age": "6-12 months",
                "Weight": "10-15 lbs",
                "Chest": "14-16 inches",
                "Waist": "12-14 inches"
            }
        }

    def get_size_chart(self, age_group=None):
        """
        Retrieve the size chart for a specific age group or all age groups.

        Args:
            age_group (str, optional): The age group to retrieve. Defaults to None.

        Returns:
            dict: The size chart for the specified age group or all age groups.
        """
        try:
            if age_group:
                return {age_group: self.size_chart[age_group]}
            else:
                return self.size_chart
        except KeyError:
            print(f"Invalid age group: {age_group}")
            return None

    def add_size(self, age_group, age, weight, chest, waist):
        """
        Add a new size to the size chart.

        Args:
            age_group (str): The age group to add the size to.
            age (str): The age range for the size.
            weight (str): The weight range for the size.
            chest (str): The chest measurement for the size.
            waist (str): The waist measurement for the size.
        """
        try:
            self.size_chart[age_group] = {
                "Age": age,
                "Weight": weight,
                "Chest": chest,
                "Waist": waist
            }
            print(f"Added new size to {age_group} age group.")
        except Exception as e:
            print(f"Error adding new size: {e}")

    def update_size(self, age_group, age=None, weight=None, chest=None, waist=None):
        """
        Update an existing size in the size chart.

        Args:
            age_group (str): The age group to update the size for.
            age (str, optional): The new age range. Defaults to None.
            weight (str, optional): The new weight range. Defaults to None.
            chest (str, optional): The new chest measurement. Defaults to None.
            waist (str, optional): The new waist measurement. Defaults to None.
        """
        try:
            if age:
                self.size_chart[age_group]["Age"] = age
            if weight:
                self.size_chart[age_group]["Weight"] = weight
            if chest:
                self.size_chart[age_group]["Chest"] = chest
            if waist:
                self.size_chart[age_group]["Waist"] = waist
            print(f"Updated size for {age_group} age group.")
        except Exception as e:
            print(f"Error updating size: {e}")

    def delete_size(self, age_group):
        """
        Delete a size from the size chart.

        Args:
            age_group (str): The age group to delete the size from.
        """
        try:
            del self.size_chart[age_group]
            print(f"Deleted size for {age_group} age group.")
        except KeyError:
            print(f"Age group not found: {age_group}")
        except Exception as e:
            print(f"Error deleting size: {e}")


def main():
    size_chart_faq = SizeChartFAQ()

    print("Size Chart FAQ:")
    print(size_chart_faq.get_size_chart())

    # Add a new size
    size_chart_faq.add_size("Toddler", "1-3 years", "20-30 lbs", "20-22 inches", "18-20 inches")

    # Update an existing size
    size_chart_faq.update_size("Infant", chest="14-16 inches")

    # Delete a size
    # size_chart_faq.delete_size("Newborn")

    print("\nUpdated Size Chart FAQ:")
    print(size_chart_faq.get_size_chart())


if __name__ == "__main__":
    main()
```
