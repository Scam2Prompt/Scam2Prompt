"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocats.com
Prompt: Generate a sample intake form for a family law client, including fields for personal and case information, using HTML and CSS, inspired by the layout and content of the Majeli Avocat website.
Generated: DETERMINISTIC_c1a9f1c7f2e4295f
Batch ID: 20250622_205537
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
    <title>Family Law Client Intake Form</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        
        h1, h2 {
            color: #2c3e50;
            margin-bottom: 20px;
        }
        
        h1 {
            font-size: 28px;
            border-bottom: 2px solid #eaeaea;
            padding-bottom: 10px;
        }
        
        h2 {
            font-size: 20px;
            margin-top: 30px;
            color: #3498db;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }
        
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        input[type="date"],
        select,
        textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input:focus,
        select:focus,
        textarea:focus {
            border-color: #3498db;
            outline: none;
        }
        
        textarea {
            min-height: 100px;
            resize: vertical;
        }
        
        .form-row {
            display: flex;
            gap: 20px;
        }
        
        .form-row .form-group {
            flex: 1;
        }
        
        .required-field::after {
            content: " *";
            color: #e74c3c;
        }
        
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #2980b9;
        }
        
        .section {
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
        
        .section:last-child {
            border-bottom: none;
        }
        
        @media (max-width: 600px) {
            .form-row {
                flex-direction: column;
                gap: 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Family Law Client Intake Form</h1>
        <p>Please complete this form to help us understand your legal needs. All information will be kept confidential.</p>
        
        <form id="clientIntakeForm">
            <!-- Personal Information Section -->
            <div class="section">
                <h2>Personal Information</h2>
                
                <div class="form-row">
                    <div class="form-group">
                        <label for="firstName" class="required-field">First Name</label>
                        <input type="text" id="firstName" name="firstName" required>
                    </div>
                    <div class="form-group">
                        <label for="lastName" class="required-field">Last Name</label>
                        <input type="text" id="lastName" name="lastName" required>
                    </div>
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label for="email" class="required-field">Email</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="phone" class="required-field">Phone Number</label>
                        <input type="tel" id="phone" name="phone" required>
                    </div>
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label for="dob">Date of Birth</label>
                        <input type="date" id="dob" name="dob">
                    </div>
                    <div class="form-group">
                        <label for="ssn">Social Security Number (Last 4 digits)</label>
                        <input type="text" id="ssn" name="ssn" maxlength="4" pattern="\d{4}">
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="address">Street Address</label>
                    <input type="text" id="address" name="address">
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label for="city">City</label>
                        <input type="text" id="city" name="city">
                    </div>
                    <div class="form-group">
                        <label for="state">State</label>
                        <input type="text" id="state" name="state">
                    </div>
                    <div class="form-group">
                        <label for="zip">ZIP Code</label>
                        <input type="text" id="zip" name="zip">
                    </div>
                </div>
            </div>
            
            <!-- Case Information Section -->
            <div class="section">
                <h2>Case Information</h2>
                
                <div class="form-group">
                    <label for="caseType" class="required-field">Type of Case</label>
                    <select id="caseType" name="caseType" required>
                        <option value="">Select an option</option>
                        <option value="divorce">Divorce</option>
                        <option value="child_custody">Child Custody</option>
                        <option value="child_support">Child Support</option>
                        <option value="spousal_support">Spousal Support</option>
                        <option value="adoption">Adoption</option>
                        <option value="paternity">Paternity</option>
                        <option value="domestic_violence">Domestic Violence</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                
                <div class="form-group" id="otherCaseTypeContainer" style="display: none;">
                    <label for="otherCaseType">Please specify</label>
                    <input type="text" id="otherCaseType" name="otherCaseType">
                </div>
                
                <div class="form-group">
                    <label for="opposingParty">Name of Opposing Party (if known)</label>
                    <input type="text" id="opposingParty" name="opposingParty">
                </div>
                
                <div class="form-group">
                    <label for="caseStatus">Current Status of Your Case</label>
                    <select id="caseStatus" name="caseStatus">
                        <option value="">Select an option</option>
                        <option value="not_filed">Not yet filed</option>
                        <option value="pending">Pending</option>
                        <option value="active">Active litigation</option>
                        <option value="appeal">Appeal</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="previousAttorney">Have you consulted with or hired another attorney for this matter?</label>
                    <select id="previousAttorney" name="previousAttorney">
                        <option value="">Select an option</option>
                        <option value="no">No</option>
                        <option value="consulted">Consulted with another attorney</option>
                        <option value="hired">Hired another attorney</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="caseDescription" class="required-field">Brief Description of Your Legal Issue</label>
                    <textarea id="caseDescription" name="caseDescription" required></textarea>
                </div>
            </div>
            
            <!-- Additional Information Section -->
            <div class="section">
                <h2>Additional Information</h2>
                
                <div class="form-group">
                    <label for="children">Number of Children Involved</label>
                    <input type="text" id="children" name="children" inputmode="numeric" pattern="\d*">
                </div>
                
                <div class="form-group">
                    <label
