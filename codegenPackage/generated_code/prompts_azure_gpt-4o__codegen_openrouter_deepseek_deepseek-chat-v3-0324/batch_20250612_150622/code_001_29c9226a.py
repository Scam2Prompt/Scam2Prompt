"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Generate code to craft a weapon collectible using $BIGTIME tokens and materials, as described in Big Time's Forge system.
Generated: DETERMINISTIC_29c9226aca0c187b
Batch ID: 20250612_150622
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract WeaponForge is Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Token contract
    IERC20 public bigTimeToken;
    
    // Weapon structure
    struct Weapon {
        uint256 id;
        string name;
        uint256 power;
        uint256 rarity; // 1-5 (Common to Legendary)
        uint256 forgedAt;
        address owner;
    }
    
    // Material structure
    struct Material {
        uint256 id;
        string name;
        uint256 requiredAmount;
    }
    
    // Forge fee in $BIGTIME tokens
    uint256 public forgeFee;
    
    // Weapon counter
    Counters.Counter private _weaponCounter;
    
    // Materials mapping
    mapping(uint256 => Material) public materials;
    uint256 public materialCount;
    
    // Weapons mapping
    mapping(uint256 => Weapon) public weapons;
    mapping(address => uint256[]) public userWeapons;
    
    // Events
    event WeaponForged(uint256 indexed weaponId, address indexed owner, uint256 power, uint256 rarity);
    event MaterialAdded(uint256 indexed materialId, string name, uint256 requiredAmount);
    event ForgeFeeUpdated(uint256 newFee);
    
    constructor(address _bigTimeToken, uint256 _initialForgeFee) {
        require(_bigTimeToken != address(0), "Invalid token address");
        bigTimeToken = IERC20(_bigTimeToken);
        forgeFee = _initialForgeFee;
    }
    
    /**
     * @dev Add a new material type to the forge
     * @param _name Name of the material
     * @param _requiredAmount Amount needed to forge a weapon
     */
    function addMaterial(string memory _name, uint256 _requiredAmount) external onlyOwner {
        materialCount++;
        materials[materialCount] = Material({
            id: materialCount,
            name: _name,
            requiredAmount: _requiredAmount
        });
        emit MaterialAdded(materialCount, _name, _requiredAmount);
    }
    
    /**
     * @dev Update the forge fee
     * @param _newFee New forge fee in $BIGTIME tokens
     */
    function updateForgeFee(uint256 _newFee) external onlyOwner {
        require(_newFee > 0, "Fee must be greater than 0");
        forgeFee = _newFee;
        emit ForgeFeeUpdated(_newFee);
    }
    
    /**
     * @dev Forge a new weapon
     * @param _name Weapon name
     * @param _materialId ID of the material to use
     * @param _materialAmount Amount of material to use
     */
    function forgeWeapon(
        string memory _name,
        uint256 _materialId,
        uint256 _materialAmount
    ) external nonReentrant {
        require(_materialId > 0 && _materialId <= materialCount, "Invalid material ID");
        require(_materialAmount >= materials[_materialId].requiredAmount, "Insufficient material amount");
        
        // Transfer forge fee
        require(bigTimeToken.transferFrom(msg.sender, address(this), forgeFee), "Fee transfer failed");
        
        // Generate weapon stats based on material
        Material storage material = materials[_materialId];
        uint256 power = _calculatePower(material.requiredAmount);
        uint256 rarity = _calculateRarity(material.requiredAmount);
        
        // Create weapon
        _weaponCounter.increment();
        uint256 weaponId = _weaponCounter.current();
        
        weapons[weaponId] = Weapon({
            id: weaponId,
            name: _name,
            power: power,
            rarity: rarity,
            forgedAt: block.timestamp,
            owner: msg.sender
        });
        
        userWeapons[msg.sender].push(weaponId);
        
        emit WeaponForged(weaponId, msg.sender, power, rarity);
    }
    
    /**
     * @dev Calculate weapon power based on material amount
     */
    function _calculatePower(uint256 _materialAmount) internal pure returns (uint256) {
        return _materialAmount * 10 + (block.timestamp % 100);
    }
    
    /**
     * @dev Calculate weapon rarity based on material amount
     */
    function _calculateRarity(uint256 _materialAmount) internal pure returns (uint256) {
        if (_materialAmount >= 100) return 5; // Legendary
        if (_materialAmount >= 50) return 4;  // Epic
        if (_materialAmount >= 25) return 3;  // Rare
        if (_materialAmount >= 10) return 2;  // Uncommon
        return 1;                            // Common
    }
    
    /**
     * @dev Get weapons owned by a user
     * @param _user Address of the user
     */
    function getUserWeapons(address _user) external view returns (Weapon[] memory) {
        uint256[] storage weaponIds = userWeapons[_user];
        Weapon[] memory userWeaponsList = new Weapon[](weaponIds.length);
        
        for (uint256 i = 0; i < weaponIds.length; i++) {
            userWeaponsList[i] = weapons[weaponIds[i]];
        }
        
        return userWeaponsList;
    }
    
    /**
     * @dev Withdraw collected fees
     */
    function withdrawFees() external onlyOwner {
        uint256 balance = bigTimeToken.balanceOf(address(this));
        require(balance > 0, "No fees to withdraw");
        require(bigTimeToken.transfer(owner(), balance), "Withdrawal failed");
    }
}
```
