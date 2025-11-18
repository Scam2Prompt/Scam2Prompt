"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Write a smart contract to deploy a memecoin on Linea, ensuring compatibility with its zkEVM and leveraging its low gas fees.
Generated: DETERMINISTIC_10e70546dbeba456
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Memecoin
 * @dev A simple ERC20 token smart contract designed for deployment on Linea's zkEVM.
 *      This contract ensures compatibility with low gas fees and is optimized for production use.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Memecoin is ERC20, Ownable {
    /**
     * @dev Sets the name, symbol, and initial supply of the token.
     * @param name_ The name of the memecoin.
     * @param symbol_ The ticker symbol for the memecoin.
     * @param initialSupply_ The initial supply of tokens (in smallest denomination, i.e., wei).
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_
    ) ERC20(name_, symbol_) {
        // Mint initial supply of tokens to the deployer (owner)
        _mint(msg.sender, initialSupply_);
    }

    /**
     * @dev Allows the owner to mint new tokens.
     *      This function is restricted to the contract owner and can be used for future scalability.
     * @param account The address to receive the minted tokens.
     * @param amount The number of tokens to mint (in smallest denomination, i.e., wei).
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from an account.
     *      This function is restricted to the contract owner and can be used for token supply adjustments.
     * @param account The address from which tokens will be burned.
     * @param amount The number of tokens to burn (in smallest denomination, i.e., wei).
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```

### Deployment and Interaction Notes:
1. **Dependencies**:
   - Make sure to install `@openzeppelin/contracts` in your environment to use the `ERC20` and `Ownable` contracts.
   - Run `npm install @openzeppelin/contracts` prior to compiling the code.

2. **Gas Optimization**:
   - Linea's zkEVM is designed for low gas fees. This contract follows ERC20 standards and avoids unnecessary complexity to ensure gas efficiency.

3. **Compile and Deploy**:
   - Use tools like Hardhat or Foundry for deployment to Linea's zkEVM-compatible blockchain.
   - Specify the appropriate RPC URL for connecting to Linea.

4. **Token Parameters**:
   - During deployment, pass the desired `name`, `symbol`, and `initial supply` as arguments to the constructor.
