"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Write a code snippet for a decentralized application that allows users to stake QI tokens and manage collateral for MAI issuance.
Generated: DETERMINISTIC_bf49b63286fecc68
Batch ID: 20250612_162431
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the MAI issuance contract
interface IMaiIssuer {
    function issueMAI(address user, uint256 amount) external;
    function redeemMAI(address user, uint256 amount) external;
}

// Main contract for staking QI tokens and managing collateral for MAI issuance
contract QIStaking is Ownable {
    // State variables
    IERC20 public qiToken; // The QI token contract
    IMaiIssuer public maiIssuer; // The MAI issuer contract

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;
    
    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event MAIIssued(address indexed user, uint256 amount);
    event MAIRedeemed(address indexed user, uint256 amount);

    // Constructor to set the QI token and MAI issuer addresses
    constructor(address _qiTokenAddress, address _maiIssuerAddress) {
        require(_qiTokenAddress != address(0), "Invalid QI token address");
        require(_maiIssuerAddress != address(0), "Invalid MAI issuer address");
        
        qiToken = IERC20(_qiTokenAddress);
        maiIssuer = IMaiIssuer(_maiIssuerAddress);
    }

    // Function to stake QI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer QI tokens from user to contract
        require(qiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update user's stake
        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake QI tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient stake balance");

        // Update user's stake
        stakes[msg.sender] -= amount;

        // Transfer QI tokens back to user
        require(qiToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to issue MAI based on staked QI tokens
    function issueMAI(uint256 amount) external {
        require(stakes[msg.sender] > 0, "No staked tokens to issue MAI");
        
        // Issue MAI to the user
        maiIssuer.issueMAI(msg.sender, amount);
        
        emit MAIIssued(msg.sender, amount);
    }

    // Function to redeem MAI
    function redeemMAI(uint256 amount) external {
        // Redeem MAI from the user
        maiIssuer.redeemMAI(msg.sender, amount);
        
        emit MAIRedeemed(msg.sender, amount);
    }

    // Function to withdraw the contract's balance of QI tokens (only owner)
    function withdrawQI(uint256 amount) external onlyOwner {
        require(qiToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(qiToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
