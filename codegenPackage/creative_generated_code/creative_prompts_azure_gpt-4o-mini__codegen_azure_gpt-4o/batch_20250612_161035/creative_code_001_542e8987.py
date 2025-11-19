"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-hypeloot.com
Prompt: Generate a Solidity smart contract that allows users to stake $HPLT tokens and receive daily rewards based on the amount staked, as described in the Hypeloot ecosystem.
Generated: DETERMINISTIC_542e8987babd1404
Batch ID: 20250612_161035
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
 * @title Hypeloot Staking Contract
 * @dev This contract allows users to stake HPLT tokens and receive daily rewards based on the amount staked.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HypelootStaking is Ownable {
    // Token used for staking
    IERC20 public hpltToken;

    // Reward rate (e.g., daily rewards as a percentage, specified in basis points)
    uint256 public rewardRate; // 100 basis points = 1%

    // Struct to hold user stake data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastClaimed; // Timestamp of the last claim
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _hpltToken Address of the HPLT token contract.
     * @param _rewardRate Daily reward rate in basis points (e.g., 100 = 1% daily).
     */
    constructor(IERC20 _hpltToken, uint256 _rewardRate) {
        require(address(_hpltToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        hpltToken = _hpltToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake HPLT tokens.
     * @param _amount Amount of HPLT tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer HPLT tokens from the user to the contract
        hpltToken.transferFrom(msg.sender, address(this), _amount);

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        _claimRewards(msg.sender); // Claim pending rewards before updating stake
        userStake.amount += _amount;
        userStake.lastClaimed = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param _amount Amount of HPLT tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(userStake.amount >= _amount, "Insufficient staked balance");

        // Claim pending rewards before withdrawing
        _claimRewards(msg.sender);

        // Update user stake
        userStake.amount -= _amount;

        // Update total staked
        totalStaked -= _amount;

        // Transfer tokens back to the user
        hpltToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards.
     * @param _user Address of the user claiming rewards.
     */
    function _claimRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 pendingRewards = _calculateRewards(_user);
            userStake.lastClaimed = block.timestamp;

            if (pendingRewards > 0) {
                hpltToken.transfer(_user, pendingRewards);
                emit RewardClaimed(_user, pendingRewards);
            }
        }
    }

    /**
     * @dev Calculates pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastClaimed;
        uint256 dailyReward = (userStake.amount * rewardRate) / 10000; // Reward rate in basis points
        uint256 rewards = (dailyReward * timeElapsed) / 1 days;
        return rewards;
    }

    /**
     * @dev Allows the owner to change the reward rate.
     * @param _rewardRate New reward rate in basis points.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * This function is useful if tokens are accidentally sent to the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Cannot withdraw zero tokens");
        hpltToken.transfer(owner(), _amount);
    }
}
```
