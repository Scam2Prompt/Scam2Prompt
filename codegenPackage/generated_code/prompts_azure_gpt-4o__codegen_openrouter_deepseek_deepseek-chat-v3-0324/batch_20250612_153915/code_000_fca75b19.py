"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: Write a script to integrate $SOON token functionality into a Web3 gaming platform, referencing the tokenomics and utility described in TON Station's Season 2 guide.
Generated: DETERMINISTIC_fca75b19b8dd2dc0
Batch ID: 20250612_153915
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title $SOON Token Contract for Web3 Gaming Platform
 * @dev Implements tokenomics and utility features as described in TON Station's Season 2 guide
 */
contract SoonToken is ERC20, Ownable, Pausable {
    // Token distribution parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = 200_000_000 * 10**18; // 20%
    uint256 public constant ECOSYSTEM_FUND = 150_000_000 * 10**18; // 15%
    uint256 public constant PLAY_TO_EARN_POOL = 350_000_000 * 10**18; // 35%
    uint256 public constant COMMUNITY_REWARDS = 300_000_000 * 10**18; // 30%

    // Vesting parameters
    uint256 public constant VESTING_DURATION = 365 days; // 1 year vesting
    uint256 public constant VESTING_CLIFF = 90 days; // 3 month cliff
    uint256 public teamVestingStart;
    uint256 public teamVestedAmount;

    // Game utility parameters
    uint256 public stakingRewardRate = 10; // 10% APY
    uint256 public gameplayMultiplier = 2; // 2x multiplier for in-game rewards

    // Addresses
    address public ecosystemFund;
    address public playToEarnPool;
    address public communityRewards;

    // Game-related mappings
    mapping(address => bool) public gameContracts;
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public lastStakeTime;
    mapping(address => uint256) public gameplayScores;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event GameplayReward(address indexed user, uint256 score, uint256 reward);

    modifier onlyGameContract() {
        require(gameContracts[msg.sender], "Caller is not a game contract");
        _;
    }

    constructor(
        address _ecosystemFund,
        address _playToEarnPool,
        address _communityRewards,
        address _teamWallet
    ) ERC20("SOON Token", "SOON") {
        require(_ecosystemFund != address(0), "Invalid ecosystem fund address");
        require(_playToEarnPool != address(0), "Invalid play-to-earn pool address");
        require(_communityRewards != address(0), "Invalid community rewards address");
        require(_teamWallet != address(0), "Invalid team wallet address");

        ecosystemFund = _ecosystemFund;
        playToEarnPool = _playToEarnPool;
        communityRewards = _communityRewards;

        // Mint initial allocations
        _mint(ecosystemFund, ECOSYSTEM_FUND);
        _mint(playToEarnPool, PLAY_TO_EARN_POOL);
        _mint(communityRewards, COMMUNITY_REWARDS);
        
        // Team allocation is vested
        teamVestingStart = block.timestamp;
        
        // Remaining supply can be minted later for rewards
    }

    /**
     * @dev Pause token transfers (for emergency situations)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override transfer to respect pause state
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Add a game contract address
     */
    function addGameContract(address gameContract) external onlyOwner {
        require(gameContract != address(0), "Invalid game contract address");
        gameContracts[gameContract] = true;
    }

    /**
     * @dev Remove a game contract address
     */
    function removeGameContract(address gameContract) external onlyOwner {
        gameContracts[gameContract] = false;
    }

    /**
     * @dev Stake tokens to earn rewards
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _claimRewards();
        
        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        lastStakeTime[msg.sender] = block.timestamp;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        _claimRewards();
        
        stakedBalances[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimRewards() external {
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and distribute staking rewards
     */
    function _claimRewards() internal {
        if (stakedBalances[msg.sender] == 0) return;
        
        uint256 stakingDuration = block.timestamp - lastStakeTime[msg.sender];
        uint256 reward = (stakedBalances[msg.sender] * stakingRewardRate * stakingDuration) / 
                        (100 * 365 days);
        
        if (reward > 0) {
            _mint(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
        
        lastStakeTime[msg.sender] = block.timestamp;
    }

    /**
     * @dev Distribute gameplay rewards (called by game contracts)
     */
    function distributeGameplayReward(address player, uint256 score) external onlyGameContract {
        require(score > 0, "Score must be positive");
        
        gameplayScores[player] += score;
        uint256 reward = score * gameplayMultiplier;
        
        _mint(player, reward);
        emit GameplayReward(player, score, reward);
    }

    /**
     * @dev Release vested team tokens
     */
    function releaseTeamTokens() external onlyOwner {
        require(block.timestamp >= teamVestingStart + VESTING_CLIFF, "Cliff period not over");
        
        uint256 elapsedTime = block.timestamp - teamVestingStart;
        uint256 vestedAmount;
        
        if (elapsedTime >= VESTING_DURATION) {
            vestedAmount = TEAM_ALLOCATION - teamVestedAmount;
        } else {
            vestedAmount = (TEAM_ALLOCATION * elapsedTime) / VESTING_DURATION - teamVestedAmount;
        }
        
        if (vestedAmount > 0) {
            teamVestedAmount += vestedAmount;
            _mint(owner(), vestedAmount);
        }
    }

    /**
     * @dev Update staking reward rate (owner only)
     */
    function setStakingRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Rate too high"); // Max 100% APY
        stakingRewardRate = newRate;
    }

    /**
     * @dev Update gameplay multiplier (owner only)
     */
    function setGameplayMultiplier(uint256 newMultiplier) external onlyOwner {
        require(newMultiplier <= 10, "Multiplier too high"); // Max 10x
        gameplayMultiplier = newMultiplier;
    }

    /**
     * @dev Mint additional tokens for rewards (owner only)
     */
    function mintRewards(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
    }
}
```
