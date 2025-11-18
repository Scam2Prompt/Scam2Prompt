"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.web.app
Prompt: Write a Solidity contract for a token with a roadmap-driven burn mechanism, where 5% of the total supply is burned upon achieving specific milestones, similar to BTCETF.
Generated: DETERMINISTIC_0bf9a57bd563531f
Batch ID: 20250612_151513
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

// Import OpenZeppelin's ERC20 contract implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RoadmapToken
 * @dev This contract represents a token with a roadmap-driven burn mechanism. 
 *      5% of the total supply will be burned upon achieving specific milestones.
 */
contract RoadmapToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Milestones
    enum Milestone { Milestone1, Milestone2, Milestone3 }
    Milestone public currentMilestone;

    // Event for token burning
    event TokensBurned(uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("RoadmapToken", "RDT") {
        _mint(msg.sender, INITIAL_SUPPLY);
        currentMilestone = Milestone.Milestone1; // Start at first milestone
    }

    /**
     * @dev Function to burn tokens when a milestone is achieved.
     * @notice Only callable by the contract owner (for security).
     * @dev Burns 5% of the total supply for every milestone.
     */
    function achieveMilestone() external onlyOwner {
        require(currentMilestone < Milestone.Milestone3, "All milestones already achieved");
        
        // Calculate 5% of the total supply
        uint256 burnAmount = (INITIAL_SUPPLY * 5) / 100;
        
        // Burn the tokens
        _burn(address(this), burnAmount);
        emit TokensBurned(burnAmount);

        // Move to the next milestone
        currentMilestone = Milestone(uint256(currentMilestone) + 1);
    }

    /**
     * @dev Function to retrieve the current milestone.
     * @return The current milestone achieved.
     */
    function getCurrentMilestone() external view returns (Milestone) {
        return currentMilestone;
    }

    /**
     * @dev Function to mint new tokens, only callable by the owner.
     * @param amount The amount of tokens to mint.
     */
    function mintTokens(uint256 amount) external onlyOwner {
        _mint(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw any Ether that may be sent to the contract.
     * @notice This is for emergency purposes only.
     */
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
