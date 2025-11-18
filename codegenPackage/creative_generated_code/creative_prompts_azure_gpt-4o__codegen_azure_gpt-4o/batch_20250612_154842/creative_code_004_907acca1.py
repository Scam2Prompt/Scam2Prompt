"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-stargate.net
Prompt: Create a smart contract that leverages Stargate Finance's composable infrastructure to enable seamless DeFi swaps across multiple blockchains.
Generated: DETERMINISTIC_907acca17fb33328
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a Solidity smart contract that interfaces with Stargate Finance to enable cross-chain swaps. The contract includes error handling, follows best practices, and includes comments for clarity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

// Import the interfaces needed from Stargate Finance
import "@layerzerolabs/stargate/contracts/interfaces/IStargateRouter.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CrossChainSwap is Ownable {
    // Stargate Router interface
    IStargateRouter public immutable stargateRouter;

    // Event to log swaps
    event CrossChainSwapInitiated(
        address indexed user,
        uint16 dstChainId,
        uint256 srcPoolId,
        uint256 dstPoolId,
        uint256 amount,
        address indexed receiver
    );

    /**
     * @dev Constructor to initialize the Stargate Router contract address.
     * @param _stargateRouter Address of the Stargate Router contract.
     */
    constructor(address _stargateRouter) {
        require(_stargateRouter != address(0), "Invalid Stargate Router address");
        stargateRouter = IStargateRouter(_stargateRouter);
    }

    /**
     * @dev Function to execute a cross-chain swap using Stargate.
     * @param dstChainId Destination chain ID.
     * @param srcPoolId Source pool ID.
     * @param dstPoolId Destination pool ID.
     * @param amount Amount of tokens to swap.
     * @param receiver Address to receive tokens on the destination chain.
     * @param token Address of the token to be swapped.
     * @param payload Additional payload for the destination chain (optional).
     */
    function swap(
        uint16 dstChainId,
        uint256 srcPoolId,
        uint256 dstPoolId,
        uint256 amount,
        address receiver,
        address token,
        bytes calldata payload
    ) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(receiver != address(0), "Receiver address must be valid");

        // Transfer the tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve Stargate Router to spend the tokens
        IERC20(token).approve(address(stargateRouter), amount);

        // Stargate swap parameters
        IStargateRouter.lzTxObj memory lzTxParams = IStargateRouter.lzTxObj({
            dstGasForCall: 0,
            dstNativeAmount: 0,
            dstNativeAddr: abi.encodePacked(receiver)
        });

        // Execute the swap
        try stargateRouter.swap{value: msg.value}(
            dstChainId,
            srcPoolId,
            dstPoolId,
            payable(msg.sender),
            amount,
            0, // Minimum amount for destination chain
            lzTxParams,
            abi.encodePacked(receiver),
            payload
        ) {
            emit CrossChainSwapInitiated(msg.sender, dstChainId, srcPoolId, dstPoolId, amount, receiver);
        } catch Error(string memory errorMessage) {
            revert(errorMessage);
        } catch {
            revert("Cross-chain swap failed");
        }
    }

    /**
     * @dev Withdraw function to recover tokens accidentally sent to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function withdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(owner(), amount);
    }

    /**
     * @dev Fallback function to accept Ether for gas fees.
     */
    receive() external payable {}

    /**
     * @dev Fallback function for non-existent function calls.
     */
    fallback() external payable {}
}
```

### Key Points
- **Error Handling**: The `try-catch` block ensures proper error handling during Stargate's `swap` call.
- **Security**: The contract uses the `Ownable` contract from OpenZeppelin to restrict access to administrative functions (e.g., `withdraw`).
- **Comments**: Each function and important logic block is well-documented.
- **Best Practices**: Approval is handled explicitly, and `msg.value` is passed for native gas fees.

Make sure to test and deploy this smart contract in a staging/test environment before deploying to production. Additionally, verify that the Stargate Router address and supported chain/pool IDs are properly configured.
