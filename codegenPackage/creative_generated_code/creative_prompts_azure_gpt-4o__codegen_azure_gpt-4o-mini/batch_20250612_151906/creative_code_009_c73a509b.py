"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-io.web.app
Prompt: Create a Solidity smart contract for managing presale stages of a utility token, including automatic bonus application for each stage, inspired by Everlodge's token sale structure.
Generated: DETERMINISTIC_c73a509b7dc28cfa
Batch ID: 20250612_151906
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
 * @title PresaleContract
 * @dev Smart contract for managing token presale stages with automatic bonus application.
 */
contract PresaleContract is Ownable {
    // Token to be sold in the presale
    IERC20 public utilityToken;

    // Structure to hold presale stage information
    struct SaleStage {
        uint256 price; // Price per token in wei
        uint256 bonus; // Bonus percentage (e.g. 10 for 10%)
        uint256 startTime; // Start time of the presale stage
        uint256 endTime; // End time of the presale stage
        bool isActive; // Flag to mark if the stage is active
    }

    SaleStage[] public saleStages; // Array to hold all sale stages
    mapping(address => uint256) public contributions; // Mapping to track contributions per address

    event TokensPurchased(address indexed purchaser, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to initialize the presale contract with the utility token address.
     * @param _utilityToken Address of the utility token contract.
     */
    constructor(IERC20 _utilityToken) {
        utilityToken = _utilityToken;
    }

    /**
     * @dev Add a new sale stage to the presale contract.
     * @param _price Price per token in wei.
     * @param _bonus Bonus percentage for the stage.
     * @param _startTime Start time of the sale stage.
     * @param _endTime End time of the sale stage.
     */
    function addSaleStage(uint256 _price, uint256 _bonus, uint256 _startTime, uint256 _endTime) external onlyOwner {
        require(_endTime > _startTime, "End time must be greater than start time");
        
        saleStages.push(SaleStage({
            price: _price,
            bonus: _bonus,
            startTime: _startTime,
            endTime: _endTime,
            isActive: true
        }));
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param _amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        SaleStage memory currentStage = getCurrentSaleStage();
        uint256 totalCost = calculateCost(_amount, currentStage);

        require(msg.value >= totalCost, "Insufficient funds sent");

        contributions[msg.sender] += _amount;
        emit TokensPurchased(msg.sender, _amount, totalCost);
    }

    /**
     * @dev Calculate the cost of tokens with bonus.
     * @param _amount Amount of tokens to purchase.
     * @param _stage The current sale stage.
     * @return totalCost The total cost of the tokens with applied bonus.
     */
    function calculateCost(uint256 _amount, SaleStage memory _stage) internal pure returns (uint256) {
        uint256 bonusTokens = (_amount * _stage.bonus) / 100; // Calculate bonus tokens
        uint256 totalTokens = _amount + bonusTokens; // Total tokens to be purchased
        return totalTokens * _stage.price; // Total cost in wei
    }

    /**
     * @dev Retrieve the current active sale stage.
     * @return currentStage The currently active SaleStage.
     */
    function getCurrentSaleStage() public view returns (SaleStage memory) {
        for (uint256 i = 0; i < saleStages.length; i++) {
            if (saleStages[i].isActive && block.timestamp >= saleStages[i].startTime && block.timestamp <= saleStages[i].endTime) {
                return saleStages[i];
            }
        }
        revert("No active sale stage");
    }

    /**
     * @dev Finalize the presale and transfer collected funds to the owner.
     */
    function finalizePresale() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Allow the owner to deactivate a sale stage.
     * @param _stageIndex Index of the sale stage to deactivate.
     */
    function deactivateSaleStage(uint256 _stageIndex) external onlyOwner {
        require(_stageIndex < saleStages.length, "Invalid stage index");
        saleStages[_stageIndex].isActive = false;
    }
}
```
