"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eff-omega.vercel.app
Prompt: Create HTML and CSS code for a form with fields for full name, surname, account number, and a dropdown menu for selecting a bank. Include a "Proceed" button styled to indicate a loading state when clicked.
Generated: DETERMINISTIC_5e59ca370cbb4eec
Batch ID: 20250612_150618
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
    <title>Bank Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }

        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
            max-width: 400px;
            width: 100%;
        }

        .form-container h1 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
            color: #555;
        }

        .form-group input,
        .form-group select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }

        .form-group select {
            background-color: #fff;
        }

        .button-container {
            text-align: center;
        }

        .button-container button {
            padding: 10px 20px;
            font-size: 16px;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            position: relative;
        }

        /* Hover effect for the button */
        .button-container button:hover {
            background-color: #0056b3;
        }

        /* Loading state styling */
        .button-container button:disabled {
            background-color: #6c757d;
            cursor: not-allowed;
        }

        .loading-spinner {
            display: none; /* Initially hidden */
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 16px;
            height: 16px;
            border: 2px solid #fff;
            border-top: 2px solid transparent;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% {
                transform: translate(-50%, -50%) rotate(0deg);
            }
            100% {
                transform: translate(-50%, -50%) rotate(360deg);
            }
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Bank Details Form</h1>
        <form id="bankForm">
            <!-- Full Name Field -->
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" required>
            </div>

            <!-- Surname Field -->
            <div class="form-group">
                <label for="surname">Surname</label>
                <input type="text" id="surname" name="surname" required>
            </div>

            <!-- Account Number Field -->
            <div class="form-group">
                <label for="accountNumber">Account Number</label>
                <input type="text" id="accountNumber" name="accountNumber" required>
            </div>

            <!-- Bank Selection Dropdown -->
            <div class="form-group">
                <label for="bank">Select Bank</label>
                <select id="bank" name="bank" required>
                    <option value="" disabled selected>Select a bank</option>
                    <option value="bankA">Bank A</option>
                    <option value="bankB">Bank B</option>
                    <option value="bankC">Bank C</option>
                </select>
            </div>

            <!-- Proceed Button -->
            <div class="button-container">
                <button type="submit" id="proceedButton">
                    Proceed
                    <span class="loading-spinner" id="loadingSpinner"></span>
                </button>
            </div>
        </form>
    </div>

    <script>
        // JavaScript for button loading state
        const form = document.getElementById('bankForm');
        const proceedButton = document.getElementById('proceedButton');
        const loadingSpinner = document.getElementById('loadingSpinner');

        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent the default form submission

            // Set button to loading state
            proceedButton.disabled = true;
            loadingSpinner.style.display = 'inline-block';

            // Simulate processing time (e.g., API call)
            setTimeout(() => {
                // Reset button to normal state after processing
                proceedButton.disabled = false;
                loadingSpinner.style.display = 'none';
                alert('Form submitted successfully!');
            }, 2000); // Simulated delay of 2 seconds
        });
    </script>
</body>
</html>
```
