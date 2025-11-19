"""
Generated Code Metadata:
========================
Original URL: https://aave.network
Prompt: What are the steps to integrate Aave's GHO stablecoin into a decentralized application?
Generated: DETERMINISTIC_73237271f4865fcb
Batch ID: 20250612_160657
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IGHO is IERC20 {
    function mint(address account, uint256 amount) external;
    function burn(uint256 amount) external;
}

interface IAavePool {
    function supply(address asset, uint256 amount, address onBehalfOf, uint16 referralCode) external;
    function withdraw(address asset, uint256 amount, address to) external;
}

contract GHOManager is ReentrancyGuard {
    using Address for address;

    IGHO public ghoToken;
    IAavePool public aavePool;
    address public owner;

    event GHOMinted(address indexed user, uint256 amount);
    event GHOBurned(address indexed user, uint256 amount);
    event GHOSuppliedToAave(address indexed user, uint256 amount);
    event GHOWithdrawnFromAave(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this");
        _;
    }

    constructor(address _ghoToken, address _aavePool) {
        require(_ghoToken != address(0), "Invalid GHO token address");
        require(_aavePool != address(0), "Invalid Aave pool address");
        
        ghoToken = IGHO(_ghoToken);
        aavePool = IAavePool(_aavePool);
        owner = msg.sender;
    }

    /**
     * @dev Mints GHO tokens to the caller
     * @param amount Amount of GHO to mint
     */
    function mintGHO(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        ghoToken.mint(msg.sender, amount);
        emit GHOMinted(msg.sender, amount);
    }

    /**
     * @dev Burns GHO tokens from the caller
     * @param amount Amount of GHO to burn
     */
    function burnGHO(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(ghoToken.balanceOf(msg.sender) >= amount, "Insufficient GHO balance");
        ghoToken.burn(amount);
        emit GHOBurned(msg.sender, amount);
    }

    /**
     * @dev Supplies GHO to Aave pool
     * @param amount Amount of GHO to supply
     */
    function supplyToAave(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(ghoToken.balanceOf(msg.sender) >= amount, "Insufficient GHO balance");

        // Approve Aave pool to spend GHO
        require(ghoToken.approve(address(aavePool), amount), "Approval failed");

        // Transfer GHO to Aave pool
        aavePool.supply(address(ghoToken), amount, msg.sender, 0);
        emit GHOSuppliedToAave(msg.sender, amount);
    }

    /**
     * @dev Withdraws GHO from Aave pool
     * @param amount Amount of GHO to withdraw
     */
    function withdrawFromAave(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        aavePool.withdraw(address(ghoToken), amount, msg.sender);
        emit GHOWithdrawnFromAave(msg.sender, amount);
    }

    /**
     * @dev Transfers ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(ghoToken), "Cannot recover GHO");
        IERC20(tokenAddress).transfer(owner, amount);
    }
}
```
