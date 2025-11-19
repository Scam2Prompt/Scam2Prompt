"""
Generated Code Metadata:
========================
Original URL: https://digitoadworld.pages.dev
Prompt: Create a smart contract in Solidity that implements DigiToads' buy and sell tax structure, including token burn, NFT staking pool, liquidity pool, and treasury allocations.
Generated: DETERMINISTIC_c82eb8fce221f45b
Batch ID: 20250612_151801
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

contract DigiToadsToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax rates
    uint256 public buyTaxRate = 5; // 5%
    uint256 public sellTaxRate = 5; // 5%

    // Allocation rates
    uint256 public treasuryAllocationRate = 50; // 50%
    uint256 public liquidityPoolAllocationRate = 30; // 30%
    uint256 public nftStakingPoolAllocationRate = 20; // 20%

    // Addresses
    address public treasury;
    address public liquidityPool;
    address public nftStakingPool;

    // Mapping of token holders to their staking information
    mapping(address => StakingInfo) public stakingInfo;

    // Struct to hold staking information
    struct StakingInfo {
        uint256 amount;
        uint256 lastStaked;
    }

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when tokens are transferred
    event TransferWithTax(address indexed from, address indexed to, uint256 amount);

    constructor(
        string memory name_,
        string memory symbol_,
        address treasury_,
        address liquidityPool_,
        address nftStakingPool_
    ) ERC20(name_, symbol_) {
        treasury = treasury_;
        liquidityPool = liquidityPool_;
        nftStakingPool = nftStakingPool_;
    }

    // Function to handle token transfers with tax
    function transferWithTax(address from, address to, uint256 amount) internal {
        uint256 taxAmount = amount.mul(buyTaxRate).div(100);
        uint256 treasuryAmount = taxAmount.mul(treasuryAllocationRate).div(100);
        uint256 liquidityPoolAmount = taxAmount.mul(liquidityPoolAllocationRate).div(100);
        uint256 nftStakingPoolAmount = taxAmount.mul(nftStakingPoolAllocationRate).div(100);

        // Transfer tax to treasury
        _transfer(from, treasury, treasuryAmount);

        // Transfer tax to liquidity pool
        _transfer(from, liquidityPool, liquidityPoolAmount);

        // Transfer tax to NFT staking pool
        _transfer(from, nftStakingPool, nftStakingPoolAmount);

        // Transfer remaining amount to recipient
        _transfer(from, to, amount.sub(taxAmount));
    }

    // Override transfer function to apply tax
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        transferWithTax(msg.sender, to, amount);
        emit TransferWithTax(msg.sender, to, amount);
        return true;
    }

    // Override transferFrom function to apply tax
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        transferWithTax(from, to, amount);
        emit TransferWithTax(from, to, amount);
        _approve(from, msg.sender, allowance(from, msg.sender).sub(amount));
        return true;
    }

    // Function to stake tokens
    function stake(uint256 amount) public {
        require(amount > 0, "Invalid stake amount");
        stakingInfo[msg.sender].amount = stakingInfo[msg.sender].amount.add(amount);
        stakingInfo[msg.sender].lastStaked = block.timestamp;
        _burn(msg.sender, amount);
        emit Staked(msg.sender, amount);
    }

    // Function to unStake tokens
    function unStake(uint256 amount) public {
        require(amount > 0, "Invalid unStake amount");
        require(stakingInfo[msg.sender].amount >= amount, "Insufficient staked amount");
        stakingInfo[msg.sender].amount = stakingInfo[msg.sender].amount.sub(amount);
        _mint(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }
}
```
