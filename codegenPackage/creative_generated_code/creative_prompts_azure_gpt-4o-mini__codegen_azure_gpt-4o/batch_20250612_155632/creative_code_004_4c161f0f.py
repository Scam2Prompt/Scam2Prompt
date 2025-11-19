"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectautofixing.vercel.app
Prompt: Provide an example of a smart contract that facilitates the swapping and exchanging of cryptocurrencies on a decentralized platform.
Generated: DETERMINISTIC_4c161f0fe2de574e
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/// @title Decentralized Token Swap Smart Contract
/// @notice This contract facilitates cryptocurrency swaps between two parties.
contract TokenSwap {
    // Address of the token being exchanged by Party A
    address public tokenA;

    // Address of the token being exchanged by Party B
    address public tokenB;

    // Address of Party A
    address public partyA;

    // Address of Party B
    address public partyB;

    // Amount of tokens Party A is offering
    uint256 public amountA;

    // Amount of tokens Party B is offering
    uint256 public amountB;

    // Contract state: true when the swap is active
    bool public active;

    /// @notice Event emitted when the swap is successfully executed
    event SwapExecuted(address indexed partyA, address indexed partyB, uint256 amountA, uint256 amountB);

    /// @notice Event emitted when the contract is initialized
    event SwapInitialized(address indexed partyA, address indexed partyB, uint256 amountA, uint256 amountB);

    /// @notice Constructor to initialize swap parameters
    /// @param _tokenA Address of token A
    /// @param _tokenB Address of token B
    /// @param _partyA Address of Party A
    /// @param _partyB Address of Party B
    /// @param _amountA Amount of token A Party A is offering
    /// @param _amountB Amount of token B Party B is offering
    constructor(
        address _tokenA,
        address _tokenB,
        address _partyA,
        address _partyB,
        uint256 _amountA,
        uint256 _amountB
    ) {
        require(_tokenA != address(0), "Token A address cannot be zero");
        require(_tokenB != address(0), "Token B address cannot be zero");
        require(_partyA != address(0), "Party A address cannot be zero");
        require(_partyB != address(0), "Party B address cannot be zero");
        require(_amountA > 0, "Amount A must be greater than zero");
        require(_amountB > 0, "Amount B must be greater than zero");

        tokenA = _tokenA;
        tokenB = _tokenB;
        partyA = _partyA;
        partyB = _partyB;
        amountA = _amountA;
        amountB = _amountB;
        active = true;

        emit SwapInitialized(_partyA, _partyB, _amountA, _amountB);
    }

    /// @notice Execute the token swap between Party A and Party B
    /// @dev Both parties must have approved the contract to transfer their tokens
    function executeSwap() external {
        require(active, "Swap is no longer active");
        require(msg.sender == partyA || msg.sender == partyB, "Unauthorized");

        // Ensure Party A has enough token A balance
        require(IERC20(tokenA).balanceOf(partyA) >= amountA, "Insufficient token A balance");
        // Ensure Party B has enough token B balance
        require(IERC20(tokenB).balanceOf(partyB) >= amountB, "Insufficient token B balance");

        // Transfer token A from Party A to Party B
        bool sentA = IERC20(tokenA).transferFrom(partyA, partyB, amountA);
        require(sentA, "Token A transfer failed");

        // Transfer token B from Party B to Party A
        bool sentB = IERC20(tokenB).transferFrom(partyB, partyA, amountB);
        require(sentB, "Token B transfer failed");

        // Update contract state to inactive
        active = false;

        emit SwapExecuted(partyA, partyB, amountA, amountB);
    }

    /// @notice Allows either party to cancel the swap before execution
    function cancelSwap() external {
        require(active, "Swap is no longer active");
        require(msg.sender == partyA || msg.sender == partyB, "Unauthorized");

        // Mark the swap as inactive
        active = false;
    }
}
```
