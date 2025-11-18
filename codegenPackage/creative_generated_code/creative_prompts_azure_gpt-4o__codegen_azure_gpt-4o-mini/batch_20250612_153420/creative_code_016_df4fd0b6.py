"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Provide code in Solidity to implement a multi-stage presale mechanism for a token like $GFOX, including price adjustments after each stage.
Generated: DETERMINISTIC_df4fd0b65828f548
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MultiStagePresale
 * @dev This contract implements a multi-stage presale mechanism for a token.
 */
contract MultiStagePresale is Ownable {
    // Struct to hold the details of each presale stage
    struct Stage {
        uint256 price; // Price of the token in wei per token
        uint256 tokenAllocation; // Number of tokens allocated for this stage
        uint256 tokensSold; // Number of tokens sold in this stage
        bool isActive; // Is the stage currently active
    }

    // Mapping of stages by their index
    mapping(uint256 => Stage) public stages;
    uint256 public currentStageIndex; // Current active stage index
    uint256 public totalStages; // Total number of stages
    IERC20 public token; // The token being sold

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 stageIndex);
    event StageUpdated(uint256 index, uint256 price, uint256 allocation);
    event StageActivated(uint256 index);
    event StageDeactivated(uint256 index);

    /**
     * @dev Constructor to initialize the presale with the token address.
     * @param _token Address of the token being sold
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Function to add a new stage to the presale.
     * @param price Price of the token in wei for the new stage
     * @param tokenAllocation Number of tokens allocated for the new stage
     */
    function addStage(uint256 price, uint256 tokenAllocation) external onlyOwner {
        stages[totalStages] = Stage(price, tokenAllocation, 0, true);
        totalStages++;
        emit StageUpdated(totalStages - 1, price, tokenAllocation);
    }

    /**
     * @dev Function to activate a stage.
     * @param index Index of the stage to activate
     */
    function activateStage(uint256 index) external onlyOwner {
        require(index < totalStages, "Stage does not exist");
        require(!stages[index].isActive, "Stage is already active");
        
        // Deactivate the previous stage
        if (currentStageIndex < totalStages) {
            stages[currentStageIndex].isActive = false;
            emit StageDeactivated(currentStageIndex);
        }

        // Activate the new stage
        stages[index].isActive = true;
        currentStageIndex = index;
        emit StageActivated(index);
    }

    /**
     * @dev Function to purchase tokens in the current stage.
     * @param amount Number of tokens to purchase
     */
    function purchaseTokens(uint256 amount) external payable {
        Stage storage currentStage = stages[currentStageIndex];
        
        require(currentStage.isActive, "Current stage is not active");
        require(currentStage.tokensSold + amount <= currentStage.tokenAllocation, "Not enough tokens available");
        require(msg.value == amount * currentStage.price, "Incorrect Ether sent");

        // Update tokens sold in the current stage
        currentStage.tokensSold += amount;

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount, currentStageIndex);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to withdraw unsold tokens after the presale is finished.
     * Only the owner can call this function.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        for (uint256 i = 0; i < totalStages; i++) {
            uint256 unsoldTokens = stages[i].tokenAllocation - stages[i].tokensSold;
            if (unsoldTokens > 0) {
                require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
            }
        }
    }
}
```
