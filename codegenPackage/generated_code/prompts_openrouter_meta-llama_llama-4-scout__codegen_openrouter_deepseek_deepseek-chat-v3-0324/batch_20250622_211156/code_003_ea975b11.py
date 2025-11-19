"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Generate an example of a ParaSwap implementation in a Solidity smart contract that includes best practices for safety and security, such as checking caller contracts and forwarding ERC1967 proxy upgrade checks.
Generated: DETERMINISTIC_ea975b11097ef415
Batch ID: 20250622_211156
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";

contract ParaSwapImplementation is Initializable, UUPSUpgradeable, Ownable {
    using SafeERC20 for IERC20;

    // Whitelist of allowed caller contracts
    mapping(address => bool) public whitelistedCallers;

    event SwapExecuted(
        address indexed user,
        address indexed fromToken,
        address indexed toToken,
        uint256 fromAmount,
        uint256 toAmount
    );

    event CallerWhitelisted(address indexed caller);
    event CallerRemoved(address indexed caller);

    /// @custom:oz-upgrades-unsafe-allow constructor
    constructor() initializer {}

    function initialize() public initializer {
        __Ownable_init();
        __UUPSUpgradeable_init();
    }

    function _authorizeUpgrade(address newImplementation) internal override onlyOwner {}

    /**
     * @dev Whitelist a contract address to call the swap function
     * @param caller Address of the contract to whitelist
     */
    function whitelistCaller(address caller) external onlyOwner {
        require(caller != address(0), "Invalid caller address");
        whitelistedCallers[caller] = true;
        emit CallerWhitelisted(caller);
    }

    /**
     * @dev Remove a contract address from the whitelist
     * @param caller Address of the contract to remove
     */
    function removeCaller(address caller) external onlyOwner {
        require(whitelistedCallers[caller], "Caller not whitelisted");
        whitelistedCallers[caller] = false;
        emit CallerRemoved(caller);
    }

    /**
     * @dev Execute a token swap
     * @param fromToken Token to swap from
     * @param toToken Token to swap to
     * @param fromAmount Amount of fromToken to swap
     * @param toAmountMin Minimum amount of toToken to receive
     * @param data Additional swap data
     */
    function swap(
        IERC20 fromToken,
        IERC20 toToken,
        uint256 fromAmount,
        uint256 toAmountMin,
        bytes calldata data
    ) external {
        require(whitelistedCallers[msg.sender], "Caller not whitelisted");
        require(fromAmount > 0, "Invalid from amount");
        require(address(fromToken) != address(toToken), "Same tokens");

        // Transfer tokens from user to this contract
        fromToken.safeTransferFrom(msg.sender, address(this), fromAmount);

        // Approve the external contract to spend fromToken
        fromToken.safeApprove(address(this), fromAmount);

        // Execute swap (simplified for example)
        uint256 toAmount = fromAmount; // In a real implementation, this would be the actual swap logic
        require(toAmount >= toAmountMin, "Insufficient output amount");

        // Transfer swapped tokens to user
        toToken.safeTransfer(msg.sender, toAmount);

        emit SwapExecuted(msg.sender, address(fromToken), address(toToken), fromAmount, toAmount);
    }

    /**
     * @dev Emergency function to withdraw tokens stuck in the contract
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        token.safeTransfer(owner(), amount);
    }
}
```
