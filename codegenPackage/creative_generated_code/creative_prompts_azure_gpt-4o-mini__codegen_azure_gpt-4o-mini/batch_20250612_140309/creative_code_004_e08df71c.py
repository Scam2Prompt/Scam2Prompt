"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getfundscontrol.net
Prompt: Generate a sample HTML page for a loan application that includes disclosures about tribal lenders and state-licensed lenders, as seen on Getfundscontrol.net.
Generated: DETERMINISTIC_e08df71cdeb8b4ce
Batch ID: 20250612_140309
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
    <title>Loan Application</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external stylesheet for better styling -->
</head>
<body>
    <header>
        <h1>Loan Application Form</h1>
    </header>

    <main>
        <form id="loanApplicationForm" action="/submit-loan-application" method="POST">
            <fieldset>
                <legend>Personal Information</legend>
                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>

                <label for="loanAmount">Loan Amount:</label>
                <input type="number" id="loanAmount" name="loanAmount" required>
            </fieldset>

            <fieldset>
                <legend>Loan Type</legend>
                <label for="tribalLender">
                    <input type="radio" id="tribalLender" name="lenderType" value="tribal" required>
                    Tribal Lender
                </label>
                <label for="stateLicensedLender">
                    <input type="radio" id="stateLicensedLender" name="lenderType" value="state-licensed">
                    State-Licensed Lender
                </label>
            </fieldset>

            <button type="submit">Submit Application</button>
        </form>

        <section id="disclosures">
            <h2>Important Disclosures</h2>
            <article>
                <h3>Tribal Lender Disclosure</h3>
                <p>
                    Tribal lenders are not subject to state laws and regulations. They are governed by the regulations of their respective tribes.
                    Borrowers are encouraged to fully understand the terms of the loan and their obligations prior to accepting a loan from a tribal lender.
                </p>
            </article>
            <article>
                <h3>State-Licensed Lender Disclosure</h3>
                <p>
                    State-licensed lenders are required to comply with state regulations and laws regarding lending practices.
                    This includes interest rate limits, loan terms, and other disclosure requirements. Make sure to review all terms and conditions before proceeding.
                </p>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Loan Application Portal. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler for client-side validation
        document.getElementById('loanApplicationForm').addEventListener('submit', function(event) {
            // Add any additional client-side validation logic here
            // Example: Check loan amount is positive
            const loanAmount = document.getElementById('loanAmount').value;
            if (loanAmount <= 0) {
                alert('Please enter a valid loan amount.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
