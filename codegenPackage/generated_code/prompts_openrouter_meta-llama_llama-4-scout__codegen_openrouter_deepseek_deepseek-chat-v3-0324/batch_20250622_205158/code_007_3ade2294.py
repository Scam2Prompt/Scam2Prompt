"""
Generated Code Metadata:
========================
Original URL: https://metamaskextension.wikidot.com
Prompt: Generate an example of how to structure a Wikidot page to include a membership application form that integrates with the site's existing user management system.
Generated: DETERMINISTIC_3ade22942c98bd65
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- Wikidot Membership Application Form -->
[[module CSS]]
/* Form styling */
.membership-form {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.membership-form label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
}

.membership-form input[type="text"],
.membership-form input[type="email"],
.membership-form input[type="password"],
.membership-form textarea,
.membership-form select {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
}

.membership-form .form-group {
    margin-bottom: 20px;
}

.membership-form .submit-btn {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

.membership-form .submit-btn:hover {
    background-color: #45a049;
}

.error-message {
    color: #ff0000;
    margin-bottom: 15px;
}
[[/module]]

[[div class="membership-form"]]
    [[form action="javascript:;" id="applicationForm"]]
        [[h2]] Membership Application [[/h2]]
        
        [[div class="form-group"]]
            [[label for="username"]] Desired Username: [[/label]]
            [[input type="text" id="username" name="username" required]]
        [[/div]]
        
        [[div class="form-group"]]
            [[label for="email"]] Email Address: [[/label]]
            [[input type="email" id="email" name="email" required]]
        [[/div]]
        
        [[div class="form-group"]]
            [[label for="password"]] Password: [[/label]]
            [[input type="password" id="password" name="password" required]]
        [[/div]]
        
        [[div class="form-group"]]
            [[label for="confirm_password"]] Confirm Password: [[/label]]
            [[input type="password" id="confirm_password" name="confirm_password" required]]
        [[/div]]
        
        [[div class="form-group"]]
            [[label for="bio"]] Tell us about yourself: [[/label]]
            [[textarea id="bio" name="bio" rows="4" required]][[/textarea]]
        [[/div]]
        
        [[div class="form-group"]]
            [[label for="reason"]] Why do you want to join? [[/label]]
            [[select id="reason" name="reason" required]]
                [[option value=""]] -- Select a reason -- [[/option]]
                [[option value="community"]] To participate in the community [[/option]]
                [[option value="collaboration"]] To collaborate on projects [[/option]]
                [[option value="learning"]] To learn from others [[/option]]
                [[option value="other"]] Other [[/option]]
            [[/select]]
        [[/div]]
        
        [[div id="errorMessage" class="error-message" style="display: none;"]][[/div]]
        
        [[input type="submit" class="submit-btn" value="Submit Application"]]
    [[/form]]
[[/div]]

[[module JS]]
// Form submission handler
document.getElementById('applicationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Clear previous error messages
    document.getElementById('errorMessage').style.display = 'none';
    
    // Validate form
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    const bio = document.getElementById('bio').value.trim();
    const reason = document.getElementById('reason').value;
    
    // Simple validation
    if (password !== confirmPassword) {
        showError("Passwords do not match");
        return;
    }
    
    if (password.length < 8) {
        showError("Password must be at least 8 characters");
        return;
    }
    
    // Prepare data for Wikidot API
    const formData = {
        username: username,
        email: email,
        password: password,
        bio: bio,
        reason: reason
    };
    
    // Simulate API call (in a real implementation, this would be a Wikidot API call)
    setTimeout(() => {
        // This would be replaced with actual Wikidot API integration
        console.log("Form data:", formData);
        alert("Application submitted successfully! You'll receive an email confirmation shortly.");
        document.getElementById('applicationForm').reset();
    }, 1000);
});

function showError(message) {
    const errorElement = document.getElementById('errorMessage');
    errorElement.textContent = message;
    errorElement.style.display = 'block';
}
[[/module]]
```
