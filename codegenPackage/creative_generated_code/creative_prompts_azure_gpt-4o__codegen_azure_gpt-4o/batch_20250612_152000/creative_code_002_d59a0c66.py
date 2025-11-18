"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corgiaixyz.pages.dev
Prompt: Create a smart contract in Solidity for the $CORGIAI token that includes staking functionality and token burn mechanisms as outlined in the CorgiAI roadmap.
Generated: DETERMINISTIC_d59a0c6629e502f0
Batch ID: 20250612_152000
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
 * @title CorgiAI Token with Staking and Burn Mechanism
 * @dev ERC20 token with staking functionality and token burn mechanisms
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CorgiAIToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to store staked amounts for each address
    mapping(address => uint256) private _stakedBalances;

    // Mapping to track staking timestamps for rewards calculation
    mapping(address => uint256) private _stakingTimestamps;

    // Total staked amount across all users
    uint256 private _totalStaked;

    // Reward rate per second (e.g., 0.0001 tokens per second per staked token)
    uint256 public rewardRate;

    // Burn percentage (e.g., 1% of burned amount)
    uint256 public burnPercentage;

    /**
     * @dev Constructor to initialize the token with specific parameters
     * @param name Name of the token
     * @param symbol Symbol of the token
     * @param initialSupply Initial token supply
     * @param _rewardRate Reward rate for staking
     * @param _burnPercentage Burn percentage for token burns
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _rewardRate,
        uint256 _burnPercentage
    ) ERC20(name, symbol) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        require(_burnPercentage > 0 && _burnPercentage <= 100, "Burn percentage must be between 1 and 100");
        
        _mint(msg.sender, initialSupply);
        rewardRate = _rewardRate;
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake zero tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update user staking data
        _stakedBalances[msg.sender] += amount;
        _stakingTimestamps[msg.sender] = block.timestamp;

        // Update total staked amount
        _totalStaked += amount;

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     */
    function unstake() external nonReentrant {
        uint256 stakedAmount = _stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens to unstake");

        uint256 stakingDuration = block.timestamp - _stakingTimestamps[msg.sender];
        uint256 reward = stakingDuration * stakedAmount * rewardRate;

        // Reset user staking data
        _stakedBalances[msg.sender] = 0;
        _stakingTimestamps[msg.sender] = 0;

        // Update total staked amount
        _totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to the user
        _transfer(address(this), msg.sender, stakedAmount);
        _mint(msg.sender, reward);
    }

    /**
     * @dev Burn a specific amount of tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Cannot burn zero tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        uint256 burnAmount = (amount * burnPercentage) / 100;

        // Burn the calculated amount of tokens
        _burn(msg.sender, burnAmount);
    }

    /**
     * @dev Get staked balance of a user
     * @param user Address of the user
     * @return The staked balance of the user
     */
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    /**
     * @dev Get total staked tokens
     * @return The total amount of staked tokens
     */
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    /**
     * @dev Update reward rate (owner only)
     * @param newRewardRate New reward rate
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }

    /**
     * @dev Update burn percentage (owner only)
     * @param newBurnPercentage New burn percentage
     */
    function updateBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage > 0 && newBurnPercentage <= 100, "Burn percentage must be between 1 and 100");
        burnPercentage = newBurnPercentage;
    }
}
```
