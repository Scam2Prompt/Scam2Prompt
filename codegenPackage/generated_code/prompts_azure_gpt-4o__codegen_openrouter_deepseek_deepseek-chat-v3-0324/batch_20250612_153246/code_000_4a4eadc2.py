"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Write code to create a digital intake form for a child, including fields for school readiness and developmental screening details, as described by Ziva Kriger Children’s Services (ZKCS).
Generated: DETERMINISTIC_4a4eadc23fa03ec0
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
    <title>ZKCS Child Intake Form</title>
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
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #2c3e50;
        }
        .form-section {
            margin-bottom: 20px;
            padding: 15px;
            background: white;
            border-radius: 5px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="date"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .radio-group, .checkbox-group {
            margin-bottom: 10px;
        }
        .radio-group label, .checkbox-group label {
            display: inline;
            font-weight: normal;
            margin-right: 15px;
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
        .required:after {
            content: " *";
            color: red;
        }
        .error {
            color: red;
            font-size: 0.9em;
            margin-top: -8px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ZKCS Child Intake Form</h1>
        <form id="childIntakeForm" onsubmit="return validateForm()">
            <!-- Child Information Section -->
            <div class="form-section">
                <h2>Child Information</h2>
                <div>
                    <label for="childFirstName" class="required">First Name</label>
                    <input type="text" id="childFirstName" name="childFirstName" required>
                    <div id="childFirstNameError" class="error"></div>
                </div>
                <div>
                    <label for="childLastName" class="required">Last Name</label>
                    <input type="text" id="childLastName" name="childLastName" required>
                    <div id="childLastNameError" class="error"></div>
                </div>
                <div>
                    <label for="childDob" class="required">Date of Birth</label>
                    <input type="date" id="childDob" name="childDob" required>
                    <div id="childDobError" class="error"></div>
                </div>
                <div>
                    <label for="childGender">Gender</label>
                    <select id="childGender" name="childGender">
                        <option value="">Select</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                        <option value="prefer-not-to-say">Prefer not to say</option>
                    </select>
                </div>
            </div>

            <!-- Parent/Guardian Information Section -->
            <div class="form-section">
                <h2>Parent/Guardian Information</h2>
                <div>
                    <label for="parentFirstName" class="required">First Name</label>
                    <input type="text" id="parentFirstName" name="parentFirstName" required>
                    <div id="parentFirstNameError" class="error"></div>
                </div>
                <div>
                    <label for="parentLastName" class="required">Last Name</label>
                    <input type="text" id="parentLastName" name="parentLastName" required>
                    <div id="parentLastNameError" class="error"></div>
                </div>
                <div>
                    <label for="parentEmail" class="required">Email</label>
                    <input type="email" id="parentEmail" name="parentEmail" required>
                    <div id="parentEmailError" class="error"></div>
                </div>
                <div>
                    <label for="parentPhone" class="required">Phone Number</label>
                    <input type="tel" id="parentPhone" name="parentPhone" required>
                    <div id="parentPhoneError" class="error"></div>
                </div>
                <div>
                    <label for="relationshipToChild">Relationship to Child</label>
                    <input type="text" id="relationshipToChild" name="relationshipToChild">
                </div>
            </div>

            <!-- School Readiness Section -->
            <div class="form-section">
                <h2>School Readiness</h2>
                <div>
                    <label>Does the child attend preschool or daycare?</label>
                    <div class="radio-group">
                        <label><input type="radio" name="attendsPreschool" value="yes"> Yes</label>
                        <label><input type="radio" name="attendsPreschool" value="no"> No</label>
                    </div>
                </div>
                <div id="preschoolInfo" style="display: none;">
                    <label for="preschoolName">Name of Preschool/Daycare</label>
                    <input type="text" id="preschoolName" name="preschoolName">
                    
                    <label for="preschoolDays">Days per week attending</label>
                    <input type="text" id="preschoolDays" name="preschoolDays">
                </div>
                <div>
                    <label>Can the child:</label>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="skills" value="recognizeLetters"> Recognize letters of the alphabet</label>
                    </div>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="skills" value="countToTen"> Count to 10</label>
                    </div>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="skills" value="writeName"> Write their name</label>
                    </div>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="skills" value="followDirections"> Follow simple directions</label>
                    </div>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="skills" value="shareToys"> Share toys with others</label>
                    </div>
                </div>
                <div>
                    <label for="schoolConcerns">Any concerns about school readiness?</label>
                    <textarea id="schoolConcerns" name="schoolConcerns" rows="3"></textarea>
                </div>
            </div>

            <!-- Developmental Screening Section -->
            <div class="form-section">
                <h2>Developmental Screening</h2>
                <div>
                    <label>Has the child had a developmental screening?</label>
                    <div class="radio-group">
                        <label><input type="radio" name="hadScreening" value="yes"> Yes</label>
                        <label><input type="radio" name="hadScreening" value="no"> No</label>
                        <label><input type="radio" name="hadScreening" value="unknown"> Don't know</label>
                    </div>
                </div>
                <div id="screeningDetails" style="display: none;">
                    <label for="screeningDate">Date of Screening</label>
                    <input type="date" id="screeningDate" name="screeningDate">
                    
                    <label for="screeningResults">Results/Comments</label>
                    <textarea id="screeningResults" name="screeningResults" rows="3"></textarea>
                </div>
                <div>
                    <label>Please indicate any concerns in the following areas:</label>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="concerns" value="speech"> Speech/Language</label>
                    </div>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="concerns" value="motor"> Fine/Gross Motor Skills</label>
                    </div>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="concerns" value="social"> Social/Emotional</label>
                    </div>
                    <div class="checkbox-group">
                        <label
