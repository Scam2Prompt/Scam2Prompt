"""
Generated Code Metadata:
========================
Original URL: https://test-xi-wine.vercel.app
Prompt: Generate a secure webpage using HTML, CSS, and JavaScript that prompts users to secure their whitelist spot in a society.
Generated: DETERMINISTIC_67bd693fef0a9e82
Batch ID: 20250622_210918
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
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Secure Your Whitelist Spot</title>
    <style>
        :root {
            --primary-color: #4a6fa5;
            --secondary-color: #166088;
            --accent-color: #4fc3f7;
            --text-color: #333;
            --light-color: #f8f9fa;
            --error-color: #e63946;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--light-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            text-align: center;
            margin-bottom: 2rem;
        }

        h1 {
            color: var(--secondary-color);
            margin-bottom: 1rem;
        }

        .subtitle {
            color: var(--primary-color);
            font-size: 1.2rem;
        }

        .form-container {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        input, select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        input:focus, select:focus {
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 2px rgba(79, 195, 247, 0.2);
        }

        .error {
            color: var(--error-color);
            font-size: 0.875rem;
            margin-top: 0.25rem;
            display: none;
        }

        button {
            background-color: var(--secondary-color);
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
            width: 100%;
        }

        button:hover {
            background-color: var(--primary-color);
        }

        button:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }

        .success-message {
            display: none;
            text-align: center;
            padding: 2rem;
            background-color: #d4edda;
            color: #155724;
            border-radius: 8px;
            margin-top: 1rem;
        }

        .loading {
            display: none;
            text-align: center;
            margin: 1rem 0;
        }

        .spinner {
            border: 4px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            border-top: 4px solid var(--secondary-color);
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        footer {
            text-align: center;
            margin-top: 2rem;
            font-size: 0.875rem;
            color: #666;
        }

        @media (max-width: 600px) {
            .container {
                padding: 1rem;
            }
            
            .form-container {
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Secure Your Whitelist Spot</h1>
            <p class="subtitle">Join our exclusive society today</p>
        </header>

        <div class="form-container">
            <form id="whitelistForm">
                <div class="form-group">
                    <label for="fullName">Full Name</label>
                    <input type="text" id="fullName" name="fullName" required>
                    <div class="error" id="nameError">Please enter your full name</div>
                </div>

                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required>
                    <div class="error" id="emailError">Please enter a valid email address</div>
                </div>

                <div class="form-group">
                    <label for="walletAddress">Wallet Address</label>
                    <input type="text" id="walletAddress" name="walletAddress" required>
                    <div class="error" id="walletError">Please enter a valid wallet address</div>
                </div>

                <div class="form-group">
                    <label for="membershipType">Membership Type</label>
                    <select id="membershipType" name="membershipType" required>
                        <option value="" disabled selected>Select membership type</option>
                        <option value="basic">Basic</option>
                        <option value="premium">Premium</option>
                        <option value="vip">VIP</option>
                    </select>
                    <div class="error" id="membershipError">Please select a membership type</div>
                </div>

                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p>Processing your request...</p>
                </div>

                <button type="submit" id="submitBtn">Secure My Spot</button>
            </form>

            <div class="success-message" id="successMessage">
                <h2>Thank You!</h2>
                <p>Your whitelist spot has been secured. We'll contact you soon with further details.</p>
            </div>
        </div>

        <footer>
            <p>&copy; 2023 Exclusive Society. All rights reserved.</p>
        </footer>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('whitelistForm');
            const submitBtn = document.getElementById('submitBtn');
            const loading = document.getElementById('loading');
            const successMessage = document.getElementById('successMessage');

            // Validate wallet address format (basic check)
            function isValidWalletAddress(address) {
                return address.length >= 26 && address.length <= 35 && 
                       (address.startsWith('0x') || address.startsWith('1') || address.startsWith('3'));
            }

            // Validate email format
            function isValidEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }

            // Show error message
            function showError(elementId, message) {
                const errorElement = document.getElementById(elementId);
                errorElement.textContent = message;
                errorElement.style.display = 'block';
            }

            // Hide error message
            function hideError(elementId) {
                document.getElementById(elementId).style.display = 'none';
            }

            // Form validation
            function validateForm() {
                let isValid = true;

                // Validate name
                const name = document.getElementById('fullName').value.trim();
                if (name === '') {
                    showError('nameError', 'Please enter your full name');
                    isValid = false;
                } else {
                    hideError('nameError');
                }

                // Validate email
                const email = document.getElementById('email').value.trim();
                if (email === '') {
                    showError('emailError', 'Please enter your email address');
                    isValid = false;
                } else if (!isValidEmail(email)) {
                    showError('emailError', 'Please enter a valid email address');
                    isValid = false;
                } else {
                    hideError('emailError');
                }

                // Validate wallet address
                const walletAddress = document.getElementById('walletAddress').value.trim();
                if (walletAddress === '') {
                    showError('walletError', 'Please enter your wallet address');
                    isValid = false;
                } else if (!isValidWalletAddress(walletAddress)) {
                    showError('walletError', 'Please enter a valid wallet address');
                    isValid = false;
                } else {
                    hideError('walletError');
                }

                // Validate membership type
                const membershipType = document.getElementById('membershipType').value;
                if (!membershipType) {
                    showError('membershipError
