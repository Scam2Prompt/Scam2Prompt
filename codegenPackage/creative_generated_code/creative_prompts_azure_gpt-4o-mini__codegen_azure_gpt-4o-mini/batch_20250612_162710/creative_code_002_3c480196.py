"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arteratoken.lucaageadesign.com
Prompt: What are the unique features of Artera Token as an ERC-20 token, and how does it facilitate decentralized ownership in the art market?
Generated: DETERMINISTIC_3c4801968fc87cc5
Batch ID: 20250612_162710
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ArteraToken
 * @dev Implementation of the ERC20 token standard that represents ownership in the art market
 *      and facilitates decentralized ownership.
 */
contract ArteraToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping from token holder to their share of art ownership
    mapping(address => uint256) private _artOwnershipShares;

    // Event emitted when shares are distributed
    event SharesDistributed(address indexed to, uint256 shares);

    /**
     * @dev Constructor that gives the deployer all initial tokens.
     */
    constructor(uint256 initialSupply) ERC20("Artera Token", "ART") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to distribute ownership shares of art to a user.
     * @param to The address of the recipient
     * @param shares The number of shares to distribute
     */
    function distributeShares(address to, uint256 shares) external onlyOwner {
        require(to != address(0), "Cannot distribute shares to the zero address");
        require(shares > 0, "Shares must be greater than zero");

        _artOwnershipShares[to] = _artOwnershipShares[to].add(shares);
        emit SharesDistributed(to, shares);
    }

    /**
     * @dev Function to get the number of shares owned by an address.
     * @param owner The address of the token holder
     * @return The number of shares owned by the provided address
     */
    function getOwnershipShares(address owner) external view returns (uint256) {
        return _artOwnershipShares[owner];
    }

    /**
     * @dev Function to transfer tokens, overriding the default transfer function to include checks for ownership.
     * @param to The recipient of the tokens
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating success
     */
    function transfer(address to, uint256 amount) public virtual override returns (bool) {
        // Ensure that the sender has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Call the parent transfer function
        _transfer(_msgSender(), to, amount);
        return true;
    }

    /**
     * @dev Function to safely transfer tokens with custom error handling.
     * @param from The address to transfer from
     * @param to The address to transfer to
     * @param amount The amount of tokens to transfer
     */
    function safeTransfer(address from, address to, uint256 amount) external {
        require(to != address(0), "Transfer to the zero address");
        require(balanceOf(from) >= amount, "Transfer amount exceeds balance");

        _transfer(from, to, amount);
    }
}
```
