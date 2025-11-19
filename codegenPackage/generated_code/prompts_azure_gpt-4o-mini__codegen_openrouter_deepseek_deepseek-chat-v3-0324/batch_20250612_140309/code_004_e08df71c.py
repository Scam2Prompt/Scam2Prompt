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
    <title>Loan Application - GetFundsControl</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 20px;
        }
        h1 {
            color: #2c3e50;
        }
        .form-section {
            margin-bottom: 30px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 5px;
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
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .disclosure {
            background-color: #f2f2f2;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin: 20px 0;
            font-size: 14px;
        }
        .disclosure h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        footer {
            margin-top: 40px;
            text-align: center;
            font-size: 12px;
            color: #7f8c8d;
            border-top: 1px solid #eee;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Loan Application</h1>
        <p>Complete the form below to apply for a loan</p>
    </header>

    <main>
        <form id="loanApplication">
            <div class="form-section">
                <h2>Personal Information</h2>
                <div class="form-group">
                    <label for="firstName">First Name</label>
                    <input type="text" id="firstName" name="firstName" required>
                </div>
                <div class="form-group">
                    <label for="lastName">Last Name</label>
                    <input type="text" id="lastName" name="lastName" required>
                </div>
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
            </div>

            <div class="form-section">
                <h2>Loan Details</h2>
                <div class="form-group">
                    <label for="loanAmount">Loan Amount Requested ($)</label>
                    <input type="number" id="loanAmount" name="loanAmount" min="100" max="5000" required>
                </div>
                <div class="form-group">
                    <label for="loanPurpose">Purpose of Loan</label>
                    <select id="loanPurpose" name="loanPurpose" required>
                        <option value="">Select a purpose</option>
                        <option value="emergency">Emergency Expenses</option>
                        <option value="medical">Medical Bills</option>
                        <option value="debt">Debt Consolidation</option>
                        <option value="home">Home Improvement</option>
                        <option value="auto">Auto Repair</option>
                        <option value="other">Other</option>
                    </select>
                </div>
            </div>

            <div class="form-section">
                <h2>Employment Information</h2>
                <div class="form-group">
                    <label for="employmentStatus">Employment Status</label>
                    <select id="employmentStatus" name="employmentStatus" required>
                        <option value="">Select employment status</option>
                        <option value="employed">Employed</option>
                        <option value="self-employed">Self-Employed</option>
                        <option value="unemployed">Unemployed</option>
                        <option value="retired">Retired</option>
                        <option value="student">Student</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="income">Monthly Income ($)</label>
                    <input type="number" id="income" name="income" min="0" required>
                </div>
            </div>

            <div class="disclosure">
                <h3>Important Disclosures</h3>
                <p><strong>State-Licensed Lenders Disclosure:</strong> Some lenders in our network may be licensed by your state and may offer loans with terms and conditions that comply with state law. These lenders may perform credit checks with credit reporting bureaus or obtain consumer reports through alternative providers.</p>
                
                <p><strong>Tribal Lenders Disclosure:</strong> Some lenders in our network are tribal lenders operating under the sovereignty of Native American tribes and their laws. These loans may be subject to tribal law and not state law, which may include different regulations than those you're familiar with. Tribal lenders may require that disputes be resolved in a tribal court.</p>
                
                <p><strong>General Disclosure:</strong> GetFundsControl.net is not a lender and does not make credit decisions. We connect interested persons with a lender. We do not control and are not responsible for the actions of any lender. Not all lenders can provide up to $5,000. The time it takes to receive funds varies by lender. This service may not be available in all states.</p>
                
                <p>By submitting your information, you agree to our <a href="#">Terms of Use</a> and <a href="#">Privacy Policy</a>.</p>
            </div>

            <div class="form-group">
                <input type="checkbox" id="consent" name="consent" required>
                <label for="consent">I have read and agree to the disclosures above</label>
            </div>

            <button type="submit">Submit Application</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 GetFundsControl.net. All rights reserved.</p>
        <p>This is not an offer for a loan. Loan approval is subject to lender's review of your application.</p>
    </footer>

    <script>
        document.getElementById('loanApplication').addEventListener('submit', function(e) {
            e.preventDefault();
            // Form validation and submission logic would go here
            alert('Application submitted! A lender will contact you shortly.');
        });
    </script>
</body>
</html>
```
