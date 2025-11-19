"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Write a tutorial for integrating ERC-20 compliant tenderized tokens into a DeFi lending protocol, allowing users to leverage their staked assets.
Generated: DETERMINISTIC_81ab68781f6eff0f
Batch ID: 20250612_145913
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the lending protocol
interface ILendingProtocol {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function borrow(address token, uint256 amount) external;
    function repay(address token, uint256 amount) external;
}

// ERC20TenderizedToken contract for integrating ERC-20 compliant tokens
contract ERC20TenderizedToken is Ownable {
    // State variables
    IERC20 public token; // The ERC20 token being tenderized
    ILendingProtocol public lendingProtocol; // The lending protocol to interact with

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    // Constructor to initialize the token and lending protocol
    constructor(address _token, address _lendingProtocol) {
        require(_token != address(0), "Invalid token address");
        require(_lendingProtocol != address(0), "Invalid lending protocol address");
        
        token = IERC20(_token);
        lendingProtocol = ILendingProtocol(_lendingProtocol);
    }

    // Function to deposit tokens into the lending protocol
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Approve the lending protocol to spend the tokens
        token.approve(address(lendingProtocol), amount);
        
        // Deposit tokens into the lending protocol
        lendingProtocol.deposit(address(token), amount);
        
        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the lending protocol
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw tokens from the lending protocol
        lendingProtocol.withdraw(address(token), amount);
        
        // Transfer tokens back to the owner
        token.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to borrow tokens from the lending protocol
    function borrow(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Borrow tokens from the lending protocol
        lendingProtocol.borrow(address(token), amount);
        
        // Transfer borrowed tokens to the owner
        token.transfer(msg.sender, amount);
        
        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed tokens to the lending protocol
    function repay(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the owner to this contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Approve the lending protocol to spend the tokens
        token.approve(address(lendingProtocol), amount);
        
        // Repay the borrowed tokens to the lending protocol
        lendingProtocol.repay(address(token), amount);
        
        emit Repaid(msg.sender, amount);
    }
}
```
