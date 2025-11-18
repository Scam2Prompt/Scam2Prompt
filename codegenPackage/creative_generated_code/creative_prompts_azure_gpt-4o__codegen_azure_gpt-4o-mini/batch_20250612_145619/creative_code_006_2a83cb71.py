"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethphbi.com
Prompt: Create a frontend JavaScript application that interacts with an Ethereum smart contract to display pledge details and allow users to make new pledges.
Generated: DETERMINISTIC_2a83cb71d0ab6d1a
Batch ID: 20250612_145619
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
    <title>Pledge DApp</title>
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; }
        #pledges { margin-top: 20px; }
        .pledge { margin-bottom: 10px; }
    </style>
</head>
<body>

    <h1>Pledge DApp</h1>
    <div>
        <label for="pledgeAmount">Pledge Amount (in Ether):</label>
        <input type="number" id="pledgeAmount" step="0.01" min="0" required>
        <button id="submitPledge">Make Pledge</button>
    </div>

    <h2>Pledge Details</h2>
    <div id="pledges"></div>

    <script>
        // Ensure web3 is injected by the browser (MetaMask)
        if (typeof window.ethereum !== 'undefined') {
            console.log('MetaMask is installed!');

            // Create a web3 instance
            const web3 = new Web3(window.ethereum);
            let contract;

            // Smart contract ABI and address (replace with your own)
            const contractABI = [/* ABI goes here */];
            const contractAddress = '0xYourContractAddress';

            // Initialize the contract
            const initContract = async () => {
                contract = new web3.eth.Contract(contractABI, contractAddress);
                await loadPledges();
            };

            // Load existing pledges from the blockchain
            const loadPledges = async () => {
                try {
                    const pledgeCount = await contract.methods.getPledgeCount().call();
                    const pledgesContainer = document.getElementById('pledges');
                    pledgesContainer.innerHTML = ''; // Clear previous pledges

                    for (let i = 0; i < pledgeCount; i++) {
                        const pledge = await contract.methods.getPledge(i).call();
                        const pledgeElement = document.createElement('div');
                        pledgeElement.classList.add('pledge');
                        pledgeElement.innerHTML = `Pledge ${i + 1}: ${web3.utils.fromWei(pledge.amount, 'ether')} Ether`;
                        pledgesContainer.appendChild(pledgeElement);
                    }
                } catch (error) {
                    console.error('Error loading pledges:', error);
                    alert('Failed to load pledges. Check console for details.');
                }
            };

            // Make a new pledge
            const makePledge = async () => {
                const amount = document.getElementById('pledgeAmount').value;
                const accounts = await ethereum.request({ method: 'eth_requestAccounts' });

                try {
                    const transaction = await contract.methods.makePledge().send({
                        from: accounts[0],
                        value: web3.utils.toWei(amount, 'ether')
                    });
                    console.log('Transaction successful:', transaction);
                    await loadPledges(); // Reload pledges after making a new one
                } catch (error) {
                    console.error('Error making pledge:', error);
                    alert('Failed to make pledge. Check console for details.');
                }
            };

            // Event listener for the pledge button
            document.getElementById('submitPledge').addEventListener('click', makePledge);

            // Initialize the contract on page load
            window.onload = initContract;

        } else {
            alert('Please install MetaMask to use this DApp');
        }
    </script>
</body>
</html>
```

**Note:**
- Replace `/* ABI goes here */` with the actual ABI of your smart contract.
- Replace `0xYourContractAddress` with the actual deployed address of your smart contract.
- Ensure that your smart contract has `getPledgeCount()` and `getPledge(index)` methods defined, and that `makePledge()` accepts a value. Adjust methods as necessary based on your contract's interface.
