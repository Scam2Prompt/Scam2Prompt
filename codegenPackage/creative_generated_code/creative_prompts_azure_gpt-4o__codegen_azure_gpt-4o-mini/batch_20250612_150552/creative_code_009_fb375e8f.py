"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-22u.pages.dev
Prompt: Generate a Solidity smart contract for handling the tokenomics of $DOGEVERSE, including minting, staking, and allocation percentages for liquidity, marketing, and ecosystem funds.
Generated: DETERMINISTIC_fb375e8fe83543aa
Batch ID: 20250612_150552
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DogeVerseToken is ERC20, Ownable, ReentrancyGuard {
    // Allocation percentages
    uint256 public liquidityAllocation = 30; // 30% for liquidity
    uint256 public marketingAllocation = 20; // 20% for marketing
    uint256 public ecosystemAllocation = 50; // 50% for ecosystem funds

    // Total amount of tokens to be minted
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Staking related variables
    mapping(address => uint256) public stakedTokens;
    mapping(address => uint256) public stakingStart;
    uint256 public stakingDuration = 30 days; // Staking duration

    // Events
    event TokensMinted(address indexed to, uint256 amount);
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);

    constructor() ERC20("DogeVerse Token", "DOGEVERSE") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Mint new tokens.
     * Only the owner can call this function.
     * @param to The address to receive minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Stake tokens for a specified duration.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        stakedTokens[msg.sender] += amount;
        stakingStart[msg.sender] = block.timestamp;

        _transfer(msg.sender, address(this), amount);
        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens after the staking duration.
     */
    function unstake() external nonReentrant {
        require(stakedTokens[msg.sender] > 0, "No staked tokens");
        require(block.timestamp >= stakingStart[msg.sender] + stakingDuration, "Staking period not yet over");

        uint256 amount = stakedTokens[msg.sender];
        stakedTokens[msg.sender] = 0;

        _transfer(address(this), msg.sender, amount);
        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Get the total percentage allocated for liquidity, marketing, and ecosystem.
     * @return Total percentage.
     */
    function getTotalAllocationPercentage() external view returns (uint256) {
        return liquidityAllocation + marketingAllocation + ecosystemAllocation;
    }

    /**
     * @dev Set the allocation percentages. Only the owner can modify these.
     */
    function setAllocations(uint256 _liquidity, uint256 _marketing, uint256 _ecosystem) external onlyOwner {
        require(_liquidity + _marketing + _ecosystem == 100, "Total allocation must equal 100");
        
        liquidityAllocation = _liquidity;
        marketingAllocation = _marketing;
        ecosystemAllocation = _ecosystem;
    }
}
```
