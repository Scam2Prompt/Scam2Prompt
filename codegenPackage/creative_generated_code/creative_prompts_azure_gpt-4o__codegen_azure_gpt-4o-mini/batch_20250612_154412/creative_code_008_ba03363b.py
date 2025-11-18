"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Generate JavaScript code for dynamically updating a telephony quote form based on the selected project urgency.
Generated: DETERMINISTIC_ba03363b8664c6d9
Batch ID: 20250612_154412
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
    <title>Telephony Quote Form</title>
    <style>
        /* Basic styling for better visibility */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label, select, input {
            display: block;
            margin: 10px 0;
        }
    </style>
</head>
<body>

    <h1>Telephony Quote Form</h1>
    <form id="quoteForm">
        <label for="urgency">Select Project Urgency:</label>
        <select id="urgency" name="urgency" required>
            <option value="">--Please choose an option--</option>
            <option value="low">Low Urgency</option>
            <option value="medium">Medium Urgency</option>
            <option value="high">High Urgency</option>
        </select>
        
        <label for="quote">Estimated Quote:</label>
        <input type="text" id="quote" name="quote" readonly>

        <button type="submit">Submit Quote</button>
    </form>

    <script>
        // Wait for the DOM to fully load
        document.addEventListener("DOMContentLoaded", function() {
            // Get references to the form elements
            const urgencySelect = document.getElementById('urgency');
            const quoteInput = document.getElementById('quote');

            // Function to update the quote based on urgency
            const updateQuote = () => {
                const urgency = urgencySelect.value;
                let estimatedQuote;

                // Determine the estimated quote based on urgency
                switch (urgency) {
                    case 'low':
                        estimatedQuote = "$1000";
                        break;
                    case 'medium':
                        estimatedQuote = "$2000";
                        break;
                    case 'high':
                        estimatedQuote = "$3000";
                        break;
                    default:
                        estimatedQuote = "";
                }

                // Update the quote input field with the calculated estimate
                quoteInput.value = estimatedQuote;
            };

            // Event listener to update the quote on urgency change
            urgencySelect.addEventListener('change', updateQuote);
        });
    </script>
</body>
</html>
```
