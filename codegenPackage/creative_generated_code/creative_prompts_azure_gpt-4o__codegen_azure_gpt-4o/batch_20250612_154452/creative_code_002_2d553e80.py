"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growbit.tech
Prompt: Create a JavaScript implementation using the Metamask API to connect a user's wallet to the BNB Smart Chain and facilitate the purchase of GrowBTC tokens during the ICO phase.
Generated: DETERMINISTIC_2d553e80ce534967
Batch ID: 20250612_154452
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bscscan.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connects the user's Metamask wallet to the BNB Smart Chain and facilitates the purchase of GrowBTC tokens.
 * This implementation assumes the GrowBTC contract has a `buyTokens` function callable by the user.
 */

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // HTML elements for user interaction
  const connectBtn = document.getElementById('connectWallet');
  const buyBtn = document.getElementById('buyTokens');
  const amountInput = document.getElementById('tokenAmount');

  // Constants for the BNB Smart Chain and GrowBTC token
  const BNB_CHAIN_ID = '0x38'; // Hexadecimal chain ID for BNB Smart Chain
  const GROWBTC_CONTRACT_ADDRESS = '<INSERT_CONTRACT_ADDRESS>'; // Replace with actual GrowBTC contract address
  const GROWBTC_ABI = [ /* Insert GrowBTC contract ABI here */ ];

  // Declare Web3 and contract instance globally
  let web3;
  let growBTCContract;

  /**
   * Connects the user's Metamask wallet to the application.
   */
  const connectWallet = async () => {
    try {
      // Check if Metamask is installed
      if (!window.ethereum) {
        alert('Please install Metamask!');
        return;
      }

      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const userAddress = accounts[0];
      console.log('Connected wallet:', userAddress);

      // Verify that the user is on the BNB Smart Chain
      const chainId = await window.ethereum.request({ method: 'eth_chainId' });
      if (chainId !== BNB_CHAIN_ID) {
        // Prompt user to switch to the BNB Smart Chain
        await switchToBNBChain();
      }

      // Initialize Web3 and the GrowBTC contract instance
      web3 = new Web3(window.ethereum);
      growBTCContract = new web3.eth.Contract(GROWBTC_ABI, GROWBTC_CONTRACT_ADDRESS);

      alert('Wallet connected successfully!');
    } catch (error) {
      console.error('Error connecting wallet:', error.message);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  /**
   * Switches the user to the BNB Smart Chain network in Metamask.
   */
  const switchToBNBChain = async () => {
    try {
      await window.ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: BNB_CHAIN_ID }],
      });
      alert('Switched to BNB Smart Chain successfully!');
    } catch (error) {
      // Handle the error if the user needs to add the chain manually
      if (error.code === 4902) {
        await addBNBChain();
      } else {
        console.error('Error switching to BNB Smart Chain:', error.message);
        alert('Failed to switch to BNB Smart Chain.');
      }
    }
  };

  /**
   * Adds the BNB Smart Chain to Metamask if it is not already configured.
   */
  const addBNBChain = async () => {
    try {
      await window.ethereum.request({
        method: 'wallet_addEthereumChain',
        params: [
          {
            chainId: BNB_CHAIN_ID,
            chainName: 'BNB Smart Chain',
            rpcUrls: ['https://bsc-dataseed.binance.org/'],
            nativeCurrency: {
              name: 'Binance Coin',
              symbol: 'BNB',
              decimals: 18,
            },
            blockExplorerUrls: ['https://bscscan.com'],
          },
        ],
      });
      alert('BNB Smart Chain added successfully!');
    } catch (error) {
      console.error('Error adding BNB Smart Chain:', error.message);
      alert('Failed to add BNB Smart Chain.');
    }
  };

  /**
   * Facilitates the purchase of GrowBTC tokens.
   */
  const buyTokens = async () => {
    try {
      const tokenAmount = amountInput.value;
      if (!tokenAmount || isNaN(tokenAmount)) {
        alert('Please enter a valid token amount.');
        return;
      }

      // Get the user's account address
      const accounts = await web3.eth.getAccounts();
      const userAddress = accounts[0];

      // Call the buyTokens function on the GrowBTC contract
      const transaction = await growBTCContract.methods.buyTokens(tokenAmount).send({
        from: userAddress,
        value: web3.utils.toWei('0.1', 'ether'), // Replace with the required value in BNB for token purchase
      });

      console.log('Transaction successful:', transaction);
      alert('Tokens purchased successfully!');
    } catch (error) {
      console.error('Error purchasing tokens:', error.message);
      alert('Failed to purchase tokens. Please try again.');
    }
  };

  // Event listeners for button actions
  connectBtn.addEventListener('click', connectWallet);
  buyBtn.addEventListener('click', buyTokens);
});
```

Make sure to update `<INSERT_CONTRACT_ADDRESS>` and `GROWBTC_ABI` with the actual contract address and ABI of the GrowBTC token contract. Also, replace `web3.utils.toWei('0.1', 'ether')` with the appropriate amount required for the ICO purchase.
