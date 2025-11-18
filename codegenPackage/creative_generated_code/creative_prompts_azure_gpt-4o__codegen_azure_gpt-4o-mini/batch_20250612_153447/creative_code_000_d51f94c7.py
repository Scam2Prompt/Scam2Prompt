"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staderlabss.github.io
Prompt: Write a smart contract in Solidity that implements a permissionless investment strategy as described by Staderlabs, including asset allocation, risk management, and rebalancing mechanisms.
Generated: DETERMINISTIC_d51f94c75f3b2337
Batch ID: 20250612_153447
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a permissionless investment strategy
contract PermissionlessInvestment is Ownable {
    // Struct to store asset allocation details
    struct Asset {
        address token; // ERC20 token address
        uint256 allocation; // Allocation percentage (0-100)
    }

    // Array to hold all assets
    Asset[] public assets;

    // Total allocation percentage
    uint256 public totalAllocation;

    // Event emitted when assets are rebalanced
    event Rebalanced(uint256 timestamp, uint256[] newAllocations);

    // Modifier to check if total allocation is 100%
    modifier isTotalAllocationValid() {
        require(totalAllocation == 100, "Total allocation must be 100%");
        _;
    }

    // Function to add an asset to the investment strategy
    function addAsset(address _token, uint256 _allocation) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_allocation > 0, "Allocation must be greater than 0");

        // Update total allocation
        totalAllocation += _allocation;

        // Ensure total allocation does not exceed 100%
        require(totalAllocation <= 100, "Total allocation cannot exceed 100%");

        // Add asset to the array
        assets.push(Asset({
            token: _token,
            allocation: _allocation
        }));
    }

    // Function to rebalance the investment strategy
    function rebalance(uint256[] calldata newAllocations) external onlyOwner isTotalAllocationValid {
        require(newAllocations.length == assets.length, "Invalid allocations length");
        
        // Reset total allocation for new allocations
        totalAllocation = 0;

        // Update allocations and validate the new allocations
        for (uint256 i = 0; i < newAllocations.length; i++) {
            require(newAllocations[i] <= 100, "Allocation must be less than or equal to 100");
            assets[i].allocation = newAllocations[i];
            totalAllocation += newAllocations[i];
        }

        // Trigger rebalance event
        emit Rebalanced(block.timestamp, newAllocations);
    }

    // Function to retrieve the current asset list
    function getAssets() external view returns (Asset[] memory) {
        return assets;
    }

    // Function to withdraw tokens (for emergency purposes)
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_token);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance");
        token.transfer(msg.sender, _amount);
    }
}
```
