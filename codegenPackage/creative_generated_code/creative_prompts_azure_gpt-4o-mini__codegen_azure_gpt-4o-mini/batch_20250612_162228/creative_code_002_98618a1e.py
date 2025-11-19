"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimachain.pages.dev
Prompt: Create a Solidity contract that interacts with a DAO, inspired by the Popcorn DAO's approach to leveraging Web3 DeFi for environmental initiatives.
Generated: DETERMINISTIC_98618a1e54b15e17
Batch ID: 20250612_162228
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token management and ownership
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title EnvironmentalInitiativeDAO
 * @dev This contract serves as a DAO for managing and funding environmental initiatives using a token-based voting mechanism.
 */
contract EnvironmentalInitiativeDAO is Ownable {
    // Structure to hold initiative details
    struct Initiative {
        string description; // Description of the initiative
        address proposer;    // Address of the proposer
        uint256 fundingGoal; // Funding goal in tokens
        uint256 totalFunding; // Total tokens raised
        bool isActive;       // Status of the initiative
        uint256 endTime;     // When the initiative ends
    }

    // Mapping of initiative ID to Initiative struct
    mapping(uint256 => Initiative) public initiatives;
    uint256 public initiativeCount; // Counter for total initiatives

    // Event for proposal creation
    event InitiativeProposed(uint256 initiativeId, string description, uint256 fundingGoal, uint256 duration);
    // Event for funding an initiative
    event InitiativeFunded(uint256 initiativeId, address funder, uint256 amount);
    // Event for initiative activation
    event InitiativeActivated(uint256 initiativeId);
    
    // Token interface for funding
    IERC20 public fundingToken;

    /**
     * @dev Constructor to set the funding token address.
     * @param _fundingToken Address of the ERC20 token used for funding initiatives.
     */
    constructor(IERC20 _fundingToken) {
        fundingToken = _fundingToken;
    }

    /**
     * @dev Propose a new environmental initiative.
     * @param description Description of the initiative.
     * @param fundingGoal The funding goal for the initiative.
     * @param duration The duration (in seconds) for which the initiative will be active.
     */
    function proposeInitiative(string memory description, uint256 fundingGoal, uint256 duration) external onlyOwner {
        require(duration > 0, "Duration must be greater than zero");
        require(fundingGoal > 0, "Funding goal must be greater than zero");

        initiativeCount++;
        initiatives[initiativeCount] = Initiative({
            description: description,
            proposer: msg.sender,
            fundingGoal: fundingGoal,
            totalFunding: 0,
            isActive: true,
            endTime: block.timestamp + duration
        });

        emit InitiativeProposed(initiativeCount, description, fundingGoal, duration);
    }

    /**
     * @dev Fund an existing initiative.
     * @param initiativeId The ID of the initiative to fund.
     * @param amount The amount of tokens to fund the initiative.
     */
    function fundInitiative(uint256 initiativeId, uint256 amount) external {
        Initiative storage initiative = initiatives[initiativeId];
        
        require(initiative.isActive, "Initiative is not active");
        require(block.timestamp < initiative.endTime, "Initiative funding period has ended");
        require(initiative.totalFunding + amount <= initiative.fundingGoal, "Funding exceeds goal");

        // Transfer tokens from the funder's account to the contract
        require(fundingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        initiative.totalFunding += amount;

        emit InitiativeFunded(initiativeId, msg.sender, amount);

        // Check if funding goal is reached
        if (initiative.totalFunding == initiative.fundingGoal) {
            initiative.isActive = false;
            emit InitiativeActivated(initiativeId);
        }
    }

    /**
     * @dev Allow the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(fundingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(fundingToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Get details of an initiative.
     * @param initiativeId The ID of the initiative.
     * @return Description, proposer address, funding goal, total funding, active status, and end time of the initiative.
     */
    function getInitiative(uint256 initiativeId) external view returns (string memory, address, uint256, uint256, bool, uint256) {
        Initiative memory initiative = initiatives[initiativeId];
        return (initiative.description, initiative.proposer, initiative.fundingGoal, initiative.totalFunding, initiative.isActive, initiative.endTime);
    }
}
```
