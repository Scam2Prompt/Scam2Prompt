"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-cs6.pages.dev
Prompt: Write a Solidity smart contract that interacts with Seedify's INO launchpad to allow users to purchase NFTs using $SFUND tokens.
Generated: DETERMINISTIC_8fcc843bf70b0f0e
Batch ID: 20250612_152000
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

// Importing the IERC20 interface to interact with the $SFUND token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Seedify INO Launchpad
interface IINO {
    function buyNFT(uint256 tokenId, uint256 amount) external;
}

contract NFTPurchaser {
    // Address of the $SFUND token contract
    address public sfundTokenAddress;
    // Address of the Seedify INO contract
    address public inoContractAddress;

    // Event emitted when an NFT purchase is successful
    event NFTPurchased(address indexed buyer, uint256 tokenId, uint256 amount);

    // Constructor to set the token and INO contract addresses
    constructor(address _sfundTokenAddress, address _inoContractAddress) {
        require(_sfundTokenAddress != address(0), "Invalid SFUND token address");
        require(_inoContractAddress != address(0), "Invalid INO contract address");

        sfundTokenAddress = _sfundTokenAddress;
        inoContractAddress = _inoContractAddress;
    }

    // Function to purchase an NFT using $SFUND tokens
    function purchaseNFT(uint256 tokenId, uint256 amount) external {
        // Validate the purchase amount
        require(amount > 0, "Amount must be greater than 0");

        // Get the SFUND token contract
        IERC20 sfundToken = IERC20(sfundTokenAddress);
        
        // Calculate the total cost in SFUND tokens
        uint256 totalCost = calculateNFTPrice(tokenId) * amount;

        // Ensure the buyer has sufficient SFUND tokens
        require(sfundToken.balanceOf(msg.sender) >= totalCost, "Insufficient SFUND balance");

        // Transfer the SFUND tokens from the buyer to this contract
        require(sfundToken.transferFrom(msg.sender, address(this), totalCost), "SFUND token transfer failed");

        // Interact with the INO contract to purchase the NFT
        IINO(inoContractAddress).buyNFT(tokenId, amount);

        // Emit an event for the successful purchase
        emit NFTPurchased(msg.sender, tokenId, amount);
    }

    // Function to calculate the price of an NFT based on its token ID
    // This function can be modified to implement custom pricing logic
    function calculateNFTPrice(uint256 tokenId) internal view returns (uint256) {
        // Placeholder: Replace with actual price logic
        // For example, return a fixed price for all NFTs
        return 100 * 10 ** 18; // Example: 100 SFUND tokens
    }

    // Function to withdraw the collected SFUND tokens to a specified address
    function withdraw() external {
        uint256 balance = IERC20(sfundTokenAddress).balanceOf(address(this));
        require(balance > 0, "No SFUND tokens to withdraw");

        // Transfer the collected SFUND tokens to the owner's address
        require(IERC20(sfundTokenAddress).transfer(msg.sender, balance), "Withdrawal failed");
    }
}
```
