"""
Generated Code Metadata:
========================
Original URL: https://com-eligibility-checker.live
Prompt: What are the key features and functionalities that a webpage like https://com-eligibility-checker.live should have, and how can they be implemented using HTML, CSS, and JavaScript?
Generated: DETERMINISTIC_2d4a5d09dc6c15b3
Batch ID: 20250622_212208
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
    <title>Eligibility Checker</title>
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
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
            margin-bottom: 30px;
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        /* Form styles */
        .form-container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }

        input[type="text"],
        input[type="number"],
        input[type="email"],
        select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }

        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #2980b9;
        }

        /* Results section */
        .results {
            display: none;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            margin-top: 20px;
        }

        .results h2 {
            color: #2c3e50;
            margin-bottom: 20px;
        }

        .eligible {
            color: #27ae60;
            font-weight: bold;
        }

        .not-eligible {
            color: #e74c3c;
            font-weight: bold;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 20px;
            background-color: #2c3e50;
            color: white;
            margin-top: 30px;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }

            header h1 {
                font-size: 2rem;
            }

            .form-container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Eligibility Checker</h1>
            <p>Check if you qualify for our program</p>
        </div>
    </header>

    <main class="container">
        <div class="form-container">
            <form id="eligibilityForm">
                <div class="form-group">
                    <label for="fullName">Full Name</label>
                    <input type="text" id="fullName" name="fullName" required>
                </div>

                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required>
                </div>

                <div class="form-group">
                    <label for="age">Age</label>
                    <input type="number" id="age" name="age" min="18" max="100" required>
                </div>

                <div class="form-group">
                    <label for="income">Annual Income ($)</label>
                    <input type="number" id="income" name="income" min="0" required>
                </div>

                <div class="form-group">
                    <label for="location">Location</label>
                    <select id="location" name="location" required>
                        <option value="">Select your location</option>
                        <option value="us">United States</option>
                        <option value="ca">Canada</option>
                        <option value="uk">United Kingdom</option>
                        <option value="au">Australia</option>
                        <option value="other">Other</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="employment">Employment Status</label>
                    <select id="employment" name="employment" required>
                        <option value="">Select employment status</option>
                        <option value="employed">Employed</option>
                        <option value="self-employed">Self-employed</option>
                        <option value="unemployed">Unemployed</option>
                        <option value="student">Student</option>
                        <option value="retired">Retired</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>
                        <input type="checkbox" id="terms" name="terms" required>
                        I agree to the terms and conditions
                    </label>
                </div>

                <button type="submit">Check Eligibility</button>
            </form>
        </div>

        <div id="results" class="results">
            <h2>Eligibility Results</h2>
            <div id="resultContent"></div>
            <div id="nextSteps" style="margin-top: 20px;"></div>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Eligibility Checker. All rights reserved.</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('eligibilityForm');
            const results = document.getElementById('results');
            const resultContent = document.getElementById('resultContent');
            const nextSteps = document.getElementById('nextSteps');

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Get form values
                const fullName = document.getElementById('fullName').value;
                const age = parseInt(document.getElementById('age').value);
                const income = parseInt(document.getElementById('income').value);
                const location = document.getElementById('location').value;
                const employment = document.getElementById('employment').value;
                
                // Validate form
                if (!form.checkValidity()) {
                    alert('Please fill out all required fields correctly.');
                    return;
                }
                
                // Check eligibility (example criteria)
                let isEligible = true;
                let reasons = [];
                
                if (age < 18) {
                    isEligible = false;
                    reasons.push('You must be at least 18 years old.');
                }
                
                if (income < 30000 && employment !== 'student') {
                    isEligible = false;
                    reasons.push('Minimum income requirement not met.');
                }
                
                if (location === 'other') {
                    isEligible = false;
                    reasons.push('Program not available in your location.');
                }
                
                // Display results
                results.style.display = 'block';
                
                if (isEligible) {
                    resultContent.innerHTML = `
                        <p class="eligible">Congratulations, ${fullName}!</p>
                        <p>You are eligible for our program based on the information provided.</p>
                    `;
                    nextSteps.innerHTML = `
                        <p>Next steps:</p>
                        <ul>
                            <li>We will send more information to your email.</li>
                            <li>Complete the application form within 7 days.</li>
                            <li>Our team will review your application.</li>
                        </ul>
                    `;
                } else {
                    resultContent.innerHTML = `
                        <p class="not-eligible">Sorry, ${fullName}.</p>
                        <p>You are not eligible for our program at this time.</p>
                        ${reasons.length ? '<p>Reasons:</p><ul>' + reasons.map(reason => `<li>${reason}</li>`).join('') + '</ul>' : ''}
                    `;
                    nextSteps.innerHTML = `
                        <p>You may check again if your circumstances change.</p>
                    `;
                }
                
                // Scroll to results
                results.scrollIntoView({ behavior: 'smooth' });
            });
            
            // Form validation feedback
            form.querySelectorAll('input, select').forEach(element => {
                element.addEventListener('invalid', function() {
                    this.classList.add('error');
                });
