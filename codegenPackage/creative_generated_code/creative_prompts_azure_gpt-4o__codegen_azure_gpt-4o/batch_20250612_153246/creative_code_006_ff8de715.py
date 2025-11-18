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
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #f4f4f4;
    }

    .form-container {
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .form-container h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group select,
    .form-group input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .form-group button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-weight: bold;
    }

    .form-group button:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 0.9em;
      margin-top: 5px;
    }

    .success-message {
      color: green;
      font-size: 0.9em;
      margin-top: 5px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Upload Custom Packaging Design</h2>
    <form id="uploadForm">
      <div class="form-group">
        <!-- Dropdown for selecting packaging type -->
        <label for="packagingType">Select Packaging Type:</label>
        <select id="packagingType" name="packagingType" required>
          <option value="" disabled selected>Choose an option</option>
          <option value="Box Hamper Imlek">Box Hamper Imlek</option>
          <option value="Box Birthday Gift">Box Birthday Gift</option>
        </select>
        <span class="error-message" id="typeError"></span>
      </div>

      <div class="form-group">
        <!-- File input for uploading design -->
        <label for="designFile">Upload Your Design:</label>
        <input type="file" id="designFile" name="designFile" accept=".jpg,.jpeg,.png,.pdf" required>
        <span class="error-message" id="fileError"></span>
      </div>

      <!-- Submit button -->
      <div class="form-group">
        <button type="submit">Upload Design</button>
      </div>

      <!-- Success message container -->
      <div class="form-group">
        <span class="success-message" id="successMessage"></span>
      </div>
    </form>
  </div>

  <script>
    // JavaScript for form validation and handling
    document.getElementById('uploadForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission behavior

      // Get form elements
      const packagingType = document.getElementById('packagingType');
      const designFile = document.getElementById('designFile');
      const typeError = document.getElementById('typeError');
      const fileError = document.getElementById('fileError');
      const successMessage = document.getElementById('successMessage');

      // Reset error messages
      typeError.textContent = '';
      fileError.textContent = '';
      successMessage.textContent = '';

      let isValid = true;

      // Validate packaging type selection
      if (packagingType.value === '') {
        typeError.textContent = 'Please select a packaging type.';
        isValid = false;
      }

      // Validate file upload
      if (!designFile.files.length) {
        fileError.textContent = 'Please upload a design file.';
        isValid = false;
      }

      // If validation passes, simulate a successful upload
      if (isValid) {
        successMessage.textContent = 'Design uploaded successfully!';
        // Here you'd typically send the data to the server using an AJAX request or Form submission
        // Example: Use `fetch` API or a third-party library like Axios for server communication
      }
    });
  </script>
</body>
</html>
```
