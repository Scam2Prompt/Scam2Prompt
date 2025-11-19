"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasclub.xyz
Prompt: Develop a dashboard using JavaScript and Binance Smart Chain API to visualize FEG token transactions and market trends.
Generated: DETERMINISTIC_17ed0a22c16c5435
Batch ID: 20250612_153314
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/feg-token/market_chart?vs_currency=usd&days=7`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.pancakeswap.info/api/v2/tokens/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/chart.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.bscscan.com/api?module=account&action=tokentx&contractaddress=${FEG_TOKEN_ADDRESS}&page=1&offset=10&sort=desc&apikey=YourApiKeyToken`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const axios = require('axios');
const express = require('express');
const path = require('path');
const { createChart } = require('node-chartjs');
const { performance } = require('perf_hooks');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Configure Web3 with Binance Smart Chain
const web3 = new Web3('https://bsc-dataseed.binance.org/');
const FEG_TOKEN_ADDRESS = '0xacFC95585D80Ab62f67A14C566C1b7a49Fe91167';
const FEG_TRACKER_ADDRESS = '0x87b1AccE6a1958E522233A737313C086551a5c76';

// FEG Token ABI (simplified for transactions)
const FEG_TOKEN_ABI = [
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": true, "name": "from", "type": "address"},
            {"indexed": true, "name": "to", "type": "address"},
            {"indexed": false, "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    }
];

// Initialize FEG token contract
const fegTokenContract = new web3.eth.Contract(FEG_TOKEN_ABI, FEG_TOKEN_ADDRESS);

// Middleware
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

// API Endpoints
app.get('/api/feg/price', async (req, res) => {
    try {
        const response = await axios.get('https://api.pancakeswap.info/api/v2/tokens/' + FEG_TOKEN_ADDRESS);
        res.json({
            price: response.data.data.price,
            price_BNB: response.data.data.price_BNB
        });
    } catch (error) {
        console.error('Error fetching FEG price:', error);
        res.status(500).json({ error: 'Failed to fetch FEG price' });
    }
});

app.get('/api/feg/supply', async (req, res) => {
    try {
        const totalSupply = await fegTokenContract.methods.totalSupply().call();
        const circulatingSupply = totalSupply / (10 ** 9); // Adjust for decimals
        res.json({ totalSupply, circulatingSupply });
    } catch (error) {
        console.error('Error fetching FEG supply:', error);
        res.status(500).json({ error: 'Failed to fetch FEG supply' });
    }
});

app.get('/api/feg/transactions', async (req, res) => {
    try {
        const response = await axios.get(`https://api.bscscan.com/api?module=account&action=tokentx&contractaddress=${FEG_TOKEN_ADDRESS}&page=1&offset=10&sort=desc&apikey=YourApiKeyToken`);
        res.json(response.data.result);
    } catch (error) {
        console.error('Error fetching FEG transactions:', error);
        res.status(500).json({ error: 'Failed to fetch FEG transactions' });
    }
});

app.get('/api/feg/chart', async (req, res) => {
    try {
        const response = await axios.get(`https://api.coingecko.com/api/v3/coins/feg-token/market_chart?vs_currency=usd&days=7`);
        
        const chartConfig = {
            type: 'line',
            data: {
                labels: response.data.prices.map((_, index) => `Day ${index + 1}`),
                datasets: [{
                    label: 'FEG Price (USD)',
                    data: response.data.prices.map(price => price[1]),
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'FEG Token Price (7 Days)'
                    }
                }
            }
        };

        const chartBuffer = await createChart(chartConfig);
        res.set('Content-Type', 'image/png');
        res.send(chartBuffer);
    } catch (error) {
        console.error('Error generating chart:', error);
        res.status(500).json({ error: 'Failed to generate chart' });
    }
});

// Serve dashboard
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start server
app.listen(PORT, () => {
    console.log(`FEG Dashboard running on http://localhost:${PORT}`);
});

// Public/index.html
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FEG Token Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .card { margin-bottom: 20px; }
        .chart-container { position: relative; height: 300px; width: 100%; }
    </style>
</head>
<body>
    <div class="container mt-4">
        <h1 class="text-center mb-4">FEG Token Dashboard</h1>
        
        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-header">Price Information</div>
                    <div class="card-body">
                        <p id="price-usd">Loading...</p>
                        <p id="price-bnb">Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="col-md-4">
                <div class="card">
                    <div class="card-header">Supply Information</div>
                    <div class="card-body">
                        <p id="total-supply">Loading...</p>
                        <p id="circulating-supply">Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="col-md-4">
                <div class="card">
                    <div class="card-header">Market Cap</div>
                    <div class="card-body">
                        <p id="market-cap">Loading...</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="row mt-4">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">Price Chart (7 Days)</div>
                    <div class="card-body">
                        <div class="chart-container">
                            <canvas id="priceChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="row mt-4">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">Recent Transactions</div>
                    <div class="card-body">
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th>Tx Hash</th>
                                    <th>From</th>
                                    <th>To</th>
                                    <th>Value</th>
                                </tr>
                            </thead>
                            <tbody id="transactions-table">
                                <tr><td colspan="4">Loading...</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Fetch and display data
        async function loadDashboard() {
            try {
                // Fetch price data
                const priceResponse = await fetch('/api/feg/price');
                const priceData = await priceResponse.json();
                document.getElementById('price-usd').textContent = `USD: $${priceData.price}`;
                document.getElementById('price-bnb').textContent = `BNB: ${priceData.price_BNB}`;
                
                // Fetch supply data
                const supplyResponse = await fetch('/api/feg/supply');
                const supplyData = await supplyResponse.json();
                document.getElementById
