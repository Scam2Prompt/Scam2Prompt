"""
Generated Code Metadata:
========================
Original URL: https://dogeverse-24m.pages.dev
Prompt: Create a smart contract in Solidity to manage the Dogeverse tokenomics, including token allocation, presale, and staking mechanisms.
Generated: DETERMINISTIC_bb8eb372b8a1cc0c
Batch ID: 20250622_204646
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Dogeverse Tokenomics Smart Contract
 * @author [Your Name]
 * @notice This contract manages the Dogeverse tokenomics, including token allocation, presale, and staking mechanisms.
 */
contract DogeverseTokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token allocation
    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _stakingBalances;

    // Presale configuration
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public presaleTokenPrice;
    uint256 public presaleTokensSold;

    // Staking configuration
    uint256 public stakingStart;
    uint256 public stakingEnd;
    uint256 public stakingRewardRate;

    // Events
    event PresaleStarted();
    event PresaleEnded();
    event StakingStarted();
    event StakingEnded();
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);
    event StakingRewardClaimed(address indexed staker, uint256 amount);

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);

        // Initialize presale configuration
        presaleStart = block.timestamp;
        presaleEnd = presaleStart + 30 days;
        presaleTokenPrice = 1e18; // 1 token = 1 USD (18 decimals)

        // Initialize staking configuration
        stakingStart = presaleEnd;
        stakingEnd = stakingStart + 90 days;
        stakingRewardRate = 10; // 10% APY
    }

    /**
     * @notice Start presale
     */
    function startPresale() external onlyOwner {
        require(presaleStart == block.timestamp, "Presale already started");
        emit PresaleStarted();
    }

    /**
     * @notice End presale
     */
    function endPresale() external onlyOwner {
        require(presaleEnd <= block.timestamp, "Presale not ended yet");
        emit PresaleEnded();
    }

    /**
     * @notice Start staking
     */
    function startStaking() external onlyOwner {
        require(stakingStart == block.timestamp, "Staking already started");
        emit StakingStarted();
    }

    /**
     * @notice End staking
     */
    function endStaking() external onlyOwner {
        require(stakingEnd <= block.timestamp, "Staking not ended yet");
        emit StakingEnded();
    }

    /**
     * @notice Buy tokens during presale
     * @param amount Amount of tokens to buy
     */
    function buyTokens(uint256 amount) external nonReentrant {
        require(presaleStart <= block.timestamp && block.timestamp <= presaleEnd, "Presale not active");
        require(amount > 0, "Invalid amount");

        uint256 tokensToBuy = amount.mul(1e18).div(presaleTokenPrice);
        require(balanceOf(owner()) >= tokensToBuy, "Insufficient tokens for sale");

        _transfer(owner(), msg.sender, tokensToBuy);
        presaleTokensSold = presaleTokensSold.add(tokensToBuy);

        emit TokensStaked(msg.sender, tokensToBuy);
    }

    /**
     * @notice Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stakeTokens(uint256 amount) external nonReentrant {
        require(stakingStart <= block.timestamp && block.timestamp <= stakingEnd, "Staking not active");
        require(amount > 0, "Invalid amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstakeTokens(uint256 amount) external nonReentrant {
        require(stakingStart <= block.timestamp && block.timestamp <= stakingEnd, "Staking not active");
        require(amount > 0, "Invalid amount");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _balances[msg.sender] = _balances[msg.sender].add(amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimStakingRewards() external nonReentrant {
        require(stakingStart <= block.timestamp && block.timestamp <= stakingEnd, "Staking not active");
        require(_stakingBalances[msg.sender] > 0, "No staked balance");

        uint256 rewards = _stakingBalances[msg.sender].mul(stakingRewardRate).div(100);
        _balances[msg.sender] = _balances[msg.sender].add(rewards);

        emit StakingRewardClaimed(msg.sender, rewards);
    }

    /**
     * @notice Get token balance
     * @param account Account address
     * @return Token balance
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Get staked token balance
     * @param account Account address
     * @return Staked token balance
     */
    function stakedBalanceOf(address account) public view returns (uint256) {
        return _stakingBalances[account];
    }
}
```
