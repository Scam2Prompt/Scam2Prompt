"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smart-5wk.pages.dev
Prompt: Create a Solidity smart contract that handles the distribution of $SLN tokens during an airdrop, ensuring compliance with the rules set by Smart Layer.
Generated: DETERMINISTIC_7231e063b471b125
Batch ID: 20250612_161224
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
 * @title SLNAirdrop
 * @dev A contract to handle the distribution of SLN tokens during an airdrop.
 * Ensures compliance with basic rules for distribution.
 */
contract SLNAirdrop {
    // Address of the SLN token contract
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the token address and the owner of the contract.
     * @param _token Address of the SLN token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute tokens during the airdrop.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts corresponding to each recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts arrays must have the same length");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Token amount must be greater than zero");

            // Transfer the tokens to the recipient
            require(token.transfer(recipients[i], amounts[i]), "Token transfer failed");

            // Emit event
            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
