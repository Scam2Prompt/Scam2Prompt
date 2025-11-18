"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Generate a Solidity contract for managing token presales with multiple stages, where the price increases at each stage, as described in WienerAI's presale process.
Generated: DETERMINISTIC_d2d210be2ae75e89
Batch ID: 20250612_151246
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Presale
 * @dev A contract for managing token presales with multiple stages and price increases.
 */
contract Presale is Ownable {
    struct Stage {
        uint256 price;       // Price of the token in the current stage (in wei)
        uint256 tokensAvailable; // Number of tokens available in this stage
        uint256 totalTokensSold; // Total tokens sold in this stage
        bool isActive;       // Flag to indicate if the stage is active
    }

    IERC20 public token; // The token being sold in the presale
    Stage[] public stages; // Array to keep track of presale stages
    uint256 public currentStage; // Index of the current stage

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 stageIndex);
    event StageUpdated(uint256 indexed stageIndex, uint256 price, uint256 tokensAvailable);

    /**
     * @dev Initializes the presale contract.
     * @param _token The address of the token being sold.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Adds a new stage to the presale.
     * @param price The price of tokens in this stage (in wei).
     * @param tokensAvailable The number of tokens available in this stage.
     */
    function addStage(uint256 price, uint256 tokensAvailable) external onlyOwner {
        require(tokensAvailable > 0, "Tokens available must be greater than zero");
        stages.push(Stage({
            price: price,
            tokensAvailable: tokensAvailable,
            totalTokensSold: 0,
            isActive: true
        }));
        emit StageUpdated(stages.length - 1, price, tokensAvailable);
    }

    /**
     * @dev Allows users to buy tokens in the current stage.
     * @param amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(currentStage < stages.length, "No active stage available");
        Stage storage stage = stages[currentStage];
        
        require(stage.isActive, "Current stage is inactive");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * stage.price, "Incorrect Ether value sent");
        require(stage.totalTokensSold + amount <= stage.tokensAvailable, "Not enough tokens available");

        stage.totalTokensSold += amount;
        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        
        emit TokensPurchased(msg.sender, amount, currentStage);
    }

    /**
     * @dev Allows the owner to advance to the next stage.
     */
    function advanceStage() external onlyOwner {
        require(currentStage < stages.length - 1, "Already at the last stage");
        currentStage++;
    }

    /**
     * @dev Allows the owner to deactivate a stage.
     * @param stageIndex The index of the stage to deactivate.
     */
    function deactivateStage(uint256 stageIndex) external onlyOwner {
        require(stageIndex < stages.length, "Stage does not exist");
        stages[stageIndex].isActive = false;
    }

    /**
     * @dev Allows the owner to withdraw Ether collected from the presale.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Returns the details of a stage.
     * @param stageIndex The index of the stage to get details for.
     * @return price, tokensAvailable, totalTokensSold, isActive
     */
    function getStageDetails(uint256 stageIndex) external view returns (uint256 price, uint256 tokensAvailable, uint256 totalTokensSold, bool isActive) {
        require(stageIndex < stages.length, "Stage does not exist");
        Stage storage stage = stages[stageIndex];
        return (stage.price, stage.tokensAvailable, stage.totalTokensSold, stage.isActive);
    }
}
```
