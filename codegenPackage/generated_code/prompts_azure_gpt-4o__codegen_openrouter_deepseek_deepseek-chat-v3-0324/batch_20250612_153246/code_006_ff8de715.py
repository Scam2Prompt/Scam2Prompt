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
    <title>Custom Packaging Design Upload</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .form-container {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .success {
            color: green;
            font-size: 16px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Custom Packaging Design Upload</h1>
        <form id="designUploadForm">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="packageType">Package Type</label>
                <select id="packageType" name="packageType" required>
                    <option value="">Select a package type</option>
                    <option value="Box Hamper Imlek">Box Hamper Imlek</option>
                    <option value="Box Birthday Gift">Box Birthday Gift</option>
                    <option value="Other">Other (please specify)</option>
                </select>
                <div id="packageTypeError" class="error"></div>
            </div>

            <div class="form-group" id="otherPackageTypeContainer" style="display: none;">
                <label for="otherPackageType">Specify Package Type</label>
                <input type="text" id="otherPackageType" name="otherPackageType">
            </div>

            <div class="form-group">
                <label for="designFile">Upload Design File</label>
                <input type="file" id="designFile" name="designFile" accept=".jpg,.jpeg,.png,.pdf,.ai,.psd" required>
                <div id="fileError" class="error"></div>
                <small>Accepted formats: JPG, PNG, PDF, AI, PSD (Max 10MB)</small>
            </div>

            <div class="form-group">
                <label for="notes">Additional Notes</label>
                <textarea id="notes" name="notes" rows="4" style="width: 100%;"></textarea>
            </div>

            <button type="submit">Submit Design</button>
            <div id="successMessage" class="success"></div>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('designUploadForm');
            const packageTypeSelect = document.getElementById('packageType');
            const otherPackageTypeContainer = document.getElementById('otherPackageTypeContainer');
            const designFileInput = document.getElementById('designFile');
            
            // Show/hide other package type field based on selection
            packageTypeSelect.addEventListener('change', function() {
                if (this.value === 'Other') {
                    otherPackageTypeContainer.style.display = 'block';
                } else {
                    otherPackageTypeContainer.style.display = 'none';
                }
            });

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                clearErrors();
                
                if (validateForm()) {
                    // In a real application, you would send the form data to a server here
                    // For demonstration, we'll just show a success message
                    document.getElementById('successMessage').textContent = 
                        'Your design has been submitted successfully! We will review it and contact you soon.';
                    form.reset();
                }
            });

            function clearErrors() {
                document.querySelectorAll('.error').forEach(el => el.textContent = '');
                document.getElementById('successMessage').textContent = '';
            }

            function validateForm() {
                let isValid = true;

                // Validate name
                const name = document.getElementById('name').value.trim();
                if (!name) {
                    document.getElementById('nameError').textContent = 'Please enter your name';
                    isValid = false;
                }

                // Validate email
                const email = document.getElementById('email').value.trim();
                if (!email) {
                    document.getElementById('emailError').textContent = 'Please enter your email';
                    isValid = false;
                } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    isValid = false;
                }

                // Validate package type
                const packageType = packageTypeSelect.value;
                if (!packageType) {
                    document.getElementById('packageTypeError').textContent = 'Please select a package type';
                    isValid = false;
                } else if (packageType === 'Other') {
                    const otherType = document.getElementById('otherPackageType').value.trim();
                    if (!otherType) {
                        document.getElementById('packageTypeError').textContent = 'Please specify the package type';
                        isValid = false;
                    }
                }

                // Validate file
                const file = designFileInput.files[0];
                if (!file) {
                    document.getElementById('fileError').textContent = 'Please select a design file';
                    isValid = false;
                } else {
                    const validTypes = ['image/jpeg', 'image/png', 'application/pdf', 'application/postscript', 'image/vnd.adobe.photoshop'];
                    const maxSize = 10 * 1024 * 1024; // 10MB
                    
                    if (!validTypes.includes(file.type)) {
                        document.getElementById('fileError').textContent = 'Invalid file type. Please upload JPG, PNG, PDF, AI, or PSD.';
                        isValid = false;
                    } else if (file.size > maxSize) {
                        document.getElementById('fileError').textContent = 'File size exceeds 10MB limit';
                        isValid = false;
                    }
                }

                return isValid;
            }
        });
    </script>
</body>
</html>
```
