"""
Generated Code Metadata:
========================
Original URL: https://binance-stake.vercel.app
Prompt: Create a web-based APR calculator using HTML, CSS, and JavaScript that mimics the functionality of the Binance Stake APR Calculator.
Generated: DETERMINISTIC_7403be6aee0007a5
Batch ID: 20250612_150946
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
    <title>APR Calculator</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .calculator-container {
            background-color: white;
            border-radius: 8px;
            padding: 25px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        
        input[type="number"], select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }
        
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #2980b9;
        }
        
        .results {
            margin-top: 30px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 8px;
            display: none;
        }
        
        .result-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }
        
        .result-item:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        
        .result-label {
            font-weight: bold;
        }
        
        .result-value {
            color: #2c3e50;
        }
        
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="calculator-container">
        <h1>APR Calculator</h1>
        
        <div class="form-group">
            <label for="principal">Principal Amount ($)</label>
            <input type="number" id="principal" min="0" step="0.01" placeholder="Enter amount">
            <div id="principal-error" class="error">Please enter a valid amount</div>
        </div>
        
        <div class="form-group">
            <label for="apr">APR (%)</label>
            <input type="number" id="apr" min="0" step="0.01" placeholder="Enter APR">
            <div id="apr-error" class="error">Please enter a valid APR</div>
        </div>
        
        <div class="form-group">
            <label for="duration">Duration (Days)</label>
            <input type="number" id="duration" min="1" placeholder="Enter duration">
            <div id="duration-error" class="error">Please enter a valid duration</div>
        </div>
        
        <div class="form-group">
            <label for="compounding">Compounding Frequency</label>
            <select id="compounding">
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
            </select>
        </div>
        
        <button id="calculate-btn">Calculate</button>
        
        <div id="results" class="results">
            <h2>Results</h2>
            <div class="result-item">
                <span class="result-label">Principal:</span>
                <span id="result-principal" class="result-value">$0.00</span>
            </div>
            <div class="result-item">
                <span class="result-label">APR:</span>
                <span id="result-apr" class="result-value">0.00%</span>
            </div>
            <div class="result-item">
                <span class="result-label">Duration:</span>
                <span id="result-duration" class="result-value">0 days</span>
            </div>
            <div class="result-item">
                <span class="result-label">Compounding:</span>
                <span id="result-compounding" class="result-value">Daily</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Interest:</span>
                <span id="result-interest" class="result-value">$0.00</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Value:</span>
                <span id="result-total" class="result-value">$0.00</span>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const calculateBtn = document.getElementById('calculate-btn');
            const principalInput = document.getElementById('principal');
            const aprInput = document.getElementById('apr');
            const durationInput = document.getElementById('duration');
            const compoundingSelect = document.getElementById('compounding');
            const resultsDiv = document.getElementById('results');
            
            // Error elements
            const principalError = document.getElementById('principal-error');
            const aprError = document.getElementById('apr-error');
            const durationError = document.getElementById('duration-error');
            
            calculateBtn.addEventListener('click', calculateAPR);
            
            function calculateAPR() {
                // Reset errors
                principalError.style.display = 'none';
                aprError.style.display = 'none';
                durationError.style.display = 'none';
                
                // Validate inputs
                let isValid = true;
                
                const principal = parseFloat(principalInput.value);
                if (isNaN(principal) || principal <= 0) {
                    principalError.style.display = 'block';
                    isValid = false;
                }
                
                const apr = parseFloat(aprInput.value);
                if (isNaN(apr) || apr <= 0) {
                    aprError.style.display = 'block';
                    isValid = false;
                }
                
                const duration = parseInt(durationInput.value);
                if (isNaN(duration) || duration <= 0) {
                    durationError.style.display = 'block';
                    isValid = false;
                }
                
                if (!isValid) {
                    return;
                }
                
                const compounding = compoundingSelect.value;
                
                // Calculate results
                const result = calculateCompoundInterest(principal, apr, duration, compounding);
                
                // Display results
                document.getElementById('result-principal').textContent = `$${principal.toFixed(2)}`;
                document.getElementById('result-apr').textContent = `${apr.toFixed(2)}%`;
                document.getElementById('result-duration').textContent = `${duration} days`;
                document.getElementById('result-compounding').textContent = 
                    compounding.charAt(0).toUpperCase() + compounding.slice(1);
                document.getElementById('result-interest').textContent = `$${result.interest.toFixed(2)}`;
                document.getElementById('result-total').textContent = `$${result.total.toFixed(2)}`;
                
                resultsDiv.style.display = 'block';
            }
            
            function calculateCompoundInterest(principal, apr, durationDays, compounding) {
                const aprDecimal = apr / 100;
                let periodsPerYear, n;
                
                switch (compounding) {
                    case 'daily':
                        periodsPerYear = 365;
                        break;
                    case 'weekly':
                        periodsPerYear = 52;
                        break;
                    case 'monthly':
                        periodsPerYear = 12;
                        break;
                    case 'yearly':
                        periodsPerYear = 1;
                        break;
                    default:
                        periodsPerYear = 365;
                }
                
                const years = durationDays / 365;
                n = periodsPerYear * years;
                const ratePerPeriod = aprDecimal / periodsPerYear;
                
                const total = principal * Math.pow(1 + ratePerPeriod, n);
                const interest = total - principal;
                
                return {
                    total: total,
                    interest: interest
                };
            }
            
            // Allow form submission on Enter key
            document.querySelectorAll('input').forEach(input => {
                input.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        calculateAPR();
                    }
                });
            });
        });
    </script>
</body>
</html>
```
