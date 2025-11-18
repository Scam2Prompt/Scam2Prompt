"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephantrewards.pages.dev
Prompt: Write a smart contract in Solidity for a lossless liquidity pool similar to Elephant Money Farms, ensuring deposited assets can be withdrawn without impermanent loss.
Generated: DETERMINISTIC_a17f1264985fbb0f
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's SafeERC20 for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A smart contract for a lossless liquidity pool
contract LosslessLiquidityPool is Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user deposit information
    struct UserInfo {
        uint256 amount; // Amount of tokens deposited
        uint256 depositTime; // Time of deposit
    }

    // Mapping to keep track of user deposits
    mapping(address => UserInfo) private userInfo;

    // Event emitted when a user deposits tokens
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // The token being managed by the pool
    IERC20 public token;

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        token = _token;
    }

    // Modifier to check if the user has deposited tokens
    modifier hasDeposited() {
        require(userInfo[msg.sender].amount > 0, "No tokens deposited");
        _;
    }

    // Function to allow users to deposit tokens into the liquidity pool
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the sender to this contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user deposit information
        userInfo[msg.sender].amount += _amount;
        userInfo[msg.sender].depositTime = block.timestamp;

        emit Deposited(msg.sender, _amount);
    }

    // Function to allow users to withdraw their deposited tokens without loss
    function withdraw(uint256 _amount) external hasDeposited {
        UserInfo storage user = userInfo[msg.sender];
        require(_amount <= user.amount, "Withdraw amount exceeds balance");

        // Update user balance before transferring tokens
        user.amount -= _amount;

        // Transfer tokens back to the user
        token.safeTransfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to allow the owner to withdraw any tokens accidentally sent to the contract
    function recoverTokens(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Cannot recover zero tokens");
        _token.safeTransfer(msg.sender, _amount);
    }

    // Function to check the balance of a user in the liquidity pool
    function balanceOf(address _user) external view returns (uint256) {
        return userInfo[_user].amount;
    }

    // Function to check the total balance of the liquidity pool
    function totalBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
