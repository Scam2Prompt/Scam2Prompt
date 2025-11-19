"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ozurfalim.com
Prompt: Develop a simple HTML form that allows users to submit their orders to Özurfalım Kebap, including fields for kebab and lahmacun selection.
Generated: DETERMINISTIC_88741fd8abba0226
Batch ID: 20250612_162050
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
    <title>Özurfalım Kebap Order Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external CSS file for styling -->
</head>
<body>
    <header>
        <h1>Özurfalım Kebap Order Form</h1>
    </header>
    
    <main>
        <form id="orderForm" action="submit_order.php" method="POST">
            <fieldset>
                <legend>Select Your Order</legend>
                
                <!-- Kebab Selection -->
                <label for="kebab">Select Kebab:</label>
                <select id="kebab" name="kebab" required>
                    <option value="" disabled selected>Select a kebab</option>
                    <option value="adana">Adana Kebab</option>
                    <option value="urfa">Urfa Kebab</option>
                    <option value="lamb">Lamb Kebab</option>
                    <option value="chicken">Chicken Kebab</option>
                </select>
                
                <!-- Lahmacun Selection -->
                <label for="lahmacun">Select Lahmacun:</label>
                <select id="lahmacun" name="lahmacun" required>
                    <option value="" disabled selected>Select a lahmacun</option>
                    <option value="meat">Meat Lahmacun</option>
                    <option value="vegetarian">Vegetarian Lahmacun</option>
                </select>

                <!-- Submit Button -->
                <button type="submit">Submit Order</button>
            </fieldset>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Özurfalım Kebap. All rights reserved.</p>
    </footer>

    <script>
        // Error handling for form submission
        document.getElementById('orderForm').addEventListener('submit', function(event) {
            const kebabSelected = document.getElementById('kebab').value;
            const lahmacunSelected = document.getElementById('lahmacun').value;

            // Check if both selections are made
            if (!kebabSelected || !lahmacunSelected) {
                alert('Please select both a kebab and a lahmacun before submitting the order.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
