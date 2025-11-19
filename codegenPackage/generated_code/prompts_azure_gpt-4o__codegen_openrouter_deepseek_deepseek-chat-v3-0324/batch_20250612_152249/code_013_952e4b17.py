"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Implement a cross-chain settlement mechanism for tokenized assets using Chainlink CCIP in Solidity.
Generated: DETERMINISTIC_952e4b17348f7db3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import {IRouterClient} from "@chainlink/contracts-ccip/src/v0.8/ccip/interfaces/IRouterClient.sol";
import {Client} from "@chainlink/contracts-ccip/src/v0.8/ccip/libraries/Client.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract CrossChainSettlement is Ownable {
    using SafeERC20 for IERC20;

    // Chainlink CCIP Router interface
    IRouterClient public immutable router;

    // Supported chains and their corresponding Chainlink chain selectors
    mapping(uint64 => bool) public supportedChains;
    mapping(address => bool) public supportedTokens;

    // Events
    event AssetLocked(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint64 destinationChain,
        bytes32 indexed settlementId
    );
    event AssetReleased(
        address indexed recipient,
        address indexed token,
        uint256 amount,
        bytes32 indexed settlementId
    );
    event SettlementFailed(
        bytes32 indexed settlementId,
        string reason
    );

    // Modifier to check if chain is supported
    modifier onlySupportedChain(uint64 chainSelector) {
        require(supportedChains[chainSelector], "Chain not supported");
        _;
    }

    // Modifier to check if token is supported
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    /**
     * @dev Constructor initializes the CCIP router address
     * @param _router The address of the Chainlink CCIP Router
     */
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        router = IRouterClient(_router);
    }

    /**
     * @dev Locks tokens on source chain and initiates cross-chain transfer
     * @param token Address of the token to transfer
     * @param amount Amount of tokens to transfer
     * @param destinationChain Chain selector of the destination chain
     * @param recipient Address of the recipient on the destination chain
     * @return settlementId Unique identifier for the settlement
     */
    function lockTokens(
        address token,
        uint256 amount,
        uint64 destinationChain,
        address recipient
    ) external onlySupportedChain(destinationChain) onlySupportedToken(token) returns (bytes32 settlementId) {
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        settlementId = keccak256(
            abi.encodePacked(
                block.chainid,
                destinationChain,
                token,
                amount,
                recipient,
                block.timestamp
            )
        );

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Build CCIP message
        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: abi.encode(recipient),
            data: abi.encode(token, amount, settlementId),
            tokenAmounts: new Client.EVMTokenAmount[](0),
            extraArgs: "",
            feeToken: address(0)
        });

        // Get fee for sending the message
        uint256 fee = router.getFee(destinationChain, message);

        // Send the message through the router
        bytes32 messageId = router.ccipSend{value: fee}(destinationChain, message);

        emit AssetLocked(msg.sender, token, amount, destinationChain, settlementId);
        return settlementId;
    }

    /**
     * @dev Releases tokens on the destination chain upon receiving CCIP message
     * @param token Address of the token to release
     * @param amount Amount of tokens to release
     * @param recipient Address of the recipient
     * @param settlementId Unique identifier for the settlement
     */
    function releaseTokens(
        address token,
        uint256 amount,
        address recipient,
        bytes32 settlementId
    ) external onlySupportedToken(token) {
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens to recipient
        IERC20(token).safeTransfer(recipient, amount);

        emit AssetReleased(recipient, token, amount, settlementId);
    }

    /**
     * @dev Adds a supported chain
     * @param chainSelector Chain selector of the chain to support
     */
    function addSupportedChain(uint64 chainSelector) external onlyOwner {
        supportedChains[chainSelector] = true;
    }

    /**
     * @dev Removes a supported chain
     * @param chainSelector Chain selector of the chain to remove
     */
    function removeSupportedChain(uint64 chainSelector) external onlyOwner {
        supportedChains[chainSelector] = false;
    }

    /**
     * @dev Adds a supported token
     * @param token Address of the token to support
     */
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
    }

    /**
     * @dev Removes a supported token
     * @param token Address of the token to remove
     */
    function removeSupportedToken(address token) external onlyOwner {
        supportedTokens[token] = false;
    }

    /**
     * @dev Handles CCIP messages received from other chains
     * @param message CCIP message containing the settlement details
     */
    function ccipReceive(Client.Any2EVMMessage calldata message) external {
        // Verify the sender is the CCIP router
        require(msg.sender == address(router), "Invalid sender");

        // Decode the message
        (address token, uint256 amount, bytes32 settlementId) = abi.decode(
            message.data,
            (address, uint256, bytes32)
        );

        // Decode the recipient address
        address recipient = abi.decode(message.receiver, (address));

        try this.releaseTokens(token, amount, recipient, settlementId) {
            // Successfully released tokens
        } catch Error(string memory reason) {
            emit SettlementFailed(settlementId, reason);
        } catch {
            emit SettlementFailed(settlementId, "Unknown error");
        }
    }

    /**
     * @dev Withdraws stuck tokens from the contract
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawStuckTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }

    // Receive function to accept native tokens (for CCIP fees)
    receive() external payable {}
}
```
