"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20presale-claim.pages.dev
Prompt: Write code to implement an ERC-20 token presale mechanism for DOGE20, ensuring buyers can claim their tokens before the Uniswap listing.
Generated: DETERMINISTIC_0a9364863937c27c
Batch ID: 20250612_152235
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

// Importing the interface for ERC20 tokens and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the DOGE20 presale mechanism
contract DOGE20Presale is Ownable {
    // State variables for presale settings
    IERC20 public doge20Token; // The ERC20 token being sold
    uint256 public presalePrice; // Price of each DOGE20 token in wei
    uint256 public presaleCap; // Maximum amount of DOGE20 tokens available for presale
    uint256 public tokensSold; // Amount of tokens sold during the presale
    uint256 public presaleStartTime; // Start time of the presale
    uint256 public presaleEndTime; // End time of the presale

    // Mapping to track the amount of tokens bought by each address
    mapping(address => uint256) public tokensBought;

    // Events for logging presale activity
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleFinalized();

    // Constructor to initialize the presale contract
    constructor(
        address _doge20Token,
        uint256 _presalePrice,
        uint256 _presaleCap,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime
    ) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_presalePrice > 0, "Price must be greater than zero");
        require(_presaleCap > 0, "Cap must be greater than zero");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale period");

        doge20Token = IERC20(_doge20Token);
        presalePrice = _presalePrice;
        presaleCap = _presaleCap;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
    }

    // Modifier to check if the presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Function to purchase DOGE20 tokens during the presale
    function buyTokens(uint256 _amount) external payable isPresaleActive {
        require(msg.value == _amount * presalePrice, "Incorrect ETH amount sent");
        require(tokensSold + _amount <= presaleCap, "Presale cap exceeded");
        
        tokensSold += _amount;
        tokensBought[msg.sender] += _amount;
        
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function for buyers to claim their tokens after the presale
    function claimTokens() external {
        require(tokensBought[msg.sender] > 0, "No tokens to claim");

        uint256 amount = tokensBought[msg.sender];
        tokensBought[msg.sender] = 0; // Reset the buyer's token balance

        // Transfer the tokens to the buyer
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Function to finalize the presale and withdraw the raised ETH
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is not yet over");
        uint256 raisedAmount = address(this).balance;

        // Transfer ETH to the owner
        (bool success, ) = owner().call{value: raisedAmount}("");
        require(success, "Transfer failed");

        emit PresaleFinalized();
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(doge20Token.balanceOf(address(this)) >= _amount, "Insufficient tokens");

        require(doge20Token.transfer(owner(), _amount), "Token withdrawal failed");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
