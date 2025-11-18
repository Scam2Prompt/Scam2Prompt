"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Provide an example of CSS styling for a ticket booking form that includes dropdown menus, input fields, and a "Submit" button.
Generated: DETERMINISTIC_675b21c3d8fa0244
Batch ID: 20250612_154529
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
    <title>Ticket Booking Form</title>
    <style>
        /* Container for the form */
        .form-container {
            max-width: 400px; /* Maximum width of the form */
            margin: 0 auto; /* Center the form */
            padding: 20px; /* Padding inside the form */
            border: 1px solid #ccc; /* Light border around the form */
            border-radius: 8px; /* Rounded corners */
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
            background-color: #f9f9f9; /* Light background color */
        }

        /* Style for input fields */
        input[type="text"], input[type="email"], select {
            width: 100%; /* Full width inputs */
            padding: 10px; /* Padding inside inputs */
            margin: 10px 0; /* Margin between inputs */
            border: 1px solid #ccc; /* Border for inputs */
            border-radius: 4px; /* Rounded corners for inputs */
            box-sizing: border-box; /* Include padding in width */
            font-size: 16px; /* Font size for texts */
        }

        /* Style for the submit button */
        .submit-btn {
            background-color: #28a745; /* Green background for button */
            color: white; /* White text color */
            border: none; /* No border */
            border-radius: 4px; /* Rounded corners */
            padding: 12px; /* Padding inside button */
            cursor: pointer; /* Pointer cursor on hover */
            font-size: 16px; /* Font size */
            transition: background-color 0.3s; /* Smooth transition */
        }

        /* Hover effect for submit button */
        .submit-btn:hover {
            background-color: #218838; /* Darker green on hover */
        }

        /* Style for form headings */
        h2 {
            text-align: center; /* Center align the heading */
            color: #333; /* Darker text color */
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Ticket Booking Form</h2>
        <form id="bookingForm" onsubmit="return handleSubmit(event);">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="event">Select Event:</label>
            <select id="event" name="event" required>
                <option value="">--Please choose an event--</option>
                <option value="concert">Concert</option>
                <option value="theater">Theater</option>
                <option value="sport">Sport</option>
            </select>

            <button type="submit" class="submit-btn">Submit</button>
        </form>
    </div>

    <script>
        /**
         * Handles form submission.
         * @param {Event} event - The form submission event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            // Example of handling the data (e.g., send to a server)
            console.log('Form submitted:', data);

            // Add your AJAX request or form processing logic here
            // ...

            // Return false to prevent the default form submission
            return false;
        }
    </script>
</body>
</html>
```
