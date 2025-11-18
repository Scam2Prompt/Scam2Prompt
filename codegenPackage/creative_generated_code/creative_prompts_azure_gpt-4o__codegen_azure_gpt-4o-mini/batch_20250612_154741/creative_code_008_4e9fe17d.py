"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contrack-dev.pages.dev
Prompt: Create a Solidity contract that interacts with the Uniswap V2 ERC20 interface to fetch token details, inspired by the UniswapSlippageBot contract.
Generated: DETERMINISTIC_4e9fe17d80236548
Batch ID: 20250612_154741
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

// Import the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for Uniswap V2 Router
interface IUniswapV2Router02 {
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
}

// Contract to interact with Uniswap V2 for token details
contract UniswapTokenViewer {
    // Uniswap router address (mainnet)
    address private constant UNISWAP_ROUTER_ADDRESS = 0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6;

    // Router instance
    IUniswapV2Router02 private uniswapRouter;

    // Event to emit token details
    event TokenDetailsFetched(address indexed token, string name, string symbol, uint8 decimals, uint256 totalSupply);

    // Constructor to set the Uniswap router
    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to fetch ERC20 token details
    function fetchTokenDetails(address token) external {
        // Check if the address is a valid contract
        require(token != address(0), "Invalid address: zero address");
        require(isContract(token), "Invalid address: not a contract");

        // Create instance of the token
        IERC20 erc20Token = IERC20(token);

        // Fetch token details
        string memory name = erc20Token.name();
        string memory symbol = erc20Token.symbol();
        uint8 decimals = erc20Token.decimals();
        uint256 totalSupply = erc20Token.totalSupply();

        // Emit the token details
        emit TokenDetailsFetched(token, name, symbol, decimals, totalSupply);
    }

    // Function to check if an address is a contract
    function isContract(address account) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(account)
        }
        return size > 0;
    }

    // Function to get token output amounts from Uniswap
    function getTokenAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts) {
        require(amountIn > 0, "Invalid amount: must be greater than zero");
        require(path.length >= 2, "Invalid path: must have at least two tokens");

        // Fetch amounts out from Uniswap
        amounts = uniswapRouter.getAmountsOut(amountIn, path);
    }
}
```
