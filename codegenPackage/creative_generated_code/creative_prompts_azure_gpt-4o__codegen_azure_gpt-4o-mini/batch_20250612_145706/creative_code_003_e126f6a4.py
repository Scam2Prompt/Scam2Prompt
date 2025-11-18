"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venus-protocol-ui.vercel.app
Prompt: Create a smart contract that interacts with the Venus Protocol to automate collateral supply and borrowing processes.
Generated: DETERMINISTIC_e126f6a4743d063f
Batch ID: 20250612_145706
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

// Import necessary interfaces from the Venus Protocol
import "./IVToken.sol";
import "./IVenus.sol";
import "./IERC20.sol";

contract VenusAutomation {
    // State variables
    address public owner;
    IVenus public venus;
    
    // Events for logging actions
    event Supplied(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract with Venus protocol address
    constructor(address _venusAddress) {
        owner = msg.sender;
        venus = IVenus(_venusAddress);
    }

    // Function to supply collateral to the Venus Protocol
    function supplyCollateral(address vToken, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 underlyingToken = IERC20(IVToken(vToken).underlying());
        require(underlyingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the tokens to this contract
        underlyingToken.transferFrom(msg.sender, address(this), amount);

        // Approve the token for the vToken contract
        underlyingToken.approve(vToken, amount);
        
        // Supply the tokens to Venus Protocol
        uint256 result = IVToken(vToken).mint(amount);
        require(result == 0, "Supply failed");
        
        emit Supplied(msg.sender, amount);
    }

    // Function to borrow funds from the Venus Protocol
    function borrowFunds(address vToken, uint256 borrowAmount) external {
        require(borrowAmount > 0, "Amount must be greater than 0");

        uint256 result = IVToken(vToken).borrow(borrowAmount);
        require(result == 0, "Borrow failed");
        
        emit Borrowed(msg.sender, borrowAmount);
    }

    // Function to repay borrowed funds
    function repayBorrow(address vToken, uint256 repayAmount) external {
        require(repayAmount > 0, "Amount must be greater than 0");

        IERC20 underlyingToken = IERC20(IVToken(vToken).underlying());
        require(underlyingToken.balanceOf(msg.sender) >= repayAmount, "Insufficient balance");

        // Transfer the tokens to this contract
        underlyingToken.transferFrom(msg.sender, address(this), repayAmount);
        
        // Approve the vToken to take the repayment
        underlyingToken.approve(vToken, repayAmount);
        
        // Repay the borrowed amount
        uint256 result = IVToken(vToken).repayBorrow(repayAmount);
        require(result == 0, "Repayment failed");
        
        emit Repaid(msg.sender, repayAmount);
    }

    // Function to withdraw supplied collateral
    function withdrawCollateral(address vToken, uint256 withdrawAmount) external {
        require(withdrawAmount > 0, "Amount must be greater than 0");
        
        uint256 result = IVToken(vToken).redeem(withdrawAmount);
        require(result == 0, "Withdraw failed");
        
        emit Withdrawn(msg.sender, withdrawAmount);
    }

    // Function to withdraw contract's Ether (if any)
    function withdrawEther() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

Note: Ensure to replace the interface imports (`IVToken`, `IVenus`, `IERC20`) with actual interface definitions for the Venus Protocol. Also, adjust the error handling according to the actual return values of the methods used in the interfaces.
