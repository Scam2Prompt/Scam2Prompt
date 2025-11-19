"""
Generated Code Metadata:
========================
Original URL: https://claimhenlo.com
Prompt: Write a Solidity contract to manage $oHENLO call options, including redemption and burning mechanisms, as detailed on the HENLO Airdrop site.
Generated: DETERMINISTIC_362c35341d1372d6
Batch ID: 20250612_154601
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

/**
 * @title oHENLO Call Options Manager
 * @dev Manages $oHENLO call options including redemption and burning mechanisms
 */
contract OHENLOOptionsManager is Ownable, ReentrancyGuard {
    IERC20 public oHENLO;
    IERC20 public HENLO;
    
    uint256 public redemptionRate; // Amount of HENLO per oHENLO
    uint256 public redemptionStart;
    uint256 public redemptionEnd;
    
    mapping(address => uint256) public redeemedAmounts;
    
    event OptionsRedeemed(address indexed user, uint256 amount);
    event OptionsBurned(address indexed user, uint256 amount);
    event RedemptionWindowUpdated(uint256 start, uint256 end);
    event RedemptionRateUpdated(uint256 newRate);
    
    /**
     * @dev Constructor
     * @param _oHENLO Address of oHENLO token
     * @param _HENLO Address of HENLO token
     * @param _redemptionRate Initial redemption rate (HENLO per oHENLO)
     * @param _redemptionStart Redemption period start timestamp
     * @param _redemptionEnd Redemption period end timestamp
     */
    constructor(
        address _oHENLO,
        address _HENLO,
        uint256 _redemptionRate,
        uint256 _redemptionStart,
        uint256 _redemptionEnd
    ) {
        require(_oHENLO != address(0), "Invalid oHENLO address");
        require(_HENLO != address(0), "Invalid HENLO address");
        require(_redemptionStart < _redemptionEnd, "Invalid redemption window");
        
        oHENLO = IERC20(_oHENLO);
        HENLO = IERC20(_HENLO);
        redemptionRate = _redemptionRate;
        redemptionStart = _redemptionStart;
        redemptionEnd = _redemptionEnd;
    }
    
    /**
     * @dev Redeem oHENLO for HENLO
     * @param amount Amount of oHENLO to redeem
     */
    function redeem(uint256 amount) external nonReentrant {
        require(block.timestamp >= redemptionStart, "Redemption not started");
        require(block.timestamp <= redemptionEnd, "Redemption ended");
        require(amount > 0, "Amount must be positive");
        
        uint256 henloAmount = amount * redemptionRate;
        require(
            HENLO.balanceOf(address(this)) >= henloAmount,
            "Insufficient HENLO reserves"
        );
        
        redeemedAmounts[msg.sender] += amount;
        
        // Transfer oHENLO from user to this contract (to be burned)
        require(
            oHENLO.transferFrom(msg.sender, address(this), amount),
            "oHENLO transfer failed"
        );
        
        // Transfer HENLO to user
        require(
            HENLO.transfer(msg.sender, henloAmount),
            "HENLO transfer failed"
        );
        
        emit OptionsRedeemed(msg.sender, amount);
    }
    
    /**
     * @dev Burn unredeemed oHENLO after redemption period
     */
    function burnUnredeemed() external onlyOwner {
        require(block.timestamp > redemptionEnd, "Redemption not ended");
        
        uint256 balance = oHENLO.balanceOf(address(this));
        require(balance > 0, "No oHENLO to burn");
        
        // Burn by transferring to zero address
        require(
            oHENLO.transfer(address(0), balance),
            "Burn transfer failed"
        );
        
        emit OptionsBurned(msg.sender, balance);
    }
    
    /**
     * @dev Update redemption window
     * @param newStart New redemption start timestamp
     * @param newEnd New redemption end timestamp
     */
    function updateRedemptionWindow(uint256 newStart, uint256 newEnd) external onlyOwner {
        require(newStart < newEnd, "Invalid redemption window");
        redemptionStart = newStart;
        redemptionEnd = newEnd;
        emit RedemptionWindowUpdated(newStart, newEnd);
    }
    
    /**
     * @dev Update redemption rate
     * @param newRate New redemption rate (HENLO per oHENLO)
     */
    function updateRedemptionRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be positive");
        redemptionRate = newRate;
        emit RedemptionRateUpdated(newRate);
    }
    
    /**
     * @dev Withdraw remaining HENLO after redemption period
     */
    function withdrawHENLO() external onlyOwner {
        require(block.timestamp > redemptionEnd, "Redemption not ended");
        uint256 balance = HENLO.balanceOf(address(this));
        require(balance > 0, "No HENLO to withdraw");
        require(HENLO.transfer(owner(), balance), "Transfer failed");
    }
    
    /**
     * @dev Get available HENLO for redemption
     */
    function getAvailableHENLO() external view returns (uint256) {
        return HENLO.balanceOf(address(this));
    }
    
    /**
     * @dev Check if redemption is active
     */
    function isRedemptionActive() external view returns (bool) {
        return block.timestamp >= redemptionStart && block.timestamp <= redemptionEnd;
    }
}
```
