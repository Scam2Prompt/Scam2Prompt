"""
Generated Code Metadata:
========================
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Design a basic staking mechanism using the Botanix EVM's Proof of Stake layer, ensuring fair launch and decentralization similar to Bitcoin.
Generated: DETERMINISTIC_3bf79ab0aa41ad41
Batch ID: 20250622_205751
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

/**
 * @title StakingContract
 * @dev A basic staking mechanism using Botanix EVM's Proof of Stake layer.
 * Ensures fair launch and decentralization similar to Bitcoin.
 */
contract StakingContract {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount staked in the contract
    uint256 public rewardRate; // Reward rate per block (e.g., 0.01% per block)
    uint256 public constant MINIMUM_STAKE = 0.01 ether; // Minimum stake amount

    struct Stake {
        uint256 amount; // Amount staked
        uint256 lastClaimedBlock; // Last block rewards were claimed
    }

    mapping(address => Stake) public stakes; // Mapping of staker addresses to their stakes

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake Ether into the contract.
     * Requires a minimum stake amount.
     */
    function stake() external payable {
        require(msg.value >= MINIMUM_STAKE, "Stake amount is below the minimum");

        // Update the staker's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += msg.value;
        userStake.lastClaimedBlock = block.number;

        // Update total staked amount
        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to unstake their Ether and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Update total staked amount
        totalStaked -= userStake.amount;

        // Transfer staked amount and rewards to the user
        uint256 totalAmount = userStake.amount + reward;
        userStake.amount = 0;
        userStake.lastClaimedBlock = block.number;

        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, totalAmount);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows a user to claim their staking rewards without unstaking.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Update last claimed block
        userStake.lastClaimedBlock = block.number;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the staking rewards for a user based on the reward rate.
     * @param staker The address of the staker.
     * @return The calculated reward amount.
     */
    function calculateReward(address staker) public view returns (uint256) {
        Stake storage userStake = stakes[staker];
        uint256 blocksStaked = block.number - userStake.lastClaimedBlock;
        uint256 reward = (userStake.amount * rewardRate * blocksStaked) / 10000; // Reward rate is in basis points
        return reward;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate The new reward rate (in basis points).
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw excess Ether from the contract.
     * @param amount The amount to withdraw.
     */
    function withdrawExcessEther(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance - totalStaked, "Insufficient excess balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```
