"""
Generated Code Metadata:
========================
Original URL: https://eff-omega.vercel.app
Prompt: Create HTML and CSS code for a form with fields for full name, surname, account number, and a dropdown menu for selecting a bank. Include a "Proceed" button styled to indicate a loading state when clicked.
Generated: DETERMINISTIC_5e59ca370cbb4eec
Batch ID: 20250612_150618
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
    <title>Bank Account Form</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .form-container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 500px;
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
            text-align: center;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 600;
        }

        input, select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #4a90e2;
        }

        .btn {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
            font-weight: 600;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .btn:hover {
            background-color: #3a7bc8;
        }

        .btn.loading {
            background-color: #3a7bc8;
            cursor: not-allowed;
        }

        .btn.loading::after {
            content: "";
            display: inline-block;
            width: 16px;
            height: 16px;
            margin-left: 10px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .form-container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Bank Account Details</h1>
        <form id="bankForm">
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" required>
            </div>
            <div class="form-group">
                <label for="surname">Surname</label>
                <input type="text" id="surname" name="surname" required>
            </div>
            <div class="form-group">
                <label for="accountNumber">Account Number</label>
                <input type="text" id="accountNumber" name="accountNumber" required>
            </div>
            <div class="form-group">
                <label for="bank">Bank</label>
                <select id="bank" name="bank" required>
                    <option value="" disabled selected>Select your bank</option>
                    <option value="bank1">Bank One</option>
                    <option value="bank2">Bank Two</option>
                    <option value="bank3">Bank Three</option>
                    <option value="bank4">Bank Four</option>
                </select>
            </div>
            <button type="submit" class="btn" id="submitBtn">Proceed</button>
        </form>
    </div>

    <script>
        document.getElementById('bankForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            submitBtn.classList.add('loading');
            submitBtn.disabled = true;
            
            // Simulate form submission
            setTimeout(() => {
                submitBtn.classList.remove('loading');
                submitBtn.disabled = false;
                alert('Form submitted successfully!');
            }, 2000);
        });
    </script>
</body>
</html>
```
