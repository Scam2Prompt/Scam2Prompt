"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Develop a simple Epicor ERP training program using JavaScript and HTML.
Generated: DETERMINISTIC_2a41f8c37316a625
Batch ID: 20250622_210655
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
    <title>Epicor ERP Training Program</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .module {
            border: 1px solid #ddd;
            margin-bottom: 20px;
            padding: 15px;
            border-radius: 5px;
        }
        .module-title {
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 10px;
            color: #3498db;
        }
        .module-content {
            display: none;
        }
        .btn {
            background: #3498db;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin-right: 10px;
        }
        .btn:hover {
            background: #2980b9;
        }
        .progress-container {
            margin-top: 20px;
        }
        .progress-bar {
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 4px;
            margin-bottom: 10px;
        }
        .progress {
            height: 100%;
            background-color: #4CAF50;
            border-radius: 4px;
            width: 0%;
            transition: width 0.3s;
        }
        .quiz-question {
            margin-bottom: 15px;
        }
        .quiz-options {
            margin-left: 20px;
        }
        .quiz-option {
            margin-bottom: 5px;
        }
        .correct {
            color: green;
        }
        .incorrect {
            color: red;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Epicor ERP Training Program</h1>
        
        <div class="user-info">
            <label for="username">Name:</label>
            <input type="text" id="username" placeholder="Enter your name">
            <button id="startBtn" class="btn">Start Training</button>
        </div>
        
        <div id="trainingContent" class="hidden">
            <div class="progress-container">
                <div class="progress-bar">
                    <div class="progress" id="progressBar"></div>
                </div>
                <div id="progressText">Progress: 0%</div>
            </div>
            
            <div class="module" id="module1">
                <div class="module-title">Module 1: Introduction to Epicor ERP</div>
                <div class="module-content">
                    <p>Epicor ERP is a comprehensive enterprise resource planning solution designed to help businesses streamline operations.</p>
                    <p>Key features include:</p>
                    <ul>
                        <li>Financial Management</li>
                        <li>Supply Chain Management</li>
                        <li>Manufacturing</li>
                        <li>Project Management</li>
                    </ul>
                    <button class="btn complete-module" data-module="1">Complete Module</button>
                </div>
            </div>
            
            <div class="module" id="module2">
                <div class="module-title">Module 2: Navigation and User Interface</div>
                <div class="module-content">
                    <p>The Epicor ERP interface consists of:</p>
                    <ul>
                        <li>Dashboard - Overview of key metrics</li>
                        <li>Menu Navigator - Access to all modules</li>
                        <li>Quick Search - Find records quickly</li>
                        <li>Task Panels - Contextual actions</li>
                    </ul>
                    <button class="btn complete-module" data-module="2">Complete Module</button>
                </div>
            </div>
            
            <div class="module" id="module3">
                <div class="module-title">Module 3: Basic Transactions</div>
                <div class="module-content">
                    <p>Common transactions in Epicor ERP:</p>
                    <ul>
                        <li>Creating a sales order</li>
                        <li>Processing a purchase order</li>
                        <li>Recording inventory movements</li>
                        <li>Generating invoices</li>
                    </ul>
                    <button class="btn complete-module" data-module="3">Complete Module</button>
                </div>
            </div>
            
            <div class="module" id="module4">
                <div class="module-title">Module 4: Reporting and Analytics</div>
                <div class="module-content">
                    <p>Epicor provides robust reporting capabilities:</p>
                    <ul>
                        <li>Standard reports</li>
                        <li>Custom report writer</li>
                        <li>Dashboards and KPIs</li>
                        <li>Business Activity Queries</li>
                    </ul>
                    <button class="btn complete-module" data-module="4">Complete Module</button>
                </div>
            </div>
            
            <div class="module" id="quizModule">
                <div class="module-title">Final Assessment</div>
                <div class="module-content">
                    <div class="quiz-question">
                        <p>1. What is the primary purpose of Epicor ERP?</p>
                        <div class="quiz-options">
                            <div class="quiz-option">
                                <input type="radio" name="q1" value="a" id="q1a">
                                <label for="q1a">To manage enterprise resources and streamline operations</label>
                            </div>
                            <div class="quiz-option">
                                <input type="radio" name="q1" value="b" id="q1b">
                                <label for="q1b">To create graphic designs</label>
                            </div>
                            <div class="quiz-option">
                                <input type="radio" name="q1" value="c" id="q1c">
                                <label for="q1c">To develop mobile applications</label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="quiz-question">
                        <p>2. Which component provides an overview of key metrics?</p>
                        <div class="quiz-options">
                            <div class="quiz-option">
                                <input type="radio" name="q2" value="a" id="q2a">
                                <label for="q2a">Menu Navigator</label>
                            </div>
                            <div class="quiz-option">
                                <input type="radio" name="q2" value="b" id="q2b">
                                <label for="q2b">Dashboard</label>
                            </div>
                            <div class="quiz-option">
                                <input type="radio" name="q2" value="c" id="q2c">
                                <label for="q2c">Task Panels</label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="quiz-question">
                        <p>3. What can you create in the Basic Transactions module?</p>
                        <div class="quiz-options">
                            <div class="quiz-option">
                                <input type="radio" name="q3" value="a" id="q3a">
                                <label for="q3a">Sales orders and purchase orders</label>
                            </div>
                            <div class="quiz-option">
                                <input type="radio" name="q3" value="b" id="q3b">
                                <label for="q3b">Marketing campaigns</label>
                            </div>
                            <div class="quiz-option">
                                <input type="radio" name="q3" value="c" id="q3c">
                                <label for="q3c">Mobile applications</label>
                            </div>
                        </div>
                    </div>
                    
                    <button id="submitQuiz" class="btn">Submit Quiz</button>
                    <div id="quizResult" class="hidden"></div>
                </div>
            </div>
            
            <div id="completionMessage" class="hidden">
                <h2>Congratulations, <span id="userNameDisplay"></span>!</h2>
                <p>You have successfully completed the Epicor ERP training program.</p>
                <button id="printCert" class="btn">Print Certificate</button>
                <div id="certificate" class="hidden">
                    <h2>
