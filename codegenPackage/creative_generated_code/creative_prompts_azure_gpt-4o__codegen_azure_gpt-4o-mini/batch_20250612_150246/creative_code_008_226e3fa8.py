"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Implement a withdrawal request system in HTML and JavaScript that includes dropdown options for methods (Mobile Recharge, Bkash, Rocket, Nogod) and calculates personal charges (e.g., 3tk) based on the selected method.
Generated: DETERMINISTIC_226e3fa8e1d357b0
Batch ID: 20250612_150246
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
    <title>Withdrawal Request System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            max-width: 400px;
        }
        label, select, input, button {
            display: block;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>

    <h1>Withdrawal Request</h1>

    <label for="method">Select Withdrawal Method:</label>
    <select id="method" name="method">
        <option value="">--Select Method--</option>
        <option value="mobileRecharge">Mobile Recharge</option>
        <option value="bkash">Bkash</option>
        <option value="rocket">Rocket</option>
        <option value="nogod">Nogod</option>
    </select>

    <label for="amount">Enter Amount (in Tk):</label>
    <input type="number" id="amount" name="amount" min="0" placeholder="Enter amount" required>

    <button id="submitBtn">Submit Request</button>

    <div id="result" style="margin-top: 20px;"></div>

    <script>
        // Function to calculate personal charges based on the selected method
        function getCharges(method) {
            const charges = {
                mobileRecharge: 3,
                bkash: 5,
                rocket: 4,
                nogod: 2
            };
            return charges[method] || 0; // Return 0 if method is not found
        }

        // Event listener for the submit button
        document.getElementById('submitBtn').addEventListener('click', function() {
            try {
                // Get user input
                const method = document.getElementById('method').value;
                const amount = parseFloat(document.getElementById('amount').value);

                // Validate input
                if (!method) {
                    throw new Error("Please select a withdrawal method.");
                }
                if (isNaN(amount) || amount <= 0) {
                    throw new Error("Please enter a valid amount.");
                }

                // Calculate charges
                const charges = getCharges(method);
                const totalDeduction = amount + charges;

                // Display the result
                document.getElementById('result').innerText = `For ${method}, total amount deducted will be: ${totalDeduction} Tk (including charges of ${charges} Tk)`;
            } catch (error) {
                // Handle errors and display error message
                document.getElementById('result').innerText = `Error: ${error.message}`;
            }
        });
    </script>

</body>
</html>
```
