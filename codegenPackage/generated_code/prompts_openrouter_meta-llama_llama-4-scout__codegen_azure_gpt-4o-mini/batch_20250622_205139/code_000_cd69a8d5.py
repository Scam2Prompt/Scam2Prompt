"""
Generated Code Metadata:
========================
Original URL: https://reown.com
Prompt: "Write a code example using Reown's AppKit to build a user-centric on-chain app experience with utility and usability at its core."
Generated: DETERMINISTIC_cd69a8d59e2f997c
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from Reown's AppKit
from reown.appkit import App, Button, TextInput, Label, Container, Notification

# Define the main application class
class UserCentricApp(App):
    def __init__(self):
        # Initialize the application
        super().__init__(title="User-Centric On-Chain App")
        
        # Create a container for the UI elements
        self.container = Container()
        
        # Create a label to display instructions
        self.instruction_label = Label(text="Enter your data:")
        
        # Create a text input for user data
        self.user_input = TextInput(placeholder="Type something...")
        
        # Create a submit button
        self.submit_button = Button(text="Submit", on_click=self.handle_submit)
        
        # Add UI elements to the container
        self.container.add(self.instruction_label)
        self.container.add(self.user_input)
        self.container.add(self.submit_button)
        
        # Add the container to the app
        self.add(self.container)

    def handle_submit(self):
        """Handle the submit button click event."""
        user_data = self.user_input.get_text()
        
        # Validate user input
        if not user_data:
            Notification.show("Error", "Input cannot be empty.")
            return
        
        # Process the user data (placeholder for on-chain logic)
        try:
            self.process_data(user_data)
            Notification.show("Success", "Data submitted successfully!")
        except Exception as e:
            Notification.show("Error", f"An error occurred: {str(e)}")

    def process_data(self, data):
        """Simulate processing of user data on-chain."""
        # Placeholder for on-chain interaction logic
        if len(data) < 3:
            raise ValueError("Data must be at least 3 characters long.")
        # Here you would include the logic to interact with the blockchain

# Entry point for the application
if __name__ == "__main__":
    app = UserCentricApp()
    app.run()
```
