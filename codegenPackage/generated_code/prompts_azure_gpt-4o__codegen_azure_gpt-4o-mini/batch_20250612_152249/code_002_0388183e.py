"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbvuwd5kzejblzv323edzpb2o4gl4xvjm3d2ghg5fxtp4powdsxy.ipfs.dweb.link
Prompt: Create a smart contract in Solidity that integrates with Venus Protocol to automate lending and borrowing activities, leveraging Venus Prime for superior rates.
Generated: DETERMINISTIC_0388183edd2457f8
Batch ID: 20250612_152249
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

// Importing necessary interfaces from Venus Protocol
import "@venusprotocol/governance/contracts/interfaces/IVenus.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract VenusLending {
    // State variables
    IVenus public venus; // Venus Protocol interface
    IERC20 public collateralToken; // Token used as collateral
    address public owner; // Owner of the contract

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _venusAddress, address _collateralTokenAddress) {
        venus = IVenus(_venusAddress);
        collateralToken = IERC20(_collateralTokenAddress);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to deposit collateral into Venus Protocol
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer collateral tokens from user to this contract
        collateralToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve Venus to spend the collateral tokens
        collateralToken.approve(address(venus), amount);
        
        // Deposit collateral into Venus
        venus.mint(amount);
        
        emit Deposited(msg.sender, amount);
    }

    // Function to borrow assets from Venus Protocol
    function borrow(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Borrow the specified amount from Venus
        venus.borrow(amount);
        
        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed assets
    function repay(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the repayment amount from user to this contract
        IERC20(venus.getBorrowedToken()).transferFrom(msg.sender, address(this), amount);
        
        // Approve Venus to spend the repayment amount
        IERC20(venus.getBorrowedToken()).approve(address(venus), amount);
        
        // Repay the borrowed amount
        venus.repayBorrow(amount);
        
        emit Repaid(msg.sender, amount);
    }

    // Function to withdraw collateral from Venus Protocol
    function withdrawCollateral(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw collateral from Venus
        venus.redeem(amount);
        
        // Transfer collateral tokens back to the owner
        collateralToken.transfer(owner, amount);
        
        emit Withdrawn(owner, amount);
    }

    // Function to get the current collateral balance of the contract
    function getCollateralBalance() external view returns (uint256) {
        return collateralToken.balanceOf(address(this));
    }

    // Function to get the current borrowed balance of the contract
    function getBorrowedBalance() external view returns (uint256) {
        return venus.borrowBalanceCurrent(address(this));
    }
}
```
