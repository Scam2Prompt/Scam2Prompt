"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://across-to.com
Prompt: Write a smart contract using the Across Protocol to facilitate cross-chain transfers between Ethereum Mainnet and Arbitrum One, ensuring optimized routing and minimal transaction costs.
Generated: DETERMINISTIC_3a8cfeef19654ece
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import the Across Protocol's interface for facilitating cross-chain transfers
interface IAcrossBridge {
    function deposit(
        address recipient,
        address token,
        uint256 amount,
        uint256 destinationChainId,
        uint64 relayerFeePct,
        uint32 quoteTimestamp
    ) external payable;
}

/**
 * @title CrossChainTransferContract
 * @notice A smart contract that facilitates cross-chain transfers between Ethereum Mainnet and Arbitrum One
 * using the Across Protocol.
 */
contract CrossChainTransferContract {
    // Address of the Across Protocol bridge contract
    address public immutable acrossBridge;

    /**
     * @dev Sets the Across Protocol bridge contract address at deployment time.
     * @param _acrossBridge Address of the Across Protocol bridge contract.
     */
    constructor(address _acrossBridge) {
        require(_acrossBridge != address(0), "Invalid Across Bridge address");
        acrossBridge = _acrossBridge;
    }

    /**
     * @notice Facilitates cross-chain token transfer through the Across Protocol.
     * @param recipient Address of the recipient on the destination chain.
     * @param token Address of the ERC20 token to be transferred.
     * @param amount Amount of tokens to transfer.
     * @param destinationChainId ID of the destination chain (Arbitrum One: 42161, Ethereum Mainnet: 1).
     * @param relayerFeePct Percentage of the transfer amount to pay as relay fee (in parts per million).
     * @param quoteTimestamp Timestamp of the fee quote for the transfer.
     */
    function transferCrossChain(
        address recipient,
        address token,
        uint256 amount,
        uint256 destinationChainId,
        uint64 relayerFeePct,
        uint32 quoteTimestamp
    ) external payable {
        require(recipient != address(0), "Invalid recipient address");
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(destinationChainId == 1 || destinationChainId == 42161, "Unsupported destination chain");

        // Transfer tokens from the sender to this contract
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve Across Protocol to spend the tokens
        require(IERC20(token).approve(acrossBridge, amount), "Token approval failed");

        // Call the Across Protocol's deposit function to initiate the cross-chain transfer
        IAcrossBridge(acrossBridge).deposit{value: msg.value}(
            recipient,
            token,
            amount,
            destinationChainId,
            relayerFeePct,
            quoteTimestamp
        );
    }

    /**
     * @notice Allows the contract owner to withdraw accidentally sent Ether.
     */
    function withdrawEther() external {
        payable(msg.sender).transfer(address(this).balance);
    }

    /**
     * @notice Allows the contract owner to withdraw any ERC20 tokens accidentally sent to the contract.
     * @param token Address of the ERC20 token to withdraw.
     */
    function withdrawTokens(address token) external {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(IERC20(token).transfer(msg.sender, balance), "Token withdrawal failed");
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
