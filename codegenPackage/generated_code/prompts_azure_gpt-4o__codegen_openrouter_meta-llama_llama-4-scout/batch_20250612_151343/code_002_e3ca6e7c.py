"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: Generate a smart contract example that utilizes Gravity's omnichain intent protocol to manage yield-enabled unified balances across multiple chains.
Generated: DETERMINISTIC_e3ca6e7c2ee298dd
Batch ID: 20250612_151343
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Gravity Omnichain Yield Manager
 * @author [Your Name]
 * @notice This contract manages yield-enabled unified balances across multiple chains using Gravity's omnichain intent protocol.
 */
contract GravityOmnichainYieldManager is Ownable {
    using SafeMath for uint256;

    // Mapping of chain IDs to their respective yield strategies
    mapping(uint256 => YieldStrategy) public chainStrategies;

    // Mapping of user addresses to their unified balances
    mapping(address => UnifiedBalance) public userBalances;

    // Gravity's omnichain intent protocol interface
    IGravityOmnichainIntent public gravity;

    /**
     * @param _gravity Address of Gravity's omnichain intent protocol contract
     */
    constructor(address _gravity) public {
        require(_gravity != address(0), "Gravity address cannot be zero");
        gravity = IGravityOmnichainIntent(_gravity);
    }

    /**
     * @notice Add a new chain strategy
     * @param _chainId ID of the chain to add strategy for
     * @param _strategy Address of the yield strategy contract
     */
    function addChainStrategy(uint256 _chainId, address _strategy) public onlyOwner {
        require(_strategy != address(0), "Strategy address cannot be zero");
        chainStrategies[_chainId] = YieldStrategy(_strategy);
    }

    /**
     * @notice Update an existing chain strategy
     * @param _chainId ID of the chain to update strategy for
     * @param _strategy Address of the new yield strategy contract
     */
    function updateChainStrategy(uint256 _chainId, address _strategy) public onlyOwner {
        require(_strategy != address(0), "Strategy address cannot be zero");
        chainStrategies[_chainId] = YieldStrategy(_strategy);
    }

    /**
     * @notice Deposit funds into a chain's yield strategy
     * @param _chainId ID of the chain to deposit into
     * @param _amount Amount of funds to deposit
     */
    function deposit(uint256 _chainId, uint256 _amount) public {
        require(chainStrategies[_chainId] != YieldStrategy(address(0)), "Chain strategy not found");
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer funds from user to chain strategy
        IERC20 token = IERC20(chainStrategies[_chainId].token());
        require(token.transferFrom(msg.sender, address(chainStrategies[_chainId]), _amount), "Token transfer failed");

        // Update user's unified balance
        userBalances[msg.sender].balances[_chainId] = userBalances[msg.sender].balances[_chainId].add(_amount);
    }

    /**
     * @notice Withdraw funds from a chain's yield strategy
     * @param _chainId ID of the chain to withdraw from
     * @param _amount Amount of funds to withdraw
     */
    function withdraw(uint256 _chainId, uint256 _amount) public {
        require(chainStrategies[_chainId] != YieldStrategy(address(0)), "Chain strategy not found");
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender].balances[_chainId] >= _amount, "Insufficient balance");

        // Update user's unified balance
        userBalances[msg.sender].balances[_chainId] = userBalances[msg.sender].balances[_chainId].sub(_amount);

        // Transfer funds from chain strategy to user
        IERC20 token = IERC20(chainStrategies[_chainId].token());
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }

    /**
     * @notice Execute an omnichain intent to manage yield across multiple chains
     * @param _intent Intent data containing chain IDs and amounts to manage
     */
    function executeOmnichainIntent(bytes calldata _intent) public {
        // Validate intent data
        require(_intent.length > 0, "Intent data cannot be empty");

        // Execute intent using Gravity's omnichain intent protocol
        gravity.executeIntent(_intent);
    }

    /**
     * @notice Get a user's unified balance across all chains
     * @param _user Address of the user to retrieve balance for
     * @return Unified balance of the user
     */
    function getUnifiedBalance(address _user) public view returns (UnifiedBalance memory) {
        return userBalances[_user];
    }
}

/**
 * @title Yield Strategy Interface
 */
interface YieldStrategy {
    function token() external view returns (address);
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
}

/**
 * @title Unified Balance Struct
 */
struct UnifiedBalance {
    mapping(uint256 => uint256) balances;
}

/**
 * @title Gravity Omnichain Intent Protocol Interface
 */
interface IGravityOmnichainIntent {
    function executeIntent(bytes calldata _intent) external;
}
```
