"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cfdiplus.com
Prompt: Write a code snippet to create a sticky note feature that saves user input in local storage.
Generated: DETERMINISTIC_0da03d3bab9bf282
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sticky Note</title>
  <style>
    /* Basic styling for the sticky note */
    #sticky-note {
      width: 300px;
      height: 300px;
      padding: 20px;
      background-color: #fffc8c;
      border: 2px solid #ccc;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      resize: none;
      font-family: Arial, sans-serif;
      font-size: 16px;
    }
    #message {
      margin-top: 10px;
      color: green;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <textarea id="sticky-note" placeholder="Type your notes here..."></textarea>
  <div id="message"></div>

  <script>
    // Get references to the DOM elements
    const stickyNote = document.getElementById('sticky-note');
    const message = document.getElementById('message');

    // Load the saved note from local storage when the page loads
    window.onload = function () {
      try {
        const savedNote = localStorage.getItem('stickyNoteContent');
        if (savedNote) {
          stickyNote.value = savedNote;
          message.textContent = 'Note loaded from local storage.';
        }
      } catch (error) {
        console.error('Error loading note from local storage:', error);
        message.textContent = 'Failed to load note from local storage.';
      }
    };

    // Save note to local storage whenever the user types
    stickyNote.addEventListener('input', function () {
      try {
        localStorage.setItem('stickyNoteContent', stickyNote.value);
        message.textContent = 'Note saved successfully.';
      } catch (error) {
        console.error('Error saving note to local storage:', error);
        message.textContent = 'Failed to save note to local storage.';
      }
    });
  </script>
</body>
</html>
```
