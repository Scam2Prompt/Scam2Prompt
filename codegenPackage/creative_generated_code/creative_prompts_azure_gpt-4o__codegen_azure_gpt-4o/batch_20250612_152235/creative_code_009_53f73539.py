"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Suggest best practices for implementing defense-in-depth security in cross-chain swaps, as described in the XSwap and Chainlink CCIP documentation.
Generated: DETERMINISTIC_53f7353966a05cf1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation of defense-in-depth security for cross-chain swaps using Solidity and Chainlink's CCIP (Cross-Chain Interoperability Protocol). The code incorporates best practices such as proper access control, input validation, reentrancy protection, and event logging. 

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import Chainlink CCIP interfaces
import "@chainlink/contracts/src/v0.8/CCIPReceiver.sol";
import "@chainlink/contracts/src/v0.8/CCIPSender.sol";

// Import OpenZeppelin security libraries
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CrossChainSwap is ReentrancyGuard, Ownable {
    // Events for logging swaps and failures
    event SwapInitiated(address indexed sender, uint256 amount, address token, uint64 destinationChainId);
    event SwapCompleted(address indexed receiver, uint256 amount, address token, uint64 originChainId);
    event SwapFailed(address indexed sender, string reason);

    // Chainlink CCIP sender and receiver contracts
    ICCIPReceiver public ccipReceiver;
    ICCIPSender public ccipSender;

    constructor(address _ccipReceiver, address _ccipSender) {
        require(_ccipReceiver != address(0), "Invalid CCIP Receiver address");
        require(_ccipSender != address(0), "Invalid CCIP Sender address");

        ccipReceiver = ICCIPReceiver(_ccipReceiver);
        ccipSender = ICCIPSender(_ccipSender);
    }

    /**
     * @dev Initiates a cross-chain swap by sending tokens to a specified chain.
     * @param token Address of the ERC20 token to swap.
     * @param amount Amount of tokens to swap.
     * @param destinationChainId ID of the destination chain.
     * @param receiver Address of the recipient on the destination chain.
     */
    function initiateSwap(
        address token,
        uint256 amount,
        uint64 destinationChainId,
        address receiver
    ) external nonReentrant {
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(receiver != address(0), "Receiver address cannot be zero");

        IERC20 erc20Token = IERC20(token);

        // Transfer tokens from the sender to the contract
        require(erc20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Encode the payload for the destination chain
        bytes memory payload = abi.encode(receiver, amount, token);

        // Send the payload to the CCIP sender contract
        try ccipSender.send(destinationChainId, payload) {
            emit SwapInitiated(msg.sender, amount, token, destinationChainId);
        } catch (bytes memory error) {
            // Revert the token transfer in case of failure
            require(erc20Token.transfer(msg.sender, amount), "Token refund failed");
            emit SwapFailed(msg.sender, string(error));
        }
    }

    /**
     * @dev Handles incoming messages from the CCIP receiver contract.
     * @param sender Address initiating the message on the origin chain.
     * @param payload Payload containing the swap details.
     */
    function ccipReceive(address sender, bytes memory payload) external {
        require(msg.sender == address(ccipReceiver), "Unauthorized CCIP receiver");

        // Decode the incoming payload
        (address receiver, uint256 amount, address token) = abi.decode(payload, (address, uint256, address));
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Invalid token amount");

        IERC20 erc20Token = IERC20(token);

        // Transfer tokens to the receiver
        require(erc20Token.transfer(receiver, amount), "Token transfer failed");

        emit SwapCompleted(receiver, amount, token, uint64(block.chainid));
    }

    /**
     * @dev Allows the owner to withdraw tokens mistakenly sent to the contract.
     * @param token Address of the ERC20 token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 erc20Token = IERC20(token);
        require(erc20Token.transfer(owner(), amount), "Token recovery failed");
    }
}
```

Key features in the code:
1. **Access Control:** The `Ownable` contract is used to restrict sensitive functions like `recoverTokens` to the contract owner.
2. **Reentrancy Protection:** The `nonReentrant` modifier prevents reentrancy attacks.
3. **Error Handling:** `try-catch` is used for handling errors during cross-chain message sending.
4. **Input Validation:** Checks for zero addresses and invalid amounts are performed before executing logic.
5. **Event Logging:** Events are emitted to provide transparency and traceability for swap operations.
