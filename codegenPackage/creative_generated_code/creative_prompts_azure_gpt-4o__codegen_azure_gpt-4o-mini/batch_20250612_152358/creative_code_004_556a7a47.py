"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choccoin-dashboard.pages.dev
Prompt: Write a smart contract snippet for distributing $CHOC tokens after the presale ends, ensuring compliance with the outlined tokenomics (50% presale, 20% project funds, etc.).
Generated: DETERMINISTIC_556a7a47912ec39f
Batch ID: 20250612_152358
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

// Importing SafeERC20 and Ownable from OpenZeppelin libraries for security and ownership management
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC20 token
interface IToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract CHOCDistributor is Ownable {
    using SafeERC20 for IToken;

    // State variables
    IToken public chocToken; // The $CHOC token instance
    uint256 public presaleEndTime; // The timestamp when the presale ends
    bool public isDistributed; // A flag to check if distribution has occurred

    // Tokenomics distribution percentages
    uint256 constant PRESALE_PERCENTAGE = 50; // 50% for presale
    uint256 constant PROJECT_FUNDS_PERCENTAGE = 20; // 20% for project funds
    uint256 constant TEAM_PERCENTAGE = 20; // 20% for team
    uint256 constant MARKETING_PERCENTAGE = 10; // 10% for marketing

    address public projectFundsAddress; // Address for project funds
    address public teamAddress; // Address for team allocation
    address public marketingAddress; // Address for marketing allocation

    // Event to log the distribution of tokens
    event TokensDistributed(address to, uint256 amount);

    // Constructor to initialize the contract
    constructor(
        address _chocToken,
        uint256 _presaleDuration,
        address _projectFundsAddress,
        address _teamAddress,
        address _marketingAddress
    ) {
        chocToken = IToken(_chocToken);
        presaleEndTime = block.timestamp + _presaleDuration;
        projectFundsAddress = _projectFundsAddress;
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;
        isDistributed = false;
    }

    // Function to distribute tokens after the presale ends
    function distributeTokens(uint256 totalSupply) external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        require(!isDistributed, "Tokens have already been distributed");

        // Calculate the amounts to distribute based on tokenomics
        uint256 presaleAmount = (totalSupply * PRESALE_PERCENTAGE) / 100;
        uint256 projectFundsAmount = (totalSupply * PROJECT_FUNDS_PERCENTAGE) / 100;
        uint256 teamAmount = (totalSupply * TEAM_PERCENTAGE) / 100;
        uint256 marketingAmount = (totalSupply * MARKETING_PERCENTAGE) / 100;

        // Transfer the calculated amounts to the respective addresses
        chocToken.safeTransfer(msg.sender, presaleAmount); // Presale tokens to the owner
        chocToken.safeTransfer(projectFundsAddress, projectFundsAmount);
        chocToken.safeTransfer(teamAddress, teamAmount);
        chocToken.safeTransfer(marketingAddress, marketingAmount);

        // Mark distribution as completed
        isDistributed = true;

        // Emit events for each distribution
        emit TokensDistributed(projectFundsAddress, projectFundsAmount);
        emit TokensDistributed(teamAddress, teamAmount);
        emit TokensDistributed(marketingAddress, marketingAmount);
    }

    // Function to withdraw tokens in case of emergency (onlyOwner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        chocToken.safeTransfer(msg.sender, amount);
    }
}
```
