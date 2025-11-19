"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-en.pages.dev
Prompt: Generate a Solidity smart contract snippet to implement tokenomics similar to WienerAI's allocation percentages (e.g., presale, staking, rewards, liquidity, marketing).
Generated: DETERMINISTIC_b0f968524fee949a
Batch ID: 20250612_151117
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

/**
 * @title WienerAI Tokenomics Contract
 * @author [Your Name]
 * @notice This contract implements tokenomics similar to WienerAI's allocation percentages.
 */
contract WienerAITokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tokenomics allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant STAKING_ALLOCATION = 15; // 15%
    uint256 public constant REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 25; // 25%

    // Tokenomics allocation addresses
    address public presaleAddress;
    address public stakingAddress;
    address public rewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Mapping of address to allocation
    mapping(address => uint256) public allocations;

    /**
     * @notice Constructor function
     * @param _presaleAddress Presale address
     * @param _stakingAddress Staking address
     * @param _rewardsAddress Rewards address
     * @param _liquidityAddress Liquidity address
     * @param _marketingAddress Marketing address
     */
    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _rewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) ERC20("WienerAI", "WAI") {
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;

        // Initialize token supply
        uint256 totalSupply = 1000 * 10**18; // 1000 tokens with 18 decimals

        // Allocate tokens
        allocateTokens(presaleAddress, PRESALE_ALLOCATION, totalSupply);
        allocateTokens(stakingAddress, STAKING_ALLOCATION, totalSupply);
        allocateTokens(rewardsAddress, REWARDS_ALLOCATION, totalSupply);
        allocateTokens(liquidityAddress, LIQUIDITY_ALLOCATION, totalSupply);
        allocateTokens(marketingAddress, MARKETING_ALLOCATION, totalSupply);

        // Mint tokens to respective addresses
        _mint(presaleAddress, calculateAllocation(PRESALE_ALLOCATION, totalSupply));
        _mint(stakingAddress, calculateAllocation(STAKING_ALLOCATION, totalSupply));
        _mint(rewardsAddress, calculateAllocation(REWARDS_ALLOCATION, totalSupply));
        _mint(liquidityAddress, calculateAllocation(LIQUIDITY_ALLOCATION, totalSupply));
        _mint(marketingAddress, calculateAllocation(MARKETING_ALLOCATION, totalSupply));
    }

    /**
     * @notice Allocate tokens to address
     * @param _address Address to allocate tokens to
     * @param _percentage Allocation percentage
     * @param _totalSupply Total token supply
     */
    function allocateTokens(
        address _address,
        uint256 _percentage,
        uint256 _totalSupply
    ) internal {
        allocations[_address] = calculateAllocation(_percentage, _totalSupply);
    }

    /**
     * @notice Calculate allocation
     * @param _percentage Allocation percentage
     * @param _totalSupply Total token supply
     * @return Allocation amount
     */
    function calculateAllocation(
        uint256 _percentage,
        uint256 _totalSupply
    ) internal pure returns (uint256) {
        return (_totalSupply * _percentage) / 100;
    }

    /**
     * @notice Transfer tokens with ReentrancyGuard
     * @param _from Sender address
     * @param _to Receiver address
     * @param _amount Token amount
     * @return bool
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) public override nonReentrant returns (bool) {
        return super.transferFrom(_from, _to, _amount);
    }

    /**
     * @notice Transfer tokens with ReentrancyGuard
     * @param _to Receiver address
     * @param _amount Token amount
     * @return bool
     */
    function transfer(
        address _to,
        uint256 _amount
    ) public override nonReentrant returns (bool) {
        return super.transfer(_to, _amount);
    }

    /**
     * @notice Burn tokens with ReentrancyGuard
     * @param _amount Token amount
     */
    function burn(uint256 _amount) public override nonReentrant {
        super.burn(_amount);
    }
}
```
