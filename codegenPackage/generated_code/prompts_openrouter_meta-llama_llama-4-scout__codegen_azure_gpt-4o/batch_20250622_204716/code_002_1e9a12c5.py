"""
Generated Code Metadata:
========================
Original URL: https://wowx.io
Prompt: "Design a smart contract on the Ethereum blockchain to distribute listing fees to WOWX token holders."
Generated: DETERMINISTIC_1e9a12c53aeeb4b5
Batch ID: 20250622_204716
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

/**
 * @title ListingFeeDistributor
 * @dev A smart contract to distribute listing fees to WOWX token holders.
 */
contract ListingFeeDistributor {
    // Address of the WOWX token contract
    address public wowxToken;

    // Owner of the contract
    address public owner;

    // Event emitted when fees are distributed
<<<<<<< HEAD
    event FeesDistributed(uint256 totalAmount, uint256 holderCount);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the owner.
     */
=======
    event FeesDistributed(uint256 totalFees, uint256 totalHolders);

    // Modifier to restrict access to the owner
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _wowxToken Address of the WOWX token contract.
     */
    constructor(address _wowxToken) {
        require(_wowxToken != address(0), "Invalid token address");
        wowxToken = _wowxToken;
        owner = msg.sender;
    }

    /**
<<<<<<< HEAD
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to distribute listing fees to WOWX token holders.
     * @param holders Array of WOWX token holder addresses.
     * @param balances Array of WOWX token balances corresponding to the holders.
     * @notice The sum of balances should equal the total supply of WOWX tokens.
     */
    function distributeFees(address[] calldata holders, uint256[] calldata balances) external payable onlyOwner {
        require(holders.length == balances.length, "Holders and balances length mismatch");
        require(msg.value > 0, "No fees provided for distribution");

        uint256 totalSupply = 0;

        // Calculate the total supply of WOWX tokens
        for (uint256 i = 0; i < balances.length; i++) {
            totalSupply += balances[i];
        }

        require(totalSupply > 0, "Total supply must be greater than zero");

        // Distribute the fees proportionally to the token holders
        for (uint256 i = 0; i < holders.length; i++) {
            uint256 share = (msg.value * balances[i]) / totalSupply;
            (bool success, ) = holders[i].call{value: share}("");
            require(success, "Fee transfer failed");
        }

        emit FeesDistributed(msg.value, holders.length);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
=======
     * @dev Function to distribute listing fees to WOWX token holders.
     * @param totalFees The total amount of fees to distribute.
     */
    function distributeFees(uint256 totalFees) external payable onlyOwner {
        require(totalFees > 0, "Fees must be greater than zero");
        require(msg.value == totalFees, "Insufficient Ether sent");

        // Interface to interact with the WOWX token contract
        IERC20 wowx = IERC20(wowxToken);

        // Get the total supply of WOWX tokens
        uint256 totalSupply = wowx.totalSupply();
        require(totalSupply > 0, "No WOWX tokens in circulation");

        // Iterate through all token holders and distribute fees proportionally
        uint256 totalHolders = 0;
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = wowx.holderAt(i); // Assuming holderAt() exists in the WOWX token contract
            uint256 balance = wowx.balanceOf(holder);
            if (balance > 0) {
                uint256 holderShare = (balance * totalFees) / totalSupply;
                payable(holder).transfer(holderShare);
                totalHolders++;
            }
        }

        emit FeesDistributed(totalFees, totalHolders);
    }

    /**
     * @dev Function to update the WOWX token contract address.
     * @param _wowxToken The new WOWX token contract address.
     */
    function updateTokenAddress(address _wowxToken) external onlyOwner {
        require(_wowxToken != address(0), "Invalid token address");
        wowxToken = _wowxToken;
    }

    /**
     * @dev Function to withdraw any remaining Ether in the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner).transfer(balance);
    }
}

/**
 * @dev Interface for the WOWX token contract.
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function holderAt(uint256 index) external view returns (address); // Assuming this function exists
}
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
