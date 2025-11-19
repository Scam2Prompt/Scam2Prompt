"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Provide code to implement tokenomics for $PEPU, including allocations for liquidity, project finance, presale, staking, and marketing as outlined in the Pepe Unchained tokenomics section.
Generated: DETERMINISTIC_4bb83904dce3ee40
Batch ID: 20250612_151459
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PepeUnchainedToken
 * @dev Implementation of the Pepe Unchained Token ($PEPU) with tokenomics allocations.
 */
contract PepeUnchainedToken is ERC20, Ownable {
    // Tokenomics allocations in percentage
    uint256 public constant LIQUIDITY_ALLOCATION = 20; // 20% for liquidity
    uint256 public constant PROJECT_FINANCE_ALLOCATION = 30; // 30% for project finance
    uint256 public constant PRESALE_ALLOCATION = 25; // 25% for presale
    uint256 public constant STAKING_ALLOCATION = 15; // 15% for staking
    uint256 public constant MARKETING_ALLOCATION = 10; // 10% for marketing

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Addresses for different allocations
    address public liquidityWallet;
    address public projectFinanceWallet;
    address public presaleWallet;
    address public stakingWallet;
    address public marketingWallet;

    /**
     * @dev Constructor that initializes the token and allocates the tokens according to the tokenomics.
     * @param _liquidityWallet Address for liquidity allocation
     * @param _projectFinanceWallet Address for project finance allocation
     * @param _presaleWallet Address for presale allocation
     * @param _stakingWallet Address for staking allocation
     * @param _marketingWallet Address for marketing allocation
     */
    constructor(
        address _liquidityWallet,
        address _projectFinanceWallet,
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet
    ) ERC20("Pepe Unchained", "$PEPU") {
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");
        require(_projectFinanceWallet != address(0), "Invalid project finance wallet address");
        require(_presaleWallet != address(0), "Invalid presale wallet address");
        require(_stakingWallet != address(0), "Invalid staking wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");

        liquidityWallet = _liquidityWallet;
        projectFinanceWallet = _projectFinanceWallet;
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;

        // Allocate tokens according to the defined percentages
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100);
        _mint(projectFinanceWallet, (TOTAL_SUPPLY * PROJECT_FINANCE_ALLOCATION) / 100);
        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100);
        _mint(stakingWallet, (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
    }

    /**
     * @dev Function to transfer tokens. Overrides the default transfer function to include additional checks if needed.
     * @param recipient The address to receive the tokens
     * @param amount The amount of tokens to transfer
     * @return success A boolean indicating the success of the transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another. Overrides the default transferFrom function.
     * @param sender The address to send tokens from
     * @param recipient The address to receive tokens
     * @param amount The amount of tokens to transfer
     * @return success A boolean indicating the success of the transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
