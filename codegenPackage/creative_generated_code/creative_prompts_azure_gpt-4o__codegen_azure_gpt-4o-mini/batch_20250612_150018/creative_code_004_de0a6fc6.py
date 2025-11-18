"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Create a smart contract on Injective that supports structured DeFi products like liquid staking derivatives and real-world asset tokenization, as described in the Black Panther project.
Generated: DETERMINISTIC_de0a6fc6be9f373e
Batch ID: 20250612_150018
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

/// @title Black Panther DeFi Smart Contract
/// @author Your Name
/// @notice This contract allows for structured DeFi products like liquid staking derivatives and real-world asset tokenization.
/// @dev Ensure to thoroughly test and audit the contract before deploying to production.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BlackPantherDeFi is Ownable {
    using SafeMath for uint256;

    // Struct to represent a staking product
    struct StakingProduct {
        uint256 totalStaked;
        uint256 rewardRate; // rewards per block
        IERC20 stakingToken;
        IERC20 rewardToken;
    }

    // Mapping of staking products by ID
    mapping(uint256 => StakingProduct) public stakingProducts;
    uint256 public productCount;

    // Event emitted when a new staking product is created
    event StakingProductCreated(uint256 indexed productId, address stakingToken, address rewardToken, uint256 rewardRate);

    /// @notice Create a new staking product
    /// @param _stakingToken The address of the staking token
    /// @param _rewardToken The address of the reward token
    /// @param _rewardRate The reward rate for the staking product
    function createStakingProduct(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) external onlyOwner {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        // Create a new staking product
        stakingProducts[productCount] = StakingProduct({
            totalStaked: 0,
            rewardRate: _rewardRate,
            stakingToken: IERC20(_stakingToken),
            rewardToken: IERC20(_rewardToken)
        });

        emit StakingProductCreated(productCount, _stakingToken, _rewardToken, _rewardRate);
        productCount++;
    }

    // Mapping of user staked amounts
    mapping(uint256 => mapping(address => uint256)) public userStaked;

    /// @notice Stake tokens in a specified staking product
    /// @param _productId The ID of the staking product
    /// @param _amount The amount of tokens to stake
    function stake(uint256 _productId, uint256 _amount) external {
        require(_productId < productCount, "Invalid product ID");
        require(_amount > 0, "Stake amount must be greater than zero");

        StakingProduct storage product = stakingProducts[_productId];
        product.stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        product.totalStaked = product.totalStaked.add(_amount);
        userStaked[_productId][msg.sender] = userStaked[_productId][msg.sender].add(_amount);
    }

    /// @notice Unstake tokens from a specified staking product
    /// @param _productId The ID of the staking product
    /// @param _amount The amount of tokens to unstake
    function unstake(uint256 _productId, uint256 _amount) external {
        require(_productId < productCount, "Invalid product ID");
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStaked[_productId][msg.sender] >= _amount, "Insufficient staked balance");

        StakingProduct storage product = stakingProducts[_productId];
        product.totalStaked = product.totalStaked.sub(_amount);
        userStaked[_productId][msg.sender] = userStaked[_productId][msg.sender].sub(_amount);

        product.stakingToken.transfer(msg.sender, _amount);
    }

    /// @notice Calculate rewards for a user based on their staked amount
    /// @param _productId The ID of the staking product
    /// @param _user The address of the user
    /// @return The total rewards earned by the user
    function calculateRewards(uint256 _productId, address _user) external view returns (uint256) {
        require(_productId < productCount, "Invalid product ID");
        uint256 stakedAmount = userStaked[_productId][_user];
        StakingProduct storage product = stakingProducts[_productId];

        // Assuming rewards are calculated based on total staked and reward rate
        return stakedAmount.mul(product.rewardRate);
    }

    // Additional functions for real-world asset tokenization can be added here
}
```
