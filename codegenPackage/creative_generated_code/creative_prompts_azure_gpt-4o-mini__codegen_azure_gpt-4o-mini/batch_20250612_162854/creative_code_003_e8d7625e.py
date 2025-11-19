"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Provide a code example for implementing the Moxie Bonding Curves in a decentralized application on Farcaster.
Generated: DETERMINISTIC_e8d7625e1748df3e
Batch ID: 20250612_162854
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

// Importing OpenZeppelin's SafeMath library for safe mathematical operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface declaration for a simple ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// MoxieBondingCurve contract implementing a Moxie Bonding Curve
contract MoxieBondingCurve {
    using SafeMath for uint256;

    // State variables
    IERC20 public token; // The ERC20 token used in the bonding curve
    uint256 public totalSupply; // Total supply of tokens minted
    uint256 public reserveBalance; // Total reserve balance held in the contract
    uint256 public constant MULTIPLIER = 1000; // Multiplier for curve calculations

    // Events
    event TokenPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokenSold(address indexed seller, uint256 amount, uint256 payout);

    // Constructor to initialize the bonding curve with an ERC20 token
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to calculate the price of tokens based on the current total supply
    function calculateBuyPrice(uint256 _amount) public view returns (uint256) {
        require(_amount > 0, "Amount must be greater than zero");
        uint256 price = (totalSupply.add(_amount)).mul(MULTIPLIER).div(1 ether);
        return price.sub(totalSupply.mul(MULTIPLIER).div(1 ether));
    }

    // Function for users to purchase tokens
    function buyTokens(uint256 _amount) external payable {
        uint256 cost = calculateBuyPrice(_amount);
        require(msg.value >= cost, "Insufficient Ether sent");
        
        // Update state variables
        totalSupply = totalSupply.add(_amount);
        reserveBalance = reserveBalance.add(msg.value);
        
        // Transfer tokens to the buyer
        emit TokenPurchased(msg.sender, _amount, cost);
    }

    // Function to calculate the sell price for tokens
    function calculateSellPrice(uint256 _amount) public view returns (uint256) {
        require(_amount > 0 && _amount <= totalSupply, "Invalid amount");
        uint256 price = totalSupply.sub(_amount).mul(MULTIPLIER).div(1 ether);
        return reserveBalance.sub(price);
    }

    // Function for users to sell tokens back to the contract
    function sellTokens(uint256 _amount) external {
        require(_amount > 0 && _amount <= totalSupply, "Invalid amount");
        
        uint256 payout = calculateSellPrice(_amount);
        require(payout <= address(this).balance, "Insufficient contract balance");

        // Update state variables
        totalSupply = totalSupply.sub(_amount);
        reserveBalance = reserveBalance.sub(payout);
        
        // Transfer Ether to the seller
        payable(msg.sender).transfer(payout);
        emit TokenSold(msg.sender, _amount, payout);
    }

    // Function to withdraw leftover Ether from the contract
    function withdraw() external {
        require(msg.sender == address(this), "Only contract can withdraw");
        payable(msg.sender).transfer(address(this).balance);
    }

    // Function to check the contract's balance
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

**Note:** Ensure you have the appropriate OpenZeppelin library installed in your environment to run this code. This contract is a simplified representation of a bonding curve and should be tested extensively before any production deployment.
