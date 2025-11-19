"""
Generated Code Metadata:
========================
Original URL: https://tayloud.io
Prompt: Generate a Solidity smart contract that implements the fee split mechanism described on the Loud platform, allocating 4% to the system and distributing rewards to contributors.
Generated: DETERMINISTIC_e62e6b1521621fa8
Batch ID: 20250612_163224
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
 * @title FeeSplitContract
 * @dev Implements a fee split mechanism where 4% of the total amount is allocated to the system,
 * and the remaining is distributed among contributors based on their shares.
 */
contract FeeSplitContract {
    address public systemAddress; // Address to receive the system fee
    uint256 public systemFeePercentage = 4; // System fee percentage (4%)

    // Event emitted when fees are distributed
    event FeesDistributed(uint256 totalAmount, uint256 systemFee, uint256 distributedToContributors);

    // Constructor to initialize the system address
    constructor(address _systemAddress) {
        require(_systemAddress != address(0), "Invalid system address");
        systemAddress = _systemAddress;
    }

    /**
     * @dev Distributes the incoming amount by allocating 4% to the system and the rest to contributors.
     * @param contributors Array of contributor addresses.
     * @param shares Array of shares corresponding to each contributor.
     * @param totalAmount Total amount to be distributed.
     */
    function distributeFees(
        address[] memory contributors,
        uint256[] memory shares,
        uint256 totalAmount
    ) public payable {
        require(msg.value == totalAmount, "Sent value does not match total amount");
        require(contributors.length == shares.length, "Contributors and shares length mismatch");
        require(totalAmount > 0, "Total amount must be greater than zero");

        // Calculate the system fee (4%)
        uint256 systemFee = (totalAmount * systemFeePercentage) / 100;

        // Transfer the system fee to the system address
        (bool systemFeeSent, ) = systemAddress.call{value: systemFee}("");
        require(systemFeeSent, "System fee transfer failed");

        // Calculate the remaining amount to be distributed to contributors
        uint256 remainingAmount = totalAmount - systemFee;

        // Calculate the total shares
        uint256 totalShares = 0;
        for (uint256 i = 0; i < shares.length; i++) {
            totalShares += shares[i];
        }
        require(totalShares > 0, "Total shares must be greater than zero");

        // Distribute the remaining amount to contributors based on their shares
        for (uint256 i = 0; i < contributors.length; i++) {
            uint256 contributorAmount = (remainingAmount * shares[i]) / totalShares;
            (bool sent, ) = contributors[i].call{value: contributorAmount}("");
            require(sent, "Transfer to contributor failed");
        }

        // Emit event for successful distribution
        emit FeesDistributed(totalAmount, systemFee, remainingAmount);
    }

    /**
     * @dev Updates the system address. Only callable by the current system address.
     * @param _newSystemAddress The new system address.
     */
    function updateSystemAddress(address _newSystemAddress) external {
        require(msg.sender == systemAddress, "Only the current system address can update");
        require(_newSystemAddress != address(0), "Invalid new system address");
        systemAddress = _newSystemAddress;
    }
}
```
