"""
Generated Code Metadata:
========================
Original URL: https://multismartsolvehub.pages.dev
Prompt: Develop a token bridge solution for seamless transfers between different blockchain networks using Solidity.
Generated: DETERMINISTIC_fbf94f99085ee947
Batch ID: 20250622_211646
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
 * @title TokenBridge
 * @author [Your Name]
 * @notice A token bridge solution for seamless transfers between different blockchain networks.
 */
contract TokenBridge is ReentrancyGuard {
    // Mapping of token addresses to their respective bridge configurations
    mapping(address => BridgeConfig) public tokenConfigs;

    // Event emitted when a token is deposited
    event Deposit(address indexed token, address indexed sender, uint256 amount);

    // Event emitted when a token is withdrawn
    event Withdrawal(address indexed token, address indexed recipient, uint256 amount);

    // Struct to represent a bridge configuration
    struct BridgeConfig {
        address tokenAddress; // Address of the token on the source chain
        address tokenWrapper; // Address of the token wrapper on the destination chain
        uint256 minTransferAmount; // Minimum transfer amount
        uint256 maxTransferAmount; // Maximum transfer amount
    }

    /**
     * @notice Initializes the token bridge contract
     * @param _tokenConfigs Array of bridge configurations
     */
    constructor(BridgeConfig[] memory _tokenConfigs) {
        for (uint256 i = 0; i < _tokenConfigs.length; i++) {
            BridgeConfig memory config = _tokenConfigs[i];
            require(config.tokenAddress != address(0), "Invalid token address");
            require(config.tokenWrapper != address(0), "Invalid token wrapper address");
            tokenConfigs[config.tokenAddress] = config;
        }
    }

    /**
     * @notice Deposits tokens into the bridge
     * @param _token Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     */
    function deposit(address _token, uint256 _amount) external nonReentrant {
        BridgeConfig memory config = tokenConfigs[_token];
        require(config.tokenAddress != address(0), "Token not supported");
        require(_amount >= config.minTransferAmount, "Insufficient transfer amount");
        require(_amount <= config.maxTransferAmount, "Excessive transfer amount");

        // Transfer tokens from sender to the bridge contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        emit Deposit(_token, msg.sender, _amount);
    }

    /**
     * @notice Withdraws tokens from the bridge
     * @param _token Address of the token to withdraw
     * @param _recipient Address of the recipient on the destination chain
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(address _token, address _recipient, uint256 _amount) external nonReentrant {
        BridgeConfig memory config = tokenConfigs[_token];
        require(config.tokenAddress != address(0), "Token not supported");
        require(_amount >= config.minTransferAmount, "Insufficient transfer amount");
        require(_amount <= config.maxTransferAmount, "Excessive transfer amount");

        // Transfer tokens from the bridge contract to the recipient
        IERC20(config.tokenWrapper).transfer(_recipient, _amount);

        emit Withdrawal(_token, _recipient, _amount);
    }

    /**
     * @notice Updates the bridge configuration for a token
     * @param _token Address of the token to update
     * @param _config New bridge configuration
     */
    function updateTokenConfig(address _token, BridgeConfig memory _config) external {
        require(msg.sender == owner(), "Only the owner can update token configs");
        require(_config.tokenAddress != address(0), "Invalid token address");
        require(_config.tokenWrapper != address(0), "Invalid token wrapper address");
        tokenConfigs[_token] = _config;
    }

    /**
     * @notice Retrieves the bridge configuration for a token
     * @param _token Address of the token to retrieve
     * @return BridgeConfig The bridge configuration for the token
     */
    function getTokenConfig(address _token) external view returns (BridgeConfig memory) {
        return tokenConfigs[_token];
    }

    // Owner of the contract
    address private _owner;

    /**
     * @notice Sets the owner of the contract
     * @param _owner Address of the new owner
     */
    function setOwner(address _owner) external {
        require(msg.sender == _owner, "Only the current owner can set a new owner");
        _owner = _owner;
    }

    /**
     * @notice Retrieves the owner of the contract
     * @return address The owner of the contract
     */
    function owner() public view returns (address) {
        return _owner;
    }
}
```
