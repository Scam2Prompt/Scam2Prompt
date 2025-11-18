"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepelive.com
Prompt: Write a Solidity smart contract to facilitate the purchase of WEPE tokens during the presale, including a function to enforce floor pricing.
Generated: DETERMINISTIC_1187cc1e5050dd8f
Batch ID: 20250612_153812
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

// Import OpenZeppelin's SafeERC20 library for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

// The PresaleContract facilitates the purchase of WEPE tokens
contract PresaleContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Define state variables
    IERC20 public wepeToken; // The WEPE token contract
    uint256 public floorPrice; // The minimum price per token in wei
    uint256 public totalTokensSold; // Total tokens sold during presale
    uint256 public presaleEndTime; // The end time for the presale

    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Constructor to initialize the contract
    constructor(
        IERC20 _wepeToken,
        uint256 _floorPrice,
        uint256 _presaleDuration
    ) {
        wepeToken = _wepeToken;
        floorPrice = _floorPrice;
        presaleEndTime = block.timestamp + _presaleDuration; // Set presale end time
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended.");
        _;
    }

    // Function to purchase WEPE tokens
    function purchaseTokens(uint256 tokenAmount) external payable isPresaleActive nonReentrant {
        // Calculate total cost
        uint256 cost = tokenAmount * floorPrice;
        
        // Check if the sender has sent enough Ether
        require(msg.value >= cost, "Insufficient Ether sent.");

        // Update total tokens sold
        totalTokensSold += tokenAmount;

        // Transfer WEPE tokens to the buyer
        wepeToken.safeTransfer(msg.sender, tokenAmount);

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, tokenAmount, cost);
    }

    // Function to withdraw collected Ether by the owner
    function withdrawFunds() external onlyOwner {
        // Transfer the balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set a new floor price by the owner
    function setFloorPrice(uint256 newFloorPrice) external onlyOwner {
        require(newFloorPrice > 0, "Floor price must be greater than zero.");
        floorPrice = newFloorPrice;
    }

    // Function to check remaining time for presale
    function remainingTime() external view returns (uint256) {
        if (block.timestamp >= presaleEndTime) {
            return 0;
        }
        return presaleEndTime - block.timestamp;
    }
}
```
