"""
Generated Code Metadata:
========================
Original URL: https://btwonsol-xyz.pages.dev
Prompt: Provide an example of a JSON configuration file for integrating $BTW token transactions into a Solana-based application.
Generated: DETERMINISTIC_7e4c38db334128bb
Batch ID: 20250612_151301
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://json-schema.org/draft-07/schema#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
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
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "BTW Token Integration Configuration",
  "description": "Configuration for integrating $BTW token transactions into a Solana-based application",
  "type": "object",
  "properties": {
    "network": {
      "description": "Solana network configuration",
      "type": "object",
      "properties": {
        "cluster": {
          "description": "Solana cluster endpoint",
          "type": "string",
          "enum": ["mainnet-beta", "testnet", "devnet"],
          "default": "mainnet-beta"
        },
        "endpoint": {
          "description": "Custom RPC endpoint URL",
          "type": "string",
          "default": "https://api.mainnet-beta.solana.com"
        }
      },
      "required": ["cluster"]
    },
    "token": {
      "description": "BTW token configuration",
      "type": "object",
      "properties": {
        "mintAddress": {
          "description": "BTW token mint address",
          "type": "string",
          "pattern": "^[1-9A-HJ-NP-Za-km-z]{32,44}$"
        },
        "decimals": {
          "description": "Number of decimal places for the token",
          "type": "integer",
          "minimum": 0,
          "maximum": 18,
          "default": 9
        },
        "symbol": {
          "description": "Token symbol",
          "type": "string",
          "default": "BTW"
        }
      },
      "required": ["mintAddress", "decimals"]
    },
    "wallet": {
      "description": "Wallet configuration",
      "type": "object",
      "properties": {
        "defaultSender": {
          "description": "Default sender wallet public key",
          "type": "string",
          "pattern": "^[1-9A-HJ-NP-Za-km-z]{32,44}$"
        },
        "feePayer": {
          "description": "Fee payer wallet public key",
          "type": "string",
          "pattern": "^[1-9A-HJ-NP-Za-km-z]{32,44}$"
        }
      }
    },
    "transactions": {
      "description": "Transaction settings",
      "type": "object",
      "properties": {
        "maxRetries": {
          "description": "Maximum number of transaction retries",
          "type": "integer",
          "minimum": 1,
          "maximum": 10,
          "default": 3
        },
        "confirmationTimeout": {
          "description": "Confirmation timeout in milliseconds",
          "type": "integer",
          "minimum": 1000,
          "default": 30000
        },
        "priorityFee": {
          "description": "Priority fee in lamports",
          "type": "integer",
          "minimum": 0,
          "default": 0
        }
      }
    },
    "logging": {
      "description": "Logging configuration",
      "type": "object",
      "properties": {
        "level": {
          "description": "Logging level",
          "type": "string",
          "enum": ["error", "warn", "info", "debug", "trace"],
          "default": "info"
        },
        "file": {
          "description": "Log file path",
          "type": "string"
        }
      }
    }
  },
  "required": ["network", "token"]
}
```
