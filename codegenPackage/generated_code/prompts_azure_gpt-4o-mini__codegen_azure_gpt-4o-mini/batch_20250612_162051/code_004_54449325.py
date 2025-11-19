"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Design a simple web form using HTML and CSS for clients to select their preferred cleaning service (residential, office, or post-renovation) based on the options provided by Maria HouseKeepers.
Generated: DETERMINISTIC_5444932529bf825c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cleaning Service Selection</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Maria HouseKeepers - Select Your Cleaning Service</h1>
        <form id="cleaningServiceForm" action="/submit" method="POST">
            <label for="serviceType">Choose your preferred cleaning service:</label>
            <select id="serviceType" name="serviceType" required>
                <option value="" disabled selected>Select a service</option>
                <option value="residential">Residential Cleaning</option>
                <option value="office">Office Cleaning</option>
                <option value="post-renovation">Post-Renovation Cleaning</option>
            </select>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Container styling */
.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Heading styling */
h1 {
    font-size: 24px;
    margin-bottom: 20px;
    text-align: center;
}

/* Form label styling */
label {
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

/* Select box styling */
select {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Button styling */
button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

/* Button hover effect */
button:hover {
    background-color: #218838;
}
```
