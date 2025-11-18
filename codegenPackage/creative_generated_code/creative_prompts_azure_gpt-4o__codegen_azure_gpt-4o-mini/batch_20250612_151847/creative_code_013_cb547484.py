"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tortoken.io
Prompt: Create a Solidity contract for an airdrop program that distributes 25% of the total TOR token supply to eligible users based on specific conditions.
Generated: DETERMINISTIC_cb5474848a7bcea2
Batch ID: 20250612_151847
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

// Interface for the TOR token contract
interface IToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Airdrop contract for distributing TOR tokens
contract Airdrop {
    // Total supply of TOR tokens
    uint256 public constant TOTAL_TOR_SUPPLY = 1000000 * 10**18; // Example total supply
    uint256 public constant AIRDROP_AMOUNT = TOTAL_TOR_SUPPLY * 25 / 100; // 25% for airdrop
    uint256 public distributedAmount; // Amount already distributed
    IToken public torToken; // Instance of the TOR token contract

    // Mapping to track eligible users
    mapping(address => bool) public isEligible;

    // Event emitted when tokens are distributed
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Modifier to check eligibility
    modifier onlyEligible() {
        require(isEligible[msg.sender], "Not eligible for airdrop");
        _;
    }

    // Constructor to initialize the contract with the TOR token address
    constructor(address _torToken) {
        torToken = IToken(_torToken);
    }

    // Function to set eligibility for users (can be restricted to owner or admin)
    function setEligibility(address[] calldata users, bool eligibility) external {
        // In production, restrict access to an admin
        for (uint256 i = 0; i < users.length; i++) {
            isEligible[users[i]] = eligibility;
        }
    }

    // Function to distribute TOR tokens to eligible users
    function distributeTokens() external onlyEligible {
        require(distributedAmount < AIRDROP_AMOUNT, "All tokens have been distributed");

        uint256 amountToDistribute = AIRDROP_AMOUNT - distributedAmount;
        // Transfer tokens to the user
        require(torToken.transfer(msg.sender, amountToDistribute), "Token transfer failed");

        // Update the distributed amount
        distributedAmount += amountToDistribute;

        // Emit event for distribution
        emit AirdropDistributed(msg.sender, amountToDistribute);
    }

    // Function to withdraw remaining tokens in case of emergency
    function withdrawRemainingTokens() external {
        require(msg.sender == address(this), "Only contract can withdraw remaining tokens");
        uint256 remainingAmount = torToken.balanceOf(address(this));
        require(remainingAmount > 0, "No remaining tokens to withdraw");

        require(torToken.transfer(msg.sender, remainingAmount), "Withdraw failed");
    }

    // Function to check the contract's balance of TOR tokens
    function getContractBalance() external view returns (uint256) {
        return torToken.balanceOf(address(this));
    }
}
```
