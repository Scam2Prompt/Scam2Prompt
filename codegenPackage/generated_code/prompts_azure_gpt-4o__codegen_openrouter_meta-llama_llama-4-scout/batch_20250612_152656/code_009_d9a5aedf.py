"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-d.web.app
Prompt: Create a Solidity contract for DOGE20 tokenomics that allocates 25% of the supply to presale, 25% to marketing, 25% to treasury, 15% to staking rewards, and 10% to liquidity.
Generated: DETERMINISTIC_d9a5aedf77717ae8
Batch ID: 20250612_152656
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
 * @notice This contract manages the DOGE20 tokenomics, including token allocation and distribution.
 */
contract DOGE20Tokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 25;
    uint256 public constant MARKETING_ALLOCATION = 25;
    uint256 public constant TREASURY_ALLOCATION = 25;
    uint256 public constant STAKING_REWARDS_ALLOCATION = 15;
    uint256 public constant LIQUIDITY_ALLOCATION = 10;

    // Token allocation addresses
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    // Total token supply
    uint256 public totalSupply_;

    /**
     * @notice Constructor function to initialize the contract
     * @param _presaleAddress Presale address
     * @param _marketingAddress Marketing address
     * @param _treasuryAddress Treasury address
     * @param _stakingRewardsAddress Staking rewards address
     * @param _liquidityAddress Liquidity address
     */
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingRewardsAddress,
        address _liquidityAddress
    ) ERC20("DOGE20", "DOGE20") {
        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Calculate total token supply
        totalSupply_ = 100 * 10**6 * 10**18; // 100 million tokens with 18 decimals

        // Allocate tokens to presale
        _mint(presaleAddress, totalSupply_.mul(PRESALE_ALLOCATION).div(100));

        // Allocate tokens to marketing
        _mint(marketingAddress, totalSupply_.mul(MARKETING_ALLOCATION).div(100));

        // Allocate tokens to treasury
        _mint(treasuryAddress, totalSupply_.mul(TREASURY_ALLOCATION).div(100));

        // Allocate tokens to staking rewards
        _mint(stakingRewardsAddress, totalSupply_.mul(STAKING_REWARDS_ALLOCATION).div(100));

        // Allocate tokens to liquidity
        _mint(liquidityAddress, totalSupply_.mul(LIQUIDITY_ALLOCATION).div(100));
    }

    /**
     * @notice Function to handle token transfers
     * @param from Sender address
     * @param to Receiver address
     * @param amount Transfer amount
     * @return bool indicating success
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(to != address(0), "ERC20: transfer to the zero address");

        uint256 senderBalance = balanceOf(msg.sender);
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");

        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @notice Function to handle token approvals
     * @param spender Spender address
     * @param amount Approved amount
     * @return bool indicating success
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "ERC20: approve to the zero address");

        _approve(msg.sender, spender, amount);
        return true;
    }
}
```
