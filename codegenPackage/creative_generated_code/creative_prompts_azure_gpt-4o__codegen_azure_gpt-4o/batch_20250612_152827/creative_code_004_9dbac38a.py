"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity function to implement staking for $GNS tokens, allowing users to earn real yield, as outlined in the Gains Network ecosystem.
Generated: DETERMINISTIC_9dbac38ac0e16f34
Batch ID: 20250612_152827
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
 * @title StakingContract
 * @dev This contract allows users to stake GNS tokens and earn rewards.
 * Users can stake, withdraw, and claim rewards. The rewards are distributed
 * proportionally based on the amount of tokens staked and the staking duration.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    IERC20 public gnsToken; // $GNS token contract reference
    uint256 public rewardRate; // Reward rate per second per token

    // Struct to track staking details for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastUpdated; // Timestamp of last interaction
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their staking details
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    event Staked(address indexed user, uint256 amount); // Emitted when a user stakes tokens
    event Withdrawn(address indexed user, uint256 amount); // Emitted when a user withdraws tokens
    event RewardClaimed(address indexed user, uint256 reward); // Emitted when a user claims rewards

    /**
     * @dev Constructor to initialize the contract with token address and reward rate.
     * @param _gnsToken Address of the $GNS token contract
     * @param _rewardRate Reward rate per second per token
     */
    constructor(IERC20 _gnsToken, uint256 _rewardRate) {
        gnsToken = _gnsToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake $GNS tokens.
     * @param _amount Number of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update user's rewards before modifying staking data
        _updateReward(msg.sender);

        // Transfer tokens to the contract
        require(gnsToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw staked tokens.
     * @param _amount Number of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update user's rewards before modifying staking data
        _updateReward(msg.sender);

        // Update staking details
        stakes[msg.sender].amount -= _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(gnsToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to claim accumulated rewards.
     */
    function claimRewards() external {
        // Update user's rewards before modifying staking data
        _updateReward(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt after claiming rewards
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(gnsToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update a user's reward data.
     * @param _user Address of the user
     */
    function _updateReward(address _user) internal {
        Stake storage stakeData = stakes[_user];
        if (stakeData.amount > 0) {
            uint256 timeElapsed = block.timestamp - stakeData.lastUpdated;
            uint256 pendingReward = (stakeData.amount * rewardRate * timeElapsed) / 1e18; // Assuming reward rate is scaled
            stakeData.rewardDebt += pendingReward;
        }
        stakeData.lastUpdated = block.timestamp;
    }

    /**
     * @dev Updates the reward rate.
     * @param _rewardRate New reward rate
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows the owner to withdraw excess $GNS tokens from the contract.
     * @param _amount Number of tokens to withdraw
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(_amount <= gnsToken.balanceOf(address(this)) - totalStaked, "Excess withdrawal amount exceeds contract balance");
        require(gnsToken.transfer(msg.sender, _amount), "Token transfer failed");
    }
}
```
