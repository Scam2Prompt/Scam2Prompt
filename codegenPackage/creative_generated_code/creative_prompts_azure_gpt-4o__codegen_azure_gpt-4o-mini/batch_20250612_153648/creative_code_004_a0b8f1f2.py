"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instantswap.vercel.app
Prompt: Develop a smart contract that integrates SushiSwap's Shoyu NFT payments system to allow users to purchase NFTs using Ethereum.
Generated: DETERMINISTIC_a0b8f1f250f0f929
Batch ID: 20250612_153648
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for SushiSwap's Shoyu NFT marketplace
interface ISushiSwapShoyu {
    function purchaseNFT(uint256 tokenId, address buyer) external payable;
}

// NFT Purchase Smart Contract
contract NFTPurchase is Ownable {
    ISushiSwapShoyu public shoyuContract; // Instance of the SushiSwap Shoyu contract
    IERC20 public paymentToken; // ERC20 token contract for payments

    // Event emitted when an NFT is purchased
    event NFTPurchased(address indexed buyer, uint256 indexed tokenId, uint256 amountPaid);

    // Constructor to set the Shoyu contract and payment token
    constructor(address _shoyuContract, address _paymentToken) {
        require(_shoyuContract != address(0), "Invalid Shoyu contract address.");
        require(_paymentToken != address(0), "Invalid payment token address.");
        
        shoyuContract = ISushiSwapShoyu(_shoyuContract);
        paymentToken = IERC20(_paymentToken);
    }

    // Purchase NFT function
    function purchaseNFT(uint256 tokenId, uint256 amount) external {
        // Validate amount
        require(amount > 0, "Amount must be greater than 0.");

        // Transfer payment from buyer to this contract
        require(paymentToken.transferFrom(msg.sender, address(this), amount), "Payment transfer failed.");

        // Transfer the NFT to the buyer
        try shoyuContract.purchaseNFT(tokenId, msg.sender) {
            // Emit NFT purchase event
            emit NFTPurchased(msg.sender, tokenId, amount);
        } catch {
            revert("NFT purchase failed.");
        }
    }

    // Withdraw function for the owner to collect ERC20 funds
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0.");
        require(paymentToken.balanceOf(address(this)) >= amount, "Insufficient balance.");

        // Transfer specified amount to the owner
        paymentToken.transfer(msg.sender, amount);
    }

    // Function to update the Shoyu contract address (onlyOwner)
    function updateShoyuContract(address _newShoyuContract) external onlyOwner {
        require(_newShoyuContract != address(0), "Invalid Shoyu contract address.");
        shoyuContract = ISushiSwapShoyu(_newShoyuContract);
    }

    // Function to update the payment token address (onlyOwner)
    function updatePaymentToken(address _newPaymentToken) external onlyOwner {
        require(_newPaymentToken != address(0), "Invalid payment token address.");
        paymentToken = IERC20(_newPaymentToken);
    }
}
```
