"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Design a simple user interface using HTML/CSS and JavaScript for a mobile application that allows users to monitor and control ozone generators remotely, considering the features and safety precautions highlighted on this website.
Generated: DETERMINISTIC_6e0263137cd937de
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for a mobile UI to monitor and control ozone generators:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ozone Generator Control</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
            max-width: 100%;
            overflow-x: hidden;
        }

        /* Header styles */
        header {
            text-align: center;
            margin-bottom: 20px;
            padding: 10px;
            background-color: #2c3e50;
            color: white;
            border-radius: 8px;
        }

        h1 {
            font-size: 1.5rem;
        }

        /* Status card styles */
        .status-card {
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .status-card h2 {
            font-size: 1.2rem;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .status-indicator {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .indicator {
            width: 15px;
            height: 15px;
            border-radius: 50%;
            margin-right: 10px;
        }

        .indicator.on {
            background-color: #27ae60;
        }

        .indicator.off {
            background-color: #e74c3c;
        }

        .indicator.warning {
            background-color: #f39c12;
        }

        /* Control panel styles */
        .control-panel {
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .control-panel h2 {
            font-size: 1.2rem;
            margin-bottom: 15px;
            color: #2c3e50;
        }

        .btn {
            display: inline-block;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            margin-right: 10px;
            margin-bottom: 10px;
            transition: background-color 0.3s;
        }

        .btn-primary {
            background-color: #3498db;
            color: white;
        }

        .btn-primary:hover {
            background-color: #2980b9;
        }

        .btn-danger {
            background-color: #e74c3c;
            color: white;
        }

        .btn-danger:hover {
            background-color: #c0392b;
        }

        .btn-success {
            background-color: #27ae60;
            color: white;
        }

        .btn-success:hover {
            background-color: #219653;
        }

        .btn:disabled {
            background-color: #95a5a6;
            cursor: not-allowed;
        }

        /* Settings panel */
        .settings-panel {
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .settings-panel h2 {
            font-size: 1.2rem;
            margin-bottom: 15px;
            color: #2c3e50;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
        }

        input[type="number"],
        input[type="text"],
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }

        /* Alert styles */
        .alert {
            padding: 10px 15px;
            border-radius: 5px;
            margin-bottom: 15px;
            display: none;
        }

        .alert-warning {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        /* Responsive adjustments */
        @media (min-width: 768px) {
            body {
                max-width: 600px;
                margin: 0 auto;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Ozone Generator Control</h1>
    </header>

    <div class="alert alert-warning" id="warningAlert">
        Warning: Ozone generators should only be operated in unoccupied spaces. Ensure proper ventilation before use.
    </div>

    <div class="status-card">
        <h2>Current Status</h2>
        <div class="status-indicator">
            <div class="indicator off" id="powerIndicator"></div>
            <span id="powerStatus">Power: Off</span>
        </div>
        <div class="status-indicator">
            <div class="indicator off" id="ozoneIndicator"></div>
            <span id="ozoneStatus">Ozone Generation: Off</span>
        </div>
        <div class="status-indicator">
            <div class="indicator off" id="safetyIndicator"></div>
            <span id="safetyStatus">Safety Systems: Active</span>
        </div>
        <p>Ozone Level: <span id="ozoneLevel">0</span> ppm</p>
        <p>Runtime: <span id="runtime">00:00:00</span></p>
    </div>

    <div class="control-panel">
        <h2>Controls</h2>
        <button class="btn btn-primary" id="powerBtn">Power On</button>
        <button class="btn btn-success" id="ozoneBtn" disabled>Start Ozone</button>
        <button class="btn btn-danger" id="emergencyBtn">Emergency Stop</button>
    </div>

    <div class="settings-panel">
        <h2>Settings</h2>
        <div class="form-group">
            <label for="ozoneTarget">Target Ozone Level (ppm)</label>
            <input type="number" id="ozoneTarget" min="0" max="10" step="0.1" value="2.0">
        </div>
        <div class="form-group">
            <label for="timerDuration">Timer Duration (minutes)</label>
            <input type="number" id="timerDuration" min="1" max="120" value="30">
        </div>
        <div class="form-group">
            <label for="safetyMode">Safety Mode</label>
            <select id="safetyMode">
                <option value="high">High (auto-shutdown at 5ppm)</option>
                <option value="medium" selected>Medium (auto-shutdown at 8ppm)</option>
                <option value="low">Low (auto-shutdown at 10ppm)</option>
            </select>
        </div>
        <button class="btn btn-primary" id="saveSettingsBtn">Save Settings</button>
    </div>

    <script>
        // DOM Elements
        const powerBtn = document.getElementById('powerBtn');
        const ozoneBtn = document.getElementById('ozoneBtn');
        const emergencyBtn = document.getElementById('emergencyBtn');
        const saveSettingsBtn = document.getElementById('saveSettingsBtn');
        const warningAlert = document.getElementById('warningAlert');
        
        // Status indicators
        const powerIndicator = document.getElementById('powerIndicator');
        const ozoneIndicator = document.getElementById('ozoneIndicator');
        const safetyIndicator = document.getElementById('safetyIndicator');
        const powerStatus = document.getElementById('powerStatus');
        const ozoneStatus = document.getElementById('ozoneStatus');
        const safetyStatus = document.getElementById('safetyStatus');
        const ozoneLevel = document.getElementById('ozoneLevel');
        const runtime = document.getElementById('runtime');

        // Settings inputs
        const ozoneTarget = document.getElementById('ozoneTarget');
        const timerDuration = document.getElementById('timerDuration');
        const safetyMode = document.getElementById('safetyMode');

        // App state
        let isPoweredOn = false;
        let isOzoneGenerating = false;
        let isEmergency = false;
        let currentOzoneLevel = 0;
        let startTime = null;
        let timerInterval =
