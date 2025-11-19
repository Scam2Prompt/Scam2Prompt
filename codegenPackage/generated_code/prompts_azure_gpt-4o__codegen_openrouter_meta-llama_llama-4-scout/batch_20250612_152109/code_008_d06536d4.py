"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-io.web.app
Prompt: Generate a Solidity contract for DOGE20 tokenomics that includes fixed supply, staking rewards distribution, and liquidity allocation, adhering to the specifications provided on the Dogecoin20 website.
Generated: DETERMINISTIC_d06536d43fff5005
Batch ID: 20250612_152109
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
 * @title Dogecoin20 Token Contract
 * @author [Your Name]
 * @notice This contract implements the DOGE20 tokenomics with fixed supply, 
 *         staking rewards distribution, and liquidity allocation.
 */
contract Dogecoin20 is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses and their respective staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of staker addresses and their respective reward claims
    mapping(address => uint256) private _rewardClaims;

    // Total staking rewards available
    uint256 public totalRewards;

    // Total liquidity allocated
    uint256 public totalLiquidity;

    // Staking rewards distribution rate (per block)
    uint256 public rewardsDistributionRate;

    // Liquidity allocation rate (per block)
    uint256 public liquidityAllocationRate;

    // Block number when staking starts
    uint256 public stakingStartBlock;

    // Block number when staking ends
    uint256 public stakingEndBlock;

    // Address of the liquidity pool
    address public liquidityPool;

    /**
     * @notice Constructor for the Dogecoin20 token contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param totalSupply The total supply of the token
     * @param rewardsDistributionRate The staking rewards distribution rate (per block)
     * @param liquidityAllocationRate The liquidity allocation rate (per block)
     * @param stakingStartBlock The block number when staking starts
     * @param stakingEndBlock The block number when staking ends
     * @param liquidityPool The address of the liquidity pool
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 rewardsDistributionRate,
        uint256 liquidityAllocationRate,
        uint256 stakingStartBlock,
        uint256 stakingEndBlock,
        address liquidityPool
    ) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);

        totalRewards = totalSupply.mul(10).div(100); // 10% of total supply for rewards
        totalLiquidity = totalSupply.mul(5).div(100); // 5% of total supply for liquidity

        this.rewardsDistributionRate = rewardsDistributionRate;
        this.liquidityAllocationRate = liquidityAllocationRate;
        this.stakingStartBlock = stakingStartBlock;
        this.stakingEndBlock = stakingEndBlock;
        this.liquidityPool = liquidityPool;
    }

    /**
     * @notice Stake DOGE20 tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period is over");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Unstake DOGE20 tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        _rewardClaims[msg.sender] = block.number;
        _transfer(address(this), msg.sender, rewards);
    }

    /**
     * @notice Calculate staking rewards for an address
     * @param account The address to calculate rewards for
     * @return The calculated rewards
     */
    function calculateRewards(address account) public view returns (uint256) {
        uint256 stakingBalance = _stakingBalances[account];
        uint256 blocksStaked = block.number.sub(_rewardClaims[account]);

        return stakingBalance.mul(rewardsDistributionRate).mul(blocksStaked);
    }

    /**
     * @notice Allocate liquidity
     */
    function allocateLiquidity() external nonReentrant {
        require(block.number >= stakingEndBlock, "Staking period is not over");

        _transfer(address(this), liquidityPool, totalLiquidity);
    }

    /**
     * @notice Get the staking balance of an address
     * @param account The address to get the staking balance for
     * @return The staking balance
     */
    function getStakingBalance(address account) public view returns (uint256) {
        return _stakingBalances[account];
    }
}
```
