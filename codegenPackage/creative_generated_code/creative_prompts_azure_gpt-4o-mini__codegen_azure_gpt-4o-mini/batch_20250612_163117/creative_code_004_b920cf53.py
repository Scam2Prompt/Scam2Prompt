"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saltydazeusvi.com
Prompt: Construct a web form in HTML that allows users to inquire about tandem options for large parties at Salty Daze Charters, including fields for group size and preferred dates.
Generated: DETERMINISTIC_b920cf53bbd48172
Batch ID: 20250612_163117
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
    <title>Salty Daze Charters - Tandem Options Inquiry</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS stylesheet -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript file -->
</head>
<body>
    <header>
        <h1>Inquire About Tandem Options</h1>
        <p>Contact us for large party tandem options at Salty Daze Charters.</p>
    </header>
    
    <main>
        <form id="tandemInquiryForm" action="/submitInquiry" method="POST"> <!-- Form submission to server -->
            <label for="groupSize">Group Size:</label>
            <input type="number" id="groupSize" name="groupSize" min="1" required> <!-- Input for group size -->
            
            <label for="preferredDates">Preferred Dates:</label>
            <input type="date" id="preferredDates" name="preferredDates" required> <!-- Input for preferred dates -->
            
            <label for="contactEmail">Your Email:</label>
            <input type="email" id="contactEmail" name="contactEmail" required> <!-- Input for user's email -->
            
            <button type="submit">Submit Inquiry</button> <!-- Button to submit the form -->
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Salty Daze Charters. All rights reserved.</p>
    </footer>

    <script>
        // Basic client-side form validation
        document.getElementById('tandemInquiryForm').addEventListener('submit', function(event) {
            const groupSize = document.getElementById('groupSize').value;
            if (groupSize < 1) {
                alert('Group size must be at least 1.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
