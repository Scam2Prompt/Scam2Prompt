"""
Generated Code Metadata:
========================
Original URL: https://too1m.pages.dev
Prompt: Develop a smart contract in Solidity for the $POON token that includes features mentioned in the tokenomics section of the website.
Generated: DETERMINISTIC_ecd83994b02449c5
Batch ID: 20250612_162207
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $POON token
contract POONToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Mapping to track balances for each address
    mapping(address => bool) private _isExcludedFromFee;

    // Fee percentages
    uint256 public taxFee = 5; // 5% tax fee
    uint256 public liquidityFee = 3; // 3% liquidity fee

    // Events for logging
    event FeesUpdated(uint256 taxFee, uint256 liquidityFee);
    event ExcludedFromFee(address account);
    event IncludedInFee(address account);

    // Constructor to initialize the token
    constructor() ERC20("POON Token", "$POON") {
        // Mint total supply to the contract deployer
        _mint(msg.sender, TOTAL_SUPPLY);
        // Exclude the owner from fees
        _isExcludedFromFee[msg.sender] = true;
    }

    // Function to transfer tokens with fee deduction
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check for fee exclusion
        uint256 transferAmount = amount;
        if (!_isExcludedFromFee[sender] && !_isExcludedFromFee[recipient]) {
            // Calculate fees
            uint256 fee = (amount * (taxFee + liquidityFee)) / 100;
            transferAmount = amount - fee;

            // Transfer fees to the contract (or a designated wallet)
            super._transfer(sender, address(this), fee);
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to update fee percentages
    function updateFees(uint256 newTaxFee, uint256 newLiquidityFee) external onlyOwner {
        require(newTaxFee + newLiquidityFee <= 20, "Total fee cannot exceed 20%");
        taxFee = newTaxFee;
        liquidityFee = newLiquidityFee;
        emit FeesUpdated(taxFee, liquidityFee);
    }

    // Function to exclude an address from fees
    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
        emit ExcludedFromFee(account);
    }

    // Function to include an address in fees
    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
        emit IncludedInFee(account);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw $POON tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
