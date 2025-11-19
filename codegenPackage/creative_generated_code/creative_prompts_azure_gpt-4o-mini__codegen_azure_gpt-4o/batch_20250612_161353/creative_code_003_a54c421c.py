"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beckeerererer.pages.dev
Prompt: Provide an example of how to implement a presale mechanism for a cryptocurrency token with a cap, similar to the BCKR presale model.
Generated: DETERMINISTIC_a54c421c6154773f
Batch ID: 20250612_161353
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

/**
 * @title TokenPresale
 * @dev Implements a capped presale mechanism for a cryptocurrency token.
 */
contract TokenPresale {
    // State variables
    address public owner;                  // Owner of the contract
    uint256 public constant CAP = 100 ether; // Max amount of ETH that can be raised
    uint256 public totalRaised;            // Total amount of ETH raised
    uint256 public presalePrice;           // Price of token per ETH during presale
    mapping(address => uint256) public contributions; // Tracks individual contributions
    
    IERC20 public token; // ERC-20 Token being sold

    bool public presaleActive; // Flag to check if presale is ongoing

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStarted();
    event PresaleEnded();

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor
    constructor(address _tokenAddress, uint256 _presalePrice) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presalePrice > 0, "Presale price must be greater than 0");

        owner = msg.sender;
        token = IERC20(_tokenAddress);
        presalePrice = _presalePrice;
    }

    /**
     * @dev Start the presale. Can only be called by the owner.
     */
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale already active");
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev End the presale. Can only be called by the owner.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale not active");
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Allows users to buy tokens during the presale.
     */
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send ETH to buy tokens");
        require(totalRaised + msg.value <= CAP, "Purchase exceeds cap");

        uint256 tokenAmount = msg.value * presalePrice; // Calculate token amount
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

        // Update state
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Transfer tokens to buyer
        token.transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Withdraw raised ETH. Can only be called by the owner.
     */
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Withdraw remaining unsold tokens after presale ends. Can only be called by the owner.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale still active");
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No unsold tokens to withdraw");

        token.transfer(owner, remainingTokens);
    }
}

// Minimal ERC-20 interface for token interaction
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
