"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaingpt-airdrop.pages.dev
Prompt: Create a smart contract for fair token distribution in an airdrop campaign, leveraging ChainGPT's AI-powered distribution model.
Generated: DETERMINISTIC_4f3e1aaccb08e78b
Batch ID: 20250612_152526
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FairTokenAirdrop
 * @dev A smart contract for fair token distribution during an airdrop campaign.
 */
contract FairTokenAirdrop is Ownable {
    // The token to be distributed
    IERC20 public token;

    // Mapping to track if an address has claimed tokens
    mapping(address => bool) public hasClaimed;

    // Total amount of tokens allocated for the airdrop
    uint256 public airdropAmount;

    // Event to log the airdrop
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address and total airdrop amount.
     * @param _token The address of the ERC20 token to be distributed.
     * @param _airdropAmount The total amount of tokens allocated for the airdrop.
     */
    constructor(IERC20 _token, uint256 _airdropAmount) {
        require(address(_token) != address(0), "Invalid token address");
        require(_airdropAmount > 0, "Airdrop amount must be greater than zero");

        token = _token;
        airdropAmount = _airdropAmount;
    }

    /**
     * @dev Function to distribute tokens to eligible recipients.
     * @param recipients An array of addresses to receive tokens.
     * @param amounts An array of amounts corresponding to each recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            // Ensure the recipient has not claimed tokens yet
            require(!hasClaimed[recipients[i]], "Recipient has already claimed tokens");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer the specified amount to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            // Mark the recipient as having claimed their tokens
            hasClaimed[recipients[i]] = true;

            // Emit the TokensDistributed event
            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to withdraw any tokens accidentally sent to this contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        bool success = token.transfer(owner(), _amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Function to get the balance of tokens held by the contract.
     * @return The balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }

    /**
     * @dev Function to check if an address has claimed their tokens.
     * @param recipient The address to check.
     * @return True if the address has claimed, otherwise false.
     */
    function hasClaimedTokens(address recipient) external view returns (bool) {
        return hasClaimed[recipient];
    }
}
```
