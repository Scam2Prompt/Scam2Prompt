"""
Generated Code Metadata:
========================
Original URL: https://en-wienerdog.pages.dev
Prompt: Generate a Solidity contract for managing token presales with multiple stages, where the price increases at each stage, as described in WienerAI's presale process.
Generated: DETERMINISTIC_d2d210be2ae75e89
Batch ID: 20250612_151246
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WienerAIPresale
 * @author [Your Name]
 * @notice A contract for managing token presales with multiple stages.
 */
contract WienerAIPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of stages with their respective details
    struct Stage {
        uint256 startTime;
        uint256 endTime;
        uint256 price;
        uint256 tokensSold;
        uint256 tokensAvailable;
    }

    // Mapping of stages
    Stage[] public stages;

    // Mapping of user contributions
    mapping (address => uint256) public userContributions;

    // Token being presold
    ERC20 public token;

    // Total tokens allocated for presale
    uint256 public totalTokensAllocated;

    // Current stage index
    uint256 public currentStageIndex;

    // Event emitted when a new stage is added
    event NewStage(uint256 indexed stageIndex, uint256 startTime, uint256 endTime, uint256 price);

    // Event emitted when a user contributes
    event Contributed(address indexed user, uint256 amount);

    // Event emitted when a stage is ended
    event StageEnded(uint256 indexed stageIndex, uint256 tokensSold);

    /**
     * @notice Initializes the contract.
     * @param _token Address of the token being presold.
     * @param _totalTokensAllocated Total tokens allocated for presale.
     */
    constructor(ERC20 _token, uint256 _totalTokensAllocated) public {
        require(_token != ERC20(address(0)), "Token address cannot be zero");
        require(_totalTokensAllocated > 0, "Total tokens allocated must be greater than zero");

        token = _token;
        totalTokensAllocated = _totalTokensAllocated;
    }

    /**
     * @notice Adds a new stage to the presale.
     * @param _startTime Start time of the stage.
     * @param _endTime End time of the stage.
     * @param _price Price of the token at this stage.
     * @param _tokensAvailable Tokens available for this stage.
     */
    function addStage(uint256 _startTime, uint256 _endTime, uint256 _price, uint256 _tokensAvailable) public onlyOwner {
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be greater than start time");
        require(_price > 0, "Price must be greater than zero");
        require(_tokensAvailable > 0, "Tokens available must be greater than zero");
        require(_tokensAvailable <= totalTokensAllocated, "Tokens available cannot exceed total tokens allocated");

        stages.push(Stage(_startTime, _endTime, _price, 0, _tokensAvailable));

        // Update current stage index if this is the first stage
        if (stages.length == 1) {
            currentStageIndex = 0;
        }

        emit NewStage(stages.length - 1, _startTime, _endTime, _price);
    }

    /**
     * @notice Contributes to the current stage.
     * @param _amount Amount to contribute.
     */
    function contribute(uint256 _amount) public nonReentrant {
        require(stages.length > 0, "No stages available");
        require(stages[currentStageIndex].startTime <= block.timestamp && block.timestamp <= stages[currentStageIndex].endTime, "Contribution is not within the current stage");

        uint256 tokensToBuy = _amount.mul(stages[currentStageIndex].price);
        require(tokensToBuy <= stages[currentStageIndex].tokensAvailable, "Not enough tokens available");

        // Update user's contribution
        userContributions[msg.sender] = userContributions[msg.sender].add(_amount);

        // Update stage details
        stages[currentStageIndex].tokensSold = stages[currentStageIndex].tokensSold.add(tokensToBuy);
        stages[currentStageIndex].tokensAvailable = stages[currentStageIndex].tokensAvailable.sub(tokensToBuy);

        // Transfer tokens to user
        require(token.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        emit Contributed(msg.sender, _amount);

        // End stage if tokens available reach zero
        if (stages[currentStageIndex].tokensAvailable == 0) {
            endStage();
        }
    }

    /**
     * @notice Ends the current stage.
     */
    function endStage() internal {
        emit StageEnded(currentStageIndex, stages[currentStageIndex].tokensSold);

        // Move to next stage if available
        if (currentStageIndex < stages.length - 1) {
            currentStageIndex++;
        }
    }

    /**
     * @notice Allows the owner to withdraw remaining tokens.
     */
    function withdrawRemainingTokens() public onlyOwner {
        uint256 remainingTokens = token.balanceOf(address(this));
        require(token.transfer(msg.sender, remainingTokens), "Token transfer failed");
    }

    // Restrict access to owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Access restricted to owner");
        _;
    }

    // Get the owner address
    function owner() public view returns (address) {
        return 0x...; // Replace with actual owner address or implement ownable
    }
}
```
