"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cookie3454.pages.dev
Prompt: Develop a smart contract in Solidity for distributing $COOKIE tokens during an airdrop, inspired by the Cookie Community's process.
Generated: DETERMINISTIC_be7cfe71f4bf4cf0
Batch ID: 20250612_151003
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @title CookieAirdrop
 * @dev Smart contract for distributing $COOKIE tokens during an airdrop
 */
contract CookieAirdrop {
    // Address of the $COOKIE token contract
    IERC20 public cookieToken;
    
    // Owner of the contract
    address public owner;

    // Event triggered when an airdrop is executed
    event AirdropExecuted(address indexed recipient, uint256 amount);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to set the $COOKIE token contract address
     * @param _tokenAddress Address of the $COOKIE ERC20 token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        cookieToken = IERC20(_tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Function to execute the airdrop to multiple recipients
     * @param recipients Array of recipient addresses
     * @param amounts Array of amounts to distribute to each recipient (in wei)
     */
    function executeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid address");
            require(amounts[i] > 0, "Amount must be greater than 0");

            // Transfer $COOKIE tokens to the recipient
            bool success = cookieToken.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit AirdropExecuted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to withdraw tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from this contract to the owner
        bool success = cookieToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}
```
