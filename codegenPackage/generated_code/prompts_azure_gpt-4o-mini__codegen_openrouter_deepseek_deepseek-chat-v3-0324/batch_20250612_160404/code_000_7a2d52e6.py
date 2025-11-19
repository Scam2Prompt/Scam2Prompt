"""
Generated Code Metadata:
========================
Original URL: https://karak-node.network
Prompt: How can I implement multiasset restaking using the Karak network to enhance cryptoeconomic security for my decentralized application?
Generated: DETERMINISTIC_7a2d52e6121d3895
Batch ID: 20250612_160404
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IKarakRestaking {
    function deposit(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function claimRewards(address asset) external;
}

contract MultiAssetRestaker is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Karak restaking contract address
    address public karakRestakingContract;

    // Mapping of supported assets
    mapping(address => bool) public supportedAssets;

    // Mapping of user balances per asset
    mapping(address => mapping(address => uint256)) public userBalances;

    // Events
    event AssetAdded(address indexed asset);
    event AssetRemoved(address indexed asset);
    event Deposited(address indexed user, address indexed asset, uint256 amount);
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);
    event RewardsClaimed(address indexed user, address indexed asset, uint256 amount);

    constructor(address _karakRestakingContract) {
        require(_karakRestakingContract != address(0), "Invalid Karak contract address");
        karakRestakingContract = _karakRestakingContract;
    }

    /**
     * @dev Add a supported asset for restaking
     * @param asset Address of the ERC20 token to support
     */
    function addSupportedAsset(address asset) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        require(!supportedAssets[asset], "Asset already supported");
        supportedAssets[asset] = true;
        emit AssetAdded(asset);
    }

    /**
     * @dev Remove a supported asset
     * @param asset Address of the ERC20 token to remove
     */
    function removeSupportedAsset(address asset) external onlyOwner {
        require(supportedAssets[asset], "Asset not supported");
        supportedAssets[asset] = false;
        emit AssetRemoved(asset);
    }

    /**
     * @dev Deposit assets for restaking
     * @param asset Address of the ERC20 token to deposit
     * @param amount Amount to deposit
     */
    function deposit(address asset, uint256 amount) external nonReentrant {
        require(supportedAssets[asset], "Asset not supported");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(asset).safeTransferFrom(msg.sender, address(this), amount);
        IERC20(asset).safeApprove(karakRestakingContract, amount);
        
        IKarakRestaking(karakRestakingContract).deposit(asset, amount);
        userBalances[msg.sender][asset] += amount;

        emit Deposited(msg.sender, asset, amount);
    }

    /**
     * @dev Withdraw assets from restaking
     * @param asset Address of the ERC20 token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address asset, uint256 amount) external nonReentrant {
        require(supportedAssets[asset], "Asset not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender][asset] >= amount, "Insufficient balance");

        IKarakRestaking(karakRestakingContract).withdraw(asset, amount);
        IERC20(asset).safeTransfer(msg.sender, amount);
        
        userBalances[msg.sender][asset] -= amount;

        emit Withdrawn(msg.sender, asset, amount);
    }

    /**
     * @dev Claim rewards for a specific asset
     * @param asset Address of the ERC20 token to claim rewards for
     */
    function claimRewards(address asset) external nonReentrant {
        require(supportedAssets[asset], "Asset not supported");
        require(userBalances[msg.sender][asset] > 0, "No balance for this asset");

        uint256 beforeBalance = IERC20(asset).balanceOf(address(this));
        IKarakRestaking(karakRestakingContract).claimRewards(asset);
        uint256 afterBalance = IERC20(asset).balanceOf(address(this));
        
        uint256 rewardAmount = afterBalance - beforeBalance;
        if (rewardAmount > 0) {
            IERC20(asset).safeTransfer(msg.sender, rewardAmount);
            emit RewardsClaimed(msg.sender, asset, rewardAmount);
        }
    }

    /**
     * @dev Get user balance for a specific asset
     * @param user Address of the user
     * @param asset Address of the ERC20 token
     * @return User's balance for the asset
     */
    function getUserBalance(address user, address asset) external view returns (uint256) {
        return userBalances[user][asset];
    }
}
```
