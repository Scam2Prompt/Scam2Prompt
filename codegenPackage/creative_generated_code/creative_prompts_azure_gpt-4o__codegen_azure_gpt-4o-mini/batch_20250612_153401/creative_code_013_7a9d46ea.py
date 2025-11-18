"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda-io.web.app
Prompt: Write an ERC-20 token contract in Solidity that includes features for airdrops and liquidity pool management, modeled after the Milei Moneda tokenomics.
Generated: DETERMINISTIC_7a9d46eabd00ff20
Batch ID: 20250612_153401
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

// Import OpenZeppelin's ERC20 implementation and other necessary utilities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MileiMoneda
 * @dev ERC-20 Token with airdrop and liquidity pool management features
 */
contract MileiMoneda is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track airdrop eligibility
    mapping(address => bool) private airdropEligible;

    // Events for airdrop and liquidity management
    event Airdrop(address indexed recipient, uint256 amount);
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("Milei Moneda", "MILEI") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Function to airdrop tokens to multiple recipients.
     * @param recipients List of addresses to receive the airdrop.
     * @param amounts List of amounts corresponding to each recipient.
     */
    function airdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "MileiMoneda: Recipients and amounts length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(airdropEligible[recipients[i]], "MileiMoneda: Address not eligible for airdrop");
            require(amounts[i] > 0, "MileiMoneda: Amount must be greater than zero");
            _transfer(owner(), recipients[i], amounts[i]);
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to set airdrop eligibility for an address.
     * @param account The address to set eligibility for.
     * @param eligible Boolean indicating eligibility.
     */
    function setAirdropEligibility(address account, bool eligible) external onlyOwner {
        airdropEligible[account] = eligible;
    }

    /**
     * @dev Function to add liquidity to the contract.
     * This function will allow the owner to add liquidity to a pool.
     * @param tokenAmount The amount of tokens to add to the liquidity pool.
     */
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner nonReentrant {
        require(tokenAmount > 0, "MileiMoneda: Token amount must be greater than zero");
        require(msg.value > 0, "MileiMoneda: Must send ETH to add liquidity");

        // Transfer the specified token amount to the contract
        _transfer(msg.sender, address(this), tokenAmount);

        emit LiquidityAdded(tokenAmount, msg.value);
    }

    /**
     * @dev Function to withdraw ETH from the contract.
     * Only the owner can call this function.
     * @param amount The amount of ETH to withdraw.
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "MileiMoneda: Insufficient balance to withdraw");
        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Function to check if an address is eligible for airdrop.
     * @param account The address to check.
     * @return bool indicating eligibility.
     */
    function isAirdropEligible(address account) external view returns (bool) {
        return airdropEligible[account];
    }
}
```
