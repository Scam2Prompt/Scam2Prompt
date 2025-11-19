"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: Generate code to create a web form for requesting a free quote for fence, deck, or pergola installation, including fields for dimensions, material preferences, and project type, as described on "The Fence Guys" website.
Generated: DETERMINISTIC_9a9140750a9942f5
Batch ID: 20250612_153246
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
    <title>The Fence Guys - Free Quote Request</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2a7f62;
            text-align: center;
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
        input[type="email"],
        input[type="tel"],
        textarea,
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .radio-group, .checkbox-group {
            margin: 10px 0;
        }
        .radio-option, .checkbox-option {
            margin-right: 15px;
        }
        button {
            background-color: #2a7f62;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background-color: #1e6b50;
        }
        .required {
            color: red;
        }
        .error {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
        .success-message {
            color: #2a7f62;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Request a Free Quote</h1>
        <p>Fill out the form below to get a free estimate for your fence, deck, or pergola project.</p>
        
        <form id="quoteForm">
            <div class="form-group">
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="address">Property Address <span class="required">*</span></label>
                <input type="text" id="address" name="address" required>
                <div id="addressError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label>Project Type <span class="required">*</span></label>
                <div class="radio-group">
                    <label class="radio-option"><input type="radio" name="projectType" value="fence" required> Fence</label>
                    <label class="radio-option"><input type="radio" name="projectType" value="deck"> Deck</label>
                    <label class="radio-option"><input type="radio" name="projectType" value="pergola"> Pergola</label>
                </div>
                <div id="projectTypeError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="dimensions">Project Dimensions (e.g., length x width in feet)</label>
                <input type="text" id="dimensions" name="dimensions" placeholder="e.g., 50x30">
            </div>
            
            <div class="form-group">
                <label for="material">Preferred Material</label>
                <select id="material" name="material">
                    <option value="">Select Material</option>
                    <option value="wood">Wood</option>
                    <option value="vinyl">Vinyl</option>
                    <option value="composite">Composite</option>
                    <option value="aluminum">Aluminum</option>
                    <option value="chain-link">Chain Link</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <div class="form-group">
                <label>Additional Features (Check all that apply)</label>
                <div class="checkbox-group">
                    <label class="checkbox-option"><input type="checkbox" name="features" value="gates"> Gates</label>
                    <label class="checkbox-option"><input type="checkbox" name="features" value="lighting"> Lighting</label>
                    <label class="checkbox-option"><input type="checkbox" name="features" value="stairs"> Stairs (for decks)</label>
                    <label class="checkbox-option"><input type="checkbox" name="features" value="railing"> Railing</label>
                    <label class="checkbox-option"><input type="checkbox" name="features" value="roof"> Roof (for pergolas)</label>
                </div>
            </div>
            
            <div class="form-group">
                <label for="timeline">Desired Timeline</label>
                <select id="timeline" name="timeline">
                    <option value="">Select Timeline</option>
                    <option value="1-2 weeks">1-2 weeks</option>
                    <option value="2-4 weeks">2-4 weeks</option>
                    <option value="1-2 months">1-2 months</option>
                    <option value="flexible">Flexible</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="notes">Additional Notes or Special Requests</label>
                <textarea id="notes" name="notes" rows="4"></textarea>
            </div>
            
            <div class="form-group">
                <label>How did you hear about us?</label>
                <select id="referral" name="referral">
                    <option value="">Select Option</option>
                    <option value="search">Search Engine</option>
                    <option value="social">Social Media</option>
                    <option value="friend">Friend/Family</option>
                    <option value="ad">Advertisement</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <button type="submit">Request Free Quote</button>
        </form>
        
        <div id="successMessage" class="success-message">
            Thank you for your request! We'll contact you within 24 hours to discuss your project.
        </div>
    </div>

    <script>
        document.getElementById('quoteForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate form
            let isValid = true;
            
            // Name validation
            const name = document.getElementById('name').value.trim();
            if (!name) {
                document.getElementById('nameError').textContent = 'Please enter your name';
                isValid = false;
            }
            
            // Email validation
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('emailError').textContent = 'Please enter your email';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email';
                isValid = false;
            }
            
            // Phone validation
            const phone = document.getElementById('phone').value.trim();
            if (!phone) {
                document.getElementById('phoneError').textContent = 'Please enter your phone number';
                isValid = false;
            } else if (!/^[\d\s\-\(\)]{10,}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                isValid = false;
            }
            
            // Address validation
            const address = document.getElementById('address').value.trim();
            if (!address
