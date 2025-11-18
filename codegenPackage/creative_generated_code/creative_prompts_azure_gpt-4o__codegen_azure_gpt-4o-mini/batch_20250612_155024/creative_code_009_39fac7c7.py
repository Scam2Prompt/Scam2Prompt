"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoststandart.ru
Prompt: Generate a Solidity smart contract that interacts with Belt Finance to automatically allocate funds into multiple liquidity pools based on user-defined risk preferences.
Generated: DETERMINISTIC_39fac7c785e98633
Batch ID: 20250612_155024
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Belt Finance
interface IBelt {
    function deposit(uint256 _amount, uint256 _pid) external;
    function withdraw(uint256 _amount, uint256 _pid) external;
}

contract AutoAllocator is Ownable {
    // State variables
    IBelt public beltContract; // Belt Finance contract address
    mapping(address => uint256[]) public userAllocations; // User allocations based on risk preferences
    mapping(address => uint256) public userBalances; // User balances in the contract

    // Event declarations
    event FundsAllocated(address indexed user, uint256 amount, uint256 pid);
    event FundsWithdrawn(address indexed user, uint256 amount, uint256 pid);

    // Constructor to initialize the Belt contract address
    constructor(address _beltAddress) {
        beltContract = IBelt(_beltAddress);
    }

    // Function to allocate funds into multiple liquidity pools
    function allocateFunds(address _token, uint256 _amount, uint256[] memory _pids) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_pids.length > 0, "No pool IDs provided");

        // Transfer tokens from user to the contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        userBalances[msg.sender] += _amount;

        // Distribute funds according to user-defined pool IDs
        uint256 totalPids = _pids.length;
        uint256 amountPerPool = _amount / totalPids;

        for (uint256 i = 0; i < totalPids; i++) {
            // Deposit funds into each specified liquidity pool
            beltContract.deposit(amountPerPool, _pids[i]);
            userAllocations[msg.sender].push(amountPerPool);
            emit FundsAllocated(msg.sender, amountPerPool, _pids[i]);
        }
    }

    // Function to withdraw funds from a specific liquidity pool
    function withdrawFunds(uint256 _pid, uint256 _amount) external {
        require(userBalances[msg.sender] >= _amount, "Insufficient balance to withdraw");

        // Withdraw funds from the specified liquidity pool
        beltContract.withdraw(_amount, _pid);
        userBalances[msg.sender] -= _amount;
        emit FundsWithdrawn(msg.sender, _amount, _pid);
    }

    // Function to check user balance
    function checkBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }

    // Function to recover ERC20 tokens in case of emergencies
    function recoverTokens(address _token) external onlyOwner {
        uint256 balance = IERC20(_token).balanceOf(address(this));
        require(balance > 0, "No tokens to recover");
        IERC20(_token).transfer(owner(), balance);
    }
}
```
