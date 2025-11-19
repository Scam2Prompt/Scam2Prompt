"""
Generated Code Metadata:
========================
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Generate a smart contract in Solidity that implements tokenomics for $POODL, including allocations for presale (50%), staking (30%), DEX liquidity (10%), and marketing (10%).
Generated: DETERMINISTIC_5b0b19a107782a83
Batch ID: 20250612_153400
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
 * @title PoodlToken
 * @author [Your Name]
 * @notice Tokenomics implementation for $POODL
 */
contract PoodlToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics allocations
    uint256 public constant PRESALE_ALLOCATION = 50;
    uint256 public constant STAKING_ALLOCATION = 30;
    uint256 public constant DEX_LIQUIDITY_ALLOCATION = 10;
    uint256 public constant MARKETING_ALLOCATION = 10;

    // Wallet addresses for allocations
    address public presaleWallet;
    address public stakingWallet;
    address public dexLiquidityWallet;
    address public marketingWallet;

    // Mapping of wallet addresses to their respective allocations
    mapping(address => uint256) public allocations;

    // Event emitted when token is minted
    event TokenMinted(address indexed to, uint256 amount);

    /**
     * @notice Constructor
     * @param _presaleWallet Presale wallet address
     * @param _stakingWallet Staking wallet address
     * @param _dexLiquidityWallet DEX liquidity wallet address
     * @param _marketingWallet Marketing wallet address
     */
    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _dexLiquidityWallet,
        address _marketingWallet
    ) ERC20("PoodlToken", "POODL") {
        require(
            _presaleWallet != address(0) &&
                _stakingWallet != address(0) &&
                _dexLiquidityWallet != address(0) &&
                _marketingWallet != address(0),
            "Invalid wallet address"
        );

        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        dexLiquidityWallet = _dexLiquidityWallet;
        marketingWallet = _marketingWallet;

        // Calculate total supply
        uint256 totalSupply = 100 * 10**18; // 100 million tokens

        // Allocate tokens
        uint256 presaleAmount = totalSupply.mul(PRESALE_ALLOCATION).div(100);
        uint256 stakingAmount = totalSupply.mul(STAKING_ALLOCATION).div(100);
        uint256 dexLiquidityAmount = totalSupply.mul(DEX_LIQUIDITY_ALLOCATION).div(100);
        uint256 marketingAmount = totalSupply.mul(MARKETING_ALLOCATION).div(100);

        // Mint tokens
        _mint(presaleWallet, presaleAmount);
        _mint(stakingWallet, stakingAmount);
        _mint(dexLiquidityWallet, dexLiquidityAmount);
        _mint(marketingWallet, marketingAmount);

        // Store allocations
        allocations[presaleWallet] = presaleAmount;
        allocations[stakingWallet] = stakingAmount;
        allocations[dexLiquidityWallet] = dexLiquidityAmount;
        allocations[marketingWallet] = marketingAmount;

        emit TokenMinted(presaleWallet, presaleAmount);
        emit TokenMinted(stakingWallet, stakingAmount);
        emit TokenMinted(dexLiquidityWallet, dexLiquidityAmount);
        emit TokenMinted(marketingWallet, marketingAmount);
    }

    /**
     * @notice Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        require(amount > 0, "Invalid burn amount");
        require(allocations[msg.sender] >= amount, "Insufficient allocation");

        // Update allocation
        allocations[msg.sender] = allocations[msg.sender].sub(amount);

        // Burn tokens
        _burn(msg.sender, amount);
    }

    /**
     * @notice Transfer tokens
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Invalid transfer amount");
        require(allocations[msg.sender] >= amount, "Insufficient allocation");

        // Update allocation
        allocations[msg.sender] = allocations[msg.sender].sub(amount);

        // Transfer tokens
        _transfer(msg.sender, to, amount);

        return true;
    }
}
```
