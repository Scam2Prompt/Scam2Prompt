"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogs.pages.dev
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security as described in the Popo ecosystem. Include features for staking and rewards allocation.
Generated: DETERMINISTIC_d817be18bfc86c7e
Batch ID: 20250612_150013
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
 * @title Multichain Token with Staking and Rewards Allocation
 * @dev This contract implements a token with staking and rewards functionality,
 * ensuring transparency and security as part of the Popo ecosystem.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MultiChainToken is ERC20, ERC20Burnable, Ownable {
    // Mapping to track staking balances and timestamps
    mapping(address => uint256) private stakedBalances;
    mapping(address => uint256) private stakingStartTime;

    // Total rewards pool
    uint256 public rewardsPool;

    // Staking interest rate (e.g., 5% annualized rewards)
    uint256 public stakingRate = 500; // Basis points (100 = 1%)

    // Event declarations for transparency
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);
    event RewardsDeposited(address indexed depositor, uint256 amount);
    event StakingRateUpdated(uint256 newRate);

    /**
     * @dev Constructor initializes the token details.
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initial mint for the owner (optional, set your own logic)
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from the user to the contract for staking
        _transfer(msg.sender, address(this), amount);

        // Update staking balances and start timestamp
        stakedBalances[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and receive rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens are staked");

        // Calculate staking duration and rewards
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = calculateRewards(stakedAmount, stakingDuration);

        // Ensure rewards pool has sufficient funds
        require(rewardsPool >= reward, "Insufficient rewards pool");

        // Update internal state
        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        rewardsPool -= reward;

        // Transfer staked tokens and rewards back to the user
        _transfer(address(this), msg.sender, stakedAmount + reward);

        emit TokensUnstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculate rewards based on staked amount and duration.
     * @param amount Staked amount
     * @param duration Duration in seconds
     * @return Reward amount
     */
    function calculateRewards(uint256 amount, uint256 duration) public view returns (uint256) {
        // Annualized reward calculation (assuming 365 days)
        uint256 annualReward = (amount * stakingRate) / 10_000;
        return (annualReward * duration) / (365 days);
    }

    /**
     * @dev Deposit tokens into the rewards pool.
     * @param amount The amount of tokens to deposit.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the owner to the contract
        _transfer(msg.sender, address(this), amount);

        // Update rewards pool
        rewardsPool += amount;

        emit RewardsDeposited(msg.sender, amount);
    }

    /**
     * @dev Update the staking rate (in basis points).
     * @param newRate The new staking rate.
     */
    function setStakingRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than zero");

        // Update staking rate
        stakingRate = newRate;

        emit StakingRateUpdated(newRate);
    }

    /**
     * @dev View staked balance for a given account.
     * @param account Address of the staker.
     * @return Staked balance.
     */
    function stakedBalanceOf(address account) external view returns (uint256) {
        return stakedBalances[account];
    }
}
```
