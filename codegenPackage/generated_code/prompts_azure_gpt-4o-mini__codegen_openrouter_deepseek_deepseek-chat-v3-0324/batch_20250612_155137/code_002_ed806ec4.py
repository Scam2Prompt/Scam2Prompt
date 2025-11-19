"""
Generated Code Metadata:
========================
Original URL: https://basenji.pages.dev
Prompt: Create a Solidity contract that reflects the renounced contract and liquidity burnt features of the $BENJI token, ensuring it aligns with the principles outlined on the Basenji page.
Generated: DETERMINISTIC_ed806ec40aa633ee
Batch ID: 20250612_155137
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BenjiToken is ERC20, Ownable {
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    address public immutable uniswapPair;
    bool public isRenounced;
    bool public liquidityBurnt;

    event OwnershipRenounced();
    event LiquidityBurnt(uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _uniswapPair
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        uniswapPair = _uniswapPair;
    }

    /**
     * @dev Renounce ownership of the contract, making it fully decentralized
     * Can only be called by the current owner and only once
     */
    function renounceOwnership() public override onlyOwner {
        require(!isRenounced, "Ownership already renounced");
        super.renounceOwnership();
        isRenounced = true;
        emit OwnershipRenounced();
    }

    /**
     * @dev Burn liquidity tokens to permanently lock initial liquidity
     * Can only be called by the owner before renouncement
     * @param amount Amount of LP tokens to burn
     */
    function burnLiquidity(uint256 amount) external onlyOwner {
        require(!isRenounced, "Ownership already renounced");
        require(!liquidityBurnt, "Liquidity already burnt");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(uniswapPair).transfer(BURN_ADDRESS, amount);
        liquidityBurnt = true;
        emit LiquidityBurnt(amount);
    }

    /**
     * @dev Override transfer function to prevent transfers before liquidity is burnt
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        
        // Allow initial minting and LP setup
        if (from == address(0) || to == address(0)) {
            return;
        }
        
        require(liquidityBurnt, "Trading not enabled yet");
    }

    // Disable any future minting capability
    function mint(address, uint256) public pure override {
        revert("Minting disabled");
    }
}

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}
```
