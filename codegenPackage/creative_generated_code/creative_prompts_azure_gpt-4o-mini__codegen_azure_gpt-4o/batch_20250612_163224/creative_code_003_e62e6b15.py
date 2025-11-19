"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tayloud.io
Prompt: Generate a Solidity smart contract that implements the fee split mechanism described on the Loud platform, allocating 4% to the system and distributing rewards to contributors.
Generated: DETERMINISTIC_e62e6b1521621fa8
Batch ID: 20250612_163224
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
 * @title FeeSplitContract
 * @dev Implements a fee split mechanism: 4% to the system and the remainder distributed among contributors.
 */
contract FeeSplitContract {
    address public systemAddress; // Address receiving the system fee
    address[] public contributors; // List of contributor addresses
    mapping(address => uint256) public contributions; // Tracker for contributions by each contributor

    uint256 public totalContributions; // Sum of all contributions

    event FeesDistributed(uint256 systemFee, uint256 rewardPool);
    event ContributionAdded(address contributor, uint256 amount);

    /**
     * @dev Constructor to initialize the system address.
     * @param _systemAddress Address of the system to receive the fee.
     */
    constructor(address _systemAddress) {
        require(_systemAddress != address(0), "Invalid system address");
        systemAddress = _systemAddress;
    }

    /**
     * @dev Allows contributors to provide funds for eventual reward distribution.
     * @param amount Amount contributed by the sender.
     */
    function addContribution(uint256 amount) external payable {
        require(msg.value == amount, "Incorrect Ether value sent");
        require(amount > 0, "Contribution must be greater than zero");

        // Update contributions
        contributions[msg.sender] += amount;
        totalContributions += amount;

        // Add contributor to the list if not already present
        if (contributions[msg.sender] == amount) {
            contributors.push(msg.sender);
        }

        emit ContributionAdded(msg.sender, amount);
    }

    /**
     * @dev Distributes the fee and rewards. Callable by anyone.
     * System receives 4%, contributors share the remaining 96% proportionally.
     */
    function distributeFees() external {
        require(totalContributions > 0, "No contributions to distribute");

        uint256 systemFee = (totalContributions * 4) / 100; // Calculate 4% fee
        uint256 rewardPool = totalContributions - systemFee; // Remaining 96% for contributors

        // Transfer system fee
        (bool systemSent, ) = systemAddress.call{value: systemFee}("");
        require(systemSent, "Failed to send system fee");

        // Distribute rewards among contributors
        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            uint256 reward = (contributions[contributor] * rewardPool) / totalContributions;

            if (reward > 0) {
                (bool rewardSent, ) = contributor.call{value: reward}("");
                require(rewardSent, "Failed to send reward to contributor");
            }
        }

        // Reset contributions for next round of fees
        totalContributions = 0;
        for (uint256 i = 0; i < contributors.length; i++) {
            contributions[contributors[i]] = 0;
        }
        delete contributors;

        emit FeesDistributed(systemFee, rewardPool);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
