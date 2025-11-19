"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: How do I create a contract facet bundle in Zoe using the Agoric SDK, and what is the significance of this bundle in contract development?
Generated: DETERMINISTIC_c05125f369bdced7
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules from the Agoric SDK
const { E, Far, contract, makeIssuerKit, prepare } = require('agoric-sdk');
const { Zoe } = require('zoe');

// Define a contract for a simple escrow
const escrowContract = contract({
  // Initialize the contract with an invitation
  init: (invitation) => {
    // Create a new issuer kit for the payout
    const payoutKit = makeIssuerKit('Payout');
    // Store the payout kit and invitation
    return { invitation, payoutKit };
  },
  // Method to deposit funds into the escrow
  deposit: (state, payment, paymentIssuer) => {
    // Check if the payment is valid
    if (!payment || !paymentIssuer) {
      throw new Error('Invalid payment');
    }
    // Add the payment to the payout kit
    state.payoutKit.issuer.addAmount(state.payoutKit.issuer.makeEmpty(), payment, paymentIssuer);
    return state;
  },
  // Method to withdraw funds from the escrow
  withdraw: (state) => {
    // Get the payout from the payout kit
    const payout = state.payoutKit.issuer.getCurrentAmount();
    // Remove the payout from the payout kit
    state.payoutKit.issuer.subtractAmount(state.payoutKit.issuer.makeEmpty(), payout);
    return payout;
  },
});

// Create a Zoe contract facet
const makeEscrowFacet = (zoe, terms) => {
  // Create a new contract instance
  return E(zoe).makeInstance(escrowContract, terms);
};

// Create a contract facet bundle
const createContractFacetBundle = async (zoe, terms) => {
  try {
    // Create a new contract facet
    const escrowFacet = await makeEscrowFacet(zoe, terms);
    // Return the contract facet
    return Far('EscrowFacet', {
      getContract: () => escrowFacet,
    });
  } catch (error) {
    // Handle any errors
    console.error('Error creating contract facet bundle:', error);
    throw error;
  }
};

// Prepare the contract facet bundle for use
prepare(createContractFacetBundle);

// Example usage
const main = async () => {
  // Create a new Zoe instance
  const zoe = Zoe.make();
  // Define the terms for the contract
  const terms = {
    // Define the payout
    payout: 100,
  };
  // Create a new contract facet bundle
  const escrowFacetBundle = await createContractFacetBundle(zoe, terms);
  // Use the contract facet bundle
  const escrowFacet = await escrowFacetBundle.getContract();
  // Deposit funds into the escrow
  await E(escrowFacet).deposit(100, 'Payment');
  // Withdraw funds from the escrow
  const payout = await E(escrowFacet).withdraw();
  console.log('Payout:', payout);
};

main();
```
