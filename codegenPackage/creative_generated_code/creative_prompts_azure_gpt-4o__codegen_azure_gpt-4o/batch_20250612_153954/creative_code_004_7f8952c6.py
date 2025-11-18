"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venus-protocol-interface-gupd1px1-poyaku.4everland.app
Prompt: Write a smart contract in Solidity that interacts with the Venus Protocol to automate lending and borrowing operations.
Generated: DETERMINISTIC_7f8952c6122b5364
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title VenusProtocolAutomation
 * @dev A smart contract to automate lending and borrowing operations on the Venus Protocol.
 *      This contract interacts with the Venus Protocol's vToken contracts.
 */
interface IVToken {
    function mint(uint256 mintAmount) external returns (uint256);
    function redeem(uint256 redeemTokens) external returns (uint256);
    function borrow(uint256 borrowAmount) external returns (uint256);
    function repayBorrow(uint256 repayAmount) external returns (uint256);
    function balanceOf(address owner) external view returns (uint256);
    function underlying() external view returns (address);
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract VenusProtocolAutomation {
    address public owner;

    // Venus vToken contract address
    IVToken public vToken;

    // Event declarations for monitoring contract activity
    event SuppliedToVenus(uint256 amount);
    event RedeemedFromVenus(uint256 amount);
    event BorrowedFromVenus(uint256 amount);
    event RepaidBorrow(uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _vToken Address of the Venus vToken contract.
     */
    constructor(address _vToken) {
        owner = msg.sender;
        vToken = IVToken(_vToken);
    }

    /**
     * @dev Supply tokens to Venus for lending.
     * @param amount Amount of underlying tokens to supply.
     */
    function supplyToVenus(uint256 amount) external onlyOwner {
        address underlying = vToken.underlying();
        IERC20(underlying).transferFrom(msg.sender, address(this), amount);
        IERC20(underlying).approve(address(vToken), amount);

        uint256 result = vToken.mint(amount);
        require(result == 0, "Failed to supply tokens to Venus");

        emit SuppliedToVenus(amount);
    }

    /**
     * @dev Redeem tokens from Venus.
     * @param amount Amount of vTokens to redeem.
     */
    function redeemFromVenus(uint256 amount) external onlyOwner {
        uint256 result = vToken.redeem(amount);
        require(result == 0, "Failed to redeem tokens from Venus");

        emit RedeemedFromVenus(amount);
    }

    /**
     * @dev Borrow tokens from Venus.
     * @param amount Amount of underlying tokens to borrow.
     */
    function borrowFromVenus(uint256 amount) external onlyOwner {
        uint256 result = vToken.borrow(amount);
        require(result == 0, "Failed to borrow tokens from Venus");

        emit BorrowedFromVenus(amount);
    }

    /**
     * @dev Repay borrowed tokens to Venus.
     * @param amount Amount of underlying tokens to repay.
     */
    function repayBorrowToVenus(uint256 amount) external onlyOwner {
        address underlying = vToken.underlying();
        IERC20(underlying).transferFrom(msg.sender, address(this), amount);
        IERC20(underlying).approve(address(vToken), amount);

        uint256 result = vToken.repayBorrow(amount);
        require(result == 0, "Failed to repay borrow to Venus");

        emit RepaidBorrow(amount);
    }

    /**
     * @dev Get the vToken balance of this contract.
     * @return Balance of vTokens held by this contract.
     */
    function getVTokenBalance() external view returns (uint256) {
        return vToken.balanceOf(address(this));
    }

    /**
     * @dev Change the owner of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
