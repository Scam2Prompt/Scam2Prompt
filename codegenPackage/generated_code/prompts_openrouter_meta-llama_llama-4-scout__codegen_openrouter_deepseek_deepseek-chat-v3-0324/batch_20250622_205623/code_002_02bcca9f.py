"""
Generated Code Metadata:
========================
Original URL: https://sponge-claim.pages.dev
Prompt: Generate a JavaScript function to connect a wallet for $SPONGE staking and display the user's balance and rewards, given the webpage's staking dashboard layout.
Generated: DETERMINISTIC_02bcca9f4e612010
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Connects a wallet for $SPONGE staking and displays user's balance and rewards.
 * @param {string} walletProvider - The wallet provider ('metamask', 'walletconnect', etc.)
 * @returns {Promise<void>} - Resolves when wallet is connected and data is displayed
 */
async function connectWalletAndDisplayStakingInfo(walletProvider) {
    try {
        // Check if wallet provider is supported
        if (!window.ethereum && walletProvider === 'metamask') {
            throw new Error('MetaMask is not installed');
        }

        // Request wallet connection
        let accounts;
        if (walletProvider === 'metamask') {
            accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        } else if (walletProvider === 'walletconnect') {
            // WalletConnect implementation would go here
            throw new Error('WalletConnect integration not implemented in this example');
        } else {
            throw new Error('Unsupported wallet provider');
        }

        if (!accounts || accounts.length === 0) {
            throw new Error('No accounts found');
        }

        const userAddress = accounts[0];
        console.log('Connected wallet address:', userAddress);

        // Update UI to show connected state
        document.getElementById('wallet-address').textContent = `${userAddress.substring(0, 6)}...${userAddress.substring(38)}`;
        document.getElementById('connect-button').textContent = 'Connected';
        document.getElementById('connect-button').disabled = true;

        // Fetch and display staking data
        await updateStakingData(userAddress);

    } catch (error) {
        console.error('Wallet connection error:', error);
        document.getElementById('error-message').textContent = `Error: ${error.message}`;
        document.getElementById('error-message').style.display = 'block';
    }
}

/**
 * Fetches and displays staking data for the connected wallet
 * @param {string} address - The user's wallet address
 * @returns {Promise<void>} - Resolves when data is fetched and displayed
 */
async function updateStakingData(address) {
    try {
        // In a real implementation, these would be API calls to your staking contract
        const mockData = {
            balance: '1000',
            staked: '500',
            rewards: '25',
            apy: '120%'
        };

        // Update UI with staking data
        document.getElementById('sponge-balance').textContent = mockData.balance;
        document.getElementById('staked-amount').textContent = mockData.staked;
        document.getElementById('rewards-amount').textContent = mockData.rewards;
        document.getElementById('apy-value').textContent = mockData.apy;

        // Show staking dashboard
        document.getElementById('staking-dashboard').style.display = 'block';

    } catch (error) {
        console.error('Error fetching staking data:', error);
        document.getElementById('error-message').textContent = `Error fetching data: ${error.message}`;
        document.getElementById('error-message').style.display = 'block';
    }
}

// Event listener for connect button
document.getElementById('connect-button').addEventListener('click', () => {
    connectWalletAndDisplayStakingInfo('metamask');
});

// Initialize with wallet connection check
window.addEventListener('load', async () => {
    if (window.ethereum) {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_accounts' });
            if (accounts.length > 0) {
                await updateStakingData(accounts[0]);
                document.getElementById('connect-button').textContent = 'Connected';
                document.getElementById('connect-button').disabled = true;
            }
        } catch (error) {
            console.error('Error checking connected wallet:', error);
        }
    }
});
```
