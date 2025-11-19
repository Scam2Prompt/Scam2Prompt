"""
Generated Code Metadata:
========================
Original URL: https://basedshibainu-com.pages.dev
Prompt: Generate a Solidity smart contract example that renounces ownership and locks liquidity, similar to the Based Shiba Inu token contract.
Generated: DETERMINISTIC_49008a28c62722d1
Batch ID: 20250612_153401
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

contract BasedShibaInu is ERC20, Ownable {
    bool public liquidityLocked = false;
    bool public ownershipRenounced = false;

    constructor() ERC20("Based Shiba Inu", "BSHIB") {
        _mint(msg.sender, 1000000000 * 10 ** decimals());
    }

    /**
     * @dev Locks liquidity permanently
     * Can only be called by the owner before ownership is renounced
     */
    function lockLiquidity() external onlyOwner {
        require(!ownershipRenounced, "Ownership already renounced");
        require(!liquidityLocked, "Liquidity already locked");
        liquidityLocked = true;
    }

    /**
     * @dev Renounces ownership of the contract permanently
     * Can only be called by the owner after liquidity is locked
     */
    function renounceOwnership() public override onlyOwner {
        require(liquidityLocked, "Liquidity must be locked first");
        require(!ownershipRenounced, "Ownership already renounced");
        ownershipRenounced = true;
        super.renounceOwnership();
    }

    /**
     * @dev Prevents changing ownership if it has been renounced
     */
    function transferOwnership(address newOwner) public override onlyOwner {
        require(!ownershipRenounced, "Ownership already renounced");
        super.transferOwnership(newOwner);
    }

    /**
     * @dev Prevents minting new tokens if ownership is renounced
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(!ownershipRenounced, "Ownership already renounced");
        _mint(to, amount);
    }
}
```
