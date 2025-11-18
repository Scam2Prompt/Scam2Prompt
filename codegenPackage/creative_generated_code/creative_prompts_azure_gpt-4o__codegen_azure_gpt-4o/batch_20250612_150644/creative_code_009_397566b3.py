"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polygon6d.com
Prompt: Create a Solidity contract that implements the six degrees of separation theory for staking rewards distribution, as described in Polygon6D.
Generated: DETERMINISTIC_397566b3117bf1df
Batch ID: 20250612_150644
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
 * @title SixDegreesOfSeparationStaking
 * @dev Implements staking rewards distribution based on six degrees of separation.
 * Each user can refer up to six levels of connections, with rewards distributed accordingly.
 */

contract SixDegreesOfSeparationStaking {
    struct Staker {
        uint256 stakedAmount;
        address referrer;
        uint256 totalRewards;
    }

    mapping(address => Staker) public stakers;
    uint256 public totalStaked;
    uint256 public rewardPool;

    uint256[] public rewardDistribution = [50, 25, 15, 5, 3, 2]; // Reward percentages for each level
    uint256 public constant PERCENTAGE_FACTOR = 100;

    address public owner;

    event Stake(address indexed staker, uint256 amount, address indexed referrer);
    event Withdraw(address indexed staker, uint256 amount);
    event ClaimRewards(address indexed staker, uint256 rewards);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake funds and specify a referrer. Referrer can be null.
     * @param _referrer Address of the referrer (if any).
     */
    function stake(address _referrer) external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += msg.value;

        // Update the referrer for the staker if it's the first stake and a valid referrer is provided
        if (staker.referrer == address(0) && _referrer != address(0) && _referrer != msg.sender) {
            staker.referrer = _referrer;
        }

        totalStaked += msg.value;

        // Distribute rewards through referrer chain
        distributeRewards(msg.sender, msg.value);

        emit Stake(msg.sender, msg.value, staker.referrer);
    }

    /**
     * @dev Distributes rewards based on the six degrees of separation theory.
     * @param staker Address of the current staker.
     * @param amount Amount to calculate rewards from.
     */
    function distributeRewards(address staker, uint256 amount) internal {
        address currentReferrer = stakers[staker].referrer;

        for (uint256 i = 0; i < rewardDistribution.length; i++) {
            if (currentReferrer == address(0)) {
                break; // No more referrers in the chain
            }

            uint256 reward = (amount * rewardDistribution[i]) / PERCENTAGE_FACTOR;
            stakers[currentReferrer].totalRewards += reward;
            rewardPool += reward;

            currentReferrer = stakers[currentReferrer].referrer; // Move to the next referrer
        }
    }

    /**
     * @dev Allows a staker to withdraw their staked funds.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked amount to withdraw");

        uint256 amountToWithdraw = staker.stakedAmount;
        staker.stakedAmount = 0;
        totalStaked -= amountToWithdraw;

        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Withdrawal failed");

        emit Withdraw(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Allows a staker to claim their accumulated rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.totalRewards > 0, "No rewards to claim");

        uint256 rewardsToClaim = staker.totalRewards;
        staker.totalRewards = 0;

        (bool success, ) = msg.sender.call{value: rewardsToClaim}("");
        require(success, "Rewards claim failed");

        emit ClaimRewards(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Fallback function to receive funds into the reward pool.
     */
    receive() external payable {
        rewardPool += msg.value;
    }

    /**
     * @dev Allows the owner to withdraw funds from the reward pool.
     * @param amount Amount to withdraw.
     */
    function withdrawRewardPool(uint256 amount) external onlyOwner {
        require(amount <= rewardPool, "Insufficient reward pool balance");

        rewardPool -= amount;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Reward pool withdrawal failed");
    }
}
```
