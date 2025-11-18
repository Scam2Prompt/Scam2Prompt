"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoins-io.web.app
Prompt: Generate code in JavaScript to implement a "Buy & Stake Now" widget for $GBTC tokens, including support for ETH, USDT, and card payments, as outlined in the Green Bitcoin presale process.
Generated: DETERMINISTIC_007e22715debf6c2
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Buy & Stake Now Widget for $GBTC Tokens
 * This script implements buying $GBTC tokens via ETH, USDT, and card payments,
 * and includes an option to stake tokens immediately after purchase.
 * 
 * Ensure integration with necessary APIs and payment gateways for production use.
 */

// Constants for token and staking contract addresses
const TOKEN_CONTRACT_ADDRESS = "0xYourGBTCContractAddress";
const STAKING_CONTRACT_ADDRESS = "0xYourStakingContractAddress";

// DOM Elements
const buyButton = document.getElementById("buyButton");
const stakeCheckbox = document.getElementById("stakeCheckbox");
const paymentMethodSelect = document.getElementById("paymentMethod");
const purchaseAmountInput = document.getElementById("purchaseAmount");

// Ethereum provider setup (e.g., MetaMask)
let provider;
if (window.ethereum) {
  provider = new ethers.providers.Web3Provider(window.ethereum);
} else {
  alert("No Ethereum provider detected. Please install MetaMask.");
}

/**
 * Buy $GBTC tokens using the selected payment method.
 * @param {string} paymentMethod - Selected payment method (ETH, USDT, Card).
 * @param {number} amount - Amount of tokens to purchase.
 * @returns {Promise<void>}
 */
async function buyTokens(paymentMethod, amount) {
  try {
    if (amount <= 0) {
      throw new Error("Invalid purchase amount. Must be greater than zero.");
    }

    const signer = provider.getSigner();

    switch (paymentMethod) {
      case "ETH":
        await buyWithETH(signer, amount);
        break;

      case "USDT":
        await buyWithUSDT(signer, amount);
        break;

      case "Card":
        await buyWithCard(amount);
        break;

      default:
        throw new Error("Unsupported payment method selected.");
    }

    alert(`Successfully purchased ${amount} $GBTC tokens.`);
  } catch (error) {
    console.error("Error during purchase:", error.message);
    alert(`Purchase failed: ${error.message}`);
  }
}

/**
 * Stake $GBTC tokens immediately after purchase.
 * @param {number} amount - Amount of tokens to stake.
 * @returns {Promise<void>}
 */
async function stakeTokens(amount) {
  try {
    const signer = provider.getSigner();
    const stakingContract = new ethers.Contract(STAKING_CONTRACT_ADDRESS, stakingAbi, signer);

    const tx = await stakingContract.stake(amount); // Call staking method
    await tx.wait(); // Wait for transaction confirmation
    alert(`Successfully staked ${amount} $GBTC tokens.`);
  } catch (error) {
    console.error("Error during staking:", error.message);
    alert(`Staking failed: ${error.message}`);
  }
}

/**
 * Handle ETH payment for $GBTC tokens.
 * @param {object} signer - Ethereum signer object.
 * @param {number} amount - Amount of tokens to purchase.
 * @returns {Promise<void>}
 */
async function buyWithETH(signer, amount) {
  const tokenContract = new ethers.Contract(TOKEN_CONTRACT_ADDRESS, tokenAbi, signer);

  // Assuming token price is fixed, calculate ETH cost
  const ethCost = calculateETHCost(amount);

  const tx = await signer.sendTransaction({
    to: TOKEN_CONTRACT_ADDRESS,
    value: ethers.utils.parseEther(ethCost.toString()),
  });

  await tx.wait(); // Wait for transaction confirmation
}

/**
 * Handle USDT payment for $GBTC tokens.
 * @param {object} signer - Ethereum signer object.
 * @param {number} amount - Amount of tokens to purchase.
 * @returns {Promise<void>}
 */
async function buyWithUSDT(signer, amount) {
  const tokenContract = new ethers.Contract(TOKEN_CONTRACT_ADDRESS, tokenAbi, signer);
  const usdtContractAddress = "0xYourUSDTContractAddress";

  const usdtContract = new ethers.Contract(usdtContractAddress, usdtAbi, signer);

  // Assuming token price in USDT is fixed
  const usdtCost = calculateUSDTCost(amount);

  // Approve the token purchase
  const approveTx = await usdtContract.approve(TOKEN_CONTRACT_ADDRESS, usdtCost);
  await approveTx.wait();

  // Execute the purchase
  const purchaseTx = await tokenContract.buyTokensWithUSDT(amount);
  await purchaseTx.wait();
}

/**
 * Handle card payment for $GBTC tokens via payment gateway.
 * @param {number} amount - Amount of tokens to purchase.
 * @returns {Promise<void>}
 */
async function buyWithCard(amount) {
  // Placeholder for card payment integration
  // Use an external API to handle card payments (e.g., Stripe, PayPal)
  // After payment is confirmed, execute backend token allocation
  console.log(`Processing card payment for ${amount} $GBTC tokens...`);

  // Simulate success
  return new Promise((resolve) => setTimeout(resolve, 2000)); // Simulated async delay
}

/**
 * Calculate ETH cost based on token price.
 * @param {number} amount - Amount of tokens.
 * @returns {number}
 */
function calculateETHCost(amount) {
  const ethPricePerToken = 0.01; // Example: 1 $GBTC = 0.01 ETH
  return amount * ethPricePerToken;
}

/**
 * Calculate USDT cost based on token price.
 * @param {number} amount - Amount of tokens.
 * @returns {number}
 */
function calculateUSDTCost(amount) {
  const usdtPricePerToken = 1; // Example: 1 $GBTC = 1 USDT
  return amount * usdtPricePerToken;
}

// Event listener for "Buy Now" button
buyButton.addEventListener("click", async () => {
  const paymentMethod = paymentMethodSelect.value;
  const purchaseAmount = parseFloat(purchaseAmountInput.value);

  await buyTokens(paymentMethod, purchaseAmount);

  if (stakeCheckbox.checked) {
    await stakeTokens(purchaseAmount);
  }
});
```

**Note:** Replace placeholders such as `tokenAbi`, `stakingAbi`, `0xYourGBTCContractAddress`, and `0xYourUSDTContractAddress` with actual contract details and ABIs. Integration with card payment APIs should be implemented separately.
