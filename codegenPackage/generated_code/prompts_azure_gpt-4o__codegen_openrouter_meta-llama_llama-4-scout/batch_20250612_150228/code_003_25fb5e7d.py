"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Create a Solidity smart contract that interacts with Synthetix staking mechanisms to deposit SNX and earn incentives. Include functions for querying staking rewards.
Generated: DETERMINISTIC_25fb5e7d41d348b0
Batch ID: 20250612_150228
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title SynthetixStakingContract
 * @author [Your Name]
 * @notice This contract interacts with Synthetix staking mechanisms to deposit SNX and earn incentives.
 */
contract SynthetixStakingContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Synthetix staking contract address
    address public constant SYNTHETIX_STAKING_CONTRACT = 0xBb4545C0A6C1D881bA0C9c3E398A3E575A9C2F6d;

    // SNX token address
    address public constant SNX_TOKEN_ADDRESS = 0xC0114694cB269D102b6ed0f219c27E40eF1c1b82;

    // Reward token address
    address public constant REWARD_TOKEN_ADDRESS = 0xAf88d065e77c8cC2239327C5EDb3A432268e5831;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping(address => uint256) public rewardClaims;

    /**
     * @notice Deposits SNX tokens into the Synthetix staking contract
     * @param _amount The amount of SNX tokens to deposit
     */
    function depositSNX(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than 0");
        require(IERC20(SNX_TOKEN_ADDRESS).balanceOf(msg.sender) >= _amount, "Insufficient SNX balance");

        // Approve Synthetix staking contract to spend SNX tokens
        IERC20(SNX_TOKEN_ADDRESS).safeApprove(SYNTHETIX_STAKING_CONTRACT, _amount);

        // Deposit SNX tokens into Synthetix staking contract
        IStakingContract(SYNTHETIX_STAKING_CONTRACT).deposit(_amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
    }

    /**
     * @notice Withdraws SNX tokens from the Synthetix staking contract
     * @param _amount The amount of SNX tokens to withdraw
     */
    function withdrawSNX(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Withdraw SNX tokens from Synthetix staking contract
        IStakingContract(SYNTHETIX_STAKING_CONTRACT).withdraw(_amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
    }

    /**
     * @notice Queries the staking rewards for a user
     * @return The total staking rewards for the user
     */
    function queryStakingRewards() public view returns (uint256) {
        // Get user's staking balance
        uint256 _stakingBalance = stakingBalances[msg.sender];

        // Get reward amount from Synthetix staking contract
        uint256 _rewardAmount = IStakingContract(SYNTHETIX_STAKING_CONTRACT).earned(msg.sender);

        return _rewardAmount;
    }

    /**
     * @notice Claims staking rewards for a user
     */
    function claimStakingRewards() public {
        // Get reward amount from Synthetix staking contract
        uint256 _rewardAmount = IStakingContract(SYNTHETIX_STAKING_CONTRACT).earned(msg.sender);

        // Update user's reward claim
        rewardClaims[msg.sender] = rewardClaims[msg.sender].add(_rewardAmount);

        // Transfer reward tokens to user
        IERC20(REWARD_TOKEN_ADDRESS).safeTransfer(msg.sender, _rewardAmount);

        // Notify Synthetix staking contract of reward claim
        IStakingContract(SYNTHETIX_STAKING_CONTRACT).getReward();
    }
}

interface IStakingContract {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
    function earned(address _user) external view returns (uint256);
    function getReward() external;
}
```
