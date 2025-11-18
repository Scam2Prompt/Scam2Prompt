"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-babywif-io.pages.dev
Prompt: Using Solidity, write a function to distribute Baby WIF ($BIF) tokens to multiple wallets based on the tokenomics percentages (e.g., presale, liquidity, and CEX listing).
Generated: DETERMINISTIC_5bf01d9ffda74db4
Batch ID: 20250612_153517
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

// Importing the OpenZeppelin ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for distributing Baby WIF ($BIF) tokens
contract TokenDistributor is Ownable {
    IERC20 public token;

    // Distribution percentages (scaled by 10000 to avoid floating point issues)
    uint256 public presalePercentage = 3000; // 30%
    uint256 public liquidityPercentage = 5000; // 50%
    uint256 public cexListingPercentage = 2000; // 20%

    // Events
    event TokensDistributed(address indexed wallet, uint256 amount);

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Distributes tokens to multiple wallets based on tokenomics.
     * @param _presaleWallet address of the presale wallet
     * @param _liquidityWallet address of the liquidity wallet
     * @param _cexListingWallet address of the CEX listing wallet
     * @param _totalAmount total amount of tokens to be distributed
     */
    function distributeTokens(
        address _presaleWallet,
        address _liquidityWallet,
        address _cexListingWallet,
        uint256 _totalAmount
    ) external onlyOwner {
        require(_presaleWallet != address(0), "Invalid presale wallet");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet");
        require(_cexListingWallet != address(0), "Invalid CEX wallet");
        require(_totalAmount > 0, "Total amount must be greater than zero");

        // Calculate the distribution amounts
        uint256 presaleAmount = (_totalAmount * presalePercentage) / 10000;
        uint256 liquidityAmount = (_totalAmount * liquidityPercentage) / 10000;
        uint256 cexListingAmount = (_totalAmount * cexListingPercentage) / 10000;

        // Transfer tokens to each wallet
        require(token.balanceOf(address(this)) >= _totalAmount, "Insufficient funds in contract");

        // Perform the transfers
        token.transfer(_presaleWallet, presaleAmount);
        emit TokensDistributed(_presaleWallet, presaleAmount);

        token.transfer(_liquidityWallet, liquidityAmount);
        emit TokensDistributed(_liquidityWallet, liquidityAmount);

        token.transfer(_cexListingWallet, cexListingAmount);
        emit TokensDistributed(_cexListingWallet, cexListingAmount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient funds in contract");

        token.transfer(msg.sender, _amount);
    }
}
```
