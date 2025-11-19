"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Write a code snippet for a decentralized application that allows users to stake QI tokens and manage collateral for MAI issuance.
Generated: DETERMINISTIC_bf49b63286fecc68
Batch ID: 20250612_162431
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the MAI token
interface IMAIToken {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// Main contract for staking QI tokens and managing collateral for MAI issuance
contract QIStaking is Ownable {
    // State variables
    IERC20 public qiToken; // QI token contract
    IMAIToken public maiToken; // MAI token contract

    struct Stake {
        uint256 amount; // Amount of QI tokens staked
        uint256 collateral; // Amount of collateral for MAI issuance
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event CollateralUpdated(address indexed user, uint256 newCollateral);
    event MAIMinted(address indexed user, uint256 amount);

    // Constructor to initialize the contract with QI and MAI token addresses
    constructor(address _qiToken, address _maiToken) {
        require(_qiToken != address(0), "Invalid QI token address");
        require(_maiToken != address(0), "Invalid MAI token address");
        qiToken = IERC20(_qiToken);
        maiToken = IMAIToken(_maiToken);
    }

    // Function to stake QI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(qiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender].amount += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake QI tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        stakes[msg.sender].amount -= amount;
        require(qiToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to manage collateral for MAI issuance
    function manageCollateral(uint256 collateralAmount) external {
        require(collateralAmount >= 0, "Collateral amount cannot be negative");
        stakes[msg.sender].collateral = collateralAmount;

        emit CollateralUpdated(msg.sender, collateralAmount);
    }

    // Function to mint MAI tokens based on collateral
    function mintMAI(uint256 amount) external {
        require(stakes[msg.sender].collateral >= amount, "Insufficient collateral");
        maiToken.mint(msg.sender, amount);

        emit MAIMinted(msg.sender, amount);
    }

    // Function to burn MAI tokens and release collateral
    function burnMAI(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        maiToken.burn(msg.sender, amount);
        stakes[msg.sender].collateral -= amount;

        emit CollateralUpdated(msg.sender, stakes[msg.sender].collateral);
    }
}
```
