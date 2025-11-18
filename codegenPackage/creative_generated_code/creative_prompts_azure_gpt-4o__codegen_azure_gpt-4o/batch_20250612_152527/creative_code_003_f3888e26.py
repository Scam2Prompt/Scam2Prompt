"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linksmetagalaxy-land.pages.dev
Prompt: Create a smart contract in Solidity for managing $MEGALAND token transactions, ensuring compatibility with PancakeSwap for token trading.
Generated: DETERMINISTIC_f3888e26d341bb30
Batch ID: 20250612_152527
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

/**
 * @title MEGALAND Token Smart Contract
 * @dev ERC20-compliant token with PancakeSwap compatibility and basic transaction management
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MegaLandToken is ERC20, Ownable {
    using SafeMath for uint256;

    // PancakeSwap router address (adjust this for the correct network)
    address public pancakeSwapRouter;

    // Mapping for blacklisted addresses (e.g., prevent certain accounts from trading)
    mapping(address => bool) public blacklist;

    // Event for adding/removing from blacklist
    event BlacklistUpdated(address indexed account, bool isBlacklisted);

    /**
     * @dev Constructor sets initial token details and minting.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _totalSupply The initial supply to mint (in wei).
     * @param _router The PancakeSwap router address.
     */
    constructor(
        string memory _name, 
        string memory _symbol, 
        uint256 _totalSupply, 
        address _router
    ) ERC20(_name, _symbol) {
        require(_router != address(0), "Router address cannot be zero");
        pancakeSwapRouter = _router;

        // Mint initial supply to the owner
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Override _transfer to include blacklist check.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(
        address sender, 
        address recipient, 
        uint256 amount
    ) internal override {
        require(!blacklist[sender], "Sender is blacklisted");
        require(!blacklist[recipient], "Recipient is blacklisted");
        
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Add or remove an address from the blacklist.
     * @param account The address to add/remove from the blacklist.
     * @param isBlacklisted True to blacklist the account, false to remove it.
     */
    function updateBlacklist(address account, bool isBlacklisted) external onlyOwner {
        blacklist[account] = isBlacklisted;
        emit BlacklistUpdated(account, isBlacklisted);
    }

    /**
     * @dev Allows the owner to set a new PancakeSwap router address.
     * @param _router The new router address.
     */
    function setPancakeSwapRouter(address _router) external onlyOwner {
        require(_router != address(0), "Router address cannot be zero");
        pancakeSwapRouter = _router;
    }
}
```
