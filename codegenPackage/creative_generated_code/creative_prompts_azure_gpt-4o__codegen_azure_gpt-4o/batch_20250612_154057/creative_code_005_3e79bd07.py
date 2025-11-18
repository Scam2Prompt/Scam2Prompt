"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Write a Solidity contract for distributing $99BTC tokens as staking rewards, ensuring compliance with the tokenomics allocation (14% of the total supply over two years) specified by 99Bitcoins.
Generated: DETERMINISTIC_3e79bd07c2f6bc5e
Batch ID: 20250612_154057
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
 * @title StakingRewardsDistributor
 * @dev Distributes $99BTC tokens as staking rewards over two years,
 *      ensuring compliance with the tokenomics allocation (14% of the total supply).
 */
contract StakingRewardsDistributor {
    IERC20 public immutable token; // $99BTC token contract
    address public owner; // Owner of the contract

    uint256 public immutable totalSupply; // Total supply of $99BTC tokens
    uint256 public immutable rewardsAllocation; // 14% of the total supply allocated for rewards
    uint256 public immutable distributionDuration; // Distribution duration in seconds (2 years)

    uint256 public immutable startTime; // Start time of rewards distribution
    uint256 public lastUpdateTime; // Last time rewards were calculated
    uint256 public rewardsPerSecond; // Rewards rate per second

    mapping(address => uint256) public rewards; // Rewards accumulated by each staker
    mapping(address => uint256) public lastClaimedTime; // Last claimed time for each staker

    // Events
    event RewardsClaimed(address indexed staker, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the $99BTC token contract.
     * @param _totalSupply Total supply of the $99BTC tokens.
     */
    constructor(IERC20 _token, uint256 _totalSupply) {
        require(address(_token) != address(0), "Invalid token address");
        require(_totalSupply > 0, "Invalid total supply");

        token = _token;
        totalSupply = _totalSupply;
        rewardsAllocation = (totalSupply * 14) / 100; // 14% of total supply
        distributionDuration = 2 * 365 * 24 * 60 * 60; // Two years in seconds
        startTime = block.timestamp;
        lastUpdateTime = block.timestamp;
        rewardsPerSecond = rewardsAllocation / distributionDuration;

        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Calculates the pending rewards for a given staker.
     * @param staker Address of the staker.
     * @return Pending rewards amount.
     */
    function calculatePendingRewards(address staker) public view returns (uint256) {
        uint256 elapsedTime = block.timestamp - lastClaimedTime[staker];
        uint256 pendingRewards = elapsedTime * rewardsPerSecond;
        return pendingRewards;
    }

    /**
     * @dev Allows a staker to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        require(pendingRewards > 0, "No rewards available to claim");

        rewards[msg.sender] += pendingRewards;
        lastClaimedTime[msg.sender] = block.timestamp;

        require(token.transfer(msg.sender, pendingRewards), "Token transfer failed");
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether not accepted");
    }

    receive() external payable {
        revert("Ether not accepted");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
