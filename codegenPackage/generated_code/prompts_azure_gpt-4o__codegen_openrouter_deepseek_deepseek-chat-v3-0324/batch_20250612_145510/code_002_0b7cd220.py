"""
Generated Code Metadata:
========================
Original URL: https://mainnet-dioneprotocol.pages.dev
Prompt: Generate code for deploying an ERC-20 token on the Odyssey Chain using Remix or Truffle, ensuring compatibility with its high transaction throughput of up to 4,500 transactions per second.
Generated: DETERMINISTIC_0b7cd220c5c803e1
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title OdysseyERC20
 * @dev Standard ERC20 token with minting capabilities, optimized for high throughput chains
 */
contract OdysseyERC20 is ERC20, Ownable {
    uint256 private constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    
    /**
     * @dev Constructor that initializes the token with initial supply
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial supply to mint (sent to deployer)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        require(initialSupply <= MAX_SUPPLY, "Initial supply exceeds max supply");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to mint tokens (only owner)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting would exceed max supply");
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens from caller's balance
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }
}
```

```javascript
// migrations/1_deploy_odyssey_token.js
const OdysseyERC20 = artifacts.require("OdysseyERC20");

module.exports = function (deployer) {
  const name = "OdysseyToken";
  const symbol = "ODY";
  const initialSupply = web3.utils.toWei("1000000", "ether"); // 1 million tokens
  
  deployer.deploy(OdysseyERC20, name, symbol, initialSupply);
};
```

```javascript
// truffle-config.js
module.exports = {
  networks: {
    odyssey: {
      host: "127.0.0.1",     // Odyssey Chain RPC endpoint
      port: 8545,            // Odyssey Chain port
      network_id: "*",       // Any network ID
      gas: 5000000,          // Gas limit
      gasPrice: 20000000000  // Gas price (20 Gwei)
    }
  },
  compilers: {
    solc: {
      version: "0.8.0",      // Match contract version
      settings: {
        optimizer: {
          enabled: true,
          runs: 200
        }
      }
    }
  }
};
```
