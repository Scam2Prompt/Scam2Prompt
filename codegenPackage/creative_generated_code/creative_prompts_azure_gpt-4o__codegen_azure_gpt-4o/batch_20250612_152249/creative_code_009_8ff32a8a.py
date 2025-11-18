"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Generate a Solidity contract that demonstrates how to inherit Bitcoin's fair launch properties for staking assets on the Botanix EVM.
Generated: DETERMINISTIC_8ff32a8a37ec6d6c
Batch ID: 20250612_152249
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
 * @title Botanix Fair Launch Staking Contract
 * @dev This contract demonstrates how to inherit Bitcoin's fair launch properties for staking assets.
 * It ensures a fair distribution, transparent rules, and no premining of rewards.
 */
contract FairLaunchStaking {

    // State variables
    address public owner; // Contract owner
    uint256 public startTimestamp; // When staking starts
    uint256 public stakingDuration; // Duration for staking (fair launch phase)
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per second

    mapping(address => uint256) public balances; // User staking balances
    mapping(address => uint256) public lastClaimedTimestamp; // Last timestamp when a user claimed rewards

    /**
     * @dev Modifier to restrict access to certain functions to the contract owner
     */
    modifier onlyOwner() {
        require(owner == msg.sender, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract parameters
     * @param _stakingDuration Duration of the staking period (in seconds)
     * @param _rewardRate Reward rate per second of staking
     */
    constructor(uint256 _stakingDuration, uint256 _rewardRate) {
        owner = msg.sender;
        startTimestamp = block.timestamp; // The fair launch starts at contract deployment
        stakingDuration = _stakingDuration;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake tokens into the contract
     */
    function stake() external payable {
        require(block.timestamp >= startTimestamp, "Staking has not started yet");
        require(block.timestamp <= startTimestamp + stakingDuration, "Staking period is over");
        require(msg.value > 0, "Must stake a non-zero amount");

        // Update staking balances
        balances[msg.sender] += msg.value;
        totalStaked += msg.value;

        // Update the last claimed timestamp for the user
        lastClaimedTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw staked tokens and claim rewards
     */
    function withdraw() external {
        uint256 stakedAmount = balances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        uint256 rewards = calculateRewards(msg.sender);

        // Reset user's staking balance and last claimed timestamp
        balances[msg.sender] = 0;
        lastClaimedTimestamp[msg.sender] = 0;

        // Deduct the withdrawn amount from the total staked
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to the user
        (bool successStaked, ) = msg.sender.call{value: stakedAmount}("");
        require(successStaked, "Failed to transfer staked tokens");

        if (rewards > 0) {
            (bool successRewards, ) = msg.sender.call{value: rewards}("");
            require(successRewards, "Failed to transfer rewards");
        }

        emit Withdrawn(msg.sender, stakedAmount, rewards);
    }

    /**
     * @dev Function to calculate the staking rewards for a user
     * @param user Address of the user
     * @return Rewards accrued by the user
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 lastClaimed = lastClaimedTimestamp[user];
        uint256 stakedAmount = balances[user];
        if (lastClaimed == 0 || stakedAmount == 0) {
            return 0;
        }

        // Calculate rewards based on the time elapsed and reward rate
        uint256 elapsedTime = block.timestamp - lastClaimed;
        return (elapsedTime * rewardRate * stakedAmount) / 1 ether;
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Event emitted when a user stakes tokens
     * @param user Address of the staker
     * @param amount Amount of tokens staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user withdraws staked tokens and rewards
     * @param user Address of the staker
     * @param stakedAmount Amount of tokens withdrawn
     * @param rewards Amount of rewards claimed
     */
    event Withdrawn(address indexed user, uint256 stakedAmount, uint256 rewards);
}
```
