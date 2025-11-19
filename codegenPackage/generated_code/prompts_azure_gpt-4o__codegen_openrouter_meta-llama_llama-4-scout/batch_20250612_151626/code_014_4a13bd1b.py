"""
Generated Code Metadata:
========================
Original URL: https://dogee1.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics that enforces the fixed supply and allocates tokens according to the presale, marketing, treasury, staking rewards, and liquidity provisions.
Generated: DETERMINISTIC_4a13bd1b8a82710d
Batch ID: 20250612_151626
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
 * @title DOGE20 Tokenomics Contract
 * @author [Your Name]
 * @notice This contract manages the DOGE20 tokenomics, enforcing a fixed supply and allocating tokens according to presale, marketing, treasury, staking rewards, and liquidity provisions.
 */
contract DOGE20Tokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token allocations
    mapping(address => uint256) public allocations;

    // Token supply
    uint256 public constant TOTAL_SUPPLY = 10**9 * 10**18; // 1 billion tokens with 18 decimals

    // Presale, marketing, treasury, staking rewards, and liquidity provision addresses
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityProvisionAddress;

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant TREASURY_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_PROVISION_ALLOCATION = 35; // 35%

    /**
     * @notice Initializes the DOGE20 tokenomics contract.
     * @param _presaleAddress Presale address.
     * @param _marketingAddress Marketing address.
     * @param _treasuryAddress Treasury address.
     * @param _stakingRewardsAddress Staking rewards address.
     * @param _liquidityProvisionAddress Liquidity provision address.
     */
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingRewardsAddress,
        address _liquidityProvisionAddress
    ) ERC20("DOGE20", "DOGE20") {
        require(
            PRESALE_ALLOCATION + MARKETING_ALLOCATION + TREASURY_ALLOCATION + STAKING_REWARDS_ALLOCATION + LIQUIDITY_PROVISION_ALLOCATION == 100,
            "Allocation percentages do not add up to 100%"
        );

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityProvisionAddress = _liquidityProvisionAddress;

        // Calculate token allocations
        uint256 presaleAllocation = TOTAL_SUPPLY.mul(PRESALE_ALLOCATION).div(100);
        uint256 marketingAllocation = TOTAL_SUPPLY.mul(MARKETING_ALLOCATION).div(100);
        uint256 treasuryAllocation = TOTAL_SUPPLY.mul(TREASURY_ALLOCATION).div(100);
        uint256 stakingRewardsAllocation = TOTAL_SUPPLY.mul(STAKING_REWARDS_ALLOCATION).div(100);
        uint256 liquidityProvisionAllocation = TOTAL_SUPPLY.mul(LIQUIDITY_PROVISION_ALLOCATION).div(100);

        allocations[presaleAddress] = presaleAllocation;
        allocations[marketingAddress] = marketingAllocation;
        allocations[treasuryAddress] = treasuryAllocation;
        allocations[stakingRewardsAddress] = stakingRewardsAllocation;
        allocations[liquidityProvisionAddress] = liquidityProvisionAllocation;

        // Mint tokens to allocated addresses
        _mint(presaleAddress, presaleAllocation);
        _mint(marketingAddress, marketingAllocation);
        _mint(treasuryAddress, treasuryAllocation);
        _mint(stakingRewardsAddress, stakingRewardsAllocation);
        _mint(liquidityProvisionAddress, liquidityProvisionAllocation);
    }

    /**
     * @notice Burns tokens from the contract.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        require(msg.sender != address(0), "Cannot burn from the zero address");
        _burn(msg.sender, amount);
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param from Address to transfer from.
     * @param to Address to transfer to.
     * @param amount Amount of tokens to transfer.
     * @return bool Whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 allowance = allowance(from, msg.sender);
        require(allowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(from, msg.sender, allowance.sub(amount));
        _transfer(from, to, amount);
        return true;
    }

    /**
     * @notice Checks if an address has an allocation.
     * @param account Address to check.
     * @return bool Whether the address has an allocation.
     */
    function hasAllocation(address account) public view returns (bool) {
        return allocations[account] > 0;
    }

    /**
     * @notice Gets the allocation of an address.
     * @param account Address to get allocation for.
     * @return uint256 The allocation of the address.
     */
    function getAllocation(address account) public view returns (uint256) {
        return allocations[account];
    }
}
```
