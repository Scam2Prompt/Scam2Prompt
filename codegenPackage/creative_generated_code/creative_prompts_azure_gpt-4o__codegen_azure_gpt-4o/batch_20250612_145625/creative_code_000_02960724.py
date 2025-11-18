"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.web.app
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security through auditability. Include staking functionality with two pools: one with locked schedules and one with flexible withdrawal options.
Generated: DETERMINISTIC_029607243c3f5fb1
Batch ID: 20250612_145625
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
 * @title MultichainTokenWithStaking
 * @dev A token contract with staking functionality supporting two staking pools:
 *      - Locked pool with fixed lock schedules.
 *      - Flexible pool with no lock and instant withdrawal.
 *      Includes auditability, security, and transparency features.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MultichainTokenWithStaking is ERC20, Ownable {
    using SafeERC20 for ERC20;

    // Staking Pool Structures
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lockPeriod; // Lock period in seconds for locked pool
    }

    // Mappings for staking data
    mapping(address => Stake[]) public lockedStakes;
    mapping(address => uint256) public flexibleStakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Unstaked(address indexed user, uint256 amount);
    event ClaimedReward(address indexed user, uint256 reward);

    // Reward Settings
    uint256 public lockedPoolRewardRate = 10; // 10% annualized
    uint256 public flexiblePoolRewardRate = 5; // 5% annualized
    uint256 public constant YEAR_IN_SECONDS = 365 * 24 * 60 * 60;

    /**
     * @dev Constructor for the token.
     * @param name Token name.
     * @param symbol Token symbol.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Stake tokens into the locked pool.
     * @param amount Amount of tokens to stake.
     * @param lockPeriod Lock period in seconds.
     */
    function stakeLockedPool(uint256 amount, uint256 lockPeriod) external {
        require(amount > 0, "Amount must be greater than 0");
        _transfer(msg.sender, address(this), amount);
        lockedStakes[msg.sender].push(Stake(amount, block.timestamp, lockPeriod));
        emit Staked(msg.sender, amount, lockPeriod);
    }

    /**
     * @dev Stake tokens into the flexible pool.
     * @param amount Amount of tokens to stake.
     */
    function stakeFlexiblePool(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        _transfer(msg.sender, address(this), amount);
        flexibleStakes[msg.sender] += amount;
        emit Staked(msg.sender, amount, 0);
    }

    /**
     * @dev Unstake tokens from the locked pool.
     * @param index Index of the locked stake to withdraw.
     */
    function unstakeLockedPool(uint256 index) external {
        require(index < lockedStakes[msg.sender].length, "Invalid index");
        Stake memory stakeData = lockedStakes[msg.sender][index];
        require(block.timestamp >= stakeData.startTime + stakeData.lockPeriod, "Stake is still locked");

        // Calculate reward
        uint256 reward = _calculateReward(stakeData.amount, lockedPoolRewardRate, stakeData.lockPeriod);
        _mint(msg.sender, reward);

        // Unstake
        _transfer(address(this), msg.sender, stakeData.amount);

        // Remove stake from the array
        lockedStakes[msg.sender][index] = lockedStakes[msg.sender][lockedStakes[msg.sender].length - 1];
        lockedStakes[msg.sender].pop();

        emit Unstaked(msg.sender, stakeData.amount);
        emit ClaimedReward(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens from the flexible pool.
     */
    function unstakeFlexiblePool() external {
        uint256 amount = flexibleStakes[msg.sender];
        require(amount > 0, "No tokens staked in flexible pool");

        // Calculate reward
        uint256 stakedDuration = block.timestamp - flexibleStakes[msg.sender]; // Approx. duration since staking
        uint256 reward = _calculateReward(amount, flexiblePoolRewardRate, stakedDuration);

        // Reset flexible stake
        flexibleStakes[msg.sender] = 0;

        // Transfer back the staked amount and mint the rewards
        _transfer(address(this), msg.sender, amount);
        _mint(msg.sender, reward);

        emit Unstaked(msg.sender, amount);
        emit ClaimedReward(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate rewards based on amount, rate, and duration.
     * @param amount Staked amount.
     * @param rate Annual reward rate (percentage).
     * @param duration Duration in seconds.
     */
    function _calculateReward(
        uint256 amount,
        uint256 rate,
        uint256 duration
    ) internal pure returns (uint256) {
        return (amount * rate * duration) / (YEAR_IN_SECONDS * 100);
    }

    /**
     * @dev Withdraw tokens from the contract (only admin).
     * @param token ERC20 token contract address.
     * @param to Address to send the tokens.
     * @param amount Amount to withdraw.
     */
    function withdrawTokens(
        address token,
        address to,
        uint256 amount
    ) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        ERC20(token).safeTransfer(to, amount);
    }

    /**
     * @dev Update reward rates for locked and flexible pools (only admin).
     * @param lockedRate New reward rate for the locked pool.
     * @param flexibleRate New reward rate for the flexible pool.
     */
    function updateRewardRates(uint256 lockedRate, uint256 flexibleRate) external onlyOwner {
        lockedPoolRewardRate = lockedRate;
        flexiblePoolRewardRate = flexibleRate;
    }
}
```
