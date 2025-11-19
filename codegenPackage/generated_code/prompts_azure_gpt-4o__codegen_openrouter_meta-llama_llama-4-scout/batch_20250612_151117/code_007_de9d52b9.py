"""
Generated Code Metadata:
========================
Original URL: https://weinerdog.pages.dev
Prompt: Create a step-by-step guide for implementing a token presale system in Solidity, including price increases at each stage, similar to WienerAI's presale structure.
Generated: DETERMINISTIC_de9d52b9680be076
Batch ID: 20250612_151117
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Token Presale Contract
 * @author [Your Name]
 * @notice This contract manages a token presale with multiple stages and price increases.
 */
contract TokenPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Token details
    address public tokenAddress;
    string public tokenName;
    string public tokenSymbol;

    // Presale stages
    struct PresaleStage {
        uint256 startTime;
        uint256 endTime;
        uint256 price; // in USD
        uint256 minContribution;
        uint256 maxContribution;
        uint256 tokensSold;
    }

    // Mapping of presale stages
    mapping(uint256 => PresaleStage) public stages;

    // Current stage index
    uint256 public currentStageIndex;

    // Total number of stages
    uint256 public totalStages;

    // Mapping of user contributions
    mapping(address => uint256) public userContributions;

    // Event emitted when a user contributes
    event Contribution(address indexed user, uint256 amount);

    // Event emitted when a stage is started
    event StageStarted(uint256 indexed stageIndex, uint256 startTime);

    // Event emitted when a stage is ended
    event StageEnded(uint256 indexed stageIndex, uint256 endTime);

    /**
     * @notice Initializes the token presale contract.
     * @param _tokenAddress Address of the token contract.
     * @param _tokenName Name of the token.
     * @param _tokenSymbol Symbol of the token.
     */
    constructor(address _tokenAddress, string memory _tokenName, string memory _tokenSymbol) {
        require(_tokenAddress != address(0), "Invalid token address");

        tokenAddress = _tokenAddress;
        tokenName = _tokenName;
        tokenSymbol = _tokenSymbol;

        // Initialize stages
        totalStages = 5; // 5 stages
        currentStageIndex = 0;

        // Define stages
        stages[0] = PresaleStage(
            block.timestamp, // start time
            block.timestamp + 30 days, // end time (30 days)
            0.1 ether, // price (0.1 ETH per token)
            1 ether, // min contribution
            10 ether, // max contribution
            0 // tokens sold
        );

        stages[1] = PresaleStage(
            block.timestamp + 30 days, // start time
            block.timestamp + 60 days, // end time (60 days)
            0.15 ether, // price (0.15 ETH per token)
            1 ether, // min contribution
            20 ether, // max contribution
            0 // tokens sold
        );

        stages[2] = PresaleStage(
            block.timestamp + 60 days, // start time
            block.timestamp + 90 days, // end time (90 days)
            0.2 ether, // price (0.2 ETH per token)
            1 ether, // min contribution
            30 ether, // max contribution
            0 // tokens sold
        );

        stages[3] = PresaleStage(
            block.timestamp + 90 days, // start time
            block.timestamp + 120 days, // end time (120 days)
            0.25 ether, // price (0.25 ETH per token)
            1 ether, // min contribution
            40 ether, // max contribution
            0 // tokens sold
        );

        stages[4] = PresaleStage(
            block.timestamp + 120 days, // start time
            block.timestamp + 150 days, // end time (150 days)
            0.3 ether, // price (0.3 ETH per token)
            1 ether, // min contribution
            50 ether, // max contribution
            0 // tokens sold
        );
    }

    /**
     * @notice Contributes to the current presale stage.
     * @param _amount Contribution amount in ETH.
     */
    function contribute(uint256 _amount) external payable nonReentrant {
        require(msg.value == _amount, "Invalid contribution amount");
        require(currentStageIndex < totalStages, "Presale ended");

        PresaleStage storage currentStage = stages[currentStageIndex];

        require(block.timestamp >= currentStage.startTime && block.timestamp <= currentStage.endTime, "Invalid stage timing");
        require(_amount >= currentStage.minContribution && _amount <= currentStage.maxContribution, "Invalid contribution amount");

        // Calculate tokens to be purchased
        uint256 tokensToPurchase = _amount.div(currentStage.price);

        // Update tokens sold
        currentStage.tokensSold = currentStage.tokensSold.add(tokensToPurchase);

        // Update user contribution
        userContributions[msg.sender] = userContributions[msg.sender].add(_amount);

        // Transfer tokens to user
        ERC20(tokenAddress).transfer(msg.sender, tokensToPurchase);

        // Emit contribution event
        emit Contribution(msg.sender, _amount);
    }

    /**
     * @notice Ends the current presale stage and moves to the next one.
     */
    function endStage() external {
        require(currentStageIndex < totalStages, "Presale ended");

        PresaleStage storage currentStage = stages[currentStageIndex];

        require(block.timestamp > currentStage.endTime, "Stage not ended");

        // Emit stage ended event
        emit StageEnded(currentStageIndex, block.timestamp);

        // Move to next stage
        currentStageIndex++;

        // Emit stage started event
        emit StageStarted(currentStageIndex, block.timestamp);
    }

    /**
     * @notice Retrieves the current presale stage.
     * @return Current presale stage.
     */
    function getCurrentStage() public view returns (PresaleStage memory) {
        return stages[currentStageIndex];
    }
}
```
