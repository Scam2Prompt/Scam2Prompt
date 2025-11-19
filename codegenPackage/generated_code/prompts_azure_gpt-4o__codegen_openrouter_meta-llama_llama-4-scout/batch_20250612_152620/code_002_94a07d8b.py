"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Using Solidity, write a smart contract function to distribute $SCOTTY token rewards dynamically based on the annual return percentage and the user's share of the staking pool.
Generated: DETERMINISTIC_94a07d8bfd49e634
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title ScottTokenRewardsDistributor
 * @author [Your Name]
 * @notice Distributes $SCOTTY token rewards dynamically based on the annual return percentage and the user's share of the staking pool.
 */
contract ScottTokenRewardsDistributor {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public userStakingBalances;

    // Mapping of user reward debt
    mapping (address => uint256) public userRewardDebt;

    // Total staking pool
    uint256 public totalStakingPool;

    // Annual return percentage (in basis points, e.g., 1000 = 10%)
    uint256 public annualReturnPercentage;

    // $SCOTTY token contract
    ERC20 public scottyToken;

    /**
     * @notice Constructor
     * @param _scottyTokenAddress $SCOTTY token contract address
     * @param _annualReturnPercentage Initial annual return percentage (in basis points)
     */
    constructor(address _scottyTokenAddress, uint256 _annualReturnPercentage) {
        require(_scottyTokenAddress != address(0), "Invalid token address");
        require(_annualReturnPercentage > 0, "Annual return percentage must be greater than 0");

        scottyToken = ERC20(_scottyTokenAddress);
        annualReturnPercentage = _annualReturnPercentage;
    }

    /**
     * @notice Stake $SCOTTY tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer tokens");

        userStakingBalances[msg.sender] = userStakingBalances[msg.sender].add(_amount);
        totalStakingPool = totalStakingPool.add(_amount);

        // Update user reward debt
        updateUserRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake $SCOTTY tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(userStakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        userStakingBalances[msg.sender] = userStakingBalances[msg.sender].sub(_amount);
        totalStakingPool = totalStakingPool.sub(_amount);

        // Transfer unstaked tokens back to user
        require(scottyToken.transfer(msg.sender, _amount), "Failed to transfer tokens");

        // Update user reward debt
        updateUserRewardDebt(msg.sender);
    }

    /**
     * @notice Update user reward debt
     * @param _user User address
     */
    function updateUserRewardDebt(address _user) internal {
        uint256 userBalance = userStakingBalances[_user];
        if (userBalance == 0) {
            userRewardDebt[_user] = 0;
            return;
        }

        // Calculate total rewards
        uint256 totalRewards = calculateTotalRewards();

        // Calculate user's share of rewards
        uint256 userRewards = totalRewards.mul(userBalance).div(totalStakingPool);

        // Update user reward debt
        userRewardDebt[_user] = userRewards;
    }

    /**
     * @notice Calculate total rewards
     * @return Total rewards
     */
    function calculateTotalRewards() internal view returns (uint256) {
        // Calculate total rewards based on annual return percentage and total staking pool
        uint256 totalRewards = totalStakingPool.mul(annualReturnPercentage).div(10000);

        return totalRewards;
    }

    /**
     * @notice Distribute rewards to user
     */
    function distributeRewards() external {
        uint256 userRewards = userRewardDebt[msg.sender];
        if (userRewards == 0) {
            return;
        }

        // Transfer rewards to user
        require(scottyToken.transfer(msg.sender, userRewards), "Failed to transfer rewards");

        // Reset user reward debt
        userRewardDebt[msg.sender] = 0;
    }

    /**
     * @notice Update annual return percentage
     * @param _newAnnualReturnPercentage New annual return percentage (in basis points)
     */
    function updateAnnualReturnPercentage(uint256 _newAnnualReturnPercentage) external {
        require(msg.sender == owner(), "Only owner can update annual return percentage");
        require(_newAnnualReturnPercentage > 0, "Annual return percentage must be greater than 0");

        annualReturnPercentage = _newAnnualReturnPercentage;
    }

    // Owner function to withdraw stuck tokens
    function withdrawStuckTokens(address _tokenAddress) external {
        require(msg.sender == owner(), "Only owner can withdraw stuck tokens");
        require(_tokenAddress != address(scottyToken), "Cannot withdraw $SCOTTY tokens");

        ERC20 token = ERC20(_tokenAddress);
        require(token.transfer(msg.sender, token.balanceOf(address(this))), "Failed to transfer stuck tokens");
    }

    // Get owner address ( Openzeppelin Ownable )
    address private _owner;

    function owner() public view returns (address) {
        return _owner;
    }

    function transferOwnership(address newOwner) public {
        require(msg.sender == _owner, "Only owner can transfer ownership");
        require(newOwner != address(0), "New owner address cannot be zero");

        _owner = newOwner;
    }
}
```
