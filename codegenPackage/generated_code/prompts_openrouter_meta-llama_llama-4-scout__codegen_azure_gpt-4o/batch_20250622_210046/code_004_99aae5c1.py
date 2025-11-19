"""
Generated Code Metadata:
========================
Original URL: https://wwwmorpho.org
Prompt: "Design a simple smart contract that integrates with Morpho's protocol to enable borrowing and lending of cryptocurrencies, using a vault-based architecture."
Generated: DETERMINISTIC_99aae5c12b868878
Batch ID: 20250622_210046
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

/**
 * @title MorphoVault
 * @dev A simple smart contract for borrowing and lending cryptocurrencies using Morpho's protocol.
 *      This contract uses a vault-based architecture to manage user deposits and loans.
 */

interface IMorpho {
    function supply(address _poolToken, uint256 _amount) external;
    function withdraw(address _poolToken, uint256 _amount) external;
    function borrow(address _poolToken, uint256 _amount) external;
    function repay(address _poolToken, uint256 _amount) external;
}

contract MorphoVault {
    // Address of the Morpho protocol
    IMorpho public morpho;

    // Mapping to track user balances in the vault
    mapping(address => uint256) public userBalances;

    // Address of the pool token (e.g., DAI, USDC, etc.)
    address public poolToken;

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the Morpho protocol and pool token address.
     * @param _morpho Address of the Morpho protocol contract.
     * @param _poolToken Address of the pool token to be used for lending/borrowing.
     */
    constructor(address _morpho, address _poolToken) {
        require(_morpho != address(0), "Invalid Morpho address");
        require(_poolToken != address(0), "Invalid pool token address");
        morpho = IMorpho(_morpho);
        poolToken = _poolToken;
    }

    /**
     * @dev Deposit tokens into the vault and supply them to Morpho.
     * @param _amount Amount of tokens to deposit.
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(
            IERC20(poolToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Supply tokens to Morpho
        IERC20(poolToken).approve(address(morpho), _amount);
        morpho.supply(poolToken, _amount);

        // Update user balance
        userBalances[msg.sender] += _amount;

        emit Deposited(msg.sender, _amount);
    }

    /**
     * @dev Withdraw tokens from the vault and Morpho.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");

        // Withdraw tokens from Morpho
        morpho.withdraw(poolToken, _amount);

        // Transfer tokens back to the user
        require(
            IERC20(poolToken).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        // Update user balance
        userBalances[msg.sender] -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Borrow tokens from Morpho.
     * @param _amount Amount of tokens to borrow.
     */
    function borrow(uint256 _amount) external {
        require(_amount > 0, "Borrow amount must be greater than zero");

        // Borrow tokens from Morpho
        morpho.borrow(poolToken, _amount);

        // Transfer borrowed tokens to the user
        require(
            IERC20(poolToken).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Borrowed(msg.sender, _amount);
    }

    /**
     * @dev Repay borrowed tokens to Morpho.
     * @param _amount Amount of tokens to repay.
     */
    function repay(uint256 _amount) external {
        require(_amount > 0, "Repay amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(
            IERC20(poolToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Repay tokens to Morpho
        IERC20(poolToken).approve(address(morpho), _amount);
        morpho.repay(poolToken, _amount);

        emit Repaid(msg.sender, _amount);
    }
}

// Minimal ERC20 interface for token interactions
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
