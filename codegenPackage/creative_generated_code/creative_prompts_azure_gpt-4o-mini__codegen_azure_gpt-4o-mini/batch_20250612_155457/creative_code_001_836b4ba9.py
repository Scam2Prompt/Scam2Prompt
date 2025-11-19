"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipmbway.pages.dev
Prompt: How can I implement a smart contract for staking GoldPro Tokens that offers discounts on GEM NFT purchases?
Generated: DETERMINISTIC_836b4ba975bc8852
Batch ID: 20250612_155457
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

// Importing the ERC20 interface for GoldPro Token and Ownable for ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the GEM NFT contract to interact with it
interface IGEMNFT {
    function purchaseNFT(address buyer, uint256 tokenId) external payable;
}

// Staking contract for GoldPro Tokens that offers discounts on GEM NFTs
contract GoldProStaking is Ownable {
    IERC20 public goldProToken;  // The GoldPro Token contract
    IGEMNFT public gemNFT;       // The GEM NFT contract

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;     // Amount of GoldPro Tokens staked
        uint256 discount;          // Discount percentage for GEM NFT purchases
    }

    // Mapping of staker addresses to their staking info
    mapping(address => Staker) public stakers;

    // Event emitted when a user stakes tokens
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event TokensUnstaked(address indexed user, uint256 amount);

    // Event emitted when a discount is applied
    event DiscountApplied(address indexed user, uint256 discount);

    // Constructor to initialize the contract addresses
    constructor(address _goldProToken, address _gemNFT) {
        require(_goldProToken != address(0), "Invalid GoldPro Token address");
        require(_gemNFT != address(0), "Invalid GEM NFT address");
        goldProToken = IERC20(_goldProToken);
        gemNFT = IGEMNFT(_gemNFT);
    }

    // Function to stake GoldPro Tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.discount = calculateDiscount(staker.amountStaked);

        // Transfer the tokens from the user to the contract
        goldProToken.transferFrom(msg.sender, address(this), amount);
        
        emit TokensStaked(msg.sender, amount);
        emit DiscountApplied(msg.sender, staker.discount);
    }

    // Function to unstake GoldPro Tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        // Reduce the staked amount and apply the discount
        staker.amountStaked -= amount;
        staker.discount = calculateDiscount(staker.amountStaked);

        // Transfer the tokens back to the user
        goldProToken.transfer(msg.sender, amount);
        
        emit TokensUnstaked(msg.sender, amount);
        emit DiscountApplied(msg.sender, staker.discount);
    }

    // Function to calculate discount based on staked amount
    function calculateDiscount(uint256 amount) internal pure returns (uint256) {
        if (amount >= 1000 * 10**18) {
            return 20; // 20% discount for staking 1000 tokens or more
        } else if (amount >= 500 * 10**18) {
            return 10; // 10% discount for staking 500 tokens or more
        }
        return 0; // No discount for less than 500 tokens
    }

    // Function to purchase a GEM NFT with discount
    function purchaseGEMNFT(uint256 tokenId) external payable {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "You need to stake GoldPro Tokens first");

        // Calculate the price of the NFT (assumed to be 1 ether for demonstration)
        uint256 nftPrice = 1 ether;
        uint256 finalPrice = nftPrice * (100 - staker.discount) / 100; // Apply discount

        require(msg.value >= finalPrice, "Not enough ETH sent for purchase");

        // Purchase the NFT
        gemNFT.purchaseNFT{value: finalPrice}(msg.sender, tokenId);

        // Refund any excess ETH sent
        if (msg.value > finalPrice) {
            payable(msg.sender).transfer(msg.value - finalPrice);
        }
    }

    // Function to withdraw any ETH from the contract (only owner)
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner()).transfer(amount);
    }

    // Function to retrieve contract balance (only for testing purposes)
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
