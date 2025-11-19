"""
Generated Code Metadata:
========================
Original URL: https://venus-protocol-ui.vercel.app
Prompt: Create a smart contract that interacts with the Venus Protocol to automate collateral supply and borrowing processes.
Generated: DETERMINISTIC_e126f6a4743d063f
Batch ID: 20250612_145706
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "./VenusProtocol.sol";

/**
 * @title Venus Auto Collateral Supply and Borrow Contract
 * @author [Your Name]
 * @notice This contract automates collateral supply and borrowing processes on the Venus Protocol.
 */
contract VenusAutoCollateral {
    using SafeMath for uint256;

    // Venus Protocol contract instance
    VenusProtocol public venusProtocol;

    // Mapping of user addresses to their collateral supply and borrow data
    mapping(address => UserData) public userData;

    // Event emitted when a user supplies collateral
    event CollateralSupplied(address indexed user, uint256 amount);

    // Event emitted when a user borrows assets
    event AssetsBorrowed(address indexed user, uint256 amount);

    // Event emitted when a user repays a borrow
    event BorrowRepaid(address indexed user, uint256 amount);

    // Event emitted when a user withdraws collateral
    event CollateralWithdrawn(address indexed user, uint256 amount);

    /**
     * @param _venusProtocol Address of the Venus Protocol contract
     */
    constructor(address _venusProtocol) public {
        require(_venusProtocol != address(0), "Venus Protocol address cannot be zero");
        venusProtocol = VenusProtocol(_venusProtocol);
    }

    /**
     * @dev Supplies collateral to the Venus Protocol
     * @param _amount Amount of collateral to supply
     */
    function supplyCollateral(uint256 _amount) public {
        require(_amount > 0, "Supply amount must be greater than zero");
        require(venusProtocol.getCollateralBalance(msg.sender) + _amount >= venusProtocol.getCollateralBalance(msg.sender), "Supply amount exceeds balance");

        // Approve Venus Protocol to spend collateral
        IERC20(venusProtocol.getCollateralToken()).approve(address(venusProtocol), _amount);

        // Supply collateral to Venus Protocol
        venusProtocol.supplyCollateral(msg.sender, _amount);

        // Update user data
        userData[msg.sender].collateralSupplied = userData[msg.sender].collateralSupplied.add(_amount);

        emit CollateralSupplied(msg.sender, _amount);
    }

    /**
     * @dev Borrows assets from the Venus Protocol
     * @param _amount Amount of assets to borrow
     * @param _borrowToken Address of the token to borrow
     */
    function borrowAssets(uint256 _amount, address _borrowToken) public {
        require(_amount > 0, "Borrow amount must be greater than zero");
        require(venusProtocol.getBorrowBalance(msg.sender, _borrowToken) + _amount >= venusProtocol.getBorrowBalance(msg.sender, _borrowToken), "Borrow amount exceeds balance");

        // Check collateral supply and LTV ratio
        require(userData[msg.sender].collateralSupplied > 0, "Collateral must be supplied before borrowing");
        require(venusProtocol.getLTVRatio(msg.sender) <= venusProtocol.getMaxLTVRatio(), "LTV ratio exceeds maximum allowed");

        // Borrow assets from Venus Protocol
        venusProtocol.borrowAssets(msg.sender, _borrowToken, _amount);

        // Update user data
        userData[msg.sender].borrowed = userData[msg.sender].borrowed.add(_amount);

        emit AssetsBorrowed(msg.sender, _amount);
    }

    /**
     * @dev Repays a borrow
     * @param _amount Amount to repay
     * @param _borrowToken Address of the token to repay
     */
    function repayBorrow(uint256 _amount, address _borrowToken) public {
        require(_amount > 0, "Repay amount must be greater than zero");
        require(venusProtocol.getBorrowBalance(msg.sender, _borrowToken) >= _amount, "Repay amount exceeds borrow balance");

        // Approve Venus Protocol to spend repayment
        IERC20(_borrowToken).approve(address(venusProtocol), _amount);

        // Repay borrow to Venus Protocol
        venusProtocol.repayBorrow(msg.sender, _borrowToken, _amount);

        // Update user data
        userData[msg.sender].borrowed = userData[msg.sender].borrowed.sub(_amount);

        emit BorrowRepaid(msg.sender, _amount);
    }

    /**
     * @dev Withdraws collateral from the Venus Protocol
     * @param _amount Amount of collateral to withdraw
     */
    function withdrawCollateral(uint256 _amount) public {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(userData[msg.sender].collateralSupplied >= _amount, "Withdraw amount exceeds collateral supplied");

        // Withdraw collateral from Venus Protocol
        venusProtocol.withdrawCollateral(msg.sender, _amount);

        // Update user data
        userData[msg.sender].collateralSupplied = userData[msg.sender].collateralSupplied.sub(_amount);

        emit CollateralWithdrawn(msg.sender, _amount);
    }

    // Struct to store user data
    struct UserData {
        uint256 collateralSupplied;
        uint256 borrowed;
    }
}
```
