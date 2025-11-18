"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapsale-io.pages.dev
Prompt: Write a Solidity smart contract for an ERC20 token presale, ensuring it aligns with UniswapSale's presale process and supports token claiming functionality.
Generated: DETERMINISTIC_cbeda79a6e5cc914
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for an ERC20 token
contract TokenPresale is Ownable {
    // Define state variables
    IERC20 public token; // The ERC20 token being sold
    uint256 public rate; // Number of tokens per wei
    uint256 public presaleEndTime; // Presale end time
    address public liquidityPool; // Uniswap liquidity pool address

    // Tracking contributions
    mapping(address => uint256) public contributions;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);

    // Constructor to initialize the presale
    constructor(IERC20 _token, uint256 _rate, uint256 _duration, address _liquidityPool) {
        token = _token;
        rate = _rate;
        presaleEndTime = block.timestamp + _duration;
        liquidityPool = _liquidityPool;
    }

    // Modifier to check if presale is active
    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    // Function to purchase tokens during the presale
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "Send ETH to buy tokens");
        
        // Calculate the amount of tokens to be purchased
        uint256 tokensToPurchase = msg.value * rate;
        
        // Ensure the contract has enough tokens available for sale
        require(token.balanceOf(address(this)) >= tokensToPurchase, "Not enough tokens in presale");

        // Track the contribution
        contributions[msg.sender] += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    // Function to claim tokens after presale ends
    function claimTokens() external {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        
        uint256 amountToClaim = contributions[msg.sender];
        require(amountToClaim > 0, "No tokens to claim");

        // Resetting contribution to zero before transferring tokens
        contributions[msg.sender] = 0;

        // Transfer the tokens to the buyer
        require(token.transfer(msg.sender, amountToClaim), "Token transfer failed");

        emit TokensClaimed(msg.sender, amountToClaim);
    }

    // Function to withdraw ETH to the owner after the presale ends
    function withdraw() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        
        // Transfer ETH to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Function to add liquidity to Uniswap
    function addLiquidity(uint256 tokenAmount) external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        require(tokenAmount <= token.balanceOf(address(this)), "Not enough tokens in presale");

        // Approve token transfer to the Uniswap router (pseudo-code)
        // token.approve(liquidityPool, tokenAmount);
        // uint256 ethAmount = address(this).balance;
        // (address router).addLiquidityETH{value: ethAmount}(address(token), tokenAmount, 0, 0, owner(), block.timestamp);

        // Emit an event (for illustrative purposes, implement actual Uniswap logic)
        // emit LiquidityAdded(tokenAmount, ethAmount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
