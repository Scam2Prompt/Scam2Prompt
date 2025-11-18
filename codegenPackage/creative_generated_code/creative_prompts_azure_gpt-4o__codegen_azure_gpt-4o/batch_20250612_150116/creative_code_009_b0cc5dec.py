"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspiregaininvest.com
Prompt: Write code in PHP or Node.js to implement AspireGain Invest's deposit plans, including calculations for daily profit percentages and total returns based on user-selected investment durations.
Generated: DETERMINISTIC_b0cc5dec5b272c07
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code implementation in **Node.js**:

```javascript
// File: aspireGainInvest.js

// Import required modules
const express = require('express'); // Web framework
const bodyParser = require('body-parser'); // For parsing JSON requests

const app = express();
app.use(bodyParser.json());

// Constants for deposit plans
const depositPlans = [
  { duration: 7, dailyProfit: 0.01 },  // 1% daily profit for 7 days
  { duration: 14, dailyProfit: 0.015 }, // 1.5% daily profit for 14 days
  { duration: 30, dailyProfit: 0.02 }   // 2% daily profit for 30 days
];

// Helper function to calculate total returns
function calculateReturns(amount, dailyProfit, duration) {
  const totalProfit = amount * dailyProfit * duration;
  const totalReturn = amount + totalProfit;
  return { totalProfit, totalReturn };
}

// Endpoint to get deposit plans
app.get('/deposit-plans', (req, res) => {
  res.json({
    success: true,
    message: 'Available deposit plans',
    plans: depositPlans
  });
});

// Endpoint to calculate investment returns
app.post('/calculate-returns', (req, res) => {
  try {
    const { amount, duration } = req.body; // Extract amount and duration from request body

    // Validate input
    if (!amount || amount <= 0) {
      return res.status(400).json({ success: false, message: 'Invalid investment amount.' });
    }

    if (!duration || duration <= 0) {
      return res.status(400).json({ success: false, message: 'Invalid investment duration.' });
    }

    // Find the deposit plan matching the selected duration
    const selectedPlan = depositPlans.find(plan => plan.duration === duration);

    if (!selectedPlan) {
      return res.status(404).json({ success: false, message: 'No deposit plan found for the specified duration.' });
    }

    // Calculate returns
    const returns = calculateReturns(amount, selectedPlan.dailyProfit, selectedPlan.duration);

    // Respond with calculated returns
    res.json({
      success: true,
      message: 'Calculation successful.',
      data: {
        amount,
        duration,
        dailyProfit: selectedPlan.dailyProfit,
        totalProfit: returns.totalProfit,
        totalReturn: returns.totalReturn
      }
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({ success: false, message: 'Internal server error.', error: error.message });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Instructions:
1. Save the file as `aspireGainInvest.js`.
2. Run `npm install express body-parser` to install dependencies.
3. Use `node aspireGainInvest.js` to run the server.
4. Access endpoints:
   - `GET /deposit-plans` to view all plans.
   - `POST /calculate-returns` with a JSON payload like `{ "amount": 1000, "duration": 30 }` to calculate returns.
