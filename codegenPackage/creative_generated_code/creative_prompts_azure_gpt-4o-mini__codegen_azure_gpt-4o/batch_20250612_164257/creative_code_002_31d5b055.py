"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinswapse.blogspot.com
Prompt: Create a simple HTML form that allows users to select shoe types like "sapato social" and "sandalias femininas" from a dropdown menu, inspired by the shoe categories on the Poocoinswapse blog.
Generated: DETERMINISTIC_31d5b055f9a22335
Batch ID: 20250612_164257
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
    <title>Shoe Selection Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        form {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background-color: #f9f9f9;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        select {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        /* Responsive design */
        @media (max-width: 600px) {
            form {
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <form id="shoeForm">
        <!-- Form title -->
        <h2>Select Your Shoe Type</h2>

        <!-- Dropdown menu for shoe categories -->
        <label for="shoeType">Choose a shoe type:</label>
        <select id="shoeType" name="shoeType" required>
            <option value="" disabled selected>-- Select a shoe type --</option>
            <option value="sapato_social">Sapato Social</option>
            <option value="sandalias_femininas">Sandálias Femininas</option>
            <option value="tenis_casual">Tênis Casual</option>
            <option value="botas">Botas</option>
        </select>

        <!-- Submit button -->
        <button type="submit">Submit</button>
    </form>

    <script>
        // Handle form submission
        document.getElementById('shoeForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission behavior

            const selectedShoeType = document.getElementById('shoeType').value;

            if (!selectedShoeType) {
                alert('Please select a shoe type before submitting.');
                return;
            }

            // Display the selected shoe type (you can replace this with a server-side submission)
            alert(`You selected: ${selectedShoeType}`);
        });
    </script>
</body>
</html>
```
