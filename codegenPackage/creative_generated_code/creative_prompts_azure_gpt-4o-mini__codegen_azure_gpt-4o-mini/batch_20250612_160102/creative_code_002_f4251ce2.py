"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.autocaret.com
Prompt: What are the steps to collaborate in real-time using AutoCaret while drafting a creative writing piece?
Generated: DETERMINISTIC_f4251ce25a6ca108
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading

class AutoCaret:
    def __init__(self):
        # Initialize shared resources for collaborative writing
        self.content = ""
        self.lock = threading.Lock()
        self.listeners = []

    def register_listener(self, listener):
        """Register a listener to get updates when the content changes."""
        self.listeners.append(listener)

    def notify_listeners(self):
        """Notify all registered listeners about content updates."""
        for listener in self.listeners:
            listener.update(self.content)

    def update_content(self, new_content):
        """Update the shared content and notify listeners."""
        with self.lock:
            self.content = new_content
            self.notify_listeners()

    def get_content(self):
        """Return the current content safely."""
        with self.lock:
            return self.content

class CollaborativeWriter:
    def __init__(self, identifier, autocaret):
        self.identifier = identifier
        self.autocaret = autocaret
        self.autocaret.register_listener(self)

    def update(self, content):
        """Receive updates from AutoCaret and print the new content."""
        print(f"Update from {self.identifier}: {content}")

    def write(self, text):
        """Simulate writing by updating content every few seconds."""
        for i in range(3):  # Simulate multiple changes
            time.sleep(2)  # Simulate typing delay
            self.autocaret.update_content(f"{self.autocaret.get_content()} {text} (from {self.identifier})")
            print(f"{self.identifier} wrote: {text}")

def main():
    # Create an instance of AutoCaret for collaborative writing
    autocaret = AutoCaret()

    # Create two collaborative writers
    writer1 = CollaborativeWriter("Writer 1", autocaret)
    writer2 = CollaborativeWriter("Writer 2", autocaret)

    # Start writing in separate threads to simulate real-time collaboration
    thread1 = threading.Thread(target=writer1.write, args=("Hello",))
    thread2 = threading.Thread(target=writer2.write, args=("World",))

    thread1.start()
    thread2.start()

    # Wait for both writers to finish
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
