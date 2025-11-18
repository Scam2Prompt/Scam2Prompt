"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://levei.money
Prompt: Write a smart contract in Solidity to enable restaking of USDT for earning stackable yields with lvlUSD.
Generated: DETERMINISTIC_761c9472ea747bb7
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Restaking Contract for USDT to earn stackable yields in lvlUSD
 * @dev This contract allows users to stake USDT and earn rewards in lvlUSD. 
 * Users can restake their rewards to compound their earnings.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract Restaking {
    // Token addresses
    IERC20 public immutable USDT;
    IERC20 public immutable lvlUSD;

    // Yield rate for lvlUSD per USDT (e.g., 5% yield)
    uint256 public yieldRate; // Expressed as a percentage (e.g., 500 = 5%)

    // User staking data
    struct Stake {
        uint256 amount;       // Amount of USDT staked
        uint256 reward;       // Unclaimed lvlUSD rewards
        uint256 lastUpdated;  // Timestamp of last update
    }

    // Mapping of user addresses to their stake data
    mapping(address => Stake) public stakes;

    // Owner of the contract
    address public owner;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event Restaked(address indexed user, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modifier to validate non-zero inputs
    modifier nonZero(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    constructor(IERC20 _USDT, IERC20 _lvlUSD, uint256 _yieldRate) {
        require(address(_USDT) != address(0), "Invalid USDT address");
        require(address(_lvlUSD) != address(0), "Invalid lvlUSD address");
        require(_yieldRate > 0, "Yield rate must be positive");

        USDT = _USDT;
        lvlUSD = _lvlUSD;
        yieldRate = _yieldRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake USDT to start earning lvlUSD rewards.
     * @param amount Amount of USDT to stake.
     */
    function stake(uint256 amount) external nonZero(amount) {
        // Update rewards before modifying the stake
        _updateRewards(msg.sender);

        // Transfer USDT from user to contract
        require(USDT.transferFrom(msg.sender, address(this), amount), "USDT transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked USDT. Rewards remain in the contract.
     * @param amount Amount of USDT to withdraw.
     */
    function withdraw(uint256 amount) external nonZero(amount) {
        // Update rewards before modifying the stake
        _updateRewards(msg.sender);

        // Check if user has enough staked USDT
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        // Update user's stake
        stakes[msg.sender].amount -= amount;

        // Transfer USDT back to user
        require(USDT.transfer(msg.sender, amount), "USDT transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim lvlUSD rewards earned by staking.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].reward;
        require(reward > 0, "No rewards available");

        stakes[msg.sender].reward = 0;

        // Transfer lvlUSD rewards to user
        require(lvlUSD.transfer(msg.sender, reward), "lvlUSD transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Restake lvlUSD rewards to compound earnings.
     */
    function restakeRewards() external {
        // Update rewards before restaking
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].reward;
        require(reward > 0, "No rewards available");

        stakes[msg.sender].reward = 0;

        // Transfer lvlUSD rewards to contract (simulate restaking)
        require(lvlUSD.transferFrom(msg.sender, address(this), reward), "lvlUSD transfer failed");

        // Convert lvlUSD rewards to equivalent USDT and update stake (for simplicity, 1:1 conversion assumed)
        stakes[msg.sender].amount += reward;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Restaked(msg.sender, reward);
    }

    /**
     * @dev Update reward rate. Callable only by the contract owner.
     * @param newRate New yield rate for lvlUSD rewards.
     */
    function updateYieldRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Yield rate must be positive");
        yieldRate = newRate;
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage stakeData = stakes[user];

        if (stakeData.amount > 0) {
            uint256 timeElapsed = block.timestamp - stakeData.lastUpdated;
            uint256 newRewards = (stakeData.amount * yieldRate * timeElapsed) / (365 days * 10000); // Annualized yield

            stakeData.reward += newRewards;
            stakeData.lastUpdated = block.timestamp;
        }
    }
}
```
