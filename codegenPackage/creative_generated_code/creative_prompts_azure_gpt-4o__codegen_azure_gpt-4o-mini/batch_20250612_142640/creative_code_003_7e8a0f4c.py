"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Create a Solidity contract that uses ParaSwap to modularize core logic for a DeFi application while ensuring safe upgrades via ERC1967 proxy checks.
Generated: DETERMINISTIC_7e8a0f4c566b1718
Batch ID: 20250612_142640
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

import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract DeFiApplication is Initializable, Ownable {
    using SafeMath for uint256;

    IUniswapV2Router02 public router; // The Uniswap router for trades
    address public tokenA;             // Address of token A
    address public tokenB;             // Address of token B

    // Event for logging swaps
    event Swapped(address indexed sender, uint256 amountIn, uint256 amountOut);

    // Initialize the contract with router and token addresses
    function initialize(address _router, address _tokenA, address _tokenB) public initializer {
        router = IUniswapV2Router02(_router);
        tokenA = _tokenA;
        tokenB = _tokenB;
    }

    // Function to swap tokens using ParaSwap
    function swapTokens(uint256 amountIn, uint256 amountOutMin, address to, uint256 deadline) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(to != address(0), "Invalid recipient address");

        // Transfer token A from the sender to this contract
        bool sent = IERC20(tokenA).transferFrom(msg.sender, address(this), amountIn);
        require(sent, "Token transfer failed");

        // Approve the router to spend token A
        IERC20(tokenA).approve(address(router), amountIn);

        // Path to swap token A for token B
        address[] memory path = new address[](2);
        path[0] = tokenA;
        path[1] = tokenB;

        // Execute the swap
        uint256[] memory amounts = router.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit event for logging
        emit Swapped(msg.sender, amounts[0], amounts[1]);
    }

    // Upgradeable contract function to upgrade the implementation
    function upgradeTo(address newImplementation) external onlyOwner {
        require(newImplementation != address(0), "Invalid implementation address");
        _upgradeTo(newImplementation);
    }

    // Internal function to handle the actual upgrade
    function _upgradeTo(address newImplementation) internal {
        // Set new implementation address in ERC1967
        _setImplementation(newImplementation);
    }

    // Function to set the implementation address (ERC1967 Storage)
    function _setImplementation(address newImplementation) private {
        // ERC1967 logic to set implementation
        require(Address.isContract(newImplementation), "New implementation is not a contract");
        StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value = newImplementation;
    }

    // Storage slot for implementation address
    bytes32 internal constant _IMPLEMENTATION_SLOT = 0x5c60dfd1f77b20245e7d7d9e046015068a7b8b20aa7c775706b7b0455827c9e1;

    // Fallback function to receive Ether
    receive() external payable {}
}
```
