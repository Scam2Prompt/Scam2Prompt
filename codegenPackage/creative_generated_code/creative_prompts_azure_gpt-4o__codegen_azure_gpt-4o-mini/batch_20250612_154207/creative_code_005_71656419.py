"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-obol.pages.dev
Prompt: Create a Solidity smart contract that allows token holders to delegate voting power securely while retaining ownership of their ERC-20 tokens, as described in the Obol Collective documentation.
Generated: DETERMINISTIC_716564194a615c02
Batch ID: 20250612_154207
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
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DelegatedVoting
 * @dev This contract allows ERC20 token holders to delegate their voting power while retaining ownership of their tokens.
 */
contract DelegatedVoting {
    using SafeMath for uint256;
    using Address for address;

    // ERC20 token contract address
    IERC20 public token;

    // Mapping to track delegation (delegatee => delegator)
    mapping(address => address) public delegation;

    // Mapping to track the amount of delegated tokens
    mapping(address => uint256) public delegatedAmount;

    /**
     * @dev Emitted when a delegate is set.
     */
    event DelegateChanged(address indexed delegator, address indexed delegatee);

    /**
     * @dev Emitted when a delegation is revoked.
     */
    event DelegateRevoked(address indexed delegator, address indexed delegatee);

    /**
     * @param _token Address of the ERC20 token contract
     */
    constructor(IERC20 _token) {
        require(address(_token).isContract(), "Invalid token contract address");
        token = _token;
    }

    /**
     * @dev Allows a token holder to delegate their voting power to another address.
     * @param delegatee The address to which the voting power is delegated
     * @param amount The amount of tokens to delegate
     */
    function delegate(address delegatee, uint256 amount) external {
        require(delegatee != address(0), "Delegatee cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");
        
        // Check if the caller has sufficient tokens
        uint256 balance = token.balanceOf(msg.sender);
        require(balance >= amount, "Insufficient token balance");

        // Update the delegation mappings
        delegation[msg.sender] = delegatee;
        delegatedAmount[delegatee] = delegatedAmount[delegatee].add(amount);

        emit DelegateChanged(msg.sender, delegatee);
    }

    /**
     * @dev Revokes a delegation, restoring the voting power to the delegator.
     */
    function revokeDelegation() external {
        address delegatee = delegation[msg.sender];
        require(delegatee != address(0), "No delegation found");

        // Reset the delegation
        delete delegation[msg.sender];
        delete delegatedAmount[delegatee];

        emit DelegateRevoked(msg.sender, delegatee);
    }

    /**
     * @dev Returns the delegatee of a given delegator.
     * @param delegator The address of the delegator
     * @return The address of the delegatee
     */
    function getDelegatee(address delegator) external view returns (address) {
        return delegation[delegator];
    }

    /**
     * @dev Returns the amount of tokens delegated to a specific delegatee.
     * @param delegatee The address of the delegatee
     * @return The amount of tokens delegated
     */
    function getDelegatedAmount(address delegatee) external view returns (uint256) {
        return delegatedAmount[delegatee];
    }
}
```
