"""
Generated Code Metadata:
========================
Original URL: https://popofrog-6s6.pages.dev
Prompt: Write a Solidity function to implement the tokenomics of $FROP, ensuring proper allocation of the fixed supply across presale, staking, marketing, rewards, and liquidity.
Generated: DETERMINISTIC_d6780ffc7a1c2ba3
Batch ID: 20250612_152321
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

contract FROPTokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping for token allocations
    mapping(address => uint256) public allocations;

    // Addresses for different allocations
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public liquidityAddress;

    // Token supply allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 15;
    uint256 public constant STAKING_ALLOCATION = 20;
    uint256 public constant MARKETING_ALLOCATION = 10;
    uint256 public constant REWARDS_ALLOCATION = 30;
    uint256 public constant LIQUIDITY_ALLOCATION = 25;

    // Total supply
    uint256 public constant TOTAL_SUPPLY = 1000 * 10**18; // 1000 tokens with 18 decimals

    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _liquidityAddress
    ) ERC20("FROP", "FROP") {
        require(
            PRESALE_ALLOCATION + STAKING_ALLOCATION + MARKETING_ALLOCATION + REWARDS_ALLOCATION + LIQUIDITY_ALLOCATION == 100,
            "Allocations do not add up to 100%"
        );

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Mint and allocate tokens
        _mint(address(this), TOTAL_SUPPLY);

        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 stakingAmount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        uint256 rewardsAmount = (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;

        _transfer(address(this), presaleAddress, presaleAmount);
        allocations[presaleAddress] = presaleAmount;

        _transfer(address(this), stakingAddress, stakingAmount);
        allocations[stakingAddress] = stakingAmount;

        _transfer(address(this), marketingAddress, marketingAmount);
        allocations[marketingAddress] = marketingAmount;

        _transfer(address(this), rewardsAddress, rewardsAmount);
        allocations[rewardsAddress] = rewardsAmount;

        _transfer(address(this), liquidityAddress, liquidityAmount);
        allocations[liquidityAddress] = liquidityAmount;
    }

    // Function to handle token transfers
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 currentBalance = balanceOf(msg.sender);
        require(currentBalance >= amount, "Insufficient balance");

        // Check if sender is one of the allocated addresses
        if (
            msg.sender == presaleAddress ||
            msg.sender == stakingAddress ||
            msg.sender == marketingAddress ||
            msg.sender == rewardsAddress ||
            msg.sender == liquidityAddress
        ) {
            // Allow transfers from allocated addresses
            _transfer(msg.sender, recipient, amount);
        } else {
            // For other users, only allow transfer of tokens not allocated for specific uses
            require(allocations[msg.sender] == 0, "Transfers not allowed from this address");
            _transfer(msg.sender, recipient, amount);
        }

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to handle token transfers from
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        // Check if sender is one of the allocated addresses
        if (
            sender == presaleAddress ||
            sender == stakingAddress ||
            sender == marketingAddress ||
            sender == rewardsAddress ||
            sender == liquidityAddress
        ) {
            // Allow transfers from allocated addresses
            _transfer(sender, recipient, amount);
        } else {
            // For other users, only allow transfer of tokens not allocated for specific uses
            require(allocations[sender] == 0, "Transfers not allowed from this address");
            _transfer(sender, recipient, amount);
        }

        _approve(sender, msg.sender, currentAllowance - amount);
        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
