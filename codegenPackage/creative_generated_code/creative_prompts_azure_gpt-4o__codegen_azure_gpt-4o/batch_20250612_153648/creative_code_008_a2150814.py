"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pingu-buy.pages.dev
Prompt: Write a smart contract function that enables users to adopt digital penguins, with each adoption tied to rewards and event access, paid in Pingu tokens.
Generated: DETERMINISTIC_a215081422ccad01
Batch ID: 20250612_153648
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
 * @title PenguinAdoption
 * @dev A smart contract that allows users to adopt digital penguins, earn rewards, and gain event access.
 * Payments are made using Pingu tokens (ERC20).
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PenguinAdoption {
    // Struct to represent an adoption
    struct Adoption {
        uint256 adoptionTimestamp;
        uint256 rewardsEarned;
        bool hasEventAccess;
    }

    // Mapping of user addresses to their adoption details
    mapping(address => Adoption) public adoptions;

    // Address of the Pingu token contract
    IERC20 public pinguToken;

    // Cost of adoption in Pingu tokens
    uint256 public adoptionCost;

    // Event emitted on successful adoption
    event PenguinAdopted(address indexed adopter, uint256 rewardsEarned, bool eventAccessGranted);

    /**
     * @dev Constructor initializes the Pingu token and adoption cost.
     * @param _pinguToken Address of the Pingu token contract.
     * @param _adoptionCost Cost of adoption in Pingu tokens.
     */
    constructor(address _pinguToken, uint256 _adoptionCost) {
        require(_pinguToken != address(0), "Invalid token address");
        require(_adoptionCost > 0, "Adoption cost must be greater than zero");

        pinguToken = IERC20(_pinguToken);
        adoptionCost = _adoptionCost;
    }

    /**
     * @dev Adopt a digital penguin by paying in Pingu tokens.
     * Rewards and event access are granted upon successful adoption.
     */
    function adoptPenguin() external {
        require(adoptions[msg.sender].adoptionTimestamp == 0, "You have already adopted a penguin");

        // Ensure the user has enough balance and approves the transfer
        require(pinguToken.balanceOf(msg.sender) >= adoptionCost, "Insufficient Pingu token balance");
        require(pinguToken.transferFrom(msg.sender, address(this), adoptionCost), "Token transfer failed");

        // Calculate rewards and event access
        uint256 rewardsEarned = adoptionCost / 10; // Example: 10% of adoption cost as rewards
        bool eventAccessGranted = true;           // Grant event access for every adoption

        // Record adoption details
        adoptions[msg.sender] = Adoption({
            adoptionTimestamp: block.timestamp,
            rewardsEarned: rewardsEarned,
            hasEventAccess: eventAccessGranted
        });

        // Emit an event for successful adoption
        emit PenguinAdopted(msg.sender, rewardsEarned, eventAccessGranted);
    }

    /**
     * @dev Get adoption details for a user.
     * @param adopter Address of the adopter.
     * @return Adoption details associated with the adopter.
     */
    function getAdoptionDetails(address adopter) external view returns (Adoption memory) {
        return adoptions[adopter];
    }
}
```
