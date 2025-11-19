"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashstakeio.pages.dev
Prompt: Write a code snippet that allows users to lock up crypto on Flashstake and instantly receive upfront yield for a specified duration.
Generated: DETERMINISTIC_965e45d40ec1d569
Batch ID: 20250612_163601
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
 * @title Flashstake Contract
 * @dev This contract allows users to lock up cryptocurrency and receive upfront yield.
 */
contract Flashstake {
    // Events
    event Staked(address indexed user, uint256 amount, uint256 duration, uint256 yield);
    event YieldPaid(address indexed user, uint256 yield);

    // State variables
    address public owner; // Owner of the contract
    uint256 public yieldRate; // Yield rate per second, e.g., 0.01% yield per second
    mapping(address => uint256) public balances; // Mapping of user balances

    // Constructor
    constructor(uint256 _yieldRate) {
        require(_yieldRate > 0, "Yield rate must be greater than zero");
        owner = msg.sender; // Set contract owner
        yieldRate = _yieldRate; // Set yield rate
    }

    /**
     * @dev Stake tokens and receive upfront yield.
     * @param _duration Duration in seconds for which tokens will be locked.
     */
    function stake(uint256 _duration) external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Calculate upfront yield
        uint256 yield = (msg.value * yieldRate * _duration) / (100 * 1 ether);
        require(yield > 0, "Yield must be greater than zero");

        // Update user balances
        balances[msg.sender] += msg.value;

        // Emit event for staking
        emit Staked(msg.sender, msg.value, _duration, yield);

        // Pay upfront yield to the user
        (bool success, ) = msg.sender.call{value: yield}("");
        require(success, "Yield payment failed");

        // Emit event for yield payment
        emit YieldPaid(msg.sender, yield);
    }

    /**
     * @dev Withdraw staked funds after lock duration. (Prototype, actual implementation may vary)
     */
    function withdraw() external {
        // This function can be implemented to allow users to withdraw their staked funds after the duration ends.
        // For simplicity, the withdraw function logic is omitted in this code snippet.
    }

    /**
     * @dev Change yield rate (only owner).
     * @param _newYieldRate New yield rate per second.
     */
    function setYieldRate(uint256 _newYieldRate) external {
        require(msg.sender == owner, "Only owner can change the yield rate");
        require(_newYieldRate > 0, "Yield rate must be greater than zero");
        yieldRate = _newYieldRate;
    }

    /**
     * @dev Fallback function to manage accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct deposits are not allowed");
    }
}
```
