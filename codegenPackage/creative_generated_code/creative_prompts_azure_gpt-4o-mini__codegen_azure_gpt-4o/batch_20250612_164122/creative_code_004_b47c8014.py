"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://natureexcursionsafaris.com
Prompt: Design a simple HTML form that allows users to inquire about specific safari packages, including fields for travel dates, group size, and preferred activities in East Africa.
Generated: DETERMINISTIC_b47c80144b460bbe
Batch ID: 20250612_164122
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
    <meta name="description" content="Safari Inquiry Form for East Africa">
    <title>Safari Inquiry Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .form-container {
            background-color: #fff;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-bottom: 20px;
        }

        button {
            background-color: #28a745;
            color: #fff;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Safari Inquiry Form</h1>
        <!-- Safari inquiry form -->
        <form id="safari-inquiry-form" method="POST" action="/submit-inquiry">
            <!-- Travel dates -->
            <label for="travel-dates">Travel Dates:</label>
            <input type="date" id="travel-dates" name="travelDates" required>
            
            <!-- Group size -->
            <label for="group-size">Group Size:</label>
            <input type="number" id="group-size" name="groupSize" min="1" max="50" required>
            
            <!-- Preferred activities -->
            <label for="activities">Preferred Activities:</label>
            <select id="activities" name="activities" required>
                <option value="" disabled selected>Select an activity</option>
                <option value="wildlife-safaris">Wildlife Safaris</option>
                <option value="bird-watching">Bird Watching</option>
                <option value="hiking">Hiking</option>
                <option value="cultural-tours">Cultural Tours</option>
                <option value="photography">Photography</option>
            </select>
            
            <!-- Additional comments -->
            <label for="comments">Additional Comments:</label>
            <textarea id="comments" name="comments" rows="5" placeholder="Let us know any specific preferences..."></textarea>
            
            <!-- Submit button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>
</body>
</html>
```
