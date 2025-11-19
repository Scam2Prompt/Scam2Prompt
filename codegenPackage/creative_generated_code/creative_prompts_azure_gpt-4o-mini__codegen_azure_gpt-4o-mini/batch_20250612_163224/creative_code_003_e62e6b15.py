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

/// @title Fee Split Smart Contract
/// @notice This contract implements a fee split mechanism.
/// @dev All fees collected are divided, 4% goes to the system and the rest is distributed among contributors.

contract FeeSplitter {
    address payable public systemAddress; // Address of the system (receives 4% of fees)
    mapping(address => uint256) public contributions; // Track contributions from each address
    uint256 public totalContributions; // Total contributions made
    uint256 public totalFeesCollected; // Total fees collected

    event ContributionReceived(address indexed contributor, uint256 amount);
    event FeesDistributed(uint256 amountToSystem, uint256 amountToContributors);

    /// @notice Constructor to set the system's address
    /// @param _systemAddress The address to which 4% of fees will be sent
    constructor(address payable _systemAddress) {
        require(_systemAddress != address(0), "Invalid system address");
        systemAddress = _systemAddress;
    }

    /// @notice Allows contributors to contribute Ether to the contract
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than zero");
        
        // Record the contribution
        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;
        
        // Emit the contribution event
        emit ContributionReceived(msg.sender, msg.value);
    }

    /// @notice Distributes collected fees, sending 4% to the system and the rest to contributors
    function distributeFees() external {
        require(totalContributions > 0, "No contributions available for distribution");

        // Calculate the total fee (100%)
        uint256 totalFees = address(this).balance;

        // Calculate system fee (4%)
        uint256 systemFee = (totalFees * 4) / 100;

        // Calculate remaining amount for contributors
        uint256 contributorFees = totalFees - systemFee;

        // Transfer the system fee
        (bool sentToSystem, ) = systemAddress.call{value: systemFee}("");
        require(sentToSystem, "Failed to send Ether to system");

        // Distribute remaining fees to contributors
        uint256 totalDistributed = 0;
        for (uint256 i = 0; i < contributors.length; i++) {
            uint256 contributorShare = (contributions[contributors[i]] * contributorFees) / totalContributions;
            (bool sentToContributor, ) = contributors[i].call{value: contributorShare}("");
            require(sentToContributor, "Failed to send Ether to contributor");
            totalDistributed += contributorShare;
        }

        // Emit fees distributed event
        emit FeesDistributed(systemFee, totalDistributed);
    }

    /// @notice View function to get the balance of the contract
    /// @return uint256 The balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
