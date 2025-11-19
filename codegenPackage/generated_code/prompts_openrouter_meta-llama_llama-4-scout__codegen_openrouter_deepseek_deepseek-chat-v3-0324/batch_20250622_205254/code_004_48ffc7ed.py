"""
Generated Code Metadata:
========================
Original URL: https://fdusd-mixer.com
Prompt: Design a simple user interface in HTML and CSS to facilitate users in creating a new mixing job with the FDUSD Mixer service, including input fields for address, amount, and optional timedelay and mixing code.
Generated: DETERMINISTIC_48ffc7ed0218eb6e
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML and CSS implementation for the FDUSD Mixer service UI:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FDUSD Mixer - Create New Job</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        /* Container styles */
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        /* Header styles */
        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        /* Form styles */
        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }

        input[type="text"],
        input[type="number"] {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border 0.3s;
        }

        input[type="text"]:focus,
        input[type="number"]:focus {
            border-color: #3498db;
            outline: none;
        }

        .optional-label {
            color: #7f8c8d;
            font-style: italic;
            font-weight: normal;
        }

        /* Button styles */
        .btn {
            display: inline-block;
            background: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            cursor: pointer;
            border-radius: 4px;
            font-size: 16px;
            transition: background 0.3s;
            width: 100%;
        }

        .btn:hover {
            background: #2980b9;
        }

        /* Responsive adjustments */
        @media (max-width: 640px) {
            .container {
                padding: 20px;
            }
        }

        /* Error message styling */
        .error-message {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }

        /* Success message */
        .success-message {
            color: #27ae60;
            text-align: center;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Create New Mixing Job</h1>
        
        <form id="mixingForm">
            <!-- Recipient Address -->
            <div class="form-group">
                <label for="recipientAddress">Recipient Address*</label>
                <input type="text" id="recipientAddress" name="recipientAddress" required 
                       placeholder="Enter FDUSD recipient address">
                <div class="error-message" id="addressError">Please enter a valid address</div>
            </div>
            
            <!-- Amount -->
            <div class="form-group">
                <label for="amount">Amount (FDUSD)*</label>
                <input type="number" id="amount" name="amount" required 
                       min="0.000001" step="0.000001" placeholder="Enter amount to mix">
                <div class="error-message" id="amountError">Please enter a valid amount</div>
            </div>
            
            <!-- Time Delay (Optional) -->
            <div class="form-group">
                <label for="timeDelay">Time Delay <span class="optional-label">(optional)</span></label>
                <input type="number" id="timeDelay" name="timeDelay" 
                       min="0" placeholder="Delay in hours (0 for immediate)">
            </div>
            
            <!-- Mixing Code (Optional) -->
            <div class="form-group">
                <label for="mixingCode">Mixing Code <span class="optional-label">(optional)</span></label>
                <input type="text" id="mixingCode" name="mixingCode" 
                       placeholder="Enter mixing code if you have one">
            </div>
            
            <!-- Submit Button -->
            <button type="submit" class="btn">Create Mixing Job</button>
        </form>
        
        <div class="success-message" id="successMessage">
            Mixing job created successfully!
        </div>
    </div>

    <script>
        // Form validation and submission
        document.getElementById('mixingForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error-message').forEach(el => el.style.display = 'none');
            
            // Validate form
            let isValid = true;
            const address = document.getElementById('recipientAddress').value.trim();
            const amount = document.getElementById('amount').value;
            
            // Address validation (basic check)
            if (!address || address.length < 20) {
                document.getElementById('addressError').style.display = 'block';
                isValid = false;
            }
            
            // Amount validation
            if (!amount || parseFloat(amount) <= 0) {
                document.getElementById('amountError').style.display = 'block';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would send data to server here
                // For demo, we'll just show success message
                document.getElementById('mixingForm').style.display = 'none';
                document.getElementById('successMessage').style.display = 'block';
                
                // Reset form after 3 seconds
                setTimeout(() => {
                    document.getElementById('mixingForm').style.display = 'block';
                    document.getElementById('successMessage').style.display = 'none';
                    this.reset();
                }, 3000);
            }
        });
    </script>
</body>
</html>
```
