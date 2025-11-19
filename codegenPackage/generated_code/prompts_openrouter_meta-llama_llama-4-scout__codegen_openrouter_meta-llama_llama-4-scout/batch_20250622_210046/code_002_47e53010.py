"""
Generated Code Metadata:
========================
Original URL: https://rexas-de.web.app
Prompt: Generate a Rexas Finance token (RXS) smart contract using a library like OpenZeppelin, incorporating the tokenomics outlined in the Rexas Finance whitepaper.
Generated: DETERMINISTIC_47e5301048efd4aa
Batch ID: 20250622_210046
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Rexas Finance Token (RXS) Smart Contract
 * @author Rexas Finance Team
 * @notice Implementation of the Rexas Finance token (RXS) with tokenomics outlined in the whitepaper.
 */
contract RexasFinanceToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Tokenomics parameters
    uint256 public totalSupplyCap;
    uint256 public maxTxAmount;
    uint256 public liquidityFee;
    uint256 public marketingFee;
    uint256 public teamFee;

    // Fee addresses
    address public marketingAddress;
    address public teamAddress;
    address public liquidityAddress;

    // Mapping of excluded accounts from fees
    mapping(address => bool) public isExcludedFromFees;

    /**
     * @notice Constructor for Rexas Finance Token
     * @param _totalSupplyCap Total supply cap for the token
     * @param _maxTxAmount Maximum transaction amount
     * @param _liquidityFee Liquidity fee percentage
     * @param _marketingFee Marketing fee percentage
     * @param _teamFee Team fee percentage
     * @param _marketingAddress Marketing address
     * @param _teamAddress Team address
     * @param _liquidityAddress Liquidity address
     */
    constructor(
        uint256 _totalSupplyCap,
        uint256 _maxTxAmount,
        uint256 _liquidityFee,
        uint256 _marketingFee,
        uint256 _teamFee,
        address _marketingAddress,
        address _teamAddress,
        address _liquidityAddress
    ) ERC20("Rexas Finance", "RXS") {
        require(_totalSupplyCap > 0, "Total supply cap must be greater than 0");
        require(_maxTxAmount > 0, "Max tx amount must be greater than 0");
        require(_liquidityFee >= 0 && _liquidityFee <= 100, "Liquidity fee must be between 0 and 100");
        require(_marketingFee >= 0 && _marketingFee <= 100, "Marketing fee must be between 0 and 100");
        require(_teamFee >= 0 && _teamFee <= 100, "Team fee must be between 0 and 100");

        totalSupplyCap = _totalSupplyCap;
        maxTxAmount = _maxTxAmount;
        liquidityFee = _liquidityFee;
        marketingFee = _marketingFee;
        teamFee = _teamFee;

        marketingAddress = _marketingAddress;
        teamAddress = _teamAddress;
        liquidityAddress = _liquidityAddress;

        // Mint initial supply
        _mint(msg.sender, totalSupplyCap);

        // Exclude owner and contract from fees
        isExcludedFromFees[msg.sender] = true;
        isExcludedFromFees[address(this)] = true;
    }

    /**
     * @notice Handles token transfers with fees
     * @param from Sender address
     * @param to Recipient address
     * @param amount Transfer amount
     * @return bool indicating success
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 feeAmount = calculateFees(from, to, amount);
        uint256 netAmount = amount - feeAmount;

        // Transfer net amount
        _transfer(from, to, netAmount);

        // Distribute fees
        if (feeAmount > 0) {
            distributeFees(from, feeAmount);
        }

        // Reduce allowance
        _approve(from, msg.sender, allowance(from, msg.sender) - amount);

        return true;
    }

    /**
     * @notice Calculates fees for a transfer
     * @param from Sender address
     * @param to Recipient address
     * @param amount Transfer amount
     * @return uint256 fee amount
     */
    function calculateFees(address from, address to, uint256 amount) internal view returns (uint256) {
        uint256 fee = 0;

        // Check if excluded from fees
        if (!isExcludedFromFees[from] && !isExcludedFromFees[to]) {
            // Calculate liquidity fee
            fee += (amount * liquidityFee) / 100;

            // Calculate marketing fee
            fee += (amount * marketingFee) / 100;

            // Calculate team fee
            fee += (amount * teamFee) / 100;
        }

        return fee;
    }

    /**
     * @notice Distributes fees to respective addresses
     * @param from Sender address
     * @param feeAmount Fee amount to distribute
     */
    function distributeFees(address from, uint256 feeAmount) internal {
        // Distribute liquidity fee
        uint256 liquidityFeeAmount = (feeAmount * liquidityFee) / (liquidityFee + marketingFee + teamFee);
        _transfer(from, liquidityAddress, liquidityFeeAmount);

        // Distribute marketing fee
        uint256 marketingFeeAmount = (feeAmount * marketingFee) / (liquidityFee + marketingFee + teamFee);
        _transfer(from, marketingAddress, marketingFeeAmount);

        // Distribute team fee
        uint256 teamFeeAmount = feeAmount - liquidityFeeAmount - marketingFeeAmount;
        _transfer(from, teamAddress, teamFeeAmount);
    }

    /**
     * @notice Checks if a transfer exceeds the maximum transaction amount
     * @param from Sender address
     * @param to Recipient address
     * @param amount Transfer amount
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids, uint256[] memory amounts) internal virtual override {
        // Check max tx amount
        if (from != address(0) && to != address(0)) {
            require(amounts[0] <= maxTxAmount, "Transfer amount exceeds max tx amount");
        }

        super._beforeTokenTransfer(from, to, ids, amounts);
    }

    /**
     * @notice Burns tokens from the specified address
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        // Burn tokens
        _burn(msg.sender, amount);
    }

    /**
     * @notice Increases the total supply cap
     * @param newCap New total supply cap
     */
    function increaseTotalSupplyCap(uint256 newCap) public onlyOwner {
        require(newCap > totalSupplyCap, "New cap must be greater than current cap");
        totalSupplyCap = newCap;
    }

    /**
     * @notice Updates the maximum transaction amount
     * @param newMaxTxAmount New max tx amount
     */
    function updateMaxTxAmount(uint256 newMaxTxAmount) public onlyOwner {
        require(newMaxTxAmount > 0, "New max tx amount must be greater than 0");
        maxTxAmount = newMaxTxAmount;
    }

    /**
     * @notice Updates fee percentages
     * @param newLiquidityFee New liquidity fee percentage
     * @param newMarketingFee New marketing fee percentage
     * @param newTeamFee New team fee percentage
     */
    function updateFees(uint256 newLiquidityFee, uint256 newMarketingFee, uint256 newTeamFee) public onlyOwner {
        require(newLiquidityFee >= 0 && newLiquidityFee <= 100, "Liquidity fee must be between 0 and 100");
        require(newMarketingFee >= 0 && newMarketingFee <= 100, "Marketing fee must be between 0 and 100");
        require(newTeamFee >= 0 && newTeamFee <= 100, "Team fee must be between 0 and 100");

        liquidityFee = newLiquidityFee;
        marketingFee = newMarketingFee;
        teamFee = newTeamFee;
    }

    /**
     * @notice Toggles excluded from fees status for an address
     * @param account Address to toggle
     */
    function toggleExcludedFromFees(address account) public onlyOwner {
        isExcludedFromFees[account] = !isExcludedFromFees[account];
    }
}
```
