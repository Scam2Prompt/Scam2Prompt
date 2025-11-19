"""
Generated Code Metadata:
========================
Original URL: https://procreaition.pages.dev
Prompt: Write a Solidity or Rust program to implement a dual-token model for a blockchain ecosystem, similar to Procreation AI's $PAI and $NEURA token system.
Generated: DETERMINISTIC_020b2ba46484a977
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title DualTokenSystem
 * @dev Implements a dual-token model with PAI (utility token) and NEURA (governance token)
 */
contract DualTokenSystem is Ownable, Pausable {
    // Token contracts
    ERC20 public paiToken;
    ERC20 public neuraToken;

    // Conversion rate from PAI to NEURA (with 18 decimal precision)
    uint256 public conversionRate;
    
    // Minimum and maximum conversion amounts
    uint256 public minConversionAmount;
    uint256 public maxConversionAmount;

    // Address where converted PAI tokens are sent
    address public treasury;

    // Events
    event TokensConverted(address indexed user, uint256 paiAmount, uint256 neuraAmount);
    event ConversionRateUpdated(uint256 newRate);
    event TreasuryUpdated(address newTreasury);
    event LimitsUpdated(uint256 min, uint256 max);

    /**
     * @dev Constructor initializes the token contracts and conversion parameters
     * @param _paiToken Address of the PAI token contract
     * @param _neuraToken Address of the NEURA token contract
     * @param _conversionRate Initial conversion rate (PAI to NEURA)
     * @param _treasury Address where converted PAI tokens are sent
     */
    constructor(
        address _paiToken,
        address _neuraToken,
        uint256 _conversionRate,
        address _treasury
    ) {
        require(_paiToken != address(0), "Invalid PAI token address");
        require(_neuraToken != address(0), "Invalid NEURA token address");
        require(_treasury != address(0), "Invalid treasury address");
        require(_conversionRate > 0, "Conversion rate must be positive");

        paiToken = ERC20(_paiToken);
        neuraToken = ERC20(_neuraToken);
        conversionRate = _conversionRate;
        treasury = _treasury;

        // Default conversion limits
        minConversionAmount = 1 ether; // 1 PAI
        maxConversionAmount = 10000 ether; // 10,000 PAI
    }

    /**
     * @dev Convert PAI tokens to NEURA tokens
     * @param amount Amount of PAI tokens to convert
     */
    function convert(uint256 amount) external whenNotPaused {
        require(amount >= minConversionAmount, "Amount below minimum");
        require(amount <= maxConversionAmount, "Amount exceeds maximum");

        // Calculate NEURA amount
        uint256 neuraAmount = (amount * conversionRate) / 1 ether;

        // Check contract has enough NEURA balance
        require(
            neuraToken.balanceOf(address(this)) >= neuraAmount,
            "Insufficient NEURA balance"
        );

        // Transfer PAI from user to treasury
        require(
            paiToken.transferFrom(msg.sender, treasury, amount),
            "PAI transfer failed"
        );

        // Transfer NEURA to user
        require(
            neuraToken.transfer(msg.sender, neuraAmount),
            "NEURA transfer failed"
        );

        emit TokensConverted(msg.sender, amount, neuraAmount);
    }

    /**
     * @dev Update the conversion rate (owner only)
     * @param newRate New conversion rate
     */
    function setConversionRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Conversion rate must be positive");
        conversionRate = newRate;
        emit ConversionRateUpdated(newRate);
    }

    /**
     * @dev Update the treasury address (owner only)
     * @param newTreasury New treasury address
     */
    function setTreasury(address newTreasury) external onlyOwner {
        require(newTreasury != address(0), "Invalid treasury address");
        treasury = newTreasury;
        emit TreasuryUpdated(newTreasury);
    }

    /**
     * @dev Update conversion limits (owner only)
     * @param min Minimum conversion amount
     * @param max Maximum conversion amount
     */
    function setConversionLimits(uint256 min, uint256 max) external onlyOwner {
        require(min > 0, "Minimum must be positive");
        require(max > min, "Max must be greater than min");
        minConversionAmount = min;
        maxConversionAmount = max;
        emit LimitsUpdated(min, max);
    }

    /**
     * @dev Pause conversions (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause conversions (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Withdraw any ERC20 tokens (owner only)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawERC20(address token, uint256 amount) external onlyOwner {
        require(token != address(paiToken), "Cannot withdraw PAI");
        require(token != address(neuraToken), "Cannot withdraw NEURA");
        require(
            ERC20(token).transfer(msg.sender, amount),
            "Token transfer failed"
        );
    }
}

/**
 * @title PAI Token
 * @dev Utility token contract
 */
contract PAIToken is ERC20, Ownable {
    constructor(uint256 initialSupply) ERC20("Procreation AI", "PAI") {
        _mint(msg.sender, initialSupply);
    }

    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}

/**
 * @title NEURA Token
 * @dev Governance token contract
 */
contract NEURAToken is ERC20, Ownable {
    constructor(uint256 initialSupply) ERC20("Neural Network", "NEURA") {
        _mint(msg.sender, initialSupply);
    }

    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
```
