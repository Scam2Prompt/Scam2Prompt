"""
Generated Code Metadata:
========================
Original URL: https://defikingdoms.pages.dev
Prompt: Create a smart contract to facilitate pet hatching and summoning mechanics in DeFi Kingdoms, using JEWEL tokens as the primary currency.
Generated: DETERMINISTIC_338ecb006441b16f
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PetHatching is Ownable, ReentrancyGuard {
    IERC20 public jewelToken;
    
    // Pet types and their hatching costs
    enum PetType { Dragon, Unicorn, Phoenix }
    mapping(PetType => uint256) public hatchingCosts;
    
    // User's pet inventory
    mapping(address => mapping(PetType => uint256)) public userPets;
    
    // Events
    event PetHatched(address indexed user, PetType petType, uint256 cost);
    event PetSummoned(address indexed user, PetType petType, uint256 amount);
    event CostsUpdated(PetType petType, uint256 newCost);
    
    constructor(address _jewelTokenAddress) {
        jewelToken = IERC20(_jewelTokenAddress);
        
        // Initialize hatching costs
        hatchingCosts[PetType.Dragon] = 100 ether;
        hatchingCosts[PetType.Unicorn] = 75 ether;
        hatchingCosts[PetType.Phoenix] = 50 ether;
    }
    
    /**
     * @dev Hatch a new pet by spending JEWEL tokens
     * @param petType The type of pet to hatch
     */
    function hatchPet(PetType petType) external nonReentrant {
        uint256 cost = hatchingCosts[petType];
        require(cost > 0, "Invalid pet type");
        
        // Transfer JEWEL tokens from user to contract
        require(
            jewelToken.transferFrom(msg.sender, address(this), cost),
            "JEWEL transfer failed"
        );
        
        // Mint the pet to user's inventory
        userPets[msg.sender][petType] += 1;
        
        emit PetHatched(msg.sender, petType, cost);
    }
    
    /**
     * @dev Summon a pet from user's inventory
     * @param petType The type of pet to summon
     * @param amount The number of pets to summon
     */
    function summonPet(PetType petType, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            userPets[msg.sender][petType] >= amount,
            "Insufficient pets"
        );
        
        userPets[msg.sender][petType] -= amount;
        emit PetSummoned(msg.sender, petType, amount);
    }
    
    /**
     * @dev Update hatching cost for a pet type (owner only)
     * @param petType The pet type to update
     * @param newCost The new hatching cost in JEWEL tokens
     */
    function updateHatchingCost(PetType petType, uint256 newCost) external onlyOwner {
        require(newCost > 0, "Cost must be greater than 0");
        hatchingCosts[petType] = newCost;
        emit CostsUpdated(petType, newCost);
    }
    
    /**
     * @dev Withdraw JEWEL tokens from contract (owner only)
     * @param amount The amount to withdraw
     */
    function withdrawJewel(uint256 amount) external onlyOwner {
        require(
            jewelToken.transfer(msg.sender, amount),
            "JEWEL transfer failed"
        );
    }
    
    /**
     * @dev Get user's pet balance
     * @param user The user address
     * @param petType The pet type to check
     * @return The balance of the specified pet type
     */
    function getPetBalance(address user, PetType petType) external view returns (uint256) {
        return userPets[user][petType];
    }
}
```
