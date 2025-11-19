"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-babyslerf.pages.dev
Prompt: Develop a Solidity contract that mimics the Baby Slerf token distribution model, ensuring it includes features for presale, liquidity, and airdrop allocations.
Generated: DETERMINISTIC_a5c0482db60d29ff
Batch ID: 20250612_162050
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

/**
 * @title BabySlerfToken
 * @dev A Solidity contract for a token distribution model with presale, liquidity, and airdrop allocations.
 */
contract BabySlerfToken {
    // Token details
    string public constant name = "Baby Slerf Token";
    string public constant symbol = "BSLERF";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Allocation percentages (must sum to 100%)
    uint256 public constant PRESALE_PERCENT = 40; // 40%
    uint256 public constant LIQUIDITY_PERCENT = 40; // 40%
    uint256 public constant AIRDROP_PERCENT = 20; // 20%

    // Token balances
    mapping(address => uint256) public balanceOf;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event PresaleAllocated(address indexed beneficiary, uint256 amount);
    event LiquidityAllocated(address indexed beneficiary, uint256 amount);
    event AirdropAllocated(address indexed beneficiary, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the total supply and the initial owner.
     * @param _totalSupply The total supply of tokens.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");

        totalSupply = _totalSupply;
        owner = msg.sender;

        // All tokens start in the owner's balance
        balanceOf[owner] = _totalSupply;
    }

    /**
     * @dev Allocate tokens for presale.
     * @param presaleBeneficiary Address of the presale beneficiary.
     */
    function allocatePresale(address presaleBeneficiary) external onlyOwner {
        require(presaleBeneficiary != address(0), "Invalid beneficiary address");

        uint256 presaleAmount = (totalSupply * PRESALE_PERCENT) / 100;

        // Ensure sufficient balance in the owner's account
        require(balanceOf[owner] >= presaleAmount, "Insufficient balance for presale allocation");

        // Transfer tokens
        balanceOf[owner] -= presaleAmount;
        balanceOf[presaleBeneficiary] += presaleAmount;

        emit PresaleAllocated(presaleBeneficiary, presaleAmount);
        emit Transfer(owner, presaleBeneficiary, presaleAmount);
    }

    /**
     * @dev Allocate tokens for liquidity.
     * @param liquidityBeneficiary Address of the liquidity beneficiary.
     */
    function allocateLiquidity(address liquidityBeneficiary) external onlyOwner {
        require(liquidityBeneficiary != address(0), "Invalid beneficiary address");

        uint256 liquidityAmount = (totalSupply * LIQUIDITY_PERCENT) / 100;

        // Ensure sufficient balance in the owner's account
        require(balanceOf[owner] >= liquidityAmount, "Insufficient balance for liquidity allocation");

        // Transfer tokens
        balanceOf[owner] -= liquidityAmount;
        balanceOf[liquidityBeneficiary] += liquidityAmount;

        emit LiquidityAllocated(liquidityBeneficiary, liquidityAmount);
        emit Transfer(owner, liquidityBeneficiary, liquidityAmount);
    }

    /**
     * @dev Allocate tokens for airdrop.
     * @param airdropBeneficiary Address of the airdrop beneficiary.
     */
    function allocateAirdrop(address airdropBeneficiary) external onlyOwner {
        require(airdropBeneficiary != address(0), "Invalid beneficiary address");

        uint256 airdropAmount = (totalSupply * AIRDROP_PERCENT) / 100;

        // Ensure sufficient balance in the owner's account
        require(balanceOf[owner] >= airdropAmount, "Insufficient balance for airdrop allocation");

        // Transfer tokens
        balanceOf[owner] -= airdropAmount;
        balanceOf[airdropBeneficiary] += airdropAmount;

        emit AirdropAllocated(airdropBeneficiary, airdropAmount);
        emit Transfer(owner, airdropBeneficiary, airdropAmount);
    }
}
```
