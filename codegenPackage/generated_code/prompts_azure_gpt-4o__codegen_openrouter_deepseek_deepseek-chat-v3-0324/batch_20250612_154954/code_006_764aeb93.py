"""
Generated Code Metadata:
========================
Original URL: https://convex-finance.github.io
Prompt: Develop a dashboard using JavaScript and Web3.js to visualize the boosted CRV rewards and CVX token earnings for a user staking Curve LP tokens on Convex Finance.
Generated: DETERMINISTIC_764aeb9305cb49fb
Batch ID: 20250612_154954
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/web3@1.5.2/dist/web3.min.js": {
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
// Dashboard for visualizing boosted CRV rewards and CVX earnings from Convex Finance
// Requires Web3.js and a modern browser with MetaMask or similar Web3 provider

// Import required libraries (assuming this is running in a browser environment)
// <script src="https://cdn.jsdelivr.net/npm/web3@1.5.2/dist/web3.min.js"></script>
// <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>

// Main Dashboard Class
class ConvexRewardsDashboard {
    constructor() {
        this.web3 = null;
        this.userAddress = null;
        this.contracts = {
            curveLPToken: '0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490', // 3pool LP token example
            convexBooster: '0xF403C135812408BFbE8713b5A23a04b3D48AAE31',
            convexRewards: '0xCF50b810E57Ac33B91dCF525C6ddd9881B139332',
            crvToken: '0xD533a949740bb3306d119CC777fa900bA034cd52',
            cvxToken: '0x4e3FBD56CD56c3e72c1403e103b45Db9da5B9D2B'
        };
        this.abis = {
            booster: require('./abis/convexBooster.json'), // Replace with actual ABI
            rewards: require('./abis/convexRewards.json'), // Replace with actual ABI
            erc20: require('./abis/erc20.json') // Standard ERC20 ABI
        };
        this.data = {
            crvRewards: 0,
            cvxEarnings: 0,
            historicalData: []
        };
        this.charts = {};
    }

    // Initialize the dashboard
    async init() {
        try {
            // Check if Web3 is injected
            if (window.ethereum) {
                this.web3 = new Web3(window.ethereum);
                await window.ethereum.enable();
                this.userAddress = (await this.web3.eth.getAccounts())[0];
                console.log('Connected with address:', this.userAddress);
            } else {
                throw new Error('No Web3 provider detected. Please install MetaMask.');
            }

            // Initialize contracts
            this.initContracts();
            
            // Load data
            await this.loadData();
            
            // Render dashboard
            this.renderDashboard();
            
            // Set up periodic refresh
            setInterval(() => this.loadData(), 300000); // Refresh every 5 minutes
            
        } catch (error) {
            console.error('Initialization error:', error);
            this.showError(error.message);
        }
    }

    // Initialize contract instances
    initContracts() {
        this.contractInstances = {
            booster: new this.web3.eth.Contract(this.abis.booster, this.contracts.convexBooster),
            rewards: new this.web3.eth.Contract(this.abis.rewards, this.contracts.convexRewards),
            crvToken: new this.web3.eth.Contract(this.abis.erc20, this.contracts.crvToken),
            cvxToken: new this.web3.eth.Contract(this.abis.erc20, this.contracts.cvxToken),
            lpToken: new this.web3.eth.Contract(this.abis.erc20, this.contracts.curveLPToken)
        };
    }

    // Load all required data
    async loadData() {
        try {
            // Get current CRV rewards
            const crvRewards = await this.contractInstances.rewards.methods
                .earned(this.userAddress)
                .call();
            this.data.crvRewards = this.web3.utils.fromWei(crvRewards, 'ether');
            
            // Get CVX earnings (approximation based on CRV rewards)
            // Note: Actual CVX calculation might be more complex
            this.data.cvxEarnings = this.calculateCVXEarnings(this.data.crvRewards);
            
            // Get historical data (simplified - in production would query subgraph or API)
            this.updateHistoricalData();
            
            // Update UI
            this.updateUI();
            
        } catch (error) {
            console.error('Error loading data:', error);
            this.showError('Failed to load data. Please try again.');
        }
    }

    // Calculate CVX earnings based on CRV rewards
    calculateCVXEarnings(crvRewards) {
        // Simplified calculation - in reality this would involve:
        // 1. The current CVX minting ratio
        // 2. Any lockup periods or vesting
        // 3. User's veCRV balance for boost
        return crvRewards * 0.5; // Example ratio
    }

    // Update historical data array
    updateHistoricalData() {
        const now = new Date();
        this.data.historicalData.push({
            timestamp: now,
            crvRewards: this.data.crvRewards,
            cvxEarnings: this.data.cvxEarnings
        });
        
        // Keep only last 30 days of data
        if (this.data.historicalData.length > 30) {
            this.data.historicalData.shift();
        }
    }

    // Render the dashboard UI
    renderDashboard() {
        // Create main container
        const container = document.createElement('div');
        container.className = 'convex-dashboard';
        document.body.appendChild(container);
        
        // Header
        const header = document.createElement('h1');
        header.textContent = 'Convex Finance Rewards Dashboard';
        container.appendChild(header);
        
        // Address display
        const addressDisplay = document.createElement('div');
        addressDisplay.className = 'address';
        addressDisplay.textContent = `Connected: ${this.userAddress.substring(0, 6)}...${this.userAddress.substring(38)}`;
        container.appendChild(addressDisplay);
        
        // Stats container
        const statsContainer = document.createElement('div');
        statsContainer.className = 'stats-container';
        container.appendChild(statsContainer);
        
        // CRV rewards card
        const crvCard = this.createStatCard('CRV Rewards', this.data.crvRewards, 'CRV');
        statsContainer.appendChild(crvCard);
        
        // CVX earnings card
        const cvxCard = this.createStatCard('CVX Earnings', this.data.cvxEarnings, 'CVX');
        statsContainer.appendChild(cvxCard);
        
        // Charts container
        const chartsContainer = document.createElement('div');
        chartsContainer.className = 'charts-container';
        container.appendChild(chartsContainer);
        
        // Create charts
        this.createCRVRewardsChart(chartsContainer);
        this.createCVXEarningsChart(chartsContainer);
        
        // Error container (hidden by default)
        this.errorContainer = document.createElement('div');
        this.errorContainer.className = 'error-container hidden';
        container.appendChild(this.errorContainer);
    }

    // Create a stat card element
    createStatCard(title, value, unit) {
        const card = document.createElement('div');
        card.className = 'stat-card';
        
        const titleEl = document.createElement('h3');
        titleEl.textContent = title;
        card.appendChild(titleEl);
        
        const valueEl = document.createElement('div');
        valueEl.className = 'value';
        valueEl.textContent = Number(value).toFixed(4);
        card.appendChild(valueEl);
        
        const unitEl = document.createElement('div');
        unitEl.className = 'unit';
        unitEl.textContent = unit;
        card.appendChild(unitEl);
        
        return card;
    }

    // Create CRV rewards chart
    createCRVRewardsChart(container) {
        const chartContainer = document.createElement('div');
        chartContainer.className = 'chart-container';
        container.appendChild(chartContainer);
        
        const canvas = document.createElement('canvas');
        chartContainer.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        this.charts.crvRewards = new Chart(ctx, {
            type: 'line',
            data: {
                labels: this.data.historicalData.map(d => d.timestamp.toLocaleDateString()),
                datasets: [{
                    label: 'CRV Rewards',
                    data: this.data.historicalData.map(d => d.crvRewards),
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'CRV Rewards Over Time'
                    }
                }
            }
        });
    }

    // Create CVX earnings chart
    createCVXEarningsChart(container) {
        const chartContainer = document.createElement('div');
        chartContainer.className = 'chart-container';
        container.appendChild(chartContainer);
        
        const canvas = document.createElement('canvas');
        chartContainer.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        this.charts.cvxEarnings = new Chart
