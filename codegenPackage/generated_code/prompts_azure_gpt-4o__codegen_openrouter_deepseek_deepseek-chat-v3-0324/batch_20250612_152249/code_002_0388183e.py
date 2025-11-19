"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbvuwd5kzejblzv323edzpb2o4gl4xvjm3d2ghg5fxtp4powdsxy.ipfs.dweb.link
Prompt: Create a smart contract in Solidity that integrates with Venus Protocol to automate lending and borrowing activities, leveraging Venus Prime for superior rates.
Generated: DETERMINISTIC_0388183edd2457f8
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "./interfaces/IVToken.sol";
import "./interfaces/IVenusComptroller.sol";
import "./interfaces/IVenusPrime.sol";

contract VenusAutomator {
    using SafeERC20 for IERC20;

    // Venus Protocol addresses
    IVenusComptroller public immutable comptroller;
    IVenusPrime public immutable venusPrime;

    // Owner address
    address public owner;

    // Events
    event Deposited(address indexed user, address indexed vToken, uint256 amount);
    event Withdrawn(address indexed user, address indexed vToken, uint256 amount);
    event Borrowed(address indexed user, address indexed vToken, uint256 amount);
    event Repaid(address indexed user, address indexed vToken, uint256 amount);
    event ClaimedPrime(address indexed user);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _comptroller, address _venusPrime) {
        comptroller = IVenusComptroller(_comptroller);
        venusPrime = IVenusPrime(_venusPrime);
        owner = msg.sender;
    }

    /**
     * @dev Deposit underlying tokens to mint vTokens
     * @param vToken Address of the vToken contract
     * @param amount Amount of underlying tokens to deposit
     */
    function deposit(address vToken, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        IVToken vTokenContract = IVToken(vToken);
        IERC20 underlying = IERC20(vTokenContract.underlying());

        // Transfer tokens from user to contract
        underlying.safeTransferFrom(msg.sender, address(this), amount);

        // Approve vToken to spend underlying
        underlying.approve(vToken, amount);

        // Mint vTokens
        require(vTokenContract.mint(amount) == 0, "Mint failed");

        emit Deposited(msg.sender, vToken, amount);
    }

    /**
     * @dev Withdraw underlying tokens by redeeming vTokens
     * @param vToken Address of the vToken contract
     * @param amount Amount of underlying tokens to withdraw
     */
    function withdraw(address vToken, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        IVToken vTokenContract = IVToken(vToken);
        IERC20 underlying = IERC20(vTokenContract.underlying());

        // Redeem underlying
        require(vTokenContract.redeemUnderlying(amount) == 0, "Redeem failed");

        // Transfer tokens back to user
        underlying.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, vToken, amount);
    }

    /**
     * @dev Borrow tokens from Venus Protocol
     * @param vToken Address of the vToken to borrow
     * @param amount Amount to borrow
     */
    function borrow(address vToken, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        IVToken vTokenContract = IVToken(vToken);
        IERC20 underlying = IERC20(vTokenContract.underlying());

        // Enter the market if not already entered
        address[] memory markets = new address[](1);
        markets[0] = vToken;
        comptroller.enterMarkets(markets);

        // Borrow tokens
        require(vTokenContract.borrow(amount) == 0, "Borrow failed");

        // Transfer borrowed tokens to user
        underlying.safeTransfer(msg.sender, amount);

        emit Borrowed(msg.sender, vToken, amount);
    }

    /**
     * @dev Repay borrowed tokens
     * @param vToken Address of the vToken to repay
     * @param amount Amount to repay
     */
    function repay(address vToken, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        IVToken vTokenContract = IVToken(vToken);
        IERC20 underlying = IERC20(vTokenContract.underlying());

        // Transfer tokens from user to contract
        underlying.safeTransferFrom(msg.sender, address(this), amount);

        // Approve vToken to spend underlying
        underlying.approve(vToken, amount);

        // Repay borrow
        require(vTokenContract.repayBorrow(amount) == 0, "Repay failed");

        emit Repaid(msg.sender, vToken, amount);
    }

    /**
     * @dev Claim Venus Prime rewards
     */
    function claimPrime() external {
        venusPrime.claim();
        emit ClaimedPrime(msg.sender);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param token Address of the token contract
     * @param amount Amount to recover
     */
    function recoverERC20(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner, amount);
    }
}
```
