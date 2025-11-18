"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ncdropofc.pages.dev
Prompt: Write a smart contract snippet for handling the distribution of NOT tokens in the Notcoin Airdrop system.
Generated: DETERMINISTIC_6981c4d427d1989c
Batch ID: 20250612_152358
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

/**
 * @title Notcoin Airdrop Smart Contract
 * @dev This contract handles the distribution of NOT tokens in the Notcoin Airdrop system.
 */
contract NotcoinAirdrop {
    // Token contract address
    address public tokenAddress;

    // Address of the contract owner
    address public owner;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "NotcoinAirdrop: Only owner can call this function");
        _;
    }

    // Constructor to initialize the token address and set the contract owner
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "NotcoinAirdrop: Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Distribute NOT tokens to a list of recipients.
     * @param recipients List of recipient addresses.
     * @param amounts Corresponding list of token amounts to distribute.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "NotcoinAirdrop: Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "NotcoinAirdrop: Invalid recipient address");
            require(amounts[i] > 0, "NotcoinAirdrop: Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = IERC20(tokenAddress).transfer(recipients[i], amounts[i]);
            require(success, "NotcoinAirdrop: Token transfer failed");

            // Emit event for successful distribution
            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param to Address to send the withdrawn tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "NotcoinAirdrop: Invalid withdrawal address");
        require(amount > 0, "NotcoinAirdrop: Amount must be greater than zero");

        bool success = IERC20(tokenAddress).transfer(to, amount);
        require(success, "NotcoinAirdrop: Token withdrawal failed");
    }
}

// IERC20 interface for interacting with the token contract
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
