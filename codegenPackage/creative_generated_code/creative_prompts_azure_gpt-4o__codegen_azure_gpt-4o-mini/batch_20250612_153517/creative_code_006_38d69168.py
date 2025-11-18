"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-staking-indol.vercel.app
Prompt: Design a smart contract that enforces the 100% liquidity pool deposit mechanism for funds raised through Lifinity Flares NFT sales.
Generated: DETERMINISTIC_38d69168db48087c
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LifinityFlaresNFT
 * @dev This contract is responsible for managing Lifinity Flares NFT sales
 * and ensuring that 100% of the funds raised are deposited into a liquidity pool.
 */
contract LifinityFlaresNFT is Ownable {
    // ERC721 interface for Lifinity Flares NFTs
    IERC721 public flaresNFT;
    
    // ERC20 token used for payments
    IERC20 public paymentToken;

    // Liquidity pool address
    address public liquidityPool;

    // Event emitted when a sale occurs
    event Sale(address indexed buyer, uint256 indexed tokenId, uint256 amount);

    /**
     * @dev Constructor to set the initial contract state.
     * @param _flaresNFT Address of the Lifinity Flares NFT contract.
     * @param _paymentToken Address of the ERC20 token contract used for payments.
     * @param _liquidityPool Address of the liquidity pool where funds will be deposited.
     */
    constructor(IERC721 _flaresNFT, IERC20 _paymentToken, address _liquidityPool) {
        flaresNFT = _flaresNFT;
        paymentToken = _paymentToken;
        liquidityPool = _liquidityPool;
    }

    /**
     * @dev Allows users to purchase an NFT by depositing funds.
     * @param tokenId The ID of the NFT being purchased.
     * @param amount The amount of payment being made.
     */
    function purchaseNFT(uint256 tokenId, uint256 amount) external {
        // Ensure the NFT exists
        require(flaresNFT.ownerOf(tokenId) == address(this), "NFT not available for sale");

        // Transfer payment to this contract
        require(paymentToken.transferFrom(msg.sender, address(this), amount), "Payment transfer failed");

        // Deposit 100% of the funds to the liquidity pool
        require(paymentToken.transfer(liquidityPool, amount), "Liquidity pool deposit failed");

        // Transfer the NFT to the buyer
        flaresNFT.transferFrom(address(this), msg.sender, tokenId);

        // Emit the sale event
        emit Sale(msg.sender, tokenId, amount);
    }

    /**
     * @dev Allows the contract owner to withdraw any tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = paymentToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient balance to withdraw");

        // Transfer tokens to owner
        require(paymentToken.transfer(msg.sender, amount), "Token withdrawal failed");
    }
}
```
