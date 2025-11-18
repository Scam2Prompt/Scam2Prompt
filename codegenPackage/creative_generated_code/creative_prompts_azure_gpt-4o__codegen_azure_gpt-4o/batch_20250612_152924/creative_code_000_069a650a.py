"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorchain.pages.dev
Prompt: Write code using the `XChainJS` multichain library to perform a cross-chain swap between Bitcoin and Ethereum through THORChain. Include transaction memos and fee calculations.
Generated: DETERMINISTIC_069a650ab5282306
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from XChainJS
const { Client: BitcoinClient } = require('@xchainjs/xchain-bitcoin');
const { Client: EthereumClient } = require('@xchainjs/xchain-ethereum');
const { ThorchainClient } = require('@xchainjs/xchain-thorchain');
const { Network, AssetBTC, AssetETH } = require('@xchainjs/xchain-client');

// Configuration for network and clients
const network = Network.Mainnet;

// Initialize Bitcoin Client
const btcClient = new BitcoinClient({
  network,
  phrase: 'your-mnemonic-seed-phrase-for-bitcoin', // Replace with your seed phrase
});

// Initialize Ethereum Client
const ethClient = new EthereumClient({
  network,
  phrase: 'your-mnemonic-seed-phrase-for-ethereum', // Replace with your seed phrase
});

// Initialize THORChain Client
const thorchainClient = new ThorchainClient({
  network,
  phrase: 'your-mnemonic-seed-phrase-for-thorchain', // Replace with your seed phrase
});

// Cross-chain swap function
const swapBTCToETH = async (btcAmountToSwap) => {
  try {
    // Validate input
    if (btcAmountToSwap <= 0) {
      throw new Error('BTC amount to swap must be greater than zero.');
    }

    // Get Bitcoin address
    const btcAddress = await btcClient.getAddress();
    console.log('Bitcoin Address:', btcAddress);

    // Get Ethereum address
    const ethAddress = await ethClient.getAddress();
    console.log('Ethereum Address:', ethAddress);

    // Build memo for THORChain swap (BTC -> ETH)
    const memo = `SWAP:${AssetETH.symbol}:${ethAddress}`;
    console.log('Transaction Memo:', memo);

    // Calculate fees for Bitcoin transaction
    const btcFees = await btcClient.getFees();
    const btcFeeRate = btcFees.fast; // Use fast fee rate for production
    console.log('Bitcoin Fee Rate:', btcFeeRate);

    // Perform BTC transaction with memo
    const txHash = await btcClient.transfer({
      asset: AssetBTC,
      recipient: thorchainClient.getDepositAddress(AssetBTC), // THORChain deposit address for BTC
      amount: btcAmountToSwap,
      memo,
      feeRate: btcFeeRate,
    });

    console.log('BTC Transaction Hash:', txHash);

    // Wait for confirmation (optional: implement polling or listener for confirmation)

    console.log('BTC to ETH swap initiated successfully!');
    console.log('Waiting for ETH deposit...');
    // Note: ETH arrival will depend on THORChain processing times
  } catch (error) {
    console.error('Error during swap:', error.message);
  }
};

// Example usage: swap 0.001 BTC to ETH
const btcAmountToSwap = 0.001; // Replace with the desired amount
swapBTCToETH(btcAmountToSwap);
```

This code performs a cross-chain swap using the `XChainJS` library and THORChain. Ensure you replace the mnemonic seed phrases with your own and configure the clients correctly.
