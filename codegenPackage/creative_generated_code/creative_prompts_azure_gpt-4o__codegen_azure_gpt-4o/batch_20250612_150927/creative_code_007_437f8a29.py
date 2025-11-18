"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-q62.pages.dev
Prompt: Generate a Solidity contract that implements anti-dilution rebases for veAERO voters based on Aerodrome Finance's protocol mechanics.
Generated: DETERMINISTIC_437f8a2957de83cb
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title AntiDilutionRebase
 * @dev Implements anti-dilution rebasing for veAERO voters based on Aerodrome Finance mechanics.
 *      This contract ensures veAERO holders are protected against dilution during token supply changes.
 */
contract AntiDilutionRebase {
    // State variables
    address public owner;                 // Contract owner
    address public veAERO;               // Address of the veAERO token contract
    uint256 public lastRebaseTimestamp;  // Last time a rebase occurred
    uint256 public totalLocked;          // Total veAERO locked by all voters
    uint256 public totalSupply;          // Total AERO token supply
    uint256 public rebaseInterval;       // Minimum time interval between rebases

    // Events
    event RebaseExecuted(uint256 newTotalSupply, uint256 timestamp);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier ensureRebaseInterval() {
        require(block.timestamp >= lastRebaseTimestamp + rebaseInterval, "Rebase interval not met");
        _;
    }

    /**
     * @dev Constructor initializes the contract with owner and veAERO token address.
     * @param _veAERO Address of the veAERO token contract.
     * @param _rebaseInterval Minimum time interval between rebases in seconds.
     */
    constructor(address _veAERO, uint256 _rebaseInterval) {
        require(_veAERO != address(0), "Invalid veAERO address");
        require(_rebaseInterval > 0, "Rebase interval must be greater than zero");
        owner = msg.sender;
        veAERO = _veAERO;
        rebaseInterval = _rebaseInterval;
    }

    /**
     * @dev Updates the total AERO token supply. This function ensures anti-dilution measures.
     * @param newTotalSupply Updated total supply of AERO tokens.
     */
    function rebase(uint256 newTotalSupply) external onlyOwner ensureRebaseInterval {
        require(newTotalSupply > 0, "Total supply must be greater than zero");
        
        // Fetch current total veAERO locked
        totalLocked = IVeAERO(veAERO).totalLocked();

        require(totalLocked > 0, "No veAERO locked by voters");
        
        // Calculate new total supply and adjust if necessary
        totalSupply = newTotalSupply;
        
        // Notify veAERO contract of the supply change
        IVeAERO(veAERO).updateTotalSupply(totalSupply);
        
        // Update last rebase timestamp
        lastRebaseTimestamp = block.timestamp;

        emit RebaseExecuted(totalSupply, block.timestamp);
    }

    /**
     * @dev Transfers contract ownership to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

/**
 * @dev Interface for veAERO token contract.
 */
interface IVeAERO {
    function totalLocked() external view returns (uint256);
    function updateTotalSupply(uint256 newTotalSupply) external;
}
```
