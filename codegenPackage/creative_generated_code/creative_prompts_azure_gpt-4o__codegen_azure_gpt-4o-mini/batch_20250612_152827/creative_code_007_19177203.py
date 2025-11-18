"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity contract that allows users to lend $DAI, $USDC, or $WETH and earn yield, replicating the Vault functionality described in the Gains Network ecosystem.
Generated: DETERMINISTIC_1917720317c53e38
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract YieldVault is ReentrancyGuard, Ownable {
    // Supported tokens
    IERC20 public dai;
    IERC20 public usdc;
    IERC20 public weth;

    // User struct to track deposits and earnings
    struct UserInfo {
        uint256 amount; // Amount of tokens deposited
        uint256 rewardDebt; // Reward debt for calculating yield
    }

    // Mapping of user info by address
    mapping(address => UserInfo) public userInfo;

    // Total deposited amount
    uint256 public totalDeposits;

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount, address token);
    event Withdrawn(address indexed user, uint256 amount, address token);
    event YieldClaimed(address indexed user, uint256 amount);

    // Constructor to set the token addresses
    constructor(address _dai, address _usdc, address _weth) {
        dai = IERC20(_dai);
        usdc = IERC20(_usdc);
        weth = IERC20(_weth);
    }

    // Deposit function to lend tokens
    function deposit(uint256 _amount, address _token) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            _token == address(dai) || _token == address(usdc) || _token == address(weth),
            "Unsupported token"
        );

        // Transfer tokens from the user to the contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Update user information
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;

        totalDeposits += _amount;

        emit Deposited(msg.sender, _amount, _token);
    }

    // Withdraw function to redeem deposits
    function withdraw(uint256 _amount, address _token) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient balance");

        // Update user information
        user.amount -= _amount;
        totalDeposits -= _amount;

        // Transfer tokens back to the user
        IERC20(_token).transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount, _token);
    }

    // Claim yield (this is a placeholder)
    function claimYield() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 yield = calculateYield(msg.sender); // Placeholder for yield calculation
        require(yield > 0, "No yield to claim");

        user.rewardDebt += yield; // Track yield claimed

        // Logic to transfer yield (replace with actual yield token logic)
        // For simplicity, we're assuming the yield is in DAI
        dai.transfer(msg.sender, yield);

        emit YieldClaimed(msg.sender, yield);
    }

    // Placeholder function for yield calculation
    function calculateYield(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        // Implement the actual yield calculation logic here
        // For now, returning a fixed yield for simplicity
        return (user.amount * 5) / 100; // Example: 5% yield
    }

    // Allow owner to withdraw tokens from the contract
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
