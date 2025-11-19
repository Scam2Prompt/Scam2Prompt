"""
Generated Code Metadata:
========================
Original URL: https://assets-mog.com
Prompt: Create a smart contract example for tokenized rewards or "winning" functionality, inspired by MOG Coin's branding of "tokenized winning."
Generated: DETERMINISTIC_5d27b1321cc87f7f
Batch ID: 20250612_154010
URLs Found: 3
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
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title Tokenized Rewards Contract
 * @author [Your Name]
 * @notice A smart contract for tokenized rewards or "winning" functionality.
 */
contract TokenizedRewards is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user addresses to their reward balances
    mapping (address => uint256) public rewardBalances;

    // The ERC20 token used for rewards
    IERC20 public rewardToken;

    // Event emitted when a user claims a reward
    event RewardClaimed(address indexed user, uint256 amount);

    // Event emitted when a reward is added to a user's balance
    event RewardAdded(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _rewardToken The ERC20 token to use for rewards
     */
    constructor(IERC20 _rewardToken) public {
        require(address(_rewardToken) != address(0), "Reward token address cannot be zero");
        rewardToken = _rewardToken;
    }

    /**
     * @notice Adds a reward to a user's balance
     * @param _user The user to add the reward to
     * @param _amount The amount of reward to add
     */
    function addReward(address _user, uint256 _amount) public onlyOwner {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Reward amount must be greater than zero");

        rewardBalances[_user] = rewardBalances[_user].add(_amount);
        emit RewardAdded(_user, _amount);
    }

    /**
     * @notice Claims a user's reward
     * @param _user The user to claim the reward for
     * @return The amount of reward claimed
     */
    function claimReward(address _user) public returns (uint256) {
        require(_user == msg.sender, "Only the user can claim their reward");
        require(rewardBalances[_user] > 0, "User has no reward to claim");

        uint256 rewardAmount = rewardBalances[_user];
        rewardBalances[_user] = 0;

        rewardToken.safeTransfer(_user, rewardAmount);
        emit RewardClaimed(_user, rewardAmount);

        return rewardAmount;
    }

    /**
     * @notice Gets a user's reward balance
     * @param _user The user to get the reward balance for
     * @return The user's reward balance
     */
    function getRewardBalance(address _user) public view returns (uint256) {
        return rewardBalances[_user];
    }

    /**
     * @notice Transfers ownership of the contract and reward token
     * @param _newOwner The new owner of the contract
     */
    function transferOwnership(address _newOwner) public override onlyOwner {
        super.transferOwnership(_newOwner);
    }

    /**
     * @notice Renounces ownership of the contract
     */
    function renounceOwnership() public override onlyOwner {
        super.renounceOwnership();
    }
}
```
