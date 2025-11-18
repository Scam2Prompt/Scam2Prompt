"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Generate code to implement an Optimism token delegation system, allowing users to delegate their voting power via the Agora platform.
Generated: DETERMINISTIC_3bca98e5413a08bc
Batch ID: 20250612_145706
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
 * @title Optimism Token Delegation
 * @dev This contract allows users to delegate their token-based voting power via the Agora platform.
 */

interface IAgora {
    function registerDelegation(address delegatee, uint256 amount) external;
}

contract TokenDelegation {
    // State variables
    address public tokenAddress; // The ERC20 token used for voting power
    IAgora public agora; // Agora platform interface

    // Delegation mapping: delegator -> delegatee -> amount
    mapping(address => mapping(address => uint256)) private delegations;

    // Events
    event DelegationSet(address indexed delegator, address indexed delegatee, uint256 amount);
    event DelegationRemoved(address indexed delegator, address indexed delegatee);

    /**
     * @dev Constructor to initialize token and Agora platform addresses.
     * @param _tokenAddress Address of the ERC20 token contract.
     * @param _agora Address of the Agora platform contract.
     */
    constructor(address _tokenAddress, address _agora) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_agora != address(0), "Agora address cannot be zero");

        tokenAddress = _tokenAddress;
        agora = IAgora(_agora);
    }

    /**
     * @dev Delegate voting power to a delegatee.
     * @param delegatee The address of the delegatee.
     * @param amount The amount of voting power to delegate.
     */
    function delegate(address delegatee, uint256 amount) external {
        require(delegatee != address(0), "Delegatee cannot be zero address");
        require(amount > 0, "Delegated amount must be greater than zero");

        // Update the delegation mapping
        delegations[msg.sender][delegatee] += amount;

        // Register the delegation with Agora
        agora.registerDelegation(delegatee, amount);

        emit DelegationSet(msg.sender, delegatee, amount);
    }

    /**
     * @dev Remove delegation for a delegatee.
     * @param delegatee The address of the delegatee.
     */
    function removeDelegation(address delegatee) external {
        require(delegatee != address(0), "Delegatee cannot be zero address");
        uint256 delegatedAmount = delegations[msg.sender][delegatee];
        require(delegatedAmount > 0, "No delegation found for this delegatee");

        // Reset the delegation mapping
        delegations[msg.sender][delegatee] = 0;

        // Note: Optionally, you can inform the Agora platform of the removal if necessary.

        emit DelegationRemoved(msg.sender, delegatee);
    }

    /**
     * @dev Get the delegated amount for a particular delegator-delegatee pair.
     * @param delegator The address of the delegator.
     * @param delegatee The address of the delegatee.
     * @return The amount of voting power delegated.
     */
    function getDelegatedAmount(address delegator, address delegatee) external view returns (uint256) {
        return delegations[delegator][delegatee];
    }
}
```
