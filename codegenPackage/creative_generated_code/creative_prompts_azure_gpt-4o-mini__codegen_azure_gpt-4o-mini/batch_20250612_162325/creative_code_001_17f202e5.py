"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop1.org
Prompt: Can you provide a code example for creating an airdrop smart contract on Ethereum?
Generated: DETERMINISTIC_17f202e52e404468
Batch ID: 20250612_162325
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
 * @title Airdrop
 * @dev Smart contract for distributing tokens to multiple addresses
 */
contract Airdrop {
    // Event to log the airdrop transaction
    event AirdropExecuted(address indexed recipient, uint256 amount);

    // Token to be distributed
    IERC20 public token;

    /**
     * @dev Sets the token to be used for the airdrop
     * @param _token The address of the token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Airdrop tokens to multiple addresses
     * @param recipients List of recipient addresses
     * @param amounts List of amounts to be sent to each recipient
     */
    function executeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external {
        require(recipients.length == amounts.length, "Recipients and amounts must have the same length");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit AirdropExecuted(recipients[i], amounts[i]); // Log the airdrop
        }
    }
}

/**
 * @title IERC20
 * @dev Interface for the ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
