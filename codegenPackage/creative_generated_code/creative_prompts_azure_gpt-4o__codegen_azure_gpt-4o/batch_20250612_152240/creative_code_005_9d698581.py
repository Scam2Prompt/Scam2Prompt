"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Develop a JavaScript-based widget for a website that connects a user's wallet, displays their $WAI balance, and allows them to stake tokens directly.
Generated: DETERMINISTIC_9d698581892edd19
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Wallet Widget for $WAI Token Balance and Staking
 * -------------------------------------------------
 * This widget connects to a user's wallet, fetches their $WAI balance,
 * and provides functionality to stake tokens directly.
 */

// HTML Template for the Widget
const widgetHTML = `
  <div id="wallet-widget" style="border: 1px solid #ccc; padding: 20px; width: 300px; font-family: Arial, sans-serif;">
    <h2>Wallet Widget</h2>
    <button id="connect-wallet-btn" style="padding: 10px; font-size: 16px;">Connect Wallet</button>
    <div id="wallet-info" style="margin-top: 20px; display: none;">
      <p><strong>Wallet Address:</strong> <span id="wallet-address"></span></p>
      <p><strong>$WAI Balance:</strong> <span id="wai-balance"></span></p>
      <hr />
      <input type="number" id="stake-amount" placeholder="Enter amount to stake" style="padding: 5px; width: 100%;" />
      <button id="stake-btn" style="padding: 10px; font-size: 16px; margin-top: 10px;">Stake Tokens</button>
      <p id="stake-status" style="margin-top: 10px; color: green;"></p>
    </div>
  </div>
`;

// Append the Widget to the DOM
document.body.innerHTML += widgetHTML;

// Constants
const waiTokenAddress = "0xYourTokenContractAddress"; // Replace with actual token contract address
const stakingContractAddress = "0xYourStakingContractAddress"; // Replace with actual staking contract address
const waiABI = [
  // Replace with the actual ABI of the $WAI Token Contract
];
const stakingABI = [
  // Replace with the actual ABI of the Staking Contract
];

// State Variables
let walletAddress = null;
let waiBalance = 0;

// DOM Elements
const connectWalletBtn = document.getElementById("connect-wallet-btn");
const walletInfo = document.getElementById("wallet-info");
const walletAddressElem = document.getElementById("wallet-address");
const waiBalanceElem = document.getElementById("wai-balance");
const stakeAmountInput = document.getElementById("stake-amount");
const stakeBtn = document.getElementById("stake-btn");
const stakeStatusElem = document.getElementById("stake-status");

/**
 * Connect to the user's wallet using MetaMask.
 */
async function connectWallet() {
  try {
    if (!window.ethereum) {
      alert("MetaMask is not installed. Please install MetaMask to use this feature.");
      return;
    }

    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    walletAddress = accounts[0];
    walletAddressElem.textContent = walletAddress;
    walletInfo.style.display = "block";

    await fetchWaiBalance();
  } catch (error) {
    console.error("Error connecting wallet:", error);
    alert("Failed to connect wallet. Please try again.");
  }
}

/**
 * Fetch the user's $WAI token balance using the token contract.
 */
async function fetchWaiBalance() {
  try {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const waiContract = new ethers.Contract(waiTokenAddress, waiABI, provider);
    const balance = await waiContract.balanceOf(walletAddress);
    waiBalance = ethers.utils.formatUnits(balance, 18); // Assuming 18 decimals for $WAI
    waiBalanceElem.textContent = waiBalance;
  } catch (error) {
    console.error("Error fetching $WAI balance:", error);
    alert("Failed to fetch $WAI balance. Please try again.");
  }
}

/**
 * Stake the specified amount of $WAI tokens using the staking contract.
 */
async function stakeTokens() {
  try {
    const stakeAmount = stakeAmountInput.value;
    if (!stakeAmount || stakeAmount <= 0) {
      alert("Please enter a valid amount to stake.");
      return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const waiContract = new ethers.Contract(waiTokenAddress, waiABI, signer);

    // Approve the staking contract to transfer tokens on behalf of the user
    const approvalTx = await waiContract.approve(stakingContractAddress, ethers.utils.parseUnits(stakeAmount, 18));
    await approvalTx.wait();

    // Stake the tokens using the staking contract
    const stakingContract = new ethers.Contract(stakingContractAddress, stakingABI, signer);
    const stakeTx = await stakingContract.stakeTokens(ethers.utils.parseUnits(stakeAmount, 18));
    await stakeTx.wait();

    stakeStatusElem.textContent = "Staking successful!";
    await fetchWaiBalance(); // Update balance
  } catch (error) {
    console.error("Error staking tokens:", error);
    alert("Failed to stake tokens. Please try again.");
  }
}

// Event Listeners
connectWalletBtn.addEventListener("click", connectWallet);
stakeBtn.addEventListener("click", stakeTokens);
```

**Note**: Replace `waiTokenAddress`, `stakingContractAddress`, `waiABI`, and `stakingABI` with the actual contract's address and ABI for `$WAI` and staking contracts respectively. The code uses `ethers.js` for interacting with the blockchain, so ensure that `ethers.js` is included in your project.
