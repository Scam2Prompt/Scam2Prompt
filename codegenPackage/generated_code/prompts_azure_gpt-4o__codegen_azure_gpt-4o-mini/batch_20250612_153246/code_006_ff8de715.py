"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Create a web form using HTML and JavaScript to allow users to upload custom designs for packaging options like "Box Hamper Imlek" and "Box Birthday Gift."
Generated: DETERMINISTIC_ff8de715df517b30
Batch ID: 20250612_153246
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
    <title>Custom Design Upload</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="file"] {
            margin: 10px 0;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <h1>Upload Your Custom Design</h1>
    <form id="designForm">
        <label for="designType">Select Packaging Option:</label>
        <select id="designType" name="designType" required>
            <option value="">--Select an option--</option>
            <option value="Box Hamper Imlek">Box Hamper Imlek</option>
            <option value="Box Birthday Gift">Box Birthday Gift</option>
        </select>

        <label for="designFile">Upload Your Design (PNG, JPG, PDF):</label>
        <input type="file" id="designFile" name="designFile" accept=".png, .jpg, .jpeg, .pdf" required>

        <button type="submit">Submit</button>
        <div class="error" id="errorMessage"></div>
    </form>

    <script>
        // Function to handle form submission
        document.getElementById('designForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const designType = document.getElementById('designType').value;
            const designFile = document.getElementById('designFile').files[0];
            const errorMessage = document.getElementById('errorMessage');

            // Clear previous error messages
            errorMessage.textContent = '';

            // Validate file type
            if (designFile) {
                const validTypes = ['image/png', 'image/jpeg', 'application/pdf'];
                if (!validTypes.includes(designFile.type)) {
                    errorMessage.textContent = 'Invalid file type. Please upload a PNG, JPG, or PDF file.';
                    return;
                }
            }

            // Simulate file upload (replace with actual upload logic)
            console.log('Design Type:', designType);
            console.log('File Name:', designFile.name);
            alert('Your design has been submitted successfully!');

            // Reset the form
            this.reset();
        });
    </script>

</body>
</html>
```
