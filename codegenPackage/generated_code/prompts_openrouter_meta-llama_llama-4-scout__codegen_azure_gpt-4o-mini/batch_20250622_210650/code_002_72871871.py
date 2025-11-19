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
class School:
    """
    A class to represent a school and its offered streams for classes XI and XII.
    """

    def __init__(self, name):
        """
        Initializes the School with a name and an empty list of streams.

        :param name: str - The name of the school
        """
        self.name = name
        self.streams = {
            "XI": [],
            "XII": []
        }

    def add_stream(self, class_level, stream_name):
        """
        Adds a stream to the specified class level.

        :param class_level: str - The class level ('XI' or 'XII')
        :param stream_name: str - The name of the stream to be added
        :raises ValueError: If the class level is not 'XI' or 'XII'
        """
        if class_level not in self.streams:
            raise ValueError("Invalid class level. Please use 'XI' or 'XII'.")
        
        self.streams[class_level].append(stream_name)

    def get_streams(self, class_level):
        """
        Retrieves the streams offered for the specified class level.

        :param class_level: str - The class level ('XI' or 'XII')
        :raises ValueError: If the class level is not 'XI' or 'XII'
        :return: list - A list of streams offered for the specified class level
        """
        if class_level not in self.streams:
            raise ValueError("Invalid class level. Please use 'XI' or 'XII'.")
        
        return self.streams[class_level]

# Example usage
if __name__ == "__main__":
    try:
        deepti_convent = School("Deepti Convent Higher Secondary School")
        
        # Adding streams for class XI
        deepti_convent.add_stream("XI", "Science")
        deepti_convent.add_stream("XI", "Commerce")
        
        # Adding streams for class XII
        deepti_convent.add_stream("XII", "Science")
        deepti_convent.add_stream("XII", "Arts")
        
        # Retrieving streams
        print("Streams offered for class XI:", deepti_convent.get_streams("XI"))
        print("Streams offered for class XII:", deepti_convent.get_streams("XII"))
    
    except ValueError as e:
        print(f"Error: {e}")
```
