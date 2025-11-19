"""
Generated Code Metadata:
========================
Original URL: https://1xfa.club
Prompt: Generate a simple sports betting odds calculator using JavaScript, inspired by BaxBet's sports betting section.
Generated: DETERMINISTIC_7d25fb543317b814
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sports Betting Odds Calculator
 * 
 * This script provides functionality to calculate potential winnings based on:
 * - Stake amount
 * - Odds format (Decimal, Fractional, American)
 * - Odds value
 * 
 * It supports conversion between different odds formats and calculates potential returns.
 */

class OddsCalculator {
    /**
     * Constructor for OddsCalculator
     * @param {string} oddsFormat - The format of the odds ('decimal', 'fractional', 'american')
     * @param {number} oddsValue - The value of the odds
     * @param {number} stake - The amount being wagered
     */
    constructor(oddsFormat, oddsValue, stake) {
        this.oddsFormat = oddsFormat.toLowerCase();
        this.oddsValue = oddsValue;
        this.stake = stake;
        this.validateInputs();
    }

    /**
     * Validates constructor inputs
     * @throws {Error} If inputs are invalid
     */
    validateInputs() {
        if (isNaN(this.oddsValue) || isNaN(this.stake)) {
            throw new Error('Odds value and stake must be numbers');
        }

        if (this.stake <= 0) {
            throw new Error('Stake must be greater than 0');
        }

        const validFormats = ['decimal', 'fractional', 'american'];
        if (!validFormats.includes(this.oddsFormat)) {
            throw new Error('Invalid odds format. Use: decimal, fractional, or american');
        }

        if (this.oddsFormat === 'fractional') {
            const parts = this.oddsValue.split('/');
            if (parts.length !== 2 || isNaN(parts[0]) || isNaN(parts[1])) {
                throw new Error('Fractional odds must be in format "X/Y"');
            }
        }
    }

    /**
     * Converts odds to decimal format
     * @returns {number} Decimal odds
     */
    toDecimal() {
        switch (this.oddsFormat) {
            case 'decimal':
                return parseFloat(this.oddsValue);
            case 'fractional':
                const [numerator, denominator] = this.oddsValue.split('/').map(Number);
                return numerator / denominator + 1;
            case 'american':
                const american = parseFloat(this.oddsValue);
                return american > 0 ? american / 100 + 1 : 100 / Math.abs(american) + 1;
            default:
                throw new Error('Unsupported odds format');
        }
    }

    /**
     * Converts odds to fractional format
     * @returns {string} Fractional odds
     */
    toFractional() {
        const decimal = this.toDecimal();
        const numerator = decimal - 1;
        
        // Find approximate fraction
        const tolerance = 1.0E-6;
        let h1 = 1, h2 = 0;
        let k1 = 0, k2 = 1;
        let b = numerator;
        do {
            const a = Math.floor(b);
            let aux = h1;
            h1 = a * h1 + h2;
            h2 = aux;
            aux = k1;
            k1 = a * k1 + k2;
            k2 = aux;
            b = 1 / (b - a);
        } while (Math.abs(numerator - h1 / k1) > numerator * tolerance);

        return `${h1}/${k1}`;
    }

    /**
     * Converts odds to American format
     * @returns {string} American odds
     */
    toAmerican() {
        const decimal = this.toDecimal();
        if (decimal >= 2) {
            return `+${Math.round((decimal - 1) * 100)}`;
        } else {
            return `-${Math.round(100 / (decimal - 1))}`;
        }
    }

    /**
     * Calculates potential winnings
     * @returns {object} Returns an object with potential returns and profit
     */
    calculateWinnings() {
        const decimalOdds = this.toDecimal();
        const returns = this.stake * decimalOdds;
        const profit = returns - this.stake;

        return {
            stake: this.stake,
            returns: parseFloat(returns.toFixed(2)),
            profit: parseFloat(profit.toFixed(2)),
            decimalOdds: parseFloat(decimalOdds.toFixed(2)),
            fractionalOdds: this.toFractional(),
            americanOdds: this.toAmerican()
        };
    }
}

// Example usage and UI interaction
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('odds-calculator-form');
    const resultsDiv = document.getElementById('results');

    if (form && resultsDiv) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            try {
                const formData = new FormData(form);
                const oddsFormat = formData.get('odds-format');
                const oddsValue = formData.get('odds-value');
                const stake = parseFloat(formData.get('stake'));

                const calculator = new OddsCalculator(oddsFormat, oddsValue, stake);
                const results = calculator.calculateWinnings();

                resultsDiv.innerHTML = `
                    <h3>Betting Results</h3>
                    <p><strong>Stake:</strong> $${results.stake.toFixed(2)}</p>
                    <p><strong>Decimal Odds:</strong> ${results.decimalOdds}</p>
                    <p><strong>Fractional Odds:</strong> ${results.fractionalOdds}</p>
                    <p><strong>American Odds:</strong> ${results.americanOdds}</p>
                    <p><strong>Potential Returns:</strong> $${results.returns.toFixed(2)}</p>
                    <p><strong>Potential Profit:</strong> $${results.profit.toFixed(2)}</p>
                `;
            } catch (error) {
                resultsDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
            }
        });
    }
});
```

HTML template to use with this code:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports Betting Odds Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        form {
            display: grid;
            gap: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        #results {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Sports Betting Odds Calculator</h1>
    <form id="odds-calculator-form">
        <div>
            <label for="odds-format">Odds Format:</label>
            <select id="odds-format" name="odds-format" required>
                <option value="decimal">Decimal</option>
                <option value="fractional">Fractional</option>
                <option value="american">American</option>
            </select>
        </div>
        <div>
            <label for="odds-value">Odds Value:</label>
            <input type="text" id="odds-value" name="odds-value" required placeholder="e.g., 2.5, 5/2, or +150">
        </div>
        <div>
            <label for="stake">Stake Amount ($):</label>
            <input type="number" id="stake" name="stake" min="0.01" step="0.01" required>
        </div>
        <button type="submit">Calculate</button>
    </form>
    <div id="results"></div>
    <script src="odds-calculator.js"></script>
</body>
</html>
```
