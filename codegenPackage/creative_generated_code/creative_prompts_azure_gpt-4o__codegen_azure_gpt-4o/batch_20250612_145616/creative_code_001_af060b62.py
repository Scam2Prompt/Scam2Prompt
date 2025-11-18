"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonhop.pages.dev
Prompt: Develop a smart contract in Solidity for a presale token allocation system similar to MOONHOP's, ensuring security and gradual price increases across 50 stages.
Generated: DETERMINISTIC_af060b6285d44285
Batch ID: 20250612_145616
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
 * @title PresaleTokenAllocation
 * @dev A smart contract for managing presale token allocations across multiple stages with gradual price increases.
 */
contract PresaleTokenAllocation {
    // Token-related variables
    string public constant name = "PresaleToken";
    string public constant symbol = "PST";
    uint8 public constant decimals = 18;

    // Address of the owner
    address payable public owner;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to store balances of buyers
    mapping(address => uint256) public balanceOf;

    // Presale parameters
    uint256 public constant STAGES = 50; // Number of presale stages
    uint256 public constant TOKENS_PER_STAGE = 1000 * (10**uint256(decimals)); // Tokens allocated per stage
    uint256 public constant INITIAL_PRICE = 0.01 ether; // Starting price per token in stage 1
    uint256 public constant PRICE_INCREMENT = 0.005 ether; // Price increment per stage

    uint256 public currentStage = 1; // Current presale stage
    uint256 public tokensSoldInCurrentStage = 0; // Tokens sold in the current stage

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensWithdrawn(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to owner-only functionality.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "PresaleTokenAllocation: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and set the owner.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "PresaleTokenAllocation: Total supply must be greater than zero");
        totalSupply = _totalSupply * (10**uint256(decimals));
        owner = payable(msg.sender);
    }

    /**
     * @dev Public function to purchase tokens during the presale.
     */
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(currentStage <= STAGES, "PresaleTokenAllocation: Presale has ended");
        require(tokenAmount > 0, "PresaleTokenAllocation: Token amount must be greater than zero");
        
        uint256 pricePerToken = INITIAL_PRICE + ((currentStage - 1) * PRICE_INCREMENT);
        uint256 cost = tokenAmount * pricePerToken;

        require(msg.value >= cost, "PresaleTokenAllocation: Insufficient ETH sent");
        require(tokensSoldInCurrentStage + tokenAmount <= TOKENS_PER_STAGE, "PresaleTokenAllocation: Not enough tokens in current stage");

        balanceOf[msg.sender] += tokenAmount;
        tokensSoldInCurrentStage += tokenAmount;

        // Check if the stage is completed
        if (tokensSoldInCurrentStage == TOKENS_PER_STAGE) {
            currentStage++;
            tokensSoldInCurrentStage = 0;
        }

        emit TokensPurchased(msg.sender, tokenAmount, cost);

        // Refund excess ETH if any
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Owner function to withdraw ETH collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "PresaleTokenAllocation: No funds to withdraw");

        owner.transfer(balance);
        emit TokensWithdrawn(owner, balance);
    }

    /**
     * @dev Owner function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address payable newOwner) external onlyOwner {
        require(newOwner != address(0), "PresaleTokenAllocation: New owner is the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
