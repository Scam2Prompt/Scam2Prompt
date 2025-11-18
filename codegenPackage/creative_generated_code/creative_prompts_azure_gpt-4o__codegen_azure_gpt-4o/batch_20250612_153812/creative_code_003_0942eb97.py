"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assets-maple.finance
Prompt: Create a smart contract in Solidity that integrates with Maple Finance to automate lending USDC to the High Yield Secured Lending Pool.
Generated: DETERMINISTIC_0942eb975f42ee16
Batch ID: 20250612_153812
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

// Interfaces
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IMaplePool {
    function deposit(uint256 amount) external;
}

contract MapleLender {
    // Address of the USDC token contract
    IERC20 public immutable usdcToken;

    // Address of the Maple Finance High Yield Secured Lending Pool
    IMaplePool public immutable lendingPool;

    // Owner of the contract
    address public owner;

    // Events
    event DepositMade(address indexed depositor, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the USDC and lending pool addresses.
     * @param _usdcToken Address of the USDC token contract.
     * @param _lendingPool Address of the Maple Finance lending pool contract.
     */
    constructor(address _usdcToken, address _lendingPool) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_lendingPool != address(0), "Invalid lending pool address");

        usdcToken = IERC20(_usdcToken);
        lendingPool = IMaplePool(_lendingPool);
        owner = msg.sender;
    }

    /**
     * @dev Deposit USDC into the Maple Finance lending pool.
     * @param _amount Amount of USDC to deposit.
     */
    function depositToPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(usdcToken.balanceOf(msg.sender) >= _amount, "Insufficient USDC balance");

        // Transfer USDC from the owner to this contract
        bool transferred = usdcToken.transferFrom(msg.sender, address(this), _amount);
        require(transferred, "USDC transfer failed");

        // Approve the lending pool to spend USDC
        bool approved = usdcToken.approve(address(lendingPool), _amount);
        require(approved, "USDC approval failed");

        // Deposit USDC into the lending pool
        lendingPool.deposit(_amount);

        // Emit event
        emit DepositMade(msg.sender, _amount);
    }

    /**
     * @dev Transfer ownership of the contract to a new address.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");

        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}
```
