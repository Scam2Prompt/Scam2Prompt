"""
Generated Code Metadata:
========================
Original URL: https://monadawards.xyz
Prompt: Generate a nomination form for the Monad Echo Awards, focusing on the category of "Selfie Sorcerers" and including a brief description of why the nominee deserves recognition.
Generated: DETERMINISTIC_a2920290d04b7165
Batch ID: 20250612_162554
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
    <title>Monad Echo Awards - Nomination Form</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .category {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        textarea {
            height: 150px;
            resize: vertical;
        }
        .required {
            color: #e74c3c;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1>Monad Echo Awards Nomination Form</h1>
    
    <div class="category">
        <h2>Category: Selfie Sorcerers</h2>
        <p>This award recognizes individuals who demonstrate exceptional creativity, technical skill, and artistic vision in the art of self-portraiture through mobile photography.</p>
    </div>

    <form id="nominationForm">
        <div class="form-group">
            <label for="nomineeName">Nominee's Full Name <span class="required">*</span></label>
            <input type="text" id="nomineeName" name="nomineeName" required>
            <div id="nomineeNameError" class="error"></div>
        </div>

        <div class="form-group">
            <label for="nomineeContact">Nominee's Contact Information (Email or Phone) <span class="required">*</span></label>
            <input type="text" id="nomineeContact" name="nomineeContact" required>
            <div id="nomineeContactError" class="error"></div>
        </div>

        <div class="form-group">
            <label for="nominatorName">Your Name <span class="required">*</span></label>
            <input type="text" id="nominatorName" name="nominatorName" required>
            <div id="nominatorNameError" class="error"></div>
        </div>

        <div class="form-group">
            <label for="nominatorEmail">Your Email <span class="required">*</span></label>
            <input type="email" id="nominatorEmail" name="nominatorEmail" required>
            <div id="nominatorEmailError" class="error"></div>
        </div>

        <div class="form-group">
            <label for="reason">Reason for Nomination <span class="required">*</span></label>
            <p>Please describe why this nominee deserves recognition in the Selfie Sorcerers category. Consider their creativity, technical skill, influence, and unique approach to self-portraiture (500 words max).</p>
            <textarea id="reason" name="reason" required></textarea>
            <div id="reasonError" class="error"></div>
        </div>

        <div class="form-group">
            <label for="examples">Examples of Work (Links to social media profiles or specific posts)</label>
            <textarea id="examples" name="examples" placeholder="e.g., Instagram profile, specific post URLs"></textarea>
        </div>

        <button type="submit">Submit Nomination</button>
    </form>

    <script>
        document.getElementById('nominationForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate form
            let isValid = true;
            
            // Validate nominee name
            const nomineeName = document.getElementById('nomineeName').value.trim();
            if (!nomineeName) {
                document.getElementById('nomineeNameError').textContent = 'Please enter the nominee\'s name';
                isValid = false;
            }
            
            // Validate nominee contact
            const nomineeContact = document.getElementById('nomineeContact').value.trim();
            if (!nomineeContact) {
                document.getElementById('nomineeContactError').textContent = 'Please enter contact information';
                isValid = false;
            }
            
            // Validate nominator name
            const nominatorName = document.getElementById('nominatorName').value.trim();
            if (!nominatorName) {
                document.getElementById('nominatorNameError').textContent = 'Please enter your name';
                isValid = false;
            }
            
            // Validate nominator email
            const nominatorEmail = document.getElementById('nominatorEmail').value.trim();
            if (!nominatorEmail) {
                document.getElementById('nominatorEmailError').textContent = 'Please enter your email';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(nominatorEmail)) {
                document.getElementById('nominatorEmailError').textContent = 'Please enter a valid email address';
                isValid = false;
            }
            
            // Validate reason
            const reason = document.getElementById('reason').value.trim();
            if (!reason) {
                document.getElementById('reasonError').textContent = 'Please provide a reason for nomination';
                isValid = false;
            } else if (reason.split(/\s+/).length > 500) {
                document.getElementById('reasonError').textContent = 'Reason must be 500 words or less';
                isValid = false;
            }
            
            if (isValid) {
                // Form is valid, proceed with submission
                alert('Thank you for your nomination! We will review your submission and contact you if needed.');
                this.reset();
            }
        });
    </script>
</body>
</html>
```
