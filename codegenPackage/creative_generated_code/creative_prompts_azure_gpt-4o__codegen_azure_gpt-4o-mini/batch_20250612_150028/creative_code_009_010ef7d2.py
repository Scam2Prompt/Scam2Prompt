"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismsio.vercel.app
Prompt: Generate code to integrate an application with Optimism’s governance model, enabling users to delegate voting power on-chain.
Generated: DETERMINISTIC_010ef7d29cee3a30
Batch ID: 20250612_150028
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

interface IDelegator {
    function delegate(address to) external;
    function getDelegate() external view returns (address);
}

contract GovernanceDelegate is IDelegator {
    // Mapping of addresses to their delegated votes
    mapping(address => address) private _delegates;

    // Event emitted when delegation occurs
    event Delegated(address indexed delegator, address indexed to);

    /**
     * @dev Delegate voting power to a specific address
     * @param to The address to delegate voting power to
     */
    function delegate(address to) external override {
        require(to != address(0), "Cannot delegate to the zero address");
        require(to != msg.sender, "Cannot delegate to yourself");

        // Update the delegate mapping
        _delegates[msg.sender] = to;

        // Emit the delegation event
        emit Delegated(msg.sender, to);
    }

    /**
     * @dev Retrieve the address to which the caller has delegated their voting power
     * @return The address of the delegate
     */
    function getDelegate() external view override returns (address) {
        return _delegates[msg.sender];
    }

    /**
     * @dev Function to revoke delegation by setting delegate to zero address
     */
    function revokeDelegation() external {
        // Revoke the delegation by setting it to address(0)
        _delegates[msg.sender] = address(0);
        
        // Emit the revocation event
        emit Delegated(msg.sender, address(0));
    }

    /**
     * @dev Check if an address is a delegate of a specific account
     * @param delegator The address of the delegator
     * @param delegatee The address of the potential delegate
     * @return True if delegatee is the delegate of delegator, false otherwise
     */
    function isDelegate(address delegator, address delegatee) external view returns (bool) {
        return _delegates[delegator] == delegatee;
    }
}
```

This smart contract allows users to delegate their voting power on-chain in accordance with Optimism's governance model. It includes functions to delegate, revoke delegation, and check the delegation status, while ensuring proper error handling and emitting relevant events.
