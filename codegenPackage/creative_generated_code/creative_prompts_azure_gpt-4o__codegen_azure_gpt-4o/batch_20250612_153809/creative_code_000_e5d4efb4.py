"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfinanciallabs.com
Prompt: Write a smart contract in Solidity to facilitate the transition of WLFI tokens to PWLFI tokens, ensuring secure and verified token transfer as described on the World Liberty Financial Labs website.
Generated: DETERMINISTIC_e5d4efb4493db037
Batch ID: 20250612_153809
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
 * @title TokenSwap
 * @dev A smart contract to facilitate the transition of WLFI tokens to PWLFI tokens securely and efficiently.
 * Users can swap WLFI for PWLFI tokens at a 1:1 ratio. The contract includes security measures and proper error handling.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TokenSwap {

    // Address of the WLFI token contract
    IERC20 public immutable WLFI;

    // Address of the PWLFI token contract
    IERC20 public immutable PWLFI;

    // Owner of the contract
    address public owner;

    // Events
    event TokensSwapped(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "TokenSwap: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with WLFI and PWLFI token addresses.
     * @param _WLFI Address of the WLFI token contract
     * @param _PWLFI Address of the PWLFI token contract
     */
    constructor(address _WLFI, address _PWLFI) {
        require(_WLFI != address(0) && _PWLFI != address(0), "TokenSwap: Invalid token addresses");
        WLFI = IERC20(_WLFI);
        PWLFI = IERC20(_PWLFI);
        owner = msg.sender;
    }

    /**
     * @dev Allows users to swap their WLFI tokens for PWLFI tokens at a 1:1 ratio.
     * @param amount The number of WLFI tokens to swap
     */
    function swapTokens(uint256 amount) external {
        require(amount > 0, "TokenSwap: Amount must be greater than zero");
        require(WLFI.balanceOf(msg.sender) >= amount, "TokenSwap: Insufficient WLFI balance");
        require(PWLFI.balanceOf(address(this)) >= amount, "TokenSwap: Insufficient PWLFI balance in contract");

        // Transfer WLFI tokens from the user to the contract
        bool wlfiTransferSuccess = WLFI.transferFrom(msg.sender, address(this), amount);
        require(wlfiTransferSuccess, "TokenSwap: WLFI transfer failed");

        // Transfer PWLFI tokens from the contract to the user
        bool pwlfiTransferSuccess = PWLFI.transfer(msg.sender, amount);
        require(pwlfiTransferSuccess, "TokenSwap: PWLFI transfer failed");

        emit TokensSwapped(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw excess PWLFI tokens from the contract.
     * @param amount The number of PWLFI tokens to withdraw
     */
    function withdrawPWLFI(uint256 amount) external onlyOwner {
        require(amount > 0, "TokenSwap: Amount must be greater than zero");
        require(PWLFI.balanceOf(address(this)) >= amount, "TokenSwap: Insufficient PWLFI balance in contract");

        bool success = PWLFI.transfer(owner, amount);
        require(success, "TokenSwap: PWLFI withdrawal failed");
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "TokenSwap: New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to reject any incoming Ether.
     */
    receive() external payable {
        revert("TokenSwap: Contract does not accept Ether");
    }
}
```
