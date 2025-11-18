"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Create a web form using HTML and JavaScript to allow users to upload custom designs for packaging options like "Box Hamper Imlek" and "Box Birthday Gift."
Generated: DETERMINISTIC_ff8de715df517b30
Batch ID: 20250612_153246
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
    <title>Custom Packaging Design Upload</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        .upload-field {
            margin-bottom: 15px;
        }
        .upload-field label {
            display: block;
            margin-bottom: 5px;
        }
        .upload-field input[type="file"] {
            display: block;
        }
        .upload-field input[type="submit"] {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
        }
        .upload-field input[type="submit"]:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
        .success {
            color: green;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Upload Your Custom Design</h1>
        <form id="uploadForm" enctype="multipart/form-data">
            <div class="upload-field">
                <label for="packagingType">Select Packaging Type:</label>
                <select id="packagingType" name="packagingType" required>
                    <option value="Box Hamper Imlek">Box Hamper Imlek</option>
                    <option value="Box Birthday Gift">Box Birthday Gift</option>
                </select>
            </div>
            <div class="upload-field">
                <label for="designFile">Upload Design File (PDF, JPG, PNG):</label>
                <input type="file" id="designFile" name="designFile" accept=".pdf, .jpg, .jpeg, .png" required>
            </div>
            <div class="error" id="errorMessage" style="display: none;"></div>
            <input type="submit" value="Upload Design">
            <div class="success" id="successMessage" style="display: none;"></div>
        </form>
    </div>

    <script>
        document.getElementById('uploadForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            const packagingType = document.getElementById('packagingType').value;
            const designFile = document.getElementById('designFile').files[0];
            const errorMessage = document.getElementById('errorMessage');
            const successMessage = document.getElementById('successMessage');

            // Clear previous messages
            errorMessage.style.display = 'none';
            successMessage.style.display = 'none';

            // Simple validation for file type
            if (designFile && !['application/pdf', 'image/jpeg', 'image/png'].includes(designFile.type)) {
                errorMessage.textContent = 'Invalid file type. Please upload a PDF, JPG, or PNG.';
                errorMessage.style.display = 'block';
                return;
            }

            // Create a FormData object to send the file
            const formData = new FormData();
            formData.append('packagingType', packagingType);
            formData.append('designFile', designFile);

            // Make an asynchronous POST request to upload the design
            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                return response.json();
            })
            .then(data => {
                successMessage.textContent = 'Your design has been uploaded successfully!';
                successMessage.style.display = 'block';
            })
            .catch(error => {
                errorMessage.textContent = 'An error occurred: ' + error.message;
                errorMessage.style.display = 'block';
            });
        });
    </script>
</body>
</html>
```
