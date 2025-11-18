"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidtnckzvkdfd4adyg7s3vhgnsxy3sxyvceyaty6bcbuxmmlfvut3a.ipfs.dweb.link
Prompt: Write a Solidity smart contract that integrates Pendle's yield tokenization feature to split stETH into fixed yield and principal components.
Generated: DETERMINISTIC_37ef265dc8ef51f5
Batch ID: 20250612_150228
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

// Import required interfaces from Pendle and Lido
interface IPendleRouter {
    function tokenizeYield(
        address underlyingAsset,
        uint256 amount,
        address to
    ) external returns (address ot, address yt);
}

interface ILido {
    function submit(address _referral) external payable returns (uint256);
}

contract STETHYieldSplitter {
    // State variables
    address public immutable pendleRouter; // Address of Pendle Router
    address public immutable stETH; // Address of stETH token (from Lido)
    address public immutable lidoContract; // Address of Lido Contract

    // Events
    event YieldTokenized(address indexed user, address ot, address yt, uint256 amount);

    // Constructor to set Pendle Router, stETH, and Lido contract addresses
    constructor(address _pendleRouter, address _stETH, address _lidoContract) {
        pendleRouter = _pendleRouter;
        stETH = _stETH;
        lidoContract = _lidoContract;
    }

    /**
     * @dev Tokenizes stETH yield into fixed yield (OT) and principal (YT) components.
     * @param amount Amount of Ether to deposit and tokenize.
     */
    function tokenizeYield(uint256 amount) external payable {
        require(msg.value == amount, "Incorrect Ether amount sent");

        // Deposit Ether into Lido to receive stETH
        uint256 stETHReceived = ILido(lidoContract).submit{value: amount}(address(0));
        require(stETHReceived > 0, "Failed to mint stETH");

        // Approve Pendle Router to use stETH
        IERC20(stETH).approve(pendleRouter, stETHReceived);

        // Tokenize stETH yield using Pendle Router
        (address ot, address yt) = IPendleRouter(pendleRouter).tokenizeYield(stETH, stETHReceived, msg.sender);

        // Emit event
        emit YieldTokenized(msg.sender, ot, yt, stETHReceived);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw accidentally sent Ether to the contract.
     * @param to Address to withdraw funds to.
     */
    function withdrawEther(address to) external {
        require(to != address(0), "Invalid address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available");

        (bool success, ) = to.call{value: balance}("");
        require(success, "Ether withdrawal failed");
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
}
```
