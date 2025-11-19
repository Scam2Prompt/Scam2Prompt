"""
Generated Code Metadata:
========================
Original URL: https://getfundscontrol.net
Prompt: Generate a sample HTML page for a loan application that includes disclosures about tribal lenders and state-licensed lenders, as seen on Getfundscontrol.net.
Generated: DETERMINISTIC_e08df71cdeb8b4ce
Batch ID: 20250612_140309
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
    <title>Loan Application</title>
    <style>
        /* Basic styling for the page */
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            width: 80%;
            margin: 40px auto;
            padding: 20px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .disclosure {
            background-color: #f2f2f2;
            padding: 10px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Loan Application</h1>
        <form id="loan-application">
            <!-- Loan application form fields go here -->
            <label for="amount">Loan Amount:</label>
            <input type="number" id="amount" name="amount"><br><br>
            <label for="term">Loan Term:</label>
            <input type="text" id="term" name="term"><br><br>
            <input type="submit" value="Apply">
        </form>

        <div class="disclosure">
            <h2>Tribal Lenders Disclosure</h2>
            <p>Some lenders may be members of a federally recognized tribe and may be subject to tribal jurisdiction. Such lenders may offer loans with terms that differ from those offered by state-licensed lenders.</p>
            <p>Any loans made under tribal law are not subject to state laws and may not offer the same consumer protections as those under state law.</p>
        </div>

        <div class="disclosure">
            <h2>State-Licensed Lenders Disclosure</h2>
            <p>Some lenders may be licensed by one or more states. A list of the licenses and their status can be found on our <a href="#">Licenses Page</a>.</p>
            <p>State-licensed lenders are required to follow the laws and regulations of the states in which they operate.</p>
        </div>

        <div class="disclosure">
            <h2>General Disclosure</h2>
            <p>All loans involve credit and may not be suitable for all applicants. Creditworthiness and other factors may be considered in determining loan approval.</p>
            <p>Applicants should carefully review the terms and conditions of any loan before accepting.</p>
        </div>
    </div>

    <script>
        // Basic form submission handling
        const form = document.getElementById('loan-application');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // Implement form submission logic here
            console.log('Form submitted');
        });
    </script>
</body>
</html>
```
