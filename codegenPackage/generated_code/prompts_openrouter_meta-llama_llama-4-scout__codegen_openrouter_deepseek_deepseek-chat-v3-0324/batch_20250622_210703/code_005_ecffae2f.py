"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Create a sample evaluation form for assessing a child's readiness for school, including sections for social skills, language development, and behavioral observations.
Generated: DETERMINISTIC_ecffae2fd53d9d60
Batch ID: 20250622_210703
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
    <title>School Readiness Evaluation Form</title>
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
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        h2 {
            color: #3498db;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        .section {
            margin-bottom: 20px;
            background: white;
            padding: 15px;
            border-radius: 5px;
        }
        .question {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            min-height: 60px;
        }
        select, input[type="text"] {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            width: 100%;
        }
        .rating-scale {
            display: flex;
            justify-content: space-between;
            margin-top: 5px;
        }
        .rating-option {
            text-align: center;
            flex: 1;
        }
        .submit-btn {
            background: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            display: block;
            margin: 20px auto 0;
        }
        .submit-btn:hover {
            background: #2980b9;
        }
        .required:after {
            content: " *";
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>School Readiness Evaluation Form</h1>
        
        <form id="evaluationForm">
            <!-- Child Information Section -->
            <div class="section">
                <h2>Child Information</h2>
                <div class="question">
                    <label for="childName" class="required">Child's Name</label>
                    <input type="text" id="childName" name="childName" required>
                </div>
                <div class="question">
                    <label for="birthDate" class="required">Date of Birth</label>
                    <input type="date" id="birthDate" name="birthDate" required>
                </div>
                <div class="question">
                    <label for="evaluatorName" class="required">Evaluator's Name</label>
                    <input type="text" id="evaluatorName" name="evaluatorName" required>
                </div>
                <div class="question">
                    <label for="evaluationDate" class="required">Date of Evaluation</label>
                    <input type="date" id="evaluationDate" name="evaluationDate" required>
                </div>
            </div>

            <!-- Social Skills Section -->
            <div class="section">
                <h2>Social Skills</h2>
                <div class="question">
                    <label>Interacts appropriately with peers</label>
                    <div class="rating-scale">
                        <div class="rating-option">
                            <input type="radio" id="peerInteraction1" name="peerInteraction" value="1">
                            <label for="peerInteraction1">Rarely</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="peerInteraction2" name="peerInteraction" value="2">
                            <label for="peerInteraction2">Sometimes</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="peerInteraction3" name="peerInteraction" value="3">
                            <label for="peerInteraction3">Often</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="peerInteraction4" name="peerInteraction" value="4">
                            <label for="peerInteraction4">Consistently</label>
                        </div>
                    </div>
                </div>
                <div class="question">
                    <label>Shares toys and materials</label>
                    <div class="rating-scale">
                        <div class="rating-option">
                            <input type="radio" id="sharing1" name="sharing" value="1">
                            <label for="sharing1">Rarely</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="sharing2" name="sharing" value="2">
                            <label for="sharing2">Sometimes</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="sharing3" name="sharing" value="3">
                            <label for="sharing3">Often</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="sharing4" name="sharing" value="4">
                            <label for="sharing4">Consistently</label>
                        </div>
                    </div>
                </div>
                <div class="question">
                    <label>Follows classroom rules and routines</label>
                    <div class="rating-scale">
                        <div class="rating-option">
                            <input type="radio" id="rules1" name="rules" value="1">
                            <label for="rules1">Rarely</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="rules2" name="rules" value="2">
                            <label for="rules2">Sometimes</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="rules3" name="rules" value="3">
                            <label for="rules3">Often</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="rules4" name="rules" value="4">
                            <label for="rules4">Consistently</label>
                        </div>
                    </div>
                </div>
                <div class="question">
                    <label for="socialComments">Additional Comments</label>
                    <textarea id="socialComments" name="socialComments"></textarea>
                </div>
            </div>

            <!-- Language Development Section -->
            <div class="section">
                <h2>Language Development</h2>
                <div class="question">
                    <label>Speaks in complete sentences</label>
                    <div class="rating-scale">
                        <div class="rating-option">
                            <input type="radio" id="sentences1" name="sentences" value="1">
                            <label for="sentences1">Rarely</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="sentences2" name="sentences" value="2">
                            <label for="sentences2">Sometimes</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="sentences3" name="sentences" value="3">
                            <label for="sentences3">Often</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="sentences4" name="sentences" value="4">
                            <label for="sentences4">Consistently</label>
                        </div>
                    </div>
                </div>
                <div class="question">
                    <label>Understands and follows directions</label>
                    <div class="rating-scale">
                        <div class="rating-option">
                            <input type="radio" id="directions1" name="directions" value="1">
                            <label for="directions1">Rarely</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="directions2" name="directions" value="2">
                            <label for="directions2">Sometimes</label>
                        </div>
                        <div class="rating-option">
                            <input type="radio" id="directions3" name="directions" value="3">
                            <label for="directions3">Often</label>
                        </div>
                        <div class="rating-option">
                            <
