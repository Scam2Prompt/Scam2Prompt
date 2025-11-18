"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.com
Prompt: Generate code to restake ETH and other assets using EigenLayer's staking mechanism to earn rewards on staked assets.
Generated: DETERMINISTIC_91f18710d2b30ad8
Batch ID: 20250612_154049
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for EigenLayer staking functions
interface IEigenLayer {
    function restake(address _asset, uint256 _amount) external;
    function withdraw(address _asset, uint256 _amount) external;
}

// Main contract for restaking assets using EigenLayer
contract Restaker is ReentrancyGuard, Ownable {
    // Mapping of asset addresses to their staked amounts
    mapping(address => uint256) private stakedAmounts;

    // EigenLayer contract address
    IEigenLayer public eigenLayer;

    // Event emitted when assets are restaked
    event Restaked(address indexed asset, uint256 amount);
    
    // Event emitted when assets are withdrawn
    event Withdrawn(address indexed asset, uint256 amount);

    // Constructor to initialize EigenLayer contract address
    constructor(address _eigenLayerAddress) {
        require(_eigenLayerAddress != address(0), "Invalid EigenLayer address");
        eigenLayer = IEigenLayer(_eigenLayerAddress);
    }

    // Function to restake specified asset
    function restakeAssets(address _asset, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(IERC20(_asset).balanceOf(msg.sender) >= _amount, "Insufficient balance");
        require(IERC20(_asset).allowance(msg.sender, address(this)) >= _amount, "Allowance not set");

        // Transfer tokens from the user to this contract
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        // Update the staked amount mapping
        stakedAmounts[_asset] += _amount;

        // Call the EigenLayer restake function
        eigenLayer.restake(_asset, _amount);

        emit Restaked(_asset, _amount);
    }

    // Function to withdraw staked assets
    function withdrawAssets(address _asset, uint256 _amount) external onlyOwner nonReentrant {
        require(stakedAmounts[_asset] >= _amount, "Insufficient staked amount");

        // Call the EigenLayer withdraw function
        eigenLayer.withdraw(_asset, _amount);

        // Update the staked amount mapping
        stakedAmounts[_asset] -= _amount;

        // Transfer tokens back to the owner
        IERC20(_asset).transfer(msg.sender, _amount);

        emit Withdrawn(_asset, _amount);
    }

    // Function to get staked balance for an asset
    function getStakedAmount(address _asset) external view returns (uint256) {
        return stakedAmounts[_asset];
    }
}
```
