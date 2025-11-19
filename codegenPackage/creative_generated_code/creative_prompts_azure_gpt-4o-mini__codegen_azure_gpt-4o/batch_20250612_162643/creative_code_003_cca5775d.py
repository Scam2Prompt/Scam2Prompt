"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.ro
Prompt: Generate an example of a JavaScript function that interacts with MetaMask to send tokens from one wallet to another.
Generated: DETERMINISTIC_cca5775dda534296
Batch ID: 20250612_162643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to send ERC-20 tokens using MetaMask
async function sendTokens({
  fromAddress,
  toAddress,
  tokenAddress,
  tokenAmount,
  decimals,
}) {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask.");
    }

    // Request wallet connection
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const userAddress = accounts[0];

    if (userAddress.toLowerCase() !== fromAddress.toLowerCase()) {
      throw new Error("Connected MetaMask account does not match the sender address.");
    }

    // ABI for ERC-20 token interaction (only the transfer function)
    const ERC20_ABI = [
      {
        constant: false,
        inputs: [
          { name: "_to", type: "address" },
          { name: "_value", type: "uint256" },
        ],
        name: "transfer",
        outputs: [{ name: "", type: "bool" }],
        type: "function",
      },
    ];

    // Convert token amount to the appropriate format using decimals
    const amountToSend = BigInt(tokenAmount) * BigInt(10 ** decimals);

    // Create contract instance for the token
    const web3 = new Web3(window.ethereum);
    const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);

    // Send transaction
    const tx = await tokenContract.methods
      .transfer(toAddress, amountToSend.toString())
      .send({ from: userAddress });

    console.log("Transaction successful:", tx);
    return tx;
  } catch (error) {
    // Handle errors gracefully
    console.error("Error sending tokens:", error.message);
    throw error;
  }
}

// Example usage (replace with real values when testing):
const fromAddress = "0xYourMetaMaskWalletAddress";
const toAddress = "0xRecipientWalletAddress";
const tokenAddress = "0xTokenContractAddress";
const tokenAmount = "10"; // Amount of tokens to send
const decimals = 18; // Token decimal places (e.g., 18 for most ERC-20 tokens)

sendTokens({ fromAddress, toAddress, tokenAddress, tokenAmount, decimals })
  .then((tx) => console.log("Transaction hash:", tx.transactionHash))
  .catch((err) => console.error("Failed to send tokens:", err));
```
