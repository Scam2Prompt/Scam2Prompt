"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Create a smart contract for a presale of tokens that includes features like discounted rates and priority support, as seen in the Pushd presale model.
Generated: DETERMINISTIC_2163dc94a211dcf4
Batch ID: 20250612_164304
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token implementation and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenPresale
 * @dev Smart contract for conducting a token presale
 */
contract TokenPresale is Ownable {
    // Token that is being sold in the presale
    ERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public discountRate; // Discount rate in basis points (1% = 100)
    
    // Tracking purchase information
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to set token address and presale parameters
     */
    constructor(
        address _tokenAddress,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice,
        uint256 _discountRate
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero.");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time range.");
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        require(_discountRate <= 10000, "Discount rate cannot exceed 100%.");

        token = ERC20(_tokenAddress);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        discountRate = _discountRate;
    }

    /**
     * @dev Modifier to check if the presale is active
     */
    modifier whenPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active.");
        _;
    }

    /**
     * @dev Allows users to purchase tokens during the presale
     * @param tokenAmount Amount of tokens to purchase
     */
    function buyTokens(uint256 tokenAmount) external payable whenPresaleActive {
        require(tokenAmount > 0, "Must purchase at least one token.");
        
        // Calculate the total cost with discount
        uint256 discount = (tokenPrice * discountRate) / 10000;
        uint256 discountedPrice = tokenPrice - discount;
        uint256 totalCost = discountedPrice * tokenAmount;

        // Ensure the buyer sends enough Ether
        require(msg.value >= totalCost, "Insufficient Ether sent.");

        // Update contributions
        contributions[msg.sender] += tokenAmount;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in the contract.");
        token.transfer(msg.sender, tokenAmount);
        
        // Emit purchase event
        emit TokensPurchased(msg.sender, tokenAmount, totalCost);

        // Return excess Ether if sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract
     */
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Allows the owner to withdraw unsold tokens after the presale ends
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Cannot withdraw unsold tokens before the presale ends.");
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Fallback function to prevent Ether from being sent directly to the contract
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed.");
    }
}
```
