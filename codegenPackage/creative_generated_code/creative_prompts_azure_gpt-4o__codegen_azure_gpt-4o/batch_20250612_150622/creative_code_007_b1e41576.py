"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-route.pages.dev
Prompt: Write a Solidity contract that integrates with Morpho's peer-to-peer lending layer to optimize yield generation for OUSD stablecoin deposits.
Generated: DETERMINISTIC_b1e4157652c653f8
Batch ID: 20250612_150622
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

/**
 * @title YieldOptimizer
 * @dev A contract to integrate with Morpho's peer-to-peer lending layer for optimizing yield generation on OUSD deposits.
 *      This contract allows users to deposit OUSD and automatically optimizes yield using Morpho's protocol.
 */
interface IMorpho {
    function supply(address _poolToken, address _onBehalf, uint256 _amount) external;
    function withdraw(address _poolToken, uint256 _amount) external;
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract YieldOptimizer {
    // Address of Morpho's integration contract
    address public immutable morphoContract;

    // Address of OUSD token
    address public immutable ousdToken;

    // Address of the lending pool token (e.g., compound's cToken or Aave aToken)
    address public immutable poolToken;

    // Mapping to keep track of user balances
    mapping(address => uint256) public userBalances;

    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @notice Initializes the contract with the required addresses.
     * @param _morphoContract Address of the Morpho contract.
     * @param _ousdToken Address of the OUSD stablecoin token.
     * @param _poolToken Address of the lending pool token (e.g., cToken/aToken).
     */
    constructor(address _morphoContract, address _ousdToken, address _poolToken) {
        require(_morphoContract != address(0), "Invalid Morpho contract address");
        require(_ousdToken != address(0), "Invalid OUSD token address");
        require(_poolToken != address(0), "Invalid pool token address");

        morphoContract = _morphoContract;
        ousdToken = _ousdToken;
        poolToken = _poolToken;
    }

    /**
     * @notice Deposits OUSD into the contract and supplies it to Morpho for yield optimization.
     * @param _amount Amount of OUSD to deposit.
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than 0");

        // Transfer OUSD from user to contract
        IERC20(ousdToken).transferFrom(msg.sender, address(this), _amount);

        // Approve Morpho to spend OUSD
        IERC20(ousdToken).approve(morphoContract, _amount);

        // Supply OUSD to Morpho
        IMorpho(morphoContract).supply(poolToken, msg.sender, _amount);

        // Update user balance
        userBalances[msg.sender] += _amount;

        emit Deposited(msg.sender, _amount);
    }

    /**
     * @notice Withdraws OUSD from Morpho and returns it to the user.
     * @param _amount Amount of OUSD to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than 0");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");

        // Withdraw OUSD from Morpho
        IMorpho(morphoContract).withdraw(poolToken, _amount);

        // Transfer OUSD back to user
        IERC20(ousdToken).transfer(msg.sender, _amount);

        // Update user balance
        userBalances[msg.sender] -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @notice Returns the balance of OUSD deposited by a user.
     * @param _user Address of the user.
     * @return The balance of the user in OUSD.
     */
    function getUserBalance(address _user) external view returns (uint256) {
        return userBalances[_user];
    }
}
```
