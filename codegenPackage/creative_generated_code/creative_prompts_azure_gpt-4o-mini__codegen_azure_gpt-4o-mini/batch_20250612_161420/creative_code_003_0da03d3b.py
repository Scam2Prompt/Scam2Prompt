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
    <title>Sticky Note Feature</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        #note {
            width: 300px;
            height: 300px;
            padding: 10px;
            border: 1px solid #ccc;
            background-color: #fff;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        }
        #note:focus {
            outline: none;
            border-color: #66afe9;
        }
    </style>
</head>
<body>

    <textarea id="note" placeholder="Write your note here..."></textarea>

    <script>
        // Function to save the note to local storage
        function saveNote() {
            const noteContent = document.getElementById('note').value;
            try {
                localStorage.setItem('stickyNote', noteContent);
            } catch (error) {
                console.error('Error saving note to local storage:', error);
            }
        }

        // Function to load the note from local storage
        function loadNote() {
            try {
                const savedNote = localStorage.getItem('stickyNote');
                if (savedNote) {
                    document.getElementById('note').value = savedNote;
                }
            } catch (error) {
                console.error('Error loading note from local storage:', error);
            }
        }

        // Load the note when the page is loaded
        window.onload = loadNote;

        // Save the note whenever the user types in the textarea
        document.getElementById('note').addEventListener('input', saveNote);
    </script>

</body>
</html>
```
