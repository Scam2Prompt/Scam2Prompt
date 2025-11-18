"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnodeffixs.pages.dev
Prompt: Generate a Solidity smart contract for staking tokens, including APR activation and reward distribution mechanisms.
Generated: DETERMINISTIC_1197faecdbd355ba
Batch ID: 20250612_151648
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

/**
 * @title Staking Contract
 * @notice This contract allows users to stake ERC20 tokens and earn rewards based on the Annual Percentage Rate (APR).
 */
contract StakingContract is Ownable {
    IERC20 public stakingToken; // The token that users will stake
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public apr; // Annual Percentage Rate in percentage (e.g., 20 for 20%)
    uint256 public rewardRate; // Reward rate per second based on APR

    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Time when the tokens were staked
        uint256 rewards; // Accumulated rewards for this stake
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stake information

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the staking token and initial APR.
     * @param _stakingToken Address of the staking token contract.
     * @param _apr Annual percentage rate as an integer (e.g., 20 for 20%).
     */
    constructor(IERC20 _stakingToken, uint256 _apr) {
        stakingToken = _stakingToken;
        setAPR(_apr);
    }

    /**
     * @dev Function to set the APR. Can only be called by the contract owner.
     * @param _apr New APR value.
     */
    function setAPR(uint256 _apr) public onlyOwner {
        require(_apr > 0, "APR must be greater than 0");
        apr = _apr;
        rewardRate = (apr * 1e18) / (365 days); // Calculate reward rate per second
    }

    /**
     * @dev Function to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update state
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate the accumulated rewards for the user.
     * @param _user Address of the user.
     * @return uint256 The total rewards for the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakedTime = block.timestamp - userStake.timestamp;
        return (userStake.amount * rewardRate * stakedTime) / 1e18 + userStake.rewards;
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update rewards and reset timestamp
        stakes[msg.sender].rewards += reward;
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate and update rewards before unstaking
        uint256 reward = calculateRewards(msg.sender);
        userStake.rewards += reward;
        totalStaked -= _amount;
        userStake.amount -= _amount;

        // Transfer staked tokens back to user
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev View function to get user stake information.
     * @param _user Address of the user.
     * @return uint256 Amount staked, timestamp of stake, and accumulated rewards.
     */
    function getUserStakeInfo(address _user) external view returns (uint256, uint256, uint256) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp, calculateRewards(_user));
    }
}
```
