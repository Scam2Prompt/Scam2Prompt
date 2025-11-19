"""
Generated Code Metadata:
========================
Original URL: https://register-jessecoin.pages.dev
Prompt: Generate a smart contract in Solidity that enforces a presale cap of 1000 BASE for JESSE tokens, ensuring that purchases exceeding the cap are rejected.
Generated: DETERMINISTIC_454169c1662f4ca8
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title JesseTokenPresale
 * @dev A smart contract for managing a presale of JESSE tokens with a cap of 1000 BASE.
 */
contract JesseTokenPresale {
    // Presale parameters
    uint256 public constant PRESALE_CAP = 1000 * 10**18; // 1000 BASE (assuming 18 decimals)
    uint256 public totalContributed;
    address public owner;
    
    // Mapping to track contributions
    mapping(address => uint256) public contributions;
    
    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event PresaleCapReached(uint256 totalContributed);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    modifier presaleNotEnded() {
        require(totalContributed < PRESALE_CAP, "Presale cap has been reached");
        _;
    }
    
    /**
     * @dev Constructor sets the owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Allows users to contribute to the presale
     */
    function contribute() external payable presaleNotEnded {
        require(msg.value > 0, "Contribution must be greater than 0");
        
        uint256 remainingCap = PRESALE_CAP - totalContributed;
        uint256 acceptedContribution = msg.value;
        uint256 excessContribution = 0;
        
        if (msg.value > remainingCap) {
            acceptedContribution = remainingCap;
            excessContribution = msg.value - remainingCap;
        }
        
        contributions[msg.sender] += acceptedContribution;
        totalContributed += acceptedContribution;
        
        emit ContributionReceived(msg.sender, acceptedContribution);
        
        if (excessContribution > 0) {
            payable(msg.sender).transfer(excessContribution);
        }
        
        if (totalContributed == PRESALE_CAP) {
            emit PresaleCapReached(totalContributed);
        }
    }
    
    /**
     * @dev Allows the owner to withdraw the collected funds
     */
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
    
    /**
     * @dev Returns the remaining presale cap
     */
    function getRemainingCap() external view returns (uint256) {
        return PRESALE_CAP - totalContributed;
    }
}
```
