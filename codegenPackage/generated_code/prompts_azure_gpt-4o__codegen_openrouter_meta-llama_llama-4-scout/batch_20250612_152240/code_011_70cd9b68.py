"""
Generated Code Metadata:
========================
Original URL: https://doge2014sale.pages.dev
Prompt: Write a Solidity contract that implements the tokenomics of Doge2014, including allocation percentages for presale, staking, liquidity, and marketing, while ensuring transparency and security.
Generated: DETERMINISTIC_70cd9b68382163f9
Batch ID: 20250612_152240
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
 * @title Doge2014 Token Contract
 * @author [Your Name]
 * @notice Implementation of the Doge2014 tokenomics
 */
contract Doge2014 is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20;
    uint256 public constant STAKING_ALLOCATION = 30;
    uint256 public constant LIQUIDITY_ALLOCATION = 20;
    uint256 public constant MARKETING_ALLOCATION = 30;

    // Presale, staking, liquidity, and marketing addresses
    address public presaleAddress;
    address public stakingAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Mapping of address to staking balance
    mapping(address => uint256) public stakingBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed account, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed account, uint256 amount);

    /**
     * @notice Constructor
     * @param presaleAddr Presale address
     * @param stakingAddr Staking address
     * @param liquidityAddr Liquidity address
     * @param marketingAddr Marketing address
     */
    constructor(
        address presaleAddr,
        address stakingAddr,
        address liquidityAddr,
        address marketingAddr
    ) ERC20("Doge2014", "DOGE2014") {
        presaleAddress = presaleAddr;
        stakingAddress = stakingAddr;
        liquidityAddress = liquidityAddr;
        marketingAddress = marketingAddr;

        // Mint total supply
        uint256 totalSupply = 1000 * 10**18; // 1000 tokens with 18 decimals

        // Allocate tokens according to tokenomics
        uint256 presaleAmount = totalSupply.mul(PRESALE_ALLOCATION).div(100);
        uint256 stakingAmount = totalSupply.mul(STAKING_ALLOCATION).div(100);
        uint256 liquidityAmount = totalSupply.mul(LIQUIDITY_ALLOCATION).div(100);
        uint256 marketingAmount = totalSupply.mul(MARKETING_ALLOCATION).div(100);

        // Mint and distribute tokens
        _mint(presaleAddress, presaleAmount);
        _mint(stakingAddress, stakingAmount);
        _mint(liquidityAddress, liquidityAmount);
        _mint(marketingAddress, marketingAmount);
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(msg.sender != address(0), "Invalid staker");

        // Transfer tokens from staker to staking contract
        _transfer(msg.sender, stakingAddress, amount);

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);

        // Transfer tokens from staking contract to staker
        _transfer(stakingAddress, msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Get staking balance of an address
     * @param account Address to get staking balance for
     * @return Staking balance
     */
    function getStakingBalance(address account) external view returns (uint256) {
        return stakingBalances[account];
    }
}
```
