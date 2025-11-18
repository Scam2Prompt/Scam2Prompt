"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zknysc.github.io
Prompt: Write a Solidity smart contract that interacts with zkSync Era Mainnet, demonstrating token transfers and querying transaction details using zkSync's scaling features.
Generated: DETERMINISTIC_0db4a44802df08b9
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import the interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// ZkSync-specific interface for interacting with L2 contracts
interface IZkSync {
    function getTransactionDetails(uint256 transactionHash) external view returns (bytes memory);
}

contract ZkSyncTokenInteractor {
    // Address of Token to interact with
    IERC20 public token; 

    // Address of zkSync interface
    IZkSync public zkSync;

    // Event emitted when tokens are successfully transferred
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);

    // Event emitted when transaction details are fetched
    event TransactionDetails(bytes details);

    /**
     * @dev Constructor to initialize contract with token and zkSync addresses
     * @param _token Address of the ERC20 token contract
     * @param _zkSync Address of zkSync contract
     */
    constructor(address _token, address _zkSync) {
        require(_token != address(0), "Invalid token address");
        require(_zkSync != address(0), "Invalid zkSync address");
        token = IERC20(_token);
        zkSync = IZkSync(_zkSync);
    }

    /**
     * @dev Transfers tokens to a recipient
     * @param recipient Address of the token recipient
     * @param amount Amount of tokens to transfer
     */
    function transferTokens(address recipient, uint256 amount) external {
        require(recipient != address(0), "Cannot transfer to zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Execute the token transfer
        bool success = token.transferFrom(msg.sender, recipient, amount);
        require(success, "Token transfer failed");

        // Emit the event
        emit TokensTransferred(msg.sender, recipient, amount);
    }

    /**
     * @dev Fetches transaction details from zkSync
     * @param transactionHash Hash of the transaction to query
     */
    function getTransactionDetails(uint256 transactionHash) external {
        // Fetch the transaction details
        bytes memory details = zkSync.getTransactionDetails(transactionHash);

        // Emit the event with transaction details
        emit TransactionDetails(details);
    }

    /**
     * @dev Retrieves the token balance of the caller
     * @return balance The token balance of the caller
     */
    function getMyTokenBalance() external view returns (uint256 balance) {
        balance = token.balanceOf(msg.sender);
    }
}
```
