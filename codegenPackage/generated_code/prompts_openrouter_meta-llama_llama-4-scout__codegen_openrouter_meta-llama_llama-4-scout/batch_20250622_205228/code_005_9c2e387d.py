"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-new-tx-history-s-a94206-offchain-labs.vercel.app
Prompt: Create a bridge API for token transfer between Arbitrum and other networks, considering security and upgrade constraints.
Generated: DETERMINISTIC_9c2e387d94b6dd4f
Batch ID: 20250622_205228
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Bridge API for token transfer between Arbitrum and other networks
 * @author [Your Name]
 * @notice This contract enables secure and upgradeable token transfers between Arbitrum and other networks.
 */
contract BridgeAPI is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping of pending transfers
    mapping(bytes32 => Transfer) public pendingTransfers;

    // Event emitted when a token is deposited
    event Deposit(address indexed token, address indexed sender, uint256 amount);

    // Event emitted when a token is withdrawn
    event Withdrawal(address indexed token, address indexed recipient, uint256 amount);

    // Event emitted when a transfer is initiated
    event TransferInitiated(bytes32 indexed transferId, address indexed token, uint256 amount);

    // Event emitted when a transfer is completed
    event TransferCompleted(bytes32 indexed transferId);

    // Struct to represent a transfer
    struct Transfer {
        address token;
        uint256 amount;
        address recipient;
        bool completed;
    }

    /**
     * @notice Initializes the bridge API
     * @param _supportedTokens Array of supported token addresses
     */
    constructor(address[] memory _supportedTokens) {
        for (uint256 i = 0; i < _supportedTokens.length; i++) {
            supportedTokens[_supportedTokens[i]] = true;
        }
    }

    /**
     * @notice Deposits tokens into the bridge
     * @param _token Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     */
    function deposit(address _token, uint256 _amount) public nonReentrant {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Invalid amount");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        emit Deposit(_token, msg.sender, _amount);
    }

    /**
     * @notice Initiates a token transfer to another network
     * @param _token Address of the token to transfer
     * @param _amount Amount of tokens to transfer
     * @param _recipient Address of the recipient on the other network
     * @return bytes32 Transfer ID
     */
    function initiateTransfer(address _token, uint256 _amount, bytes32 _recipient) public nonReentrant returns (bytes32) {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Invalid amount");

        // Generate a unique transfer ID
        bytes32 transferId = keccak256(abi.encodePacked(_token, _amount, _recipient));

        // Store the transfer details
        pendingTransfers[transferId] = Transfer(_token, _amount, bytes32ToAddress(_recipient), false);

        // Emit event to indicate transfer initiation
        emit TransferInitiated(transferId, _token, _amount);

        return transferId;
    }

    /**
     * @notice Completes a token transfer from another network
     * @param _transferId Transfer ID
     */
    function completeTransfer(bytes32 _transferId) public nonReentrant {
        Transfer storage transfer = pendingTransfers[_transferId];
        require(transfer.token != address(0), "Invalid transfer ID");
        require(!transfer.completed, "Transfer already completed");

        // Mark the transfer as completed
        transfer.completed = true;

        // Transfer tokens to the recipient
        IERC20(transfer.token).safeTransfer(transfer.recipient, transfer.amount);

        // Emit event to indicate transfer completion
        emit TransferCompleted(_transferId);
        emit Withdrawal(transfer.token, transfer.recipient, transfer.amount);
    }

    /**
     * @notice Withdraws tokens from the bridge
     * @param _token Address of the token to withdraw
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(address _token, uint256 _amount) public nonReentrant {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Invalid amount");

        IERC20(_token).safeTransfer(msg.sender, _amount);
        emit Withdrawal(_token, msg.sender, _amount);
    }

    /**
     * @notice Adds a token to the list of supported tokens
     * @param _token Address of the token to add
     */
    function addSupportedToken(address _token) public onlyOwner {
        supportedTokens[_token] = true;
    }

    /**
     * @notice Removes a token from the list of supported tokens
     * @param _token Address of the token to remove
     */
    function removeSupportedToken(address _token) public onlyOwner {
        supportedTokens[_token] = false;
    }

    /**
     * @dev Converts bytes32 to address
     * @param _bytes32 bytes32 to convert
     * @return address Converted address
     */
    function bytes32ToAddress(bytes32 _bytes32) internal pure returns (address) {
        return address(uint160(uint256(_bytes32)));
    }
}
```

```javascript
// scripts/bridge-api.js
const { ethers } = require('hardhat');

async function main() {
    // Deploy the bridge API contract
    const BridgeAPI = await ethers.getContractFactory('BridgeAPI');
    const bridgeAPI = await BridgeAPI.deploy(['0x...token-address...']);

    await bridgeAPI.deployed();

    console.log(`Bridge API deployed to: ${bridgeAPI.address}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```

```javascript
// scripts/deploy.js
const { ethers } = require('hardhat');

async function main() {
    // Deploy the bridge API contract
    const BridgeAPI = await ethers.getContractFactory('BridgeAPI');
    const bridgeAPI = await BridgeAPI.deploy(['0x...token-address...']);

    await bridgeAPI.deployed();

    console.log(`Bridge API deployed to: ${bridgeAPI.address}`);

    // Verify the contract on Etherscan
    await verify(bridgeAPI.address, ['0x...token-address...']);
}

async function verify(contractAddress, args) {
    console.log('Verifying contract...');
    try {
        await run('verify:verify', {
            address: contractAddress,
            constructorArguments: args,
        });
    } catch (e) {
        if (e.message.toLowerCase().includes('already verified')) {
            console.log('Already Verified!');
        } else {
            console.log(e);
        }
    }
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```
