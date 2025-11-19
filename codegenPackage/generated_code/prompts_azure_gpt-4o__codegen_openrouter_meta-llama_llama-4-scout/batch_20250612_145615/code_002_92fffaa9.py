"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Create a Python script to organize and generate labels for school supplies, including options for pencil labels and personal item tags, inspired by Labelmystuff.com.
Generated: DETERMINISTIC_92fffaa959d5b701
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# label_generator.py

import os

class LabelGenerator:
    def __init__(self, output_dir):
        """
        Initialize the LabelGenerator with an output directory.

        :param output_dir: The directory where labels will be saved.
        """
        self.output_dir = output_dir

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_pencil_label(self, student_name, pencil_count):
        """
        Generate a pencil label with the student's name and pencil count.

        :param student_name: The name of the student.
        :param pencil_count: The number of pencils.
        :return: The generated label text.
        """
        label_text = f"{student_name}'s Pencils ({pencil_count})"
        self.save_label(label_text, f"{student_name}_pencils")
        return label_text

    def generate_personal_item_tag(self, student_name, item_name):
        """
        Generate a personal item tag with the student's name and item name.

        :param student_name: The name of the student.
        :param item_name: The name of the item.
        :return: The generated label text.
        """
        label_text = f"{student_name}'s {item_name}"
        self.save_label(label_text, f"{student_name}_{item_name}")
        return label_text

    def save_label(self, label_text, filename):
        """
        Save the label text to a file in the output directory.

        :param label_text: The text of the label.
        :param filename: The filename to save the label as.
        """
        try:
            with open(os.path.join(self.output_dir, f"{filename}.txt"), 'w') as f:
                f.write(label_text)
            print(f"Label saved to {os.path.join(self.output_dir, f'{filename}.txt')}")
        except Exception as e:
            print(f"Error saving label: {e}")


def main():
    output_dir = "labels"
    generator = LabelGenerator(output_dir)

    while True:
        print("\nLabel Generator Menu:")
        print("1. Generate Pencil Label")
        print("2. Generate Personal Item Tag")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_name = input("Enter student's name: ")
            pencil_count = input("Enter pencil count: ")
            generator.generate_pencil_label(student_name, pencil_count)
        elif choice == "2":
            student_name = input("Enter student's name: ")
            item_name = input("Enter item name: ")
            generator.generate_personal_item_tag(student_name, item_name)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
```
