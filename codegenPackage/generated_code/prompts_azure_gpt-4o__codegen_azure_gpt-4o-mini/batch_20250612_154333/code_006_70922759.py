"""
Generated Code Metadata:
========================
Original URL: https://flockerz-it.web.app
Prompt: Develop a Solidity smart contract for a DAO vault similar to the Flock Vault, allowing token holders to collectively allocate resources and earn rewards based on participation.
Generated: DETERMINISTIC_70922759f59bdfae
Batch ID: 20250612_154333
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DAO Vault
 * @dev A smart contract for a DAO vault that allows token holders to collectively allocate resources and earn rewards.
 */
contract DAOVault is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each member's stake
    struct Member {
        uint256 stake; // Amount of tokens staked by the member
        uint256 lastClaimed; // Last time rewards were claimed
    }

    // Mapping of member addresses to their information
    mapping(address => Member) public members;

    // Total amount of tokens staked in the vault
    uint256 public totalStaked;

    // The ERC20 token used for staking
    IERC20 public stakingToken;

    // Reward rate per second (in tokens)
    uint256 public rewardRate;

    // Event emitted when a member stakes tokens
    event Staked(address indexed member, uint256 amount);

    // Event emitted when a member withdraws tokens
    event Withdrawn(address indexed member, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed member, uint256 amount);

    /**
     * @dev Constructor to initialize the DAO vault.
     * @param _stakingToken The address of the ERC20 token used for staking.
     * @param _rewardRate The reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a member to stake tokens in the vault.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update member's stake and total staked amount
        members[msg.sender].stake = members[msg.sender].stake.add(amount);
        totalStaked = totalStaked.add(amount);
        members[msg.sender].lastClaimed = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a member to withdraw their staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(members[msg.sender].stake >= amount, "Insufficient stake");

        // Update member's stake and total staked amount
        members[msg.sender].stake = members[msg.sender].stake.sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows a member to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update last claimed time
        members[msg.sender].lastClaimed = block.timestamp;

        // Transfer rewards to the member
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the rewards for a member based on their stake and last claimed time.
     * @param memberAddress The address of the member.
     * @return The calculated reward amount.
     */
    function calculateRewards(address memberAddress) public view returns (uint256) {
        Member memory member = members[memberAddress];
        uint256 timeElapsed = block.timestamp.sub(member.lastClaimed);
        return member.stake.mul(rewardRate).mul(timeElapsed);
    }

    /**
     * @dev Allows the owner to withdraw any tokens from the vault.
     * @param amount The amount of tokens to withdraw.
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
