"""
Generated Code Metadata:
========================
Original URL: https://buy-dogepreneur.pages.dev
Prompt: Generate a smart contract code in Solidity that enables the creation and management of RWA Tokens, like Dogepreneur, for real estate investment and rental income generation on a blockchain platform.
Generated: DETERMINISTIC_9436f1ee2293700b
Batch ID: 20250622_204615
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RWAToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct Property {
        string name;
        string location;
        uint256 value;
        uint256 rentalIncome;
        uint256 tokenizedPercentage;
        bool isActive;
    }

    struct Investment {
        address investor;
        uint256 propertyId;
        uint256 amount;
        uint256 timestamp;
    }

    mapping(uint256 => Property) public properties;
    mapping(address => mapping(uint256 => uint256)) public investorShares;
    mapping(uint256 => Investment[]) public propertyInvestments;
    mapping(address => uint256[]) public investorProperties;

    uint256 public propertyCount;
    uint256 public totalTokenizedValue;
    uint256 public constant MIN_INVESTMENT = 0.01 ether;

    event PropertyAdded(uint256 indexed propertyId, string name, string location, uint256 value);
    event PropertyTokenized(uint256 indexed propertyId, uint256 percentage);
    event InvestmentMade(address indexed investor, uint256 indexed propertyId, uint256 amount);
    event RentalIncomeDistributed(uint256 indexed propertyId, uint256 amount);
    event PropertyDeactivated(uint256 indexed propertyId);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        propertyCount = 0;
        totalTokenizedValue = 0;
    }

    function addProperty(
        string memory _name,
        string memory _location,
        uint256 _value,
        uint256 _rentalIncome
    ) external onlyOwner {
        require(_value > 0, "Property value must be greater than zero");
        require(_rentalIncome > 0, "Rental income must be greater than zero");

        propertyCount++;
        properties[propertyCount] = Property({
            name: _name,
            location: _location,
            value: _value,
            rentalIncome: _rentalIncome,
            tokenizedPercentage: 0,
            isActive: true
        });

        emit PropertyAdded(propertyCount, _name, _location, _value);
    }

    function tokenizeProperty(uint256 _propertyId, uint256 _percentage) external onlyOwner {
        require(_propertyId > 0 && _propertyId <= propertyCount, "Invalid property ID");
        require(properties[_propertyId].isActive, "Property is not active");
        require(_percentage > 0 && _percentage <= 100, "Percentage must be between 1 and 100");

        Property storage property = properties[_propertyId];
        require(property.tokenizedPercentage.add(_percentage) <= 100, "Total tokenization cannot exceed 100%");

        uint256 tokenAmount = property.value.mul(_percentage).div(100);
        _mint(address(this), tokenAmount);

        property.tokenizedPercentage = property.tokenizedPercentage.add(_percentage);
        totalTokenizedValue = totalTokenizedValue.add(tokenAmount);

        emit PropertyTokenized(_propertyId, _percentage);
    }

    function investInProperty(uint256 _propertyId) external payable whenNotPaused {
        require(_propertyId > 0 && _propertyId <= propertyCount, "Invalid property ID");
        require(properties[_propertyId].isActive, "Property is not active");
        require(msg.value >= MIN_INVESTMENT, "Investment amount below minimum");
        require(properties[_propertyId].tokenizedPercentage > 0, "Property not tokenized");

        Property storage property = properties[_propertyId];
        uint256 investorShare = msg.value.mul(100).div(property.value);
        require(investorShare <= 100.sub(property.tokenizedPercentage), "Investment exceeds available tokenization");

        investorShares[msg.sender][_propertyId] = investorShares[msg.sender][_propertyId].add(investorShare);
        propertyInvestments[_propertyId].push(Investment(msg.sender, _propertyId, msg.value, block.timestamp));
        investorProperties[msg.sender].push(_propertyId);

        emit InvestmentMade(msg.sender, _propertyId, msg.value);
    }

    function distributeRentalIncome(uint256 _propertyId) external onlyOwner {
        require(_propertyId > 0 && _propertyId <= propertyCount, "Invalid property ID");
        Property storage property = properties[_propertyId];
        require(property.isActive, "Property is not active");
        require(property.tokenizedPercentage > 0, "Property not tokenized");

        uint256 totalIncome = property.rentalIncome;
        uint256 distributableIncome = totalIncome.mul(property.tokenizedPercentage).div(100);

        for (uint256 i = 0; i < propertyInvestments[_propertyId].length; i++) {
            Investment memory investment = propertyInvestments[_propertyId][i];
            uint256 share = investorShares[investment.investor][_propertyId];
            uint256 incomeShare = distributableIncome.mul(share).div(property.tokenizedPercentage);
            
            if (incomeShare > 0) {
                payable(investment.investor).transfer(incomeShare);
            }
        }

        emit RentalIncomeDistributed(_propertyId, distributableIncome);
    }

    function deactivateProperty(uint256 _propertyId) external onlyOwner {
        require(_propertyId > 0 && _propertyId <= propertyCount, "Invalid property ID");
        require(properties[_propertyId].isActive, "Property already deactivated");

        properties[_propertyId].isActive = false;
        emit PropertyDeactivated(_propertyId);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function getInvestorProperties(address _investor) external view returns (uint256[] memory) {
        return investorProperties[_investor];
    }

    function getPropertyInvestments(uint256 _propertyId) external view returns (Investment[] memory) {
        return propertyInvestments[_propertyId];
    }
}
```
