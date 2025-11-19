"""
Generated Code Metadata:
========================
Original URL: https://arbinu.app
Prompt: Write a script to display Arbinu token statistics (e.g., total supply, burned tokens, staked tokens) on a webpage using data retrieved from the Arbitrum blockchain.
Generated: DETERMINISTIC_66889023f138adea
Batch ID: 20250612_153916
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js": {
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
  },
  "https://arb1.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arbinu Token Statistics</title>
    <script src="https://cdn.jsdelivr.net/npm/web3@1.5.2/dist/web3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stat-value {
            font-size: 24px;
            font-weight: bold;
            margin: 10px 0;
            color: #2c3e50;
        }
        .stat-label {
            color: #7f8c8d;
            font-size: 14px;
        }
        .chart-container {
            margin-top: 30px;
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .loading {
            text-align: center;
            padding: 20px;
            font-style: italic;
            color: #7f8c8d;
        }
        .error {
            color: #e74c3c;
            padding: 10px;
            background: #fadbd8;
            border-radius: 4px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Arbinu Token Statistics</h1>
    <div id="network-info"></div>
    
    <div id="loading" class="loading">Loading token data from Arbitrum blockchain...</div>
    
    <div id="stats-container" class="stats-container" style="display: none;">
        <div class="stat-card">
            <div class="stat-label">Total Supply</div>
            <div id="total-supply" class="stat-value">-</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Circulating Supply</div>
            <div id="circulating-supply" class="stat-value">-</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Burned Tokens</div>
            <div id="burned-tokens" class="stat-value">-</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Staked Tokens</div>
            <div id="staked-tokens" class="stat-value">-</div>
        </div>
    </div>

    <div class="chart-container">
        <canvas id="tokenDistributionChart"></canvas>
    </div>

    <script>
        // Arbinu Token Contract Address (replace with actual contract address)
        const TOKEN_CONTRACT_ADDRESS = '0x123456789...';
        
        // ABI for standard ERC20 functions plus any custom functions needed
        const TOKEN_ABI = [
            // ERC20 Standard functions
            {
                "constant": true,
                "inputs": [],
                "name": "totalSupply",
                "outputs": [{"name": "", "type": "uint256"}],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            // Custom functions (if any)
            {
                "constant": true,
                "inputs": [],
                "name": "burnedTokens",
                "outputs": [{"name": "", "type": "uint256"}],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "stakingContract",
                "outputs": [{"name": "", "type": "address"}],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            }
        ];

        // Staking Contract ABI (if needed)
        const STAKING_ABI = [
            {
                "constant": true,
                "inputs": [],
                "name": "totalStaked",
                "outputs": [{"name": "", "type": "uint256"}],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            }
        ];

        // Initialize Web3
        let web3;
        let tokenContract;
        let stakingContract;

        async function initWeb3() {
            try {
                // Check if Web3 is injected by MetaMask or other provider
                if (window.ethereum) {
                    web3 = new Web3(window.ethereum);
                    try {
                        // Request account access
                        await window.ethereum.request({ method: 'eth_requestAccounts' });
                        await setupContracts();
                        await updateNetworkInfo();
                        await fetchTokenStats();
                    } catch (error) {
                        console.error("User denied account access", error);
                        showError("Please connect to MetaMask to view token statistics.");
                    }
                } else if (window.web3) {
                    // Legacy dapp browsers
                    web3 = new Web3(window.web3.currentProvider);
                    await setupContracts();
                    await updateNetworkInfo();
                    await fetchTokenStats();
                } else {
                    // Fallback to public node (Alchemy, Infura, etc.)
                    const provider = new Web3.providers.HttpProvider('https://arb1.arbitrum.io/rpc');
                    web3 = new Web3(provider);
                    await setupContracts();
                    await updateNetworkInfo();
                    await fetchTokenStats();
                }
            } catch (error) {
                console.error("Error initializing Web3:", error);
                showError("Failed to connect to the blockchain. Please try again later.");
            }
        }

        async function setupContracts() {
            try {
                tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
                
                // Get staking contract address from token contract if needed
                const stakingContractAddress = await tokenContract.methods.stakingContract().call();
                if (stakingContractAddress && stakingContractAddress !== '0x0000000000000000000000000000000000000000') {
                    stakingContract = new web3.eth.Contract(STAKING_ABI, stakingContractAddress);
                }
            } catch (error) {
                console.error("Error setting up contracts:", error);
                throw error;
            }
        }

        async function updateNetworkInfo() {
            try {
                const networkId = await web3.eth.net.getId();
                let networkName;
                
                switch(networkId) {
                    case 42161: networkName = "Arbitrum One"; break;
                    case 421613: networkName = "Arbitrum Goerli"; break;
                    default: networkName = `Unknown Network (ID: ${networkId})`;
                }
                
                document.getElementById('network-info').innerHTML = `
                    <p>Connected to: <strong>${networkName}</strong></p>
                `;
            } catch (error) {
                console.error("Error getting network info:", error);
            }
        }

        async function fetchTokenStats() {
            try {
                // Fetch all data in parallel
                const [totalSupply, burnedTokens, stakingData] = await Promise.all([
                    tokenContract.methods.totalSupply().call(),
                    tokenContract.methods.burnedTokens().call().catch(() => "0"), // Fallback if burnedTokens not available
                    getStakedTokens()
                ]);

                const stakedTokens = stakingData || "0";
                const circulatingSupply = totalSupply - burnedTokens - stakedTokens;

                // Update UI
                document.getElementById('total-supply').textContent = formatNumber(totalSupply);
                document.getElementById('circulating-supply').textContent = formatNumber(circulatingSupply);
                document.getElementById('burned-tokens').textContent = formatNumber(burnedTokens);
                document.getElementById('staked-tokens').textContent = formatNumber(stakedTokens);

                // Hide loading, show stats
                document.getElementById('loading').style.display = '
