"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the $DOG token presale described on the webpage, including features like a presale cap and ETH-based token allocation.
Generated: DETERMINISTIC_207152e8f4efe157
Batch ID: 20250612_153420
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
 * @dev A smart contract for a token presale with an ETH-based token allocation and a presale cap.
 */
contract TokenPresale {
    // Public variables
    address public owner; // Address of contract owner
    uint256 public totalRaised; // Total amount of ETH raised during the presale
    uint256 public presaleCap; // Maximum amount of ETH allowed for the presale
    uint256 public tokenRate; // Number of tokens per 1 ETH
    bool public presaleActive; // Flag indicating if presale is ongoing

    // Token-related
    IERC20 public token; // ERC20 token contract

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 ethValue);
    event PresaleStarted();
    event PresaleEnded();
    event TokensWithdrawn(address indexed beneficiary, uint256 amount);

    // Constructor
    constructor(
        address _tokenAddress,
        uint256 _tokenRate,
        uint256 _presaleCap
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_tokenRate > 0, "Token rate must be greater than zero");
        require(_presaleCap > 0, "Presale cap must be greater than zero");

        owner = msg.sender;
        token = IERC20(_tokenAddress);
        tokenRate = _tokenRate;
        presaleCap = _presaleCap;
        presaleActive = false; // Presale starts as inactive
    }

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Modifier to check if presale is inactive
    modifier isPresaleInactive() {
        require(!presaleActive, "Presale is already active");
        _;
    }

    // Function to start the presale
    function startPresale() external onlyOwner isPresaleInactive {
        presaleActive = true;
        emit PresaleStarted();
    }

    // Function to end the presale
    function endPresale() external onlyOwner isPresaleActive {
        presaleActive = false;
        emit PresaleEnded();
    }

    // Function to purchase tokens during the presale
    function purchaseTokens() external payable isPresaleActive {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised + msg.value <= presaleCap, "Presale cap exceeded");

        // Calculate token amount to be allocated
        uint256 tokenAmount = msg.value * tokenRate;

        // Update presale state
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    // Function for owner to withdraw raised ETH
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    // Fallback function to reject accidental ETH transfers
    receive() external payable {
        revert("Use purchaseTokens to buy tokens");
    }

    // Function to recover any leftover tokens (if presale ends without full allocation)
    function recoverTokens() external onlyOwner {
        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance > 0, "No tokens to recover");

        require(token.transfer(owner, tokenBalance), "Token recovery failed");
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
