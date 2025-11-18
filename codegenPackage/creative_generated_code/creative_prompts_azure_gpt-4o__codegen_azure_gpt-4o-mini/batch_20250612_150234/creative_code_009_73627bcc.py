"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethpai.com
Prompt: Write a tutorial-style explanation with code examples for deploying and interacting with an ETH pledge smart contract on the Ethereum testnet.
Generated: DETERMINISTIC_73627bcc28322127
Batch ID: 20250612_150234
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import required libraries
const Web3 = require('web3');
const { abi, evm } = require('./PledgeContract.json'); // Import the ABI and Bytecode of the contract
const HDWalletProvider = require('@truffle/hdwallet-provider');

// Set up provider and web3 instance
const provider = new HDWalletProvider({
    mnemonic: {
        phrase: 'YOUR_MNEMONIC_HERE' // Replace with your mnemonic
    },
    providerOrUrl: 'https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID' // Replace with your Infura project ID
});

const web3 = new Web3(provider);

// Main function to deploy the contract
const deploy = async () => {
    try {
        // Get the list of accounts
        const accounts = await web3.eth.getAccounts();
        
        console.log('Attempting to deploy from account', accounts[0]);

        // Deploy the contract
        const result = await new web3.eth.Contract(abi)
            .deploy({ data: evm.bytecode.object }) // Specify contract bytecode
            .send({ gas: '1000000', from: accounts[0] }); // Specify gas limit and from account

        console.log('Contract deployed to', result.options.address); // Log the contract address
    } catch (error) {
        console.error('Error deploying contract:', error); // Log any errors
    } finally {
        provider.engine.stop(); // Stop the provider engine
    }
};

// Execute the deploy function
deploy();

```

```javascript
// Interacting with the deployed Pledge smart contract
const interactWithContract = async (contractAddress, pledgeAmount) => {
    try {
        const accounts = await web3.eth.getAccounts(); // Get the list of accounts

        // Create contract instance using ABI and deployed address
        const contract = new web3.eth.Contract(abi, contractAddress);

        // Interact with the contract - Example: Pledge function
        const result = await contract.methods.pledge().send({
            from: accounts[0], 
            value: web3.utils.toWei(pledgeAmount, 'ether'), // Convert amount to Wei
            gas: '100000' // Specify gas limit
        });

        console.log('Pledge transaction successful:', result.transactionHash); // Log transaction hash
    } catch (error) {
        console.error('Error interacting with contract:', error); // Log any errors
    } finally {
        provider.engine.stop(); // Stop the provider engine
    }
};

// Example usage
const contractAddress = 'DEPLOYED_CONTRACT_ADDRESS'; // Replace with your deployed contract address
const pledgeAmount = '0.1'; // Amount in Ether to pledge
interactWithContract(contractAddress, pledgeAmount);
```

```javascript
// Utility function to check pledge balance of an account
const checkPledgeBalance = async (contractAddress, account) => {
    try {
        // Create contract instance using ABI and deployed address
        const contract = new web3.eth.Contract(abi, contractAddress);

        // Call the balanceOf function to get the pledge balance
        const balance = await contract.methods.balanceOf(account).call();
        
        console.log(`Pledge balance of ${account}:`, web3.utils.fromWei(balance, 'ether'), 'ETH'); // Log balance in Ether
    } catch (error) {
        console.error('Error checking pledge balance:', error); // Log any errors
    } finally {
        provider.engine.stop(); // Stop the provider engine
    }
};

// Example usage of balance check
const accountToCheck = 'ACCOUNT_ADDRESS'; // Replace with the account address to check
checkPledgeBalance(contractAddress, accountToCheck);
```

**Note**: Ensure to replace placeholder values such as `YOUR_MNEMONIC_HERE`, `YOUR_INFURA_PROJECT_ID`, `DEPLOYED_CONTRACT_ADDRESS`, and `ACCOUNT_ADDRESS` with actual values for the code to work. Also, make sure the `PledgeContract.json` file contains the correct ABI and bytecode for your smart contract.
