"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: "Create a simple electrical engineering calculator using JavaScript, incorporating formulas for energy efficiency and electrical design."
Generated: DETERMINISTIC_bcaa789c571c2df0
Batch ID: 20250622_210856
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
    <title>Electrical Engineering Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .calculator {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
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
        input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #e9f7ef;
            border-radius: 4px;
            display: none;
        }
        .tabs {
            display: flex;
            margin-bottom: 20px;
        }
        .tab {
            padding: 10px 20px;
            cursor: pointer;
            background-color: #ddd;
            margin-right: 5px;
            border-radius: 4px 4px 0 0;
        }
        .tab.active {
            background-color: white;
            font-weight: bold;
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>Electrical Engineering Calculator</h1>
        
        <div class="tabs">
            <div class="tab active" onclick="openTab(event, 'power')">Power</div>
            <div class="tab" onclick="openTab(event, 'energy')">Energy Efficiency</div>
            <div class="tab" onclick="openTab(event, 'resistance')">Resistance</div>
            <div class="tab" onclick="openTab(event, 'voltageDrop')">Voltage Drop</div>
        </div>
        
        <!-- Power Calculator -->
        <div id="power" class="tab-content active">
            <div class="form-group">
                <label for="voltage">Voltage (V):</label>
                <input type="number" id="voltage" step="any" placeholder="Enter voltage in volts">
                <div class="error" id="voltage-error"></div>
            </div>
            <div class="form-group">
                <label for="current">Current (A):</label>
                <input type="number" id="current" step="any" placeholder="Enter current in amperes">
                <div class="error" id="current-error"></div>
            </div>
            <button onclick="calculatePower()">Calculate Power</button>
            <div class="result" id="power-result">
                <strong>Result:</strong> Power = <span id="power-value"></span> Watts
            </div>
        </div>
        
        <!-- Energy Efficiency Calculator -->
        <div id="energy" class="tab-content">
            <div class="form-group">
                <label for="inputPower">Input Power (W):</label>
                <input type="number" id="inputPower" step="any" placeholder="Enter input power in watts">
                <div class="error" id="inputPower-error"></div>
            </div>
            <div class="form-group">
                <label for="outputPower">Output Power (W):</label>
                <input type="number" id="outputPower" step="any" placeholder="Enter output power in watts">
                <div class="error" id="outputPower-error"></div>
            </div>
            <button onclick="calculateEnergyEfficiency()">Calculate Efficiency</button>
            <div class="result" id="energy-result">
                <strong>Result:</strong> Efficiency = <span id="energy-value"></span>%
            </div>
        </div>
        
        <!-- Resistance Calculator -->
        <div id="resistance" class="tab-content">
            <div class="form-group">
                <label for="resistivity">Resistivity (Ω·m):</label>
                <input type="number" id="resistivity" step="any" placeholder="Enter resistivity in ohm-meters">
                <div class="error" id="resistivity-error"></div>
            </div>
            <div class="form-group">
                <label for="length">Length (m):</label>
                <input type="number" id="length" step="any" placeholder="Enter length in meters">
                <div class="error" id="length-error"></div>
            </div>
            <div class="form-group">
                <label for="area">Cross-sectional Area (m²):</label>
                <input type="number" id="area" step="any" placeholder="Enter area in square meters">
                <div class="error" id="area-error"></div>
            </div>
            <button onclick="calculateResistance()">Calculate Resistance</button>
            <div class="result" id="resistance-result">
                <strong>Result:</strong> Resistance = <span id="resistance-value"></span> Ω
            </div>
        </div>
        
        <!-- Voltage Drop Calculator -->
        <div id="voltageDrop" class="tab-content">
            <div class="form-group">
                <label for="currentDrop">Current (A):</label>
                <input type="number" id="currentDrop" step="any" placeholder="Enter current in amperes">
                <div class="error" id="currentDrop-error"></div>
            </div>
            <div class="form-group">
                <label for="resistanceDrop">Resistance (Ω):</label>
                <input type="number" id="resistanceDrop" step="any" placeholder="Enter resistance in ohms">
                <div class="error" id="resistanceDrop-error"></div>
            </div>
            <button onclick="calculateVoltageDrop()">Calculate Voltage Drop</button>
            <div class="result" id="voltageDrop-result">
                <strong>Result:</strong> Voltage Drop = <span id="voltageDrop-value"></span> V
            </div>
        </div>
    </div>

    <script>
        // Tab navigation function
        function openTab(evt, tabName) {
            const tabContents = document.getElementsByClassName("tab-content");
            for (let i = 0; i < tabContents.length; i++) {
                tabContents[i].classList.remove("active");
            }
            
            const tabs = document.getElementsByClassName("tab");
            for (let i = 0; i < tabs.length; i++) {
                tabs[i].classList.remove("active");
            }
            
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.classList.add("active");
        }
        
        // Validate input is a positive number
        function validateInput(inputId, errorId) {
            const input = document.getElementById(inputId);
            const error = document.getElementById(errorId);
            const value = parseFloat(input.value);
            
            if (isNaN(value) || value < 0) {
                error.textContent = "Please enter a valid positive number";
                error.style.display = "block";
                return false;
            } else {
                error.style.display = "none";
                return true;
            }
        }
        
        // Power calculation: P = V * I
        function calculatePower() {
            const isValidVoltage = validateInput("voltage", "voltage-error");
            const isValidCurrent = validateInput("current", "current-error");
            
            if (!isValidVoltage || !isValidCurrent) return;
            
            const voltage = parseFloat(document.getElementById("voltage").value);
            const current = parseFloat(document.getElementById("current").value);
            const power = voltage * current;
            
            document.getElementById("power-value").textContent = power.toFixed(2);
            document.getElementById("power-result").style.display = "block";
        }
        
        // Energy efficiency calculation: η = (P_out / P_in) * 100
        function calculateEnergyEfficiency() {
            const isValidInputPower = validateInput("inputPower", "inputPower-error");
            const isValidOutputPower
