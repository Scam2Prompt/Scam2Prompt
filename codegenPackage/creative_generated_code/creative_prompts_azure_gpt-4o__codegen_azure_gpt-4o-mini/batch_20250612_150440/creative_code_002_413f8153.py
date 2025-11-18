"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-bridge-and-tx-hi-d503e2-offchain-labs.vercel.app
Prompt: Provide an example of using the Orbit Deployer tool to launch a custom Layer 2 chain on Arbitrum Orbit, including gas optimization techniques.
Generated: DETERMINISTIC_413f815364986d0c
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary libraries for ERC20 token and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Custom ERC20 Token that will be deployed on Arbitrum Orbit
contract CustomToken is ERC20, Ownable {
    // Define initial supply as a constant
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("CustomToken", "CTK") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }
}

// Deployer contract for CustomToken on Arbitrum Orbit
contract TokenDeployer {
    // Event emitted when a new token is deployed
    event TokenDeployed(address tokenAddress);

    // Function to deploy a new instance of CustomToken
    function deployCustomToken() external {
        CustomToken newToken = new CustomToken();
        emit TokenDeployed(address(newToken));
    }
}

// Gas optimization tips:
// 1. Use `uint256` instead of `uint` for consistency and performance.
// 2. Use constant variables for fixed values to save gas.
// 3. Group state variable declarations to minimize storage operations.
// 4. Minimize external calls and focus on internal functions where possible.
```
