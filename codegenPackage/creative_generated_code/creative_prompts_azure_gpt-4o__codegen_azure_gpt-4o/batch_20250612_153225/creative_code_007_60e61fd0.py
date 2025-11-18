"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Create a front-end interface for connecting a wallet and displaying $RIFT token rewards and referral statistics, inspired by the Rift Swap website's design.
Generated: DETERMINISTIC_60e61fd0d5cae10e
Batch ID: 20250612_153225
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/ethers/dist/ethers.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@web3modal/standalone/dist/index.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RIFT Token Rewards</title>
  <link rel="stylesheet" href="styles.css">
  <script src="https://cdn.jsdelivr.net/npm/@web3modal/standalone/dist/index.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/ethers/dist/ethers.min.js"></script>
</head>
<body>
  <header class="header">
    <h1>Rift Swap Rewards</h1>
    <button id="connect-wallet" class="button">Connect Wallet</button>
  </header>

  <main>
    <section id="wallet-info" class="hidden">
      <h2>Wallet Information</h2>
      <p><strong>Wallet Address:</strong> <span id="wallet-address"></span></p>
    </section>

    <section id="rift-rewards" class="hidden">
      <h2>$RIFT Token Rewards</h2>
      <p><strong>Rewards:</strong> <span id="rift-rewards-amount">0</span> $RIFT</p>
    </section>

    <section id="referral-stats" class="hidden">
      <h2>Referral Statistics</h2>
      <p><strong>Total Referrals:</strong> <span id="referrals-count">0</span></p>
      <p><strong>Total Referral Earnings:</strong> <span id="referrals-earnings">0</span> $RIFT</p>
    </section>
  </main>

  <footer class="footer">
    <p>Powered by Rift Swap</p>
  </footer>

  <script>
    // Wallet connection logic
    const connectWalletButton = document.getElementById('connect-wallet');
    const walletInfoSection = document.getElementById('wallet-info');
    const walletAddressSpan = document.getElementById('wallet-address');
    const riftRewardsSection = document.getElementById('rift-rewards');
    const riftRewardsAmount = document.getElementById('rift-rewards-amount');
    const referralStatsSection = document.getElementById('referral-stats');
    const referralsCount = document.getElementById('referrals-count');
    const referralsEarnings = document.getElementById('referrals-earnings');

    connectWalletButton.addEventListener('click', async () => {
      try {
        // Check for Ethereum provider
        if (!window.ethereum) {
          alert('Please install MetaMask or another wallet provider.');
          return;
        }

        // Request wallet connection
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const accounts = await provider.send('eth_requestAccounts', []);

        if (accounts.length === 0) {
          alert('No wallet connected.');
          return;
        }

        const walletAddress = accounts[0];
        walletAddressSpan.textContent = walletAddress;

        // Show wallet info section
        walletInfoSection.classList.remove('hidden');

        // Fetch and display $RIFT token rewards
        // Placeholder logic: Replace with actual contract interaction
        const mockRewards = Math.floor(Math.random() * 1000);
        riftRewardsAmount.textContent = mockRewards;
        riftRewardsSection.classList.remove('hidden');

        // Fetch and display referral statistics
        // Placeholder logic: Replace with actual contract interaction
        const mockReferrals = Math.floor(Math.random() * 50);
        const mockReferralEarnings = mockReferrals * 10;
        referralsCount.textContent = mockReferrals;
        referralsEarnings.textContent = mockReferralEarnings;
        referralStatsSection.classList.remove('hidden');
      } catch (error) {
        console.error('Error connecting wallet:', error);
        alert('An error occurred while connecting the wallet. Please try again.');
      }
    });
  </script>
</body>
</html>
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
  color: #333;
}

.header {
  background-color: #4caf50;
  color: white;
  padding: 1rem;
  text-align: center;
}

.button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 5px;
}

.button:hover {
  background-color: #45a049;
}

main {
  padding: 2rem;
  max-width: 800px;
  margin: auto;
}

section {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}

.hidden {
  display: none;
}

.footer {
  text-align: center;
  padding: 1rem;
  background-color: #4caf50;
  color: white;
}
```
