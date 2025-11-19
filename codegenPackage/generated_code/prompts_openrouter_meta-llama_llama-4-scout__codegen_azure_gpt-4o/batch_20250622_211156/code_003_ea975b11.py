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

// Importing OpenZeppelin libraries for security and upgradeability
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";
import "@openzeppelin/contracts/access/OwnableUpgradeable.sol";

/// @title ParaSwap Integration Example
/// @notice This contract demonstrates a secure integration with ParaSwap
/// @dev Implements UUPS upgradeability and follows best practices for safety
contract ParaSwapExample is UUPSUpgradeable, OwnableUpgradeable {
    // Event emitted when a swap is executed
    event SwapExecuted(address indexed user, address indexed srcToken, address indexed destToken, uint256 srcAmount, uint256 destAmount);

    /// @notice Initializer function for upgradeable contracts
    /// @dev Replaces constructor in upgradeable contracts
    function initialize() public initializer {
        __Ownable_init();
    }

    /// @notice Authorizes upgrades to the contract
    /// @dev Only the owner can authorize upgrades
    /// @param newImplementation Address of the new implementation contract
    function _authorizeUpgrade(address newImplementation) internal override onlyOwner {}

    /// @notice Executes a token swap via ParaSwap
    /// @param srcToken Address of the source token
    /// @param destToken Address of the destination token
    /// @param srcAmount Amount of source token to swap
    /// @param destAmountMin Minimum amount of destination token to receive
    /// @param callData Encoded data for ParaSwap's contract call
    /// @param paraSwapAddress Address of the ParaSwap contract
    function executeSwap(
        address srcToken,
        address destToken,
        uint256 srcAmount,
        uint256 destAmountMin,
        bytes calldata callData,
        address paraSwapAddress
    ) external {
        require(srcToken != address(0), "Invalid source token address");
        require(destToken != address(0), "Invalid destination token address");
        require(paraSwapAddress != address(0), "Invalid ParaSwap address");
        require(srcAmount > 0, "Source amount must be greater than zero");

        // Transfer source tokens from the user to this contract
        IERC20(srcToken).transferFrom(msg.sender, address(this), srcAmount);

        // Approve ParaSwap to spend the source tokens
        IERC20(srcToken).approve(paraSwapAddress, srcAmount);

        // Call ParaSwap contract
        (bool success, ) = paraSwapAddress.call(callData);
        require(success, "ParaSwap call failed");

        // Check the balance of destination tokens after the swap
        uint256 destBalance = IERC20(destToken).balanceOf(address(this));
        require(destBalance >= destAmountMin, "Insufficient destination token amount");

        // Transfer destination tokens to the user
        IERC20(destToken).transfer(msg.sender, destBalance);

        // Emit event for the swap
        emit SwapExecuted(msg.sender, srcToken, destToken, srcAmount, destBalance);
    }

    /// @notice Prevents calls from other contracts
    /// @dev Ensures only EOA (Externally Owned Accounts) can call the function
    modifier onlyEOA() {
        require(tx.origin == msg.sender, "Caller must be an EOA");
        _;
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("ETH transfers not allowed");
    }
}
```
