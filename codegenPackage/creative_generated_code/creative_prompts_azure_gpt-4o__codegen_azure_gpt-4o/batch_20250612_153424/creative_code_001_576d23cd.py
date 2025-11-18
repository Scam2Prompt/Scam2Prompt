"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://et-herfi.github.io
Prompt: Generate Solidity code for a smart contract that enables staking on Ether Fi, ensuring rewards distribution for participants based on their contribution to the Ethereum network.
Generated: DETERMINISTIC_576d23cd31375772
Batch ID: 20250612_153424
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
 * @title EtherFiStaking
 * @dev A smart contract for staking Ether on EtherFi and distributing rewards proportionally
 *      based on participants' contribution to the Ethereum network.
 */
contract EtherFiStaking {
    // State variables
    mapping(address => uint256) private stakes; // Tracks the amount staked by each address
    uint256 private totalStaked; // Total Ether staked in the contract
    mapping(address => uint256) private pendingRewards; // Tracks rewards for each address
    uint256 public rewardPool; // Total rewards available for distribution
    
    address public owner; // Contract owner

    // Events
    event Staked(address indexed user, uint256 amount);
    event WithdrawnStake(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);
    event RewardPoolFunded(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor that sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake Ether into the contract.
     */
    function stake() external payable {
        require(msg.value > 0, "Staking amount must be greater than zero");

        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their staked Ether.
     */
    function withdrawStake() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No staked amount to withdraw");

        stakes[msg.sender] = 0;
        totalStaked -= userStake;

        payable(msg.sender).transfer(userStake);

        emit WithdrawnStake(msg.sender, userStake);
    }

    /**
     * @dev Allows the owner to fund the reward pool.
     * @param amount The amount of Ether to fund the reward pool.
     */
    function fundRewardPool() external payable onlyOwner {
        require(msg.value > 0, "Funding amount must be greater than zero");

        rewardPool += msg.value;

        emit RewardPoolFunded(msg.value);
    }

    /**
     * @dev Distributes rewards to participants based on their contribution.
     *      Rewards are proportional to the amount staked.
     */
    function distributeRewards() external onlyOwner {
        require(rewardPool > 0, "No rewards available for distribution");
        require(totalStaked > 0, "No staked Ether to distribute rewards");

        for (address participant : getAllParticipants()) {
            uint256 userStake = stakes[participant];
            uint256 reward = (userStake * rewardPool) / totalStaked;

            pendingRewards[participant] += reward;
        }

        rewardPool = 0; // Reset reward pool after distribution
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = pendingRewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        pendingRewards[msg.sender] = 0;
        payable(msg.sender).transfer(reward);

        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Returns the staked amount of a user.
     * @param user The address of the user.
     * @return The amount of Ether staked by the user.
     */
    function getStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev Returns the reward pending for a user.
     * @param user The address of the user.
     * @return The amount of Ether rewards pending for the user.
     */
    function getPendingRewards(address user) external view returns (uint256) {
        return pendingRewards[user];
    }

    /**
     * @dev Helper function to fetch all participants (not implemented here).
     *      This would require off-chain tracking or an additional data structure.
     */
    function getAllParticipants() private view returns (address[] memory) {
        // Implementation needed for tracking participants
        revert("Function not implemented");
    }

    // Fallback function to accept Ether sent directly to the contract
    receive() external payable {
        rewardPool += msg.value;
        emit RewardPoolFunded(msg.value);
    }
}
```
