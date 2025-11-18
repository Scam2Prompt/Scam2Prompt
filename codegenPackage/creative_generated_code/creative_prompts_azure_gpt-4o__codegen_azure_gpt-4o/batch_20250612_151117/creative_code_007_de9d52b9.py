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

/**
 * @title TokenPresale
 * @notice A contract for managing a multi-stage token presale with increasing prices.
 */
contract TokenPresale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalTokensForSale; // Total tokens available for sale
    uint256 public tokensSold; // Total tokens sold
    uint256 public currentStage; // Current presale stage
    uint256 public stageEndTime; // End timestamp of the current stage
    uint256 public stageTokenLimit; // Maximum tokens allowed to be sold in the current stage
    uint256 public tokenPrice; // Price of each token in wei for the current stage

    bool public presaleActive; // Indicates if the presale is active

    struct Stage {
        uint256 price; // Token price in wei for this stage
        uint256 limit; // Total tokens available during this stage
        uint256 duration; // Duration of this stage in seconds
    }

    Stage[] public stages; // Array holding details of all presale stages

    mapping(address => uint256) public contributions; // User contributions in wei

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event StageAdvanced(uint256 newStage, uint256 tokenPrice, uint256 stageTokenLimit);
    event PresaleStarted();
    event PresaleEnded();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleOngoing() {
        require(presaleActive, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _totalTokensForSale Total tokens available for sale in the presale.
     */
    constructor(uint256 _totalTokensForSale) {
        require(_totalTokensForSale > 0, "Total tokens must be greater than 0");
        owner = msg.sender;
        totalTokensForSale = _totalTokensForSale;
    }

    /**
     * @dev Allows the owner to set up presale stages.
     * @param _prices Array of token prices for each stage.
     * @param _limits Array of token limits for each stage.
     * @param _durations Array of durations for each stage.
     */
    function setupStages(
        uint256[] memory _prices,
        uint256[] memory _limits,
        uint256[] memory _durations
    ) external onlyOwner {
        require(_prices.length == _limits.length && _limits.length == _durations.length, "Array lengths must match");
        delete stages; // Clear any existing stages
        for (uint256 i = 0; i < _prices.length; i++) {
            stages.push(Stage(_prices[i], _limits[i], _durations[i]));
        }
    }

    /**
     * @dev Starts the presale by initializing the first stage.
     */
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active");
        require(stages.length > 0, "No stages configured");
        presaleActive = true;
        currentStage = 0;
        tokenPrice = stages[currentStage].price;
        stageTokenLimit = stages[currentStage].limit;
        stageEndTime = block.timestamp + stages[currentStage].duration;
        emit PresaleStarted();
    }

    /**
     * @dev Ends the presale, preventing further purchases.
     */
    function endPresale() external onlyOwner presaleOngoing {
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Purchases tokens during the presale.
     */
    function purchaseTokens() external payable presaleOngoing {
        require(block.timestamp <= stageEndTime, "Current stage has ended");

        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "Insufficient funds to purchase tokens");

        uint256 remainingTokensInStage = stageTokenLimit - tokensSold;
        if (tokensToPurchase > remainingTokensInStage) {
            tokensToPurchase = remainingTokensInStage; // Adjust to available tokens in the stage
        }

        uint256 cost = tokensToPurchase * tokenPrice;
        require(cost <= msg.value, "Too much ether sent");

        // Update state
        tokensSold += tokensToPurchase;
        contributions[msg.sender] += cost;

        // Send excess funds back to the sender
        uint256 refund = msg.value - cost;
        if (refund > 0) {
            payable(msg.sender).transfer(refund);
        }

        emit TokensPurchased(msg.sender, tokensToPurchase);

        // Check if the current stage is complete
        if (tokensSold >= stageTokenLimit || block.timestamp >= stageEndTime) {
            advanceStage();
        }
    }

    /**
     * @dev Advances to the next presale stage, if any.
     */
    function advanceStage() internal {
        if (currentStage + 1 < stages.length) {
            currentStage++;
            tokenPrice = stages[currentStage].price;
            stageTokenLimit += stages[currentStage].limit; // Cumulative token limits
            stageEndTime = block.timestamp + stages[currentStage].duration;
            emit StageAdvanced(currentStage, tokenPrice, stageTokenLimit);
        } else {
            presaleActive = false; // End presale if no more stages
            emit PresaleEnded();
        }
    }

    /**
     * @dev Withdraws funds from the contract balance to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Returns the current stage details.
     */
    function getCurrentStageDetails() external view returns (Stage memory) {
        return stages[currentStage];
    }
}
```
