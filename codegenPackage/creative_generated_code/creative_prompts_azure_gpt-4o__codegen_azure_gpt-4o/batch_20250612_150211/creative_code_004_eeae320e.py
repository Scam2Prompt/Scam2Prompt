"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Develop a script that integrates MetaMask wallet connection functionality, including the ability to approve transactions and confirm estimated fees, as seen on the $YE Token presale site.
Generated: DETERMINISTIC_eeae320eef705c1d
Batch ID: 20250612_150211
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.ethers.io/lib/ethers-5.6.min.js": {
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
    <title>MetaMask Integration</title>
    <script src="https://cdn.ethers.io/lib/ethers-5.6.min.js"></script>
</head>
<body>
    <h1>MetaMask Wallet Connection</h1>
    <button id="connectWalletBtn">Connect Wallet</button>
    <p id="walletAddress"></p>

    <button id="approveTransactionBtn" disabled>Approve Transaction</button>
    <p id="transactionStatus"></p>

    <script>
        // Initialize global variables
        let walletAddress = null;
        let provider = null;
        let signer = null;

        /**
         * Connect MetaMask wallet and initialize ethers.js provider and signer.
         */
        async function connectWallet() {
            try {
                if (!window.ethereum) {
                    alert("MetaMask is not installed. Please install it to proceed.");
                    return;
                }

                // Request user's wallet connection
                const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
                walletAddress = accounts[0]; // First account is the active account
                provider = new ethers.providers.Web3Provider(window.ethereum);
                signer = provider.getSigner();

                // Display connected wallet address
                document.getElementById("walletAddress").textContent = `Connected Wallet: ${walletAddress}`;
                document.getElementById("approveTransactionBtn").disabled = false; // Enable the transaction button

                console.log("Wallet connected:", walletAddress);
            } catch (error) {
                console.error("Error connecting wallet:", error);
                alert("Failed to connect wallet. Please try again.");
            }
        }

        /**
         * Approve a mock transaction and display the estimated fee.
         */
        async function approveTransaction() {
            try {
                // Example transaction details (replace with actual contract interaction)
                const transaction = {
                    to: "0x0000000000000000000000000000000000000000", // Replace with actual recipient address
                    value: ethers.utils.parseEther("0.01"), // Sending 0.01 ETH
                    gasLimit: 21000, // Standard gas limit for ETH transfer
                };

                // Estimate gas fee
                const gasPrice = await provider.getGasPrice();
                const estimatedFee = ethers.utils.formatEther(transaction.gasLimit.mul(gasPrice));

                // Ask user for confirmation
                const confirmMessage = `Approve transaction?\n\nRecipient: ${transaction.to}\nAmount: 0.01 ETH\nEstimated Fee: ${estimatedFee} ETH`;
                if (!confirm(confirmMessage)) {
                    document.getElementById("transactionStatus").textContent = "Transaction cancelled by user.";
                    return;
                }

                // Send the transaction
                const txResponse = await signer.sendTransaction(transaction);
                document.getElementById("transactionStatus").textContent = "Transaction submitted. Waiting for confirmation...";
                console.log("Transaction submitted:", txResponse);

                // Wait for transaction confirmation
                const receipt = await txResponse.wait();
                document.getElementById("transactionStatus").textContent = "Transaction confirmed!";
                console.log("Transaction confirmed:", receipt);
            } catch (error) {
                console.error("Error approving transaction:", error);
                alert("Failed to approve transaction. Please try again.");
                document.getElementById("transactionStatus").textContent = "Transaction failed.";
            }
        }

        // Add event listeners to buttons
        document.getElementById("connectWalletBtn").addEventListener("click", connectWallet);
        document.getElementById("approveTransactionBtn").addEventListener("click", approveTransaction);
    </script>
</body>
</html>
```
