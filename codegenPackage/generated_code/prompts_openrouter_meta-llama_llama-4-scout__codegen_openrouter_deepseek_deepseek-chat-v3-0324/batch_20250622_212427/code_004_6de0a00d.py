"""
Generated Code Metadata:
========================
Original URL: https://celestia-orbit.vercel.app
Prompt: Generate an example of a deployed Orbit chain configuration file for Arbitrum Orbit.
Generated: DETERMINISTIC_6de0a00d8e4320b2
Batch ID: 20250622_212427
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://myorbitchain.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8545": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://explorer.myorbitchain.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://arbitrum-mainnet.infura.io/v3/YOUR_INFURA_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```json
{
  "chain": {
    "name": "MyOrbitChain",
    "chainId": 12345,
    "networkId": 12345,
    "rollup": {
      "type": "arbitrum",
      "version": "nitro",
      "parentChainId": 42161,
      "parentChainRpcUrl": "https://arbitrum-mainnet.infura.io/v3/YOUR_INFURA_KEY",
      "sequencerAddress": "0x1234567890123456789012345678901234567890",
      "inboxAddress": "0x1234567890123456789012345678901234567890",
      "outboxAddress": "0x1234567890123456789012345678901234567890",
      "bridgeAddress": "0x1234567890123456789012345678901234567890",
      "rollupAddress": "0x1234567890123456789012345678901234567890"
    },
    "rpc": [
      {
        "url": "https://myorbitchain.example.com",
        "rateLimit": 1000
      }
    ],
    "explorers": [
      {
        "name": "Blockscout",
        "url": "https://explorer.myorbitchain.example.com",
        "standard": "EIP3091"
      }
    ],
    "nativeCurrency": {
      "name": "Ether",
      "symbol": "ETH",
      "decimals": 18
    },
    "infoURL": "https://myorbitchain.example.com",
    "shortName": "moc",
    "chainType": "arbitrum-orbit",
    "icon": {
      "url": "ipfs://QmXYZ123",
      "width": 256,
      "height": 256,
      "format": "png"
    },
    "features": [
      {
        "name": "EIP1559"
      },
      {
        "name": "EIP155"
      }
    ]
  },
  "batchPoster": {
    "enable": true,
    "maxBatchSize": 100000,
    "batchFrequencyMs": 1000
  },
  "staker": {
    "enable": true,
    "strategy": "interval",
    "intervalMs": 60000,
    "minBalanceEth": 0.1
  },
  "node": {
    "l1RpcUrl": "https://arbitrum-mainnet.infura.io/v3/YOUR_INFURA_KEY",
    "l2ChainId": 12345,
    "l2RpcUrl": "http://localhost:8545",
    "l2WalletPrivateKey": "0xYOUR_PRIVATE_KEY",
    "sequencer": {
      "enable": true,
      "maxTxSizeBytes": 100000,
      "maxBlockSizeBytes": 1000000
    },
    "validator": {
      "enable": true,
      "requiredStakeEth": 0.1,
      "challengePeriodBlocks": 100
    }
  },
  "inbox": {
    "address": "0x1234567890123456789012345678901234567890",
    "topic": "0x1234567890123456789012345678901234567890"
  },
  "outbox": {
    "address": "0x1234567890123456789012345678901234567890",
    "topic": "0x1234567890123456789012345678901234567890"
  },
  "bridge": {
    "address": "0x1234567890123456789012345678901234567890",
    "l1GatewayRouter": "0x1234567890123456789012345678901234567890",
    "l2GatewayRouter": "0x1234567890123456789012345678901234567890"
  },
  "gas": {
    "priceOracle": {
      "type": "fixed",
      "gasPrice": 1000000000
    },
    "maxGasPerTx": 30000000,
    "minGasPerTx": 21000
  },
  "whitelist": {
    "enable": false,
    "contracts": []
  }
}
```
