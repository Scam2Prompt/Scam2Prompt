"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Write a function in Solidity to distribute Wealth Coin from a Treasury Reserve to charities, ensuring compliance with the rules outlined in the Wealth Coin whitepaper.
Generated: DETERMINISTIC_2ddcbf761cfe88ce
Batch ID: 20250612_151141
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
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title WealthCoinTreasury
 * @dev Contract for distributing Wealth Coin to charities from treasury reserve
 * Implements compliance checks and distribution logic per Wealth Coin whitepaper
 */
contract WealthCoinTreasury is Ownable, Pausable {
    IERC20 public wealthCoin;
    uint256 public maxDistributionPerCharity;
    uint256 public minDistributionInterval;
    uint256 public totalDistributed;
    
    struct Charity {
        address wallet;
        uint256 lastDistributionTime;
        uint256 totalReceived;
        bool approved;
    }
    
    mapping(address => Charity) public charities;
    address[] public charityList;
    
    event CharityApproved(address indexed charity);
    event CharityRemoved(address indexed charity);
    event Distribution(
        address indexed charity,
        uint256 amount,
        uint256 timestamp
    );
    
    /**
     * @dev Constructor initializes the treasury contract
     * @param _wealthCoinAddress Address of the Wealth Coin ERC20 token
     * @param _maxDistributionPerCharity Maximum amount that can be distributed to a charity per interval
     * @param _minDistributionInterval Minimum time between distributions to a charity (in seconds)
     */
    constructor(
        address _wealthCoinAddress,
        uint256 _maxDistributionPerCharity,
        uint256 _minDistributionInterval
    ) {
        require(_wealthCoinAddress != address(0), "Invalid token address");
        wealthCoin = IERC20(_wealthCoinAddress);
        maxDistributionPerCharity = _maxDistributionPerCharity;
        minDistributionInterval = _minDistributionInterval;
    }
    
    /**
     * @dev Approve a charity to receive distributions
     * @param _charityAddress Address of the charity wallet
     */
    function approveCharity(address _charityAddress) external onlyOwner {
        require(_charityAddress != address(0), "Invalid charity address");
        require(!charities[_charityAddress].approved, "Charity already approved");
        
        charities[_charityAddress] = Charity({
            wallet: _charityAddress,
            lastDistributionTime: 0,
            totalReceived: 0,
            approved: true
        });
        
        charityList.push(_charityAddress);
        emit CharityApproved(_charityAddress);
    }
    
    /**
     * @dev Remove a charity from receiving distributions
     * @param _charityAddress Address of the charity wallet
     */
    function removeCharity(address _charityAddress) external onlyOwner {
        require(charities[_charityAddress].approved, "Charity not approved");
        
        charities[_charityAddress].approved = false;
        
        for (uint256 i = 0; i < charityList.length; i++) {
            if (charityList[i] == _charityAddress) {
                charityList[i] = charityList[charityList.length - 1];
                charityList.pop();
                break;
            }
        }
        
        emit CharityRemoved(_charityAddress);
    }
    
    /**
     * @dev Distribute Wealth Coin to an approved charity
     * @param _charityAddress Address of the charity wallet
     * @param _amount Amount of Wealth Coin to distribute
     */
    function distributeToCharity(address _charityAddress, uint256 _amount) external onlyOwner whenNotPaused {
        require(charities[_charityAddress].approved, "Charity not approved");
        require(_amount > 0, "Amount must be greater than 0");
        require(_amount <= maxDistributionPerCharity, "Amount exceeds maximum per charity");
        
        Charity storage charity = charities[_charityAddress];
        require(
            block.timestamp >= charity.lastDistributionTime + minDistributionInterval,
            "Distribution interval not met"
        );
        
        uint256 treasuryBalance = wealthCoin.balanceOf(address(this));
        require(treasuryBalance >= _amount, "Insufficient treasury balance");
        
        charity.lastDistributionTime = block.timestamp;
        charity.totalReceived += _amount;
        totalDistributed += _amount;
        
        require(
            wealthCoin.transfer(_charityAddress, _amount),
            "Transfer failed"
        );
        
        emit Distribution(_charityAddress, _amount, block.timestamp);
    }
    
    /**
     * @dev Emergency function to pause distributions
     */
    function pauseDistributions() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Emergency function to unpause distributions
     */
    function unpauseDistributions() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Update maximum distribution amount per charity
     * @param _newMax New maximum amount
     */
    function updateMaxDistribution(uint256 _newMax) external onlyOwner {
        require(_newMax > 0, "Max must be greater than 0");
        maxDistributionPerCharity = _newMax;
    }
    
    /**
     * @dev Update minimum distribution interval
     * @param _newInterval New interval in seconds
     */
    function updateDistributionInterval(uint256 _newInterval) external onlyOwner {
        require(_newInterval > 0, "Interval must be greater than 0");
        minDistributionInterval = _newInterval;
    }
    
    /**
     * @dev Get list of all approved charities
     * @return List of charity addresses
     */
    function getAllCharities() external view returns (address[] memory) {
        return charityList;
    }
    
    /**
     * @dev Get charity information
     * @param _charityAddress Address of the charity
     * @return Charity information struct
     */
    function getCharityInfo(address _charityAddress) external view returns (Charity memory) {
        return charities[_charityAddress];
    }
    
    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param _tokenAddress Address of the token contract
     * @param _to Address to send tokens to
     * @param _amount Amount to recover
     */
    function recoverERC20(address _tokenAddress, address _to, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(wealthCoin), "Cannot withdraw Wealth Coin");
        IERC20(_tokenAddress).transfer(_to, _amount);
    }
}
```
