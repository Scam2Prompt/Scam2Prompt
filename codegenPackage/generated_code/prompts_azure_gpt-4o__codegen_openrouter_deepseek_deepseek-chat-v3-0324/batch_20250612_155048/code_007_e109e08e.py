"""
Generated Code Metadata:
========================
Original URL: https://pythim.com
Prompt: Write a Solidity smart contract that incorporates Pythim's price feed oracles to calculate the value of a portfolio in real-time.
Generated: DETERMINISTIC_e109e08e456ec348
Batch ID: 20250612_155048
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract PortfolioValuation {
    IPyth public pyth;
    
    struct Asset {
        bytes32 priceId;
        uint256 amount;
    }
    
    mapping(address => Asset[]) public userPortfolios;
    
    event PortfolioValueUpdated(address indexed user, uint256 value);
    event AssetAdded(address indexed user, bytes32 priceId, uint256 amount);
    
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }
    
    function addAsset(bytes32 _priceId, uint256 _amount) external {
        require(_priceId != bytes32(0), "Invalid price ID");
        require(_amount > 0, "Amount must be positive");
        
        userPortfolios[msg.sender].push(Asset({
            priceId: _priceId,
            amount: _amount
        }));
        
        emit AssetAdded(msg.sender, _priceId, _amount);
    }
    
    function getPortfolioValue(bytes[] calldata _priceUpdateData) external payable returns (uint256) {
        require(_priceUpdateData.length > 0, "No price update data provided");
        
        // Update prices (this will charge a fee)
        uint fee = pyth.getUpdateFee(_priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        pyth.updatePriceFeeds{value: fee}(_priceUpdateData);
        
        uint256 totalValue = 0;
        Asset[] storage portfolio = userPortfolios[msg.sender];
        
        for (uint i = 0; i < portfolio.length; i++) {
            Asset storage asset = portfolio[i];
            PythStructs.Price memory price = pyth.getPrice(asset.priceId);
            
            // Convert price to 18 decimals and multiply by amount
            uint256 priceInWei = uint256(uint64(price.price)) * 10 ** (18 - price.expo);
            uint256 assetValue = (priceInWei * asset.amount) / 10 ** 18;
            
            totalValue += assetValue;
        }
        
        emit PortfolioValueUpdated(msg.sender, totalValue);
        return totalValue;
    }
    
    function getPortfolioLength(address _user) external view returns (uint256) {
        return userPortfolios[_user].length;
    }
    
    function getAssetDetails(address _user, uint256 _index) external view returns (bytes32, uint256) {
        require(_index < userPortfolios[_user].length, "Index out of bounds");
        Asset storage asset = userPortfolios[_user][_index];
        return (asset.priceId, asset.amount);
    }
    
    // Allow contract to receive refunds for unused update fees
    receive() external payable {}
}
```
