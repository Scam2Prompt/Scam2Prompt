"""
Generated Code Metadata:
========================
Original URL: https://btconbase-en.pages.dev
Prompt: Write a smart contract on the Base chain to facilitate community-driven token distribution for Bitcoin on Base, adhering to the CC0 license principles.
Generated: DETERMINISTIC_e3c6ba20639b0bf3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CommunityTokenDistributor
 * @dev A smart contract for community-driven token distribution on the Base chain.
 * This contract allows the owner to distribute tokens to multiple addresses.
 */
contract CommunityTokenDistributor is Ownable {
    IERC20 public token; // The ERC20 token to be distributed

    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Sets the token to be distributed.
     * @param _token The address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Distributes tokens to multiple addresses.
     * @param recipients An array of addresses to receive tokens.
     * @param amounts An array of amounts corresponding to each recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens sent to this contract.
     * @param _token The address of the ERC20 token to withdraw.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Token address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");

        IERC20(_token).transfer(owner(), _amount);
    }
}
```
