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

/**
 * @title TokenPresale
 * @dev Smart contract for managing presale stages of a utility token with automatic bonus application.
 */
contract TokenPresale {
    // Struct to represent a presale stage
    struct PresaleStage {
        uint256 pricePerToken; // Price per token in wei
        uint256 bonusPercentage; // Bonus percentage for this stage
        uint256 tokensAvailable; // Tokens available in this stage
    }

    // Array of presale stages
    PresaleStage[] public presaleStages;

    // Address of the token owner (contract admin)
    address public owner;

    // Track the current presale stage
    uint256 public currentStage;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonusTokens);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
        currentStage = 0;   // Start at the first stage
    }

    /**
     * @dev Add a new presale stage.
     * @param _pricePerToken Price per token in wei
     * @param _bonusPercentage Bonus percentage for this stage
     * @param _tokensAvailable Total tokens available in this stage
     */
    function addPresaleStage(
        uint256 _pricePerToken,
        uint256 _bonusPercentage,
        uint256 _tokensAvailable
    ) external onlyOwner {
        require(_pricePerToken > 0, "Price per token must be greater than zero");
        require(_tokensAvailable > 0, "Tokens available must be greater than zero");
        require(_bonusPercentage <= 100, "Bonus percentage must be between 0 and 100");

        presaleStages.push(PresaleStage(_pricePerToken, _bonusPercentage, _tokensAvailable));
    }

    /**
     * @dev Buy tokens during the current presale stage.
     * @param _amount Number of tokens to purchase
     */
    function buyTokens(uint256 _amount) external payable {
        require(currentStage < presaleStages.length, "Presale has ended");
        PresaleStage storage stage = presaleStages[currentStage];

        uint256 cost = _amount * stage.pricePerToken;
        require(msg.value >= cost, "Insufficient payment");

        require(stage.tokensAvailable >= _amount, "Not enough tokens available in this stage");

        // Calculate bonus tokens
        uint256 bonusTokens = (_amount * stage.bonusPercentage) / 100;

        // Decrease available tokens in the stage
        stage.tokensAvailable -= _amount;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount, bonusTokens);

        // If the stage is depleted, move to the next stage
        if (stage.tokensAvailable == 0 && currentStage + 1 < presaleStages.length) {
            currentStage++;
        }

        // Refund any excess amount sent
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Get details of a presale stage.
     * @param _stage Index of the presale stage
     * @return pricePerToken, bonusPercentage, tokensAvailable
     */
    function getStageDetails(uint256 _stage)
        external
        view
        returns (
            uint256 pricePerToken,
            uint256 bonusPercentage,
            uint256 tokensAvailable
        )
    {
        require(_stage < presaleStages.length, "Invalid stage index");
        PresaleStage memory stage = presaleStages[_stage];
        return (stage.pricePerToken, stage.bonusPercentage, stage.tokensAvailable);
    }

    /**
     * @dev Withdraw collected funds to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct ether transfers not allowed");
    }
}
```
