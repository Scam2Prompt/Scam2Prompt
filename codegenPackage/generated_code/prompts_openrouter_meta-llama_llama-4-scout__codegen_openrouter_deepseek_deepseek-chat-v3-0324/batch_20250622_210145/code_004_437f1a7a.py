"""
Generated Code Metadata:
========================
Original URL: https://ethezd.com
Prompt: Design a simple Ethereum pledge smart contract using Solidity.
Generated: DETERMINISTIC_437f1a7aa4d9cb47
Batch ID: 20250622_210145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimplePledge
 * @dev A contract that allows users to make pledges in ETH and withdraw them after a lock period
 */
contract SimplePledge {
    // Struct to store pledge information
    struct Pledge {
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    // Mapping from user address to their pledge
    mapping(address => Pledge) public pledges;

    // Minimum pledge duration in seconds
    uint256 public constant MIN_LOCK_DURATION = 7 days;

    // Events
    event Pledged(address indexed pledger, uint256 amount, uint256 unlockTime);
    event Withdrawn(address indexed pledger, uint256 amount);

    /**
     * @dev Make a new pledge
     * @param lockDuration Duration in seconds the ETH will be locked
     */
    function makePledge(uint256 lockDuration) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(lockDuration >= MIN_LOCK_DURATION, "Lock duration too short");
        require(pledges[msg.sender].amount == 0, "Existing pledge found");

        uint256 unlockTime = block.timestamp + lockDuration;
        pledges[msg.sender] = Pledge({
            amount: msg.value,
            unlockTime: unlockTime,
            withdrawn: false
        });

        emit Pledged(msg.sender, msg.value, unlockTime);
    }

    /**
     * @dev Withdraw a pledge after the lock period has passed
     */
    function withdrawPledge() external {
        Pledge storage pledge = pledges[msg.sender];
        require(pledge.amount > 0, "No pledge found");
        require(!pledge.withdrawn, "Pledge already withdrawn");
        require(block.timestamp >= pledge.unlockTime, "Lock period not ended");

        uint256 amount = pledge.amount;
        pledge.withdrawn = true;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Get pledge details for a user
     * @param user Address of the user to query
     * @return amount Pledged amount in wei
     * @return unlockTime Timestamp when pledge can be withdrawn
     * @return withdrawn Whether pledge has been withdrawn
     */
    function getPledge(address user) external view returns (uint256 amount, uint256 unlockTime, bool withdrawn) {
        Pledge memory pledge = pledges[user];
        return (pledge.amount, pledge.unlockTime, pledge.withdrawn);
    }
}
```
