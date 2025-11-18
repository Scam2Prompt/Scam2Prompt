"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yearn-in.pages.dev
Prompt: Develop a smart contract that interacts with Yearn's yPrisma vault to automate deposits and track yield performance.
Generated: DETERMINISTIC_88de0e1e85fbb012
Batch ID: 20250612_151117
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

// Interface for Yearn's yPrisma vault
interface IYearnVault {
    function deposit(uint256 amount) external returns (uint256);
    function withdraw(uint256 shares) external returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract YPrismaVaultManager is Ownable {
    using SafeMath for uint256;
    
    // Address of the Yearn yPrisma vault
    address public vaultAddress;
    IYearnVault private yearnVault;

    // Event for logging deposits
    event Deposited(address indexed user, uint256 amount);
    
    // Event for logging withdrawals
    event Withdrawn(address indexed user, uint256 amount);
    
    // Constructor to initialize the smart contract with the vault address
    constructor(address _vaultAddress) {
        require(_vaultAddress != address(0), "Invalid vault address");
        vaultAddress = _vaultAddress;
        yearnVault = IYearnVault(vaultAddress);
    }

    // Deposit tokens into the Yearn vault
    function deposit(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the owner to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Approve the vault to spend the tokens
        IERC20(token).approve(vaultAddress, amount);
        
        // Deposit tokens into the Yearn vault
        uint256 shares = yearnVault.deposit(amount);
        emit Deposited(msg.sender, shares);
    }

    // Withdraw tokens from the Yearn vault
    function withdraw(uint256 shares) external onlyOwner {
        require(shares > 0, "Shares must be greater than 0");

        // Withdraw tokens from the vault
        uint256 amount = yearnVault.withdraw(shares);
        emit Withdrawn(msg.sender, amount);
        
        // Transfer withdrawn tokens back to the owner
        address token = vaultAddress; // Assuming vaultAddress is also the token address
        IERC20(token).transfer(msg.sender, amount);
    }

    // Get the balance of the vault for the owner
    function getVaultBalance() external view returns (uint256) {
        return yearnVault.balanceOf(address(this));
    }

    // Allow the contract to receive ETH
    receive() external payable {}
}
```
