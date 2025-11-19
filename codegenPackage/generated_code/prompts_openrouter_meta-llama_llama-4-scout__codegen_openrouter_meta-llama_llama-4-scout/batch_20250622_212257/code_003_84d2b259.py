"""
Generated Code Metadata:
========================
Original URL: https://swiftsdappchains.net
Prompt: Generate a Solidity code snippet for a token bridge solution to enable seamless transfers between different blockchain networks.
Generated: DETERMINISTIC_84d2b2598019acdc
Batch ID: 20250622_212257
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Token Bridge Contract
 * @author [Your Name]
 * @notice This contract enables seamless transfers of tokens between different blockchain networks.
 */
contract TokenBridge is ReentrancyGuard {
    // Mapping of token addresses to their respective bridge configurations
    mapping(address => BridgeConfig) public tokenConfigs;

    // Event emitted when a token is deposited
    event Deposit(address indexed token, address indexed sender, uint256 amount);

    // Event emitted when a token is withdrawn
    event Withdrawal(address indexed token, address indexed recipient, uint256 amount);

    // Event emitted when a token is locked on the source chain
    event TokenLocked(address indexed token, uint256 amount);

    // Event emitted when a token is unlocked on the destination chain
    event TokenUnlocked(address indexed token, uint256 amount);

    /**
     * @dev Struct representing a bridge configuration
     */
    struct BridgeConfig {
        address token;
        address counterpartyBridge;
        uint256 minTransferAmount;
        uint256 maxTransferAmount;
    }

    /**
     * @dev Function to add a new token configuration
     * @param _token Address of the token to configure
     * @param _counterpartyBridge Address of the counterparty bridge on the other chain
     * @param _minTransferAmount Minimum transfer amount
     * @param _maxTransferAmount Maximum transfer amount
     */
    function addTokenConfig(
        address _token,
        address _counterpartyBridge,
        uint256 _minTransferAmount,
        uint256 _maxTransferAmount
    ) public onlyOwner {
        require(_token != address(0), "Token address cannot be zero");
        require(_counterpartyBridge != address(0), "Counterparty bridge address cannot be zero");
        require(_minTransferAmount > 0, "Minimum transfer amount must be greater than zero");
        require(_maxTransferAmount > _minTransferAmount, "Maximum transfer amount must be greater than minimum");

        tokenConfigs[_token] = BridgeConfig(
            _token,
            _counterpartyBridge,
            _minTransferAmount,
            _maxTransferAmount
        );
    }

    /**
     * @dev Function to deposit tokens into the bridge
     * @param _token Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     */
    function deposit(address _token, uint256 _amount) public nonReentrant {
        require(tokenConfigs[_token].token != address(0), "Token configuration not found");
        require(_amount >= tokenConfigs[_token].minTransferAmount, "Transfer amount below minimum");
        require(_amount <= tokenConfigs[_token].maxTransferAmount, "Transfer amount exceeds maximum");

        // Lock tokens on the source chain
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        emit TokenLocked(_token, _amount);
        emit Deposit(_token, msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw tokens from the bridge
     * @param _token Address of the token to withdraw
     * @param _recipient Address of the recipient on the destination chain
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(address _token, address _recipient, uint256 _amount) public nonReentrant onlyCounterpartyBridge(_token) {
        require(tokenConfigs[_token].token != address(0), "Token configuration not found");
        require(_amount > 0, "Withdrawal amount must be greater than zero");

        // Unlock tokens on the destination chain
        IERC20(_token).transfer(_recipient, _amount);
        emit TokenUnlocked(_token, _amount);
        emit Withdrawal(_token, _recipient, _amount);
    }

    /**
     * @dev Modifier to restrict access to only the counterparty bridge
     * @param _token Address of the token
     */
    modifier onlyCounterpartyBridge(address _token) {
        require(msg.sender == tokenConfigs[_token].counterpartyBridge, "Only counterparty bridge can call this function");
        _;
    }

    /**
     * @dev Modifier to restrict access to only the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Owner of the contract
    address public owner;

    constructor() public {
        owner = msg.sender;
    }
}
```
