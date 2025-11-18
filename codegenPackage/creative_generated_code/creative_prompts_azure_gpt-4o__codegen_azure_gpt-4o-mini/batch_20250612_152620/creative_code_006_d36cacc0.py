"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub.web.app
Prompt: Write a Solidity smart contract to implement the token burning mechanism described in the Bitcoin Dogs tokenomics, where unsold tokens are removed after the presale ends.
Generated: DETERMINISTIC_d36cacc0f2a92785
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BitcoinDogsToken
 * @dev ERC20 token with a burn mechanism for unsold tokens after presale
 */
contract BitcoinDogsToken is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // Initial token supply
    uint256 public presaleEndTime; // Timestamp when the presale ends
    bool public presaleEnded; // Flag to indicate if presale has ended

    // Emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    constructor(uint256 _presaleDuration) ERC20("Bitcoin Dogs", "BTCDOG") {
        // Set the initial supply and transfer to owner
        _mint(msg.sender, INITIAL_SUPPLY);
        
        // Set presale end time
        presaleEndTime = block.timestamp + _presaleDuration;
        presaleEnded = false;
    }

    /**
     * @dev Function to end the presale and burn unsold tokens.
     * Only callable by the owner and only after the presale has ended.
     */
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale has already ended");
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");

        // Calculate unsold tokens
        uint256 unsoldTokens = balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to burn");

        // Burn unsold tokens
        _burn(address(this), unsoldTokens);
        emit TokensBurned(address(this), unsoldTokens);

        // Update presale status
        presaleEnded = true;
    }

    /**
     * @dev Override the transfer function to prevent transfers during the presale.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(presaleEnded, "Transfers are not allowed during presale");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to prevent transfers during the presale.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(presaleEnded, "Transfers are not allowed during presale");
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to withdraw tokens accidentally sent to this contract.
     * Only callable by the owner.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
