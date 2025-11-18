"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testforfucksakeqq.com
Prompt: Generate a smart contract snippet that facilitates delegation of staked EIGEN tokens on EigenLayer.
Generated: DETERMINISTIC_ae317d96341cba1c
Batch ID: 20250612_153947
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
 * @title EigenLayer Delegation Contract
 * @dev This contract facilitates the delegation of staked EIGEN tokens. 
 * Users can delegate their tokens to a delegatee and withdraw when needed.
 */

interface IEigenToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract EigenLayerDelegation {
    // Address of the EIGEN token contract
    IEigenToken public immutable eigenToken;

    // Mapping of delegators to their delegatees and staked amounts
    mapping(address => Delegation) public delegations;

    struct Delegation {
        address delegatee;
        uint256 amount;
    }

    // Event Definitions
    event Delegated(address indexed delegator, address indexed delegatee, uint256 amount);
    event Withdrawn(address indexed delegator, address indexed delegatee, uint256 amount);

    /**
     * @dev Constructor to set the EIGEN token address
     * @param _eigenToken Address of the EIGEN token contract
     */
    constructor(address _eigenToken) {
        require(_eigenToken != address(0), "Invalid token address");
        eigenToken = IEigenToken(_eigenToken);
    }

    /**
     * @dev Function to delegate staked EIGEN tokens to a delegatee
     * @param delegatee Address of the delegatee
     * @param amount Amount of tokens to delegate
     */
    function delegate(address delegatee, uint256 amount) external {
        require(delegatee != address(0), "Delegatee address cannot be zero");
        require(amount > 0, "Delegation amount must be greater than zero");

        // Transfer tokens from delegator to contract
        require(eigenToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Store delegation details
        delegations[msg.sender] = Delegation(delegatee, amount);

        emit Delegated(msg.sender, delegatee, amount);
    }

    /**
     * @dev Function to withdraw delegated tokens
     */
    function withdraw() external {
        Delegation memory delegation = delegations[msg.sender];
        require(delegation.amount > 0, "No tokens delegated");

        // Clear delegation data
        delete delegations[msg.sender];

        // Transfer tokens back to delegator
        require(eigenToken.transferFrom(address(this), msg.sender, delegation.amount), "Token transfer failed");

        emit Withdrawn(msg.sender, delegation.delegatee, delegation.amount);
    }

    /**
     * @dev View function to check the delegation details of a user
     * @param delegator Address of the delegator
     * @return Delegatee address and staked amount
     */
    function getDelegation(address delegator) external view returns (address delegatee, uint256 amount) {
        Delegation memory delegation = delegations[delegator];
        return (delegation.delegatee, delegation.amount);
    }
}
```
