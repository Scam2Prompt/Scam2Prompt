"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-live.pages.dev
Prompt: Develop a Solidity contract for a decentralized cloud mining platform that uses ERC-20 tokens for staking and mining credits, inspired by Bitcoin Minetrix's solution to traditional cloud mining risks.
Generated: DETERMINISTIC_6c34423ae71b1634
Batch ID: 20250612_153606
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
 * @title Decentralized Cloud Mining Platform
 * @dev This contract allows users to stake ERC-20 tokens in exchange for mining credits.
 * Inspired by Bitcoin Minetrix's solution to traditional cloud mining risks.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract DecentralizedCloudMining {
    // ERC-20 token used for staking and mining credits
    IERC20 public stakingToken;

    // Owner address
    address public owner;

    // Total staked balance
    uint256 public totalStaked;

    // Struct to hold user staking data
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 miningCredits; // Mining credits earned
        uint256 lastUpdated; // Timestamp of the last update
    }

    // Mapping of user address to their staking information
    mapping(address => StakeInfo) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims mining credits
    event MiningCreditsClaimed(address indexed user, uint256 credits);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        owner = msg.sender;
    }

    /**
     * @dev Stake tokens to earn mining credits.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from sender to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's staking information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.miningCredits += calculateMiningCredits(amount);
        stakeInfo.lastUpdated = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked balance");

        // Update user's staking information
        stakeInfo.amount -= amount;
        stakeInfo.miningCredits = calculateMiningCredits(stakeInfo.amount);
        stakeInfo.lastUpdated = block.timestamp;

        totalStaked -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned mining credits.
     */
    function claimMiningCredits() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.miningCredits > 0, "No mining credits available");

        uint256 credits = stakeInfo.miningCredits;

        // Reset mining credits
        stakeInfo.miningCredits = 0;

        emit MiningCreditsClaimed(msg.sender, credits);

        // Here, you can implement additional logic for mining credit distribution
        // e.g., transferring mining rewards or interacting with another contract.
    }

    /**
     * @dev Calculate mining credits based on staked amount.
     * @param amount The amount of tokens staked.
     * @return The calculated mining credits.
     */
    function calculateMiningCredits(uint256 amount) internal pure returns (uint256) {
        // Placeholder logic for mining credit calculation
        // Modify as needed to fit your mining algorithm
        return amount / 10; // Example: 10% of the staked amount
    }

    /**
     * @dev Retrieve the staked balance of a user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Retrieve the mining credits of a user.
     * @param user The address of the user.
     * @return The mining credits of the user.
     */
    function getMiningCredits(address user) external view returns (uint256) {
        return stakes[user].miningCredits;
    }

    /**
     * @dev Allow the owner to withdraw excess tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        require(stakingToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
