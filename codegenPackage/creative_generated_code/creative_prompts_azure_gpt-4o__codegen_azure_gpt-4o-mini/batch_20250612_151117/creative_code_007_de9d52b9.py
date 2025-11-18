"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weinerdog.pages.dev
Prompt: Create a step-by-step guide for implementing a token presale system in Solidity, including price increases at each stage, similar to WienerAI's presale structure.
Generated: DETERMINISTIC_de9d52b9680be076
Batch ID: 20250612_151117
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenPresale is Ownable {
    // Token contract instance
    ERC20 public token;
    
    // Presale stage structure
    struct PresaleStage {
        uint256 price; // Price of token in wei
        uint256 tokenSupply; // Amount of tokens available in this stage
        uint256 tokensSold; // Amount of tokens sold in this stage
        bool active; // Active status of the stage
    }
    
    // Mapping for presale stages
    mapping(uint256 => PresaleStage) public presaleStages;
    uint256 public currentStageIndex;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 stageIndex);
    event StageCreated(uint256 index, uint256 price, uint256 supply);
    event StageActivated(uint256 index);
    event StageDeactivated(uint256 index);

    // Constructor to initialize the presale with a token address
    constructor(address tokenAddress) {
        token = ERC20(tokenAddress);
    }

    // Function to create a presale stage
    function createStage(uint256 price, uint256 supply) external onlyOwner {
        require(supply > 0, "Supply must be greater than 0");
        require(price > 0, "Price must be greater than 0");

        presaleStages[currentStageIndex] = PresaleStage({
            price: price,
            tokenSupply: supply,
            tokensSold: 0,
            active: true
        });

        emit StageCreated(currentStageIndex, price, supply);
        currentStageIndex++;
    }

    // Function to purchase tokens during a presale stage
    function purchaseTokens(uint256 amount) external payable {
        PresaleStage storage stage = presaleStages[currentStageIndex - 1];
        
        require(stage.active, "Current stage is not active");
        require(msg.value >= stage.price * amount, "Insufficient funds sent");
        require(stage.tokensSold + amount <= stage.tokenSupply, "Not enough tokens available");

        stage.tokensSold += amount;
        token.transfer(msg.sender, amount);
        
        emit TokensPurchased(msg.sender, amount, currentStageIndex - 1);
    }

    // Function to activate a presale stage
    function activateStage(uint256 index) external onlyOwner {
        require(index < currentStageIndex, "Stage does not exist");
        presaleStages[index].active = true;
        emit StageActivated(index);
    }

    // Function to deactivate a presale stage
    function deactivateStage(uint256 index) external onlyOwner {
        require(index < currentStageIndex, "Stage does not exist");
        presaleStages[index].active = false;
        emit StageDeactivated(index);
    }

    // Function to withdraw funds from the contract
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to get the current stage details
    function getCurrentStage() external view returns (PresaleStage memory) {
        return presaleStages[currentStageIndex - 1];
    }
}
```
