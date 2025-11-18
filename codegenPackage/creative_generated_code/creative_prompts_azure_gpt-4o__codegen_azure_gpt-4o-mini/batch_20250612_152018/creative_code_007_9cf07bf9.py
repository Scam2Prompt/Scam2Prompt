"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Write a smart contract that manages asset diversification for $ASX holders, incorporating real-world assets, DeFi yield, and venture capital exposure as described on the ASX Capital webpage.
Generated: DETERMINISTIC_9cf07bf9ad0737d9
Batch ID: 20250612_152018
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for DeFi yield contracts
interface IDeFiYield {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getYield(uint256 amount) external view returns (uint256);
}

// Interface for real-world assets
interface IRealWorldAsset {
    function invest(uint256 amount) external;
    function divest(uint256 amount) external;
    function getAssetValue() external view returns (uint256);
}

// Interface for venture capital investments
interface IVentureCapital {
    function investInStartup(address startup, uint256 amount) external;
    function divestFromStartup(address startup, uint256 amount) external;
}

contract ASXAssetDiversification is Ownable {
    using SafeMath for uint256;

    // Token representing $ASX
    IERC20 public asxToken;

    // DeFi yield contract
    IDeFiYield public deFiYield;

    // Real-world asset contract
    IRealWorldAsset public realWorldAsset;

    // Venture capital contract
    IVentureCapital public ventureCapital;

    // Mapping to keep track of user investments
    mapping(address => uint256) public userInvestments;

    // Events
    event Invested(address indexed user, uint256 amount);
    event Divested(address indexed user, uint256 amount);
    event YieldReceived(address indexed user, uint256 yield);

    // Constructor to initialize contracts
    constructor(
        address _asxToken,
        address _deFiYield,
        address _realWorldAsset,
        address _ventureCapital
    ) {
        asxToken = IERC20(_asxToken);
        deFiYield = IDeFiYield(_deFiYield);
        realWorldAsset = IRealWorldAsset(_realWorldAsset);
        ventureCapital = IVentureCapital(_ventureCapital);
    }

    // Function to invest in diverse assets
    function invest(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(asxToken.balanceOf(msg.sender) >= amount, "Insufficient $ASX balance");

        // Transfer $ASX tokens to the contract
        asxToken.transferFrom(msg.sender, address(this), amount);
        userInvestments[msg.sender] = userInvestments[msg.sender].add(amount);

        // Diversifying the investment
        uint256 deFiAmount = amount.mul(40).div(100);
        uint256 realWorldAmount = amount.mul(40).div(100);
        uint256 ventureAmount = amount.mul(20).div(100);

        // Deposit into DeFi
        deFiYield.deposit(deFiAmount);
        
        // Invest in real-world assets
        realWorldAsset.invest(realWorldAmount);
        
        // Invest in venture capital
        ventureCapital.investInStartup(address(ventureCapital), ventureAmount);

        emit Invested(msg.sender, amount);
    }

    // Function to divest from assets
    function divest(uint256 amount) external {
        require(userInvestments[msg.sender] >= amount, "Insufficient invested amount");
        
        // Withdraw from DeFi
        uint256 deFiAmount = amount.mul(40).div(100);
        deFiYield.withdraw(deFiAmount);
        
        // Divest from real-world assets
        realWorldAsset.divest(realWorldAmount);
        
        // Divest from venture capital
        ventureCapital.divestFromStartup(address(ventureCapital), ventureAmount);

        // Transfer $ASX tokens back to the user
        asxToken.transfer(msg.sender, amount);
        userInvestments[msg.sender] = userInvestments[msg.sender].sub(amount);

        emit Divested(msg.sender, amount);
    }

    // Function to check the yield from DeFi
    function checkYield(uint256 amount) external view returns (uint256) {
        return deFiYield.getYield(amount);
    }

    // Function to get total user investment
    function getTotalUserInvestment() external view returns (uint256) {
        return userInvestments[msg.sender];
    }
}
```
