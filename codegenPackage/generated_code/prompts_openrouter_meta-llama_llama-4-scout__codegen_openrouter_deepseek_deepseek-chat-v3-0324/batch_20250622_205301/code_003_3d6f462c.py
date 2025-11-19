"""
Generated Code Metadata:
========================
Original URL: https://taiyoil.web.app
Prompt: Design a simple smart contract using Solidity to manage the minting and distribution of Taiyo Oil, including the logic for rewarding Taiyo Pilots based on oil purchased.
Generated: DETERMINISTIC_3d6f462cc407f9d4
Batch ID: 20250622_205301
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract TaiyoOil is ERC20, Ownable, Pausable {
    // Mapping to track Taiyo Pilots and their reward percentages
    mapping(address => uint256) public pilotRewards;
    // Total reward percentage allocated to all pilots (basis points)
    uint256 public totalRewardPercentage;
    // Maximum reward percentage that can be allocated (100% = 10000 basis points)
    uint256 public constant MAX_REWARD = 10000;

    // Events
    event PilotAdded(address indexed pilot, uint256 rewardPercentage);
    event PilotRemoved(address indexed pilot);
    event PilotRewardUpdated(address indexed pilot, uint256 newRewardPercentage);
    event OilPurchased(address indexed buyer, uint256 amount, uint256 pilotReward);

    constructor() ERC20("Taiyo Oil", "TAIYO") {
        // Initial supply: 1 million tokens with 18 decimals
        _mint(msg.sender, 1_000_000 * 10**decimals());
    }

    /**
     * @dev Add a new Taiyo Pilot with a reward percentage
     * @param pilot Address of the pilot
     * @param rewardPercentage Reward percentage in basis points (1% = 100)
     */
    function addPilot(address pilot, uint256 rewardPercentage) external onlyOwner {
        require(pilot != address(0), "Invalid address");
        require(rewardPercentage > 0, "Reward must be positive");
        require(totalRewardPercentage + rewardPercentage <= MAX_REWARD, "Exceeds max reward allocation");
        require(pilotRewards[pilot] == 0, "Pilot already exists");

        pilotRewards[pilot] = rewardPercentage;
        totalRewardPercentage += rewardPercentage;
        emit PilotAdded(pilot, rewardPercentage);
    }

    /**
     * @dev Remove a Taiyo Pilot
     * @param pilot Address of the pilot to remove
     */
    function removePilot(address pilot) external onlyOwner {
        require(pilotRewards[pilot] > 0, "Pilot does not exist");
        
        totalRewardPercentage -= pilotRewards[pilot];
        delete pilotRewards[pilot];
        emit PilotRemoved(pilot);
    }

    /**
     * @dev Update reward percentage for a Taiyo Pilot
     * @param pilot Address of the pilot
     * @param newRewardPercentage New reward percentage in basis points
     */
    function updatePilotReward(address pilot, uint256 newRewardPercentage) external onlyOwner {
        require(pilotRewards[pilot] > 0, "Pilot does not exist");
        require(newRewardPercentage > 0, "Reward must be positive");
        
        uint256 currentReward = pilotRewards[pilot];
        uint256 newTotal = totalRewardPercentage - currentReward + newRewardPercentage;
        require(newTotal <= MAX_REWARD, "Exceeds max reward allocation");

        totalRewardPercentage = newTotal;
        pilotRewards[pilot] = newRewardPercentage;
        emit PilotRewardUpdated(pilot, newRewardPercentage);
    }

    /**
     * @dev Purchase Taiyo Oil and distribute rewards to pilots
     * @param amount Amount of oil to purchase
     */
    function purchaseOil(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be positive");
        require(balanceOf(owner()) >= amount, "Insufficient oil supply");

        // Calculate and distribute rewards to pilots
        if (totalRewardPercentage > 0) {
            uint256 totalReward = (amount * totalRewardPercentage) / MAX_REWARD;
            uint256 remainingAmount = amount - totalReward;

            // Transfer the remaining amount to the owner
            _transfer(owner(), msg.sender, remainingAmount);

            // Distribute rewards to all pilots
            address[] memory pilots = _getActivePilots();
            for (uint256 i = 0; i < pilots.length; i++) {
                address pilot = pilots[i];
                uint256 pilotShare = (amount * pilotRewards[pilot]) / MAX_REWARD;
                _transfer(owner(), pilot, pilotShare);
            }
        } else {
            // No pilots to reward, transfer full amount
            _transfer(owner(), msg.sender, amount);
        }

        emit OilPurchased(msg.sender, amount, totalRewardPercentage);
    }

    /**
     * @dev Pause the contract to stop oil purchases
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract to resume oil purchases
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get list of active pilots
     * @return Array of active pilot addresses
     */
    function _getActivePilots() private view returns (address[] memory) {
        uint256 count = 0;
        uint256 totalPilots = 0;

        // First pass: count active pilots
        for (uint256 i = 0; i < _getPilotCount(); i++) {
            address pilot = _getPilotAtIndex(i);
            if (pilotRewards[pilot] > 0) {
                totalPilots++;
            }
        }

        // Second pass: populate array
        address[] memory pilots = new address[](totalPilots);
        for (uint256 i = 0; i < _getPilotCount(); i++) {
            address pilot = _getPilotAtIndex(i);
            if (pilotRewards[pilot] > 0) {
                pilots[count] = pilot;
                count++;
            }
        }

        return pilots;
    }

    /**
     * @dev Helper function to get total pilot count (including inactive)
     * Note: This is a simplified implementation. In production, you might want to maintain a separate array.
     */
    function _getPilotCount() private pure returns (uint256) {
        // In a real implementation, you would track pilots in an array
        // This is a placeholder - adjust based on your actual storage mechanism
        return 100; // Arbitrary limit for this example
    }

    /**
     * @dev Helper function to get pilot at index
     * Note: This is a simplified implementation. In production, you might want to maintain a separate array.
     */
    function _getPilotAtIndex(uint256) private pure returns (address) {
        // In a real implementation, you would return from a pilots array
        // This is a placeholder - adjust based on your actual storage mechanism
        return address(0);
    }
}
```
