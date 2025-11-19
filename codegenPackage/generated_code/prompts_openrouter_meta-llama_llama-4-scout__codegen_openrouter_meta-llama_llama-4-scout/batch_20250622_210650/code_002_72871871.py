"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: What are the streams offered by Deepti Convent Higher Secondary School for classes XI and XII?
Generated: DETERMINISTIC_72871871f532720b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent a school
class School:
    def __init__(self, name):
        """
        Initialize a School object.

        Args:
            name (str): The name of the school.
        """
        self.name = name
        # Sample data for streams offered by Deepti Convent Higher Secondary School
        self.streams = {
            "Deepti Convent Higher Secondary School": {
                "XI": ["Science", "Commerce", "Arts"],
                "XII": ["Science", "Commerce", "Arts"]
            }
        }

    def get_streams(self, school_name, class_level):
        """
        Get the streams offered by a school for a specific class level.

        Args:
            school_name (str): The name of the school.
            class_level (str): The class level (XI or XII).

        Returns:
            list: A list of streams offered by the school for the specified class level.

        Raises:
            ValueError: If the school name or class level is not found.
        """
        try:
            if school_name in self.streams:
                if class_level in self.streams[school_name]:
                    return self.streams[school_name][class_level]
                else:
                    raise ValueError(f"Class level {class_level} not found for school {school_name}.")
            else:
                raise ValueError(f"School {school_name} not found.")
        except ValueError as e:
            print(f"Error: {e}")
            return None


def main():
    school_name = "Deepti Convent Higher Secondary School"
    school = School(school_name)

    # Get streams for class XI
    class_xi_streams = school.get_streams(school_name, "XI")
    if class_xi_streams:
        print(f"Streams offered by {school_name} for class XI:")
        for stream in class_xi_streams:
            print(stream)

    # Get streams for class XII
    class_xii_streams = school.get_streams(school_name, "XII")
    if class_xii_streams:
        print(f"\nStreams offered by {school_name} for class XII:")
        for stream in class_xii_streams:
            print(stream)


if __name__ == "__main__":
    main()
```
