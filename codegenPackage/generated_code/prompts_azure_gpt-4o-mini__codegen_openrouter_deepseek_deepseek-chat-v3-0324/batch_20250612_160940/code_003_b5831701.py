"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-in.pages.dev
Prompt: Develop a smart contract in Solidity for the Galaxy Fox token that includes features for token burning and staking rewards distribution.
Generated: DETERMINISTIC_b5831701296b777f
Batch ID: 20250612_160940
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GalaxyFoxToken is ERC20, ERC20Burnable, Ownable, ReentrancyGuard {
    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 startTime;
    }

    mapping(address => Stake) public stakes;
    uint256 public rewardRate = 100; // 100 tokens per second per staked token (adjust as needed)
    uint256 public totalStaked;

    // Events
    event TokensBurned(address indexed burner, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(uint256 initialSupply) ERC20("GalaxyFox", "GFOX") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Burns a specific amount of tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        _burn(_msgSender(), amount);
        emit TokensBurned(_msgSender(), amount);
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Calculate pending rewards if already staking
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingRewards = calculateRewards(msg.sender);
            _mint(msg.sender, pendingRewards);
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            startTime: block.timestamp
        });
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No tokens staked");

        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 rewards = calculateRewards(msg.sender);

        // Reset stake
        delete stakes[msg.sender];
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards
        _transfer(address(this), msg.sender, stakedAmount);
        _mint(msg.sender, rewards);

        emit TokensUnstaked(msg.sender, stakedAmount, rewards);
    }

    /**
     * @dev Calculate rewards for a staker.
     * @param staker Address of the staker.
     * @return rewards The calculated rewards.
     */
    function calculateRewards(address staker) public view returns (uint256 rewards) {
        Stake memory stakeInfo = stakes[staker];
        if (stakeInfo.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        rewards = stakeInfo.amount * stakingDuration * rewardRate / 1e18;
    }

    /**
     * @dev Update the reward rate (owner only).
     * @param newRate The new reward rate.
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be positive");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Withdraw any accidentally sent ERC20 tokens (owner only).
     * @param tokenAddress Address of the token contract.
     * @param amount Amount to withdraw.
     */
    function rescueERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
