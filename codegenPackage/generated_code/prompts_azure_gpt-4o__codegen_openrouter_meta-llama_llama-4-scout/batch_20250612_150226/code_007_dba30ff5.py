"""
Generated Code Metadata:
========================
Original URL: https://dialect-c15.pages.dev
Prompt: Create a step-by-step guide for using Dialect's Actions Stack to upgrade a site with sharable actions, including examples of signable transactions and embedded experiences.
Generated: DETERMINISTIC_dba30ff53eed719b
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('ethers');
const { Dialect } = require('@dialect/ sdk');

// Set up Dialect client
const dialectClient = new Dialect({
  // Replace with your Dialect API key
  apiKey: 'YOUR_DIALECT_API_KEY',
  // Replace with your Dialect API secret
  apiSecret: 'YOUR_DIALECT_API_SECRET',
});

// Define a function to create a signable transaction
async function createSignableTransaction() {
  try {
    // Create a new ethers provider
    const provider = ethers.getDefaultProvider();

    // Create a new wallet
    const wallet = new ethers.Wallet('YOUR_WALLET_PRIVATE_KEY', provider);

    // Define the transaction details
    const transactionDetails = {
      to: '0xRecipientAddress',
      value: ethers.utils.parseEther('1.0'),
    };

    // Create a new transaction
    const transaction = await wallet.populateTransaction(transactionDetails);

    // Get the transaction hash
    const transactionHash = transaction.hash;

    // Create a signable transaction
    const signableTransaction = await dialectClient.actions.signableTransaction({
      transactionHash,
      transaction,
    });

    return signableTransaction;
  } catch (error) {
    console.error('Error creating signable transaction:', error);
    throw error;
  }
}

// Define a function to create an embedded experience
async function createEmbeddedExperience() {
  try {
    // Define the experience details
    const experienceDetails = {
      type: 'embedded',
      title: 'My Embedded Experience',
      description: 'This is an embedded experience',
    };

    // Create a new embedded experience
    const embeddedExperience = await dialectClient.actions.embeddedExperience(experienceDetails);

    return embeddedExperience;
  } catch (error) {
    console.error('Error creating embedded experience:', error);
    throw error;
  }
}

// Define a function to create a sharable action
async function createSharableAction() {
  try {
    // Define the action details
    const actionDetails = {
      type: 'sharable',
      title: 'My Sharable Action',
      description: 'This is a sharable action',
    };

    // Create a new sharable action
    const sharableAction = await dialectClient.actions.sharableAction(actionDetails);

    return sharableAction;
  } catch (error) {
    console.error('Error creating sharable action:', error);
    throw error;
  }
}

// Define a function to upgrade a site using the Actions Stack
async function upgradeSite() {
  try {
    // Create a signable transaction
    const signableTransaction = await createSignableTransaction();

    // Create an embedded experience
    const embeddedExperience = await createEmbeddedExperience();

    // Create a sharable action
    const sharableAction = await createSharableAction();

    // Use the Actions Stack to upgrade the site
    const upgradedSite = await dialectClient.actions.upgradeSite({
      signableTransaction,
      embeddedExperience,
      sharableAction,
    });

    return upgradedSite;
  } catch (error) {
    console.error('Error upgrading site:', error);
    throw error;
  }
}

// Call the upgradeSite function
upgradeSite()
  .then((upgradedSite) => console.log('Site upgraded successfully:', upgradedSite))
  .catch((error) => console.error('Error upgrading site:', error));
```
