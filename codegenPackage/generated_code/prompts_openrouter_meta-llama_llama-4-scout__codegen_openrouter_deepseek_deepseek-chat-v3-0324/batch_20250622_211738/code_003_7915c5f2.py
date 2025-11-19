"""
Generated Code Metadata:
========================
Original URL: https://tokenscreatorethpro.pages.dev
Prompt: Create a token with 100% ownership and a creation fee of $1 using a full audited smart contract solidity code.
Generated: DETERMINISTIC_7915c5f2b459da57
Batch ID: 20250622_211738
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title FeeBasedToken
 * @dev ERC20 token with a creation fee and 100% ownership by creator
 */
contract FeeBasedToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant CREATION_FEE = 1 ether; // $1 equivalent in wei
    uint256 public constant TOTAL_SUPPLY = 1000000 * (10 ** 18); // 1 million tokens

    event TokenCreated(address indexed creator, uint256 amount);

    /**
     * @dev Constructor that mints total supply to contract creator upon deployment
     * Requires payment of creation fee
     */
    constructor() ERC20("FeeBasedToken", "FBT") payable {
        require(msg.value == CREATION_FEE, "FeeBasedToken: Incorrect creation fee");
        _mint(msg.sender, TOTAL_SUPPLY);
        emit TokenCreated(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allows owner to withdraw collected fees
     */
    function withdrawFees() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "FeeBasedToken: No fees to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "FeeBasedToken: Withdrawal failed");
    }

    /**
     * @dev Override decimals to 18 for standard token precision
     */
    function decimals() public pure override returns (uint8) {
        return 18;
    }

    /**
     * @dev Receive function to handle direct ETH transfers
     */
    receive() external payable {
        revert("FeeBasedToken: Direct transfers not allowed");
    }

    /**
     * @dev Fallback function to handle unexpected calls
     */
    fallback() external payable {
        revert("FeeBasedToken: Invalid function call");
    }
}
```

Note: This contract assumes:
1. You're using Solidity 0.8.0 or higher
2. You have OpenZeppelin contracts installed (ERC20, Ownable, ReentrancyGuard)
3. The $1 fee is denominated in ETH (1 ether) - adjust according to your stablecoin/price oracle needs
4. For production use, you should add more comprehensive testing and consider using a proxy pattern for upgradeability
