"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Develop a registration form in HTML and PHP for a slot gaming website, including fields for bank account details and QRIS payment setup as described on Satria4D.
Generated: DETERMINISTIC_33c5d58bb6ee4e9f
Batch ID: 20250612_152739
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
    <title>Satria4D - Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="password"],
        input[type="email"],
        input[type="tel"],
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .btn {
            display: inline-block;
            background: #333;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background: #555;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        .success {
            color: green;
            font-size: 0.9em;
        }
        .payment-section {
            margin-top: 20px;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Satria4D Registration</h1>
        
        <?php
        // Initialize variables
        $errors = [];
        $success = '';
        
        // Check if form is submitted
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            // Validate and sanitize input
            $username = trim($_POST['username'] ?? '');
            $email = trim($_POST['email'] ?? '');
            $password = $_POST['password'] ?? '';
            $confirm_password = $_POST['confirm_password'] ?? '';
            $phone = trim($_POST['phone'] ?? '');
            $bank_name = trim($_POST['bank_name'] ?? '');
            $account_number = trim($_POST['account_number'] ?? '');
            $account_name = trim($_POST['account_name'] ?? '');
            $qris_id = trim($_POST['qris_id'] ?? '');
            
            // Validation
            if (empty($username)) {
                $errors['username'] = 'Username is required';
            } elseif (strlen($username) < 4) {
                $errors['username'] = 'Username must be at least 4 characters';
            }
            
            if (empty($email)) {
                $errors['email'] = 'Email is required';
            } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $errors['email'] = 'Invalid email format';
            }
            
            if (empty($password)) {
                $errors['password'] = 'Password is required';
            } elseif (strlen($password) < 6) {
                $errors['password'] = 'Password must be at least 6 characters';
            }
            
            if ($password !== $confirm_password) {
                $errors['confirm_password'] = 'Passwords do not match';
            }
            
            if (empty($phone)) {
                $errors['phone'] = 'Phone number is required';
            }
            
            if (empty($bank_name)) {
                $errors['bank_name'] = 'Bank name is required';
            }
            
            if (empty($account_number)) {
                $errors['account_number'] = 'Account number is required';
            } elseif (!is_numeric($account_number)) {
                $errors['account_number'] = 'Account number must be numeric';
            }
            
            if (empty($account_name)) {
                $errors['account_name'] = 'Account name is required';
            }
            
            // If no errors, proceed with registration
            if (empty($errors)) {
                // In a real application, you would:
                // 1. Hash the password
                // 2. Connect to database
                // 3. Insert user data
                // 4. Handle success/error
                
                // For this example, we'll just show a success message
                $success = 'Registration successful!';
                
                // Clear form fields
                $username = $email = $password = $confirm_password = $phone = '';
                $bank_name = $account_number = $account_name = $qris_id = '';
            }
        }
        ?>
        
        <?php if (!empty($success)): ?>
            <div class="success"><?php echo htmlspecialchars($success); ?></div>
        <?php endif; ?>
        
        <form method="post" action="">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" value="<?php echo htmlspecialchars($username ?? ''); ?>" required>
                <?php if (isset($errors['username'])): ?>
                    <div class="error"><?php echo htmlspecialchars($errors['username']); ?></div>
                <?php endif; ?>
            </div>
            
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email ?? ''); ?>" required>
                <?php if (isset($errors['email'])): ?>
                    <div class="error"><?php echo htmlspecialchars($errors['email']); ?></div>
                <?php endif; ?>
            </div>
            
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
                <?php if (isset($errors['password'])): ?>
                    <div class="error"><?php echo htmlspecialchars($errors['password']); ?></div>
                <?php endif; ?>
            </div>
            
            <div class="form-group">
                <label for="confirm_password">Confirm Password</label>
                <input type="password" id="confirm_password" name="confirm_password" required>
                <?php if (isset($errors['confirm_password'])): ?>
                    <div class="error"><?php echo htmlspecialchars($errors['confirm_password']); ?></div>
                <?php endif; ?>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" value="<?php echo htmlspecialchars($phone ?? ''); ?>" required>
                <?php if (isset($errors['phone'])): ?>
                    <div class="error"><?php echo htmlspecialchars($errors['phone']); ?></div>
                <?php endif; ?>
            </div>
            
            <div class="payment-section">
                <h3>Bank Account Details</h3>
                
                <div class="form-group">
                    <label for="bank_name">Bank Name</label>
                    <select id="bank_name" name="bank_name" required>
                        <option value="">Select Bank</option>
                        <option value="BCA" <?php echo (isset($bank_name) && $bank_name === 'BCA') ? 'selected' : ''; ?>>BCA</option>
                        <option value="BRI" <?php echo (isset($bank_name) && $bank_name === 'BRI') ? 'selected' : ''; ?>>BRI</option>
                        <option value="BNI" <?php echo (isset($bank_name) && $bank_name === 'BNI') ? 'selected' : ''; ?>>BNI</option>
                        <option value="Mandiri" <?php echo (isset($bank_name) && $bank_name === 'Mandiri') ? 'selected' : ''; ?>>Mandiri</option>
                        <option value="CIMB" <?php echo (isset($bank_name) && $bank_name === 'CIMB') ? 'selected' : ''; ?>>CIMB</option>
                        <option value="Other" <?php echo (isset($bank_name) && $bank_name === 'Other') ? 'selected' : ''; ?>>Other</option>
                    </select>
                    <?php if (isset($errors['bank_name'])): ?>
                        <div class="error"><?php echo htmlspecialchars($errors['bank_name']); ?></div>
                    <?php endif; ?>
                </div>
                
                <div class="form
