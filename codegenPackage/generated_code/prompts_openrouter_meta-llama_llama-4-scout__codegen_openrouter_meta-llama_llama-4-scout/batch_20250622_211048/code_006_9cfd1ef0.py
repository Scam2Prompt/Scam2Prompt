"""
Generated Code Metadata:
========================
Original URL: https://pioneerparticle-sigma.vercel.app
Prompt: Design a smart contract for managing Universal Gas Tokens across multiple blockchain ecosystems, inspired by Particle Network's solutions.
Generated: DETERMINISTIC_9cfd1ef00d431afe
Batch ID: 20250622_211048
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title UniversalGasToken
 * @author [Your Name]
 * @notice A smart contract for managing Universal Gas Tokens across multiple blockchain ecosystems.
 */
contract UniversalGasToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of blockchain ecosystems to their respective gas token balances
    mapping(string => uint256) public ecosystemBalances;

    // Mapping of blockchain ecosystems to their respective gas token addresses
    mapping(string => address) public ecosystemGasTokenAddresses;

    // Mapping of authorized minters
    mapping(address => bool) public authorizedMinters;

    /**
     * @notice Constructor for the UniversalGasToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Adds a new blockchain ecosystem to the contract.
     * @param ecosystem The name of the blockchain ecosystem.
     * @param gasTokenAddress The address of the gas token on the ecosystem.
     */
    function addEcosystem(string memory ecosystem, address gasTokenAddress) public onlyOwner {
        require(bytes(ecosystem).length > 0, "Ecosystem name cannot be empty");
        require(gasTokenAddress != address(0), "Gas token address cannot be zero");

        ecosystemGasTokenAddresses[ecosystem] = gasTokenAddress;
        ecosystemBalances[ecosystem] = 0;
    }

    /**
     * @notice Mints new tokens for a specific ecosystem.
     * @param ecosystem The name of the blockchain ecosystem.
     * @param amount The amount of tokens to mint.
     */
    function mint(string memory ecosystem, uint256 amount) public {
        require(authorizedMinters[msg.sender], "Only authorized minters can mint tokens");
        require(bytes(ecosystem).length > 0, "Ecosystem name cannot be empty");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(msg.sender, amount);
        ecosystemBalances[ecosystem] = ecosystemBalances[ecosystem].add(amount);
    }

    /**
     * @notice Burns tokens for a specific ecosystem.
     * @param ecosystem The name of the blockchain ecosystem.
     * @param amount The amount of tokens to burn.
     */
    function burn(string memory ecosystem, uint256 amount) public override {
        require(bytes(ecosystem).length > 0, "Ecosystem name cannot be empty");
        require(amount > 0, "Burn amount must be greater than zero");
        require(ecosystemBalances[ecosystem] >= amount, "Insufficient balance in ecosystem");

        ecosystemBalances[ecosystem] = ecosystemBalances[ecosystem].sub(amount);
        _burn(msg.sender, amount);
    }

    /**
     * @notice Transfers tokens between ecosystems.
     * @param fromEcosystem The source ecosystem.
     * @param toEcosystem The destination ecosystem.
     * @param amount The amount of tokens to transfer.
     */
    function transferBetweenEcosystems(string memory fromEcosystem, string memory toEcosystem, uint256 amount) public {
        require(bytes(fromEcosystem).length > 0, "Source ecosystem name cannot be empty");
        require(bytes(toEcosystem).length > 0, "Destination ecosystem name cannot be empty");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(ecosystemBalances[fromEcosystem] >= amount, "Insufficient balance in source ecosystem");

        ecosystemBalances[fromEcosystem] = ecosystemBalances[fromEcosystem].sub(amount);
        ecosystemBalances[toEcosystem] = ecosystemBalances[toEcosystem].add(amount);
    }

    /**
     * @notice Authorizes a new minter.
     * @param minter The address of the minter to authorize.
     */
    function authorizeMinter(address minter) public onlyOwner {
        require(minter != address(0), "Minter address cannot be zero");

        authorizedMinters[minter] = true;
    }

    /**
     * @notice Revokes a minter's authorization.
     * @param minter The address of the minter to revoke.
     */
    function revokeMinter(address minter) public onlyOwner {
        require(minter != address(0), "Minter address cannot be zero");

        authorizedMinters[minter] = false;
    }

    // Prevents accidental burns of tokens by contract
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal override {
        super._beforeTokenTransfer(from, to, ids);
    }
}
```
