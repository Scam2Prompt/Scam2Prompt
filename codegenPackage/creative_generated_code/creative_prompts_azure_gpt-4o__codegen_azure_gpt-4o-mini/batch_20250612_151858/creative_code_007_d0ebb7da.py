"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spl20-top.web.app
Prompt: Develop a Solidity smart contract that interacts with Tensor's platform to claim $TNSR rewards based on wallet activity.
Generated: DETERMINISTIC_d0ebb7da6a2b8ee3
Batch ID: 20250612_151858
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

// Interface for the Token contract
interface ITensorToken {
    function claimRewards(address user) external returns (uint256);
}

// Main contract to interact with Tensor's platform
contract TensorRewardClaimer {
    // Address of the Tensor token contract
    ITensorToken public tensorToken;

    // Event to log claimed rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to check if the caller is a valid address
    modifier onlyValidAddress(address user) {
        require(user != address(0), "Invalid address");
        _;
    }

    // Constructor to set the address of the Tensor token contract
    constructor(address _tensorTokenAddress) onlyValidAddress(_tensorTokenAddress) {
        tensorToken = ITensorToken(_tensorTokenAddress);
    }

    // Function to claim $TNSR rewards based on wallet activity
    function claimRewards() external onlyValidAddress(msg.sender) {
        uint256 claimedAmount;

        // Interacting with Tensor's token contract to claim rewards
        try tensorToken.claimRewards(msg.sender) returns (uint256 amount) {
            claimedAmount = amount;
        } catch {
            revert("Failed to claim rewards");
        }

        // Emitting an event for the claimed rewards
        emit RewardsClaimed(msg.sender, claimedAmount);
    }

    // Function to change the Tensor token address (only for contract owner)
    function updateTensorTokenAddress(address newTensorTokenAddress) external onlyValidAddress(newTensorTokenAddress) {
        // TODO: Implement access control for ownership
        tensorToken = ITensorToken(newTensorTokenAddress);
    }
}
```
