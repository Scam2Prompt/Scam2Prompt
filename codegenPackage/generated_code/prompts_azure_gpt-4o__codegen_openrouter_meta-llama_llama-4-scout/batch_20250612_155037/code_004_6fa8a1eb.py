"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Create a script using Web3.js to query and manage collateralized vaults within the QiDao protocol, ensuring the collateral value exceeds the debt amount.
Generated: DETERMINISTIC_6fa8a1eba8a82ffd
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { QIDAO } = require('./qidao-abi'); // Assuming QIDAO ABI is in a separate file

// Set up Web3 provider
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const web3 = new Web3(new Web3.providers.HttpProvider(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`));

// Set up QiDao contract instance
const QIDAO_CONTRACT_ADDRESS = '0x...QiDaoContractAddress...';
const qidaoContract = new web3.eth.Contract(QIDAO, QIDAO_CONTRACT_ADDRESS);

async function getVaults(address) {
    try {
        // Get vaults for a specific address
        const vaults = await qidaoContract.methods.getVaults(address).call();
        return vaults;
    } catch (error) {
        console.error('Error getting vaults:', error);
        throw error;
    }
}

async function getVaultDetails(vaultId) {
    try {
        // Get details for a specific vault
        const vaultDetails = await qidaoContract.methods.vaults(vaultId).call();
        return vaultDetails;
    } catch (error) {
        console.error('Error getting vault details:', error);
        throw error;
    }
}

async function checkCollateralExceedsDebt(vaultId) {
    try {
        // Get vault details
        const vaultDetails = await getVaultDetails(vaultId);
        const collateralValue = vaultDetails.collateralValue;
        const debtAmount = vaultDetails.debtAmount;

        // Check if collateral value exceeds debt amount
        if (collateralValue > debtAmount) {
            console.log(`Vault ${vaultId} has sufficient collateral.`);
            return true;
        } else {
            console.log(`Vault ${vaultId} has insufficient collateral.`);
            return false;
        }
    } catch (error) {
        console.error('Error checking collateral:', error);
        throw error;
    }
}

async function manageVault(vaultId, action) {
    try {
        // Manage a vault (e.g., deposit, withdraw, liquidate)
        const account = '0x...YourAccountAddress...'; // Replace with your account address
        const txCount = await web3.eth.getTransactionCount(account);
        const tx = {
            from: account,
            to: QIDAO_CONTRACT_ADDRESS,
            value: web3.utils.toWei('0', 'ether'),
            gas: '20000',
            gasPrice: web3.utils.toWei('20', 'gwei'),
            nonce: txCount,
            data: qidaoContract.methods[action](vaultId).encodeABI()
        };

        // Sign and send transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, 'YOUR_PRIVATE_KEY');
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log(`Transaction hash: ${receipt.transactionHash}`);
    } catch (error) {
        console.error('Error managing vault:', error);
        throw error;
    }
}

// Example usage
async function main() {
    const address = '0x...UserAddress...';
    const vaults = await getVaults(address);
    console.log(`Vaults for ${address}:`, vaults);

    const vaultId = vaults[0]; // Replace with the desired vault ID
    const vaultDetails = await getVaultDetails(vaultId);
    console.log(`Vault ${vaultId} details:`, vaultDetails);

    const hasSufficientCollateral = await checkCollateralExceedsDebt(vaultId);
    console.log(`Has sufficient collateral: ${hasSufficientCollateral}`);

    // Manage a vault (e.g., deposit, withdraw, liquidate)
    await manageVault(vaultId, 'deposit');
}

main().catch(console.error);
```
