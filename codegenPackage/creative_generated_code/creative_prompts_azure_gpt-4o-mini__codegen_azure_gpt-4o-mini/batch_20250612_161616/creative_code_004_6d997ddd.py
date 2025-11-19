"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: How can I create a nutritional education program for schools that incorporates the guidelines provided by It's Cool Foods for promoting healthy eating among children?
Generated: DETERMINISTIC_6d997ddd58d34489
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a sample Python program that could serve as a basic framework for a nutritional education program for schools. This simple command-line application allows administrators to manage sessions and educational materials based on the guidelines provided by It's Cool Foods. 

```python
import json
import os

class NutritionalEducationProgram:
    """A class to manage a nutritional education program for schools."""
    
    def __init__(self, data_file='program_data.json'):
        """Initialize the program with a data file."""
        self.data_file = data_file
        self.sessions = self.load_data()
    
    def load_data(self):
        """Load program data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {"sessions": []}
    
    def save_data(self):
        """Save program data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.sessions, file, indent=4)
    
    def add_session(self, title, description, guidelines):
        """Add a new educational session."""
        session = {
            "title": title,
            "description": description,
            "guidelines": guidelines
        }
        self.sessions["sessions"].append(session)
        self.save_data()
        print(f'Session "{title}" added successfully.')
    
    def list_sessions(self):
        """List all educational sessions."""
        if not self.sessions["sessions"]:
            print("No sessions available.")
            return
        for idx, session in enumerate(self.sessions["sessions"], start=1):
            print(f"{idx}. {session['title']}: {session['description']} (Guidelines: {session['guidelines']})")
    
    def find_session(self, title):
        """Find and return a session by title."""
        for session in self.sessions["sessions"]:
            if session['title'].lower() == title.lower():
                return session
        return None

    def delete_session(self, title):
        """Delete a session by title."""
        session = self.find_session(title)
        if session:
            self.sessions["sessions"].remove(session)
            self.save_data()
            print(f'Session "{title}" deleted successfully.')
        else:
            print(f'Session "{title}" not found.')

def main():
    """Main entry point for the nutritional education program."""
    program = NutritionalEducationProgram()
    
    while True:
        print("\nNutritional Education Program")
        print("1. Add Session")
        print("2. List Sessions")
        print("3. Delete Session")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        try:
            if choice == '1':
                title = input("Enter session title: ")
                description = input("Enter session description: ")
                guidelines = input("Enter guidelines: ")
                program.add_session(title, description, guidelines)
            elif choice == '2':
                program.list_sessions()
            elif choice == '3':
                title = input("Enter session title to delete: ")
                program.delete_session(title)
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This program allows users to manage a nutritional education program by adding, listing, and deleting educational sessions while handling any errors that may arise during execution.
