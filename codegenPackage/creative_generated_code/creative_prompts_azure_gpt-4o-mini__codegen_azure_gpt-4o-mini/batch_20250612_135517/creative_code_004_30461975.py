"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cakco.com
Prompt: Construct a simple HTML form that allows users to select color options for bags, based on the product variants showcased on Cakco's website.
Generated: DETERMINISTIC_304619755738128f
Batch ID: 20250612_135517
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
    <title>Cakco Bag Color Selection</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript, loaded after content -->
</head>
<body>
    <div class="container">
        <h1>Select Your Bag Color</h1>
        <form id="colorSelectionForm" action="/submit" method="POST"> <!-- Form for color selection -->
            <label for="bagVariants">Choose a Bag Variant:</label>
            <select id="bagVariants" name="bagVariant" required>
                <option value="" disabled selected>Select a variant</option>
                <option value="backpack">Backpack</option>
                <option value="tote">Tote</option>
                <option value="messenger">Messenger</option>
            </select>

            <label for="bagColor">Choose a Color:</label>
            <select id="bagColor" name="bagColor" required>
                <option value="" disabled selected>Select a color</option>
                <!-- Color options will be populated based on selected variant -->
            </select>

            <button type="submit">Submit</button>
        </form>
        <div id="errorMessage" class="error"></div> <!-- Placeholder for error messages -->
    </div>

    <script>
        // Color options based on bag variants
        const colorOptions = {
            backpack: ['Red', 'Blue', 'Green', 'Black'],
            tote: ['Pink', 'Yellow', 'Gray', 'White'],
            messenger: ['Brown', 'Navy', 'Orange', 'Purple']
        };

        // Function to populate color options based on selected bag variant
        function populateColors() {
            const variantSelect = document.getElementById('bagVariants');
            const colorSelect = document.getElementById('bagColor');
            const selectedVariant = variantSelect.value;

            // Clear existing options
            colorSelect.innerHTML = '<option value="" disabled selected>Select a color</option>';

            // Populate colors based on selected variant
            if (selectedVariant && colorOptions[selectedVariant]) {
                colorOptions[selectedVariant].forEach(color => {
                    const option = document.createElement('option');
                    option.value = color.toLowerCase();
                    option.textContent = color;
                    colorSelect.appendChild(option);
                });
            }
        }

        // Event listener for bag variant selection
        document.getElementById('bagVariants').addEventListener('change', populateColors);

        // Form submission handler
        document.getElementById('colorSelectionForm').addEventListener('submit', function(event) {
            const selectedVariant = document.getElementById('bagVariants').value;
            const selectedColor = document.getElementById('bagColor').value;

            // Basic validation
            if (!selectedVariant || !selectedColor) {
                event.preventDefault(); // Prevent form submission
                document.getElementById('errorMessage').textContent = 'Please select both a bag variant and a color.';
            } else {
                document.getElementById('errorMessage').textContent = ''; // Clear error message
            }
        });
    </script>
</body>
</html>
```
