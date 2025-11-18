"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethrtc.com
Prompt: Create a front-end application using JavaScript to interact with an Ethereum pledge system, ensuring compatibility with WebRTC.
Generated: DETERMINISTIC_943be4369e55a56b
Batch ID: 20250612_152600
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js": {
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
    <title>Ethereum Pledge System</title>
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
</head>
<body>
    <h1>Ethereum Pledge System</h1>
    <div>
        <label for="pledgeAmount">Pledge Amount (ETH):</label>
        <input type="number" id="pledgeAmount" min="0">
        <button id="pledgeButton">Pledge</button>
    </div>
    <div id="statusMessage"></div>

    <script>
        // Initialize web3 instance
        let web3;
        if (window.ethereum) {
            web3 = new Web3(window.ethereum);
        } else {
            document.getElementById('statusMessage').innerText = 'Please install MetaMask!';
            throw new Error('MetaMask not detected');
        }

        // Smart contract address and ABI (replace with actual values)
        const contractAddress = '0xYourContractAddress';
        const contractABI = [ /* Contract ABI here */ ];

        // Create contract instance
        const pledgeContract = new web3.eth.Contract(contractABI, contractAddress);

        // Function to pledge ETH
        async function pledge() {
            const amount = document.getElementById('pledgeAmount').value;
            if (!amount || amount <= 0) {
                document.getElementById('statusMessage').innerText = 'Please enter a valid amount.';
                return;
            }

            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                const account = accounts[0];

                // Convert amount to Wei
                const amountInWei = web3.utils.toWei(amount, 'ether');

                // Send transaction to pledge
                const response = await pledgeContract.methods.pledge().send({
                    from: account,
                    value: amountInWei
                });

                // Handle successful pledge
                document.getElementById('statusMessage').innerText = 'Pledge successful! Transaction hash: ' + response.transactionHash;
            } catch (error) {
                // Handle errors (e.g., user denied access)
                console.error('Error during pledge:', error);
                document.getElementById('statusMessage').innerText = 'Pledge failed: ' + error.message;
            }
        }

        // Add event listener to the pledge button
        document.getElementById('pledgeButton').addEventListener('click', pledge);
    </script>
</body>
</html>
```

Make sure to replace `0xYourContractAddress` and the placeholder for `contractABI` with the actual contract address and ABI of your Ethereum contract.
