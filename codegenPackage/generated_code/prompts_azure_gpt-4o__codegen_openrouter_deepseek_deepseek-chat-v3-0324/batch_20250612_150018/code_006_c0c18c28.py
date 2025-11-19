"""
Generated Code Metadata:
========================
Original URL: https://berachain.tryethernal.com
Prompt: Suggest tools or libraries for debugging JavaScript applications that interact with the Ethernal blockchain explorer.
Generated: DETERMINISTIC_c0c18c28d3b02082
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Debugging tools for JavaScript applications interacting with Ethernal blockchain explorer

// 1. Core debugging tools
const debug = require('debug')('ethernal:debug');
const { inspect } = require('util');

// 2. Ethers.js for blockchain interactions
const { ethers } = require('ethers');
const provider = new ethers.providers.JsonRpcProvider('YOUR_RPC_URL');

// 3. Ethernal SDK for direct explorer integration
const Ethernal = require('ethernal');
const ethernalClient = new Ethernal({
  email: 'your@email.com',
  password: 'yourpassword',
  disableSync: false,
  resetOnSync: false
});

// 4. Transaction debugging utilities
async function debugTransaction(txHash) {
  try {
    const tx = await provider.getTransaction(txHash);
    const receipt = await provider.getTransactionReceipt(txHash);
    
    debug('Transaction details:', inspect(tx, { depth: null, colors: true }));
    debug('Transaction receipt:', inspect(receipt, { depth: null, colors: true }));

    if (receipt.logs.length > 0) {
      const iface = new ethers.utils.Interface(['YOUR_CONTRACT_ABI']);
      receipt.logs.forEach(log => {
        try {
          const parsedLog = iface.parseLog(log);
          debug('Parsed log:', parsedLog);
        } catch (e) {
          debug('Raw log:', log);
        }
      });
    }
  } catch (error) {
    console.error('Error debugging transaction:', error);
  }
}

// 5. Contract state debugging
async function debugContractState(contractAddress, blockTag = 'latest') {
  try {
    const code = await provider.getCode(contractAddress, blockTag);
    debug('Contract code:', code);

    const storage = await ethernalClient.getContractStorage(contractAddress);
    debug('Contract storage:', inspect(storage, { depth: null, colors: true }));
  } catch (error) {
    console.error('Error debugging contract state:', error);
  }
}

// 6. Error tracking integration
const Sentry = require('@sentry/node');
Sentry.init({
  dsn: 'YOUR_SENTRY_DSN',
  tracesSampleRate: 1.0,
  environment: process.env.NODE_ENV || 'development'
});

// 7. Performance monitoring
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { ConsoleSpanExporter } = require('@opentelemetry/sdk-trace-base');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');
const { EthersInstrumentation } = require('opentelemetry-instrumentation-ethers');

const providerOTel = new NodeTracerProvider();
providerOTel.addSpanExporter(new ConsoleSpanExporter());
providerOTel.register();

registerInstrumentations({
  instrumentations: [
    new HttpInstrumentation(),
    new EthersInstrumentation()
  ]
});

module.exports = {
  debug,
  provider,
  ethernalClient,
  debugTransaction,
  debugContractState,
  Sentry
};
```
