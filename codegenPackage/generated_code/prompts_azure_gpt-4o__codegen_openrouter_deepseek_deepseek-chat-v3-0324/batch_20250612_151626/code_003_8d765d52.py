"""
Generated Code Metadata:
========================
Original URL: https://testnet-git-refactor-use-contracts-package-venus-protocol.vercel.app
Prompt: Write a function in Solidity to interact with Venus Protocol's algorithmic money market for depositing assets and earning interest.
Generated: DETERMINISTIC_8d765d52267eb458
Batch ID: 20250612_151626
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

// Interface for Venus VToken
interface IVToken {
    function mint(uint mintAmount) external returns (uint);
    function redeem(uint redeemTokens) external returns (uint);
    function redeemUnderlying(uint redeemAmount) external returns (uint);
    function borrow(uint borrowAmount) external returns (uint);
    function repayBorrow(uint repayAmount) external returns (uint);
    function balanceOf(address owner) external view returns (uint);
    function borrowBalanceCurrent(address account) external returns (uint);
    function underlying() external view returns (address);
}

// Interface for Venus Comptroller
interface IComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint[] memory);
    function exitMarket(address vToken) external returns (uint);
    function getAccountLiquidity(address account) external view returns (uint, uint, uint);
}

contract VenusInteraction {
    IComptroller public comptroller;
    address public admin;

    event Deposit(address indexed user, address indexed vToken, uint amount);
    event Withdraw(address indexed user, address indexed vToken, uint amount);
    event Borrow(address indexed user, address indexed vToken, uint amount);
    event Repay(address indexed user, address indexed vToken, uint amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this");
        _;
    }

    constructor(address _comptroller) {
        comptroller = IComptroller(_comptroller);
        admin = msg.sender;
    }

    /**
     * @dev Deposit assets into Venus Protocol
     * @param vToken Address of the VToken contract
     * @param amount Amount of underlying asset to deposit
     */
    function deposit(address vToken, uint amount) external {
        IVToken vTokenContract = IVToken(vToken);
        address underlyingAsset = vTokenContract.underlying();
        
        // Transfer underlying asset from user to this contract
        (bool success, ) = underlyingAsset.call(
            abi.encodeWithSignature(
                "transferFrom(address,address,uint256)",
                msg.sender,
                address(this),
                amount
            )
        );
        require(success, "Transfer failed");

        // Approve VToken to spend underlying asset
        (success, ) = underlyingAsset.call(
            abi.encodeWithSignature(
                "approve(address,uint256)",
                vToken,
                amount
            )
        );
        require(success, "Approval failed");

        // Enter market if not already
        address[] memory markets = new address[](1);
        markets[0] = vToken;
        comptroller.enterMarkets(markets);

        // Mint VTokens
        uint result = vTokenContract.mint(amount);
        require(result == 0, "Minting failed");

        emit Deposit(msg.sender, vToken, amount);
    }

    /**
     * @dev Withdraw assets from Venus Protocol
     * @param vToken Address of the VToken contract
     * @param amount Amount of underlying asset to withdraw
     */
    function withdraw(address vToken, uint amount) external {
        IVToken vTokenContract = IVToken(vToken);
        
        // Redeem underlying
        uint result = vTokenContract.redeemUnderlying(amount);
        require(result == 0, "Redemption failed");

        // Transfer underlying asset back to user
        address underlyingAsset = vTokenContract.underlying();
        (bool success, ) = underlyingAsset.call(
            abi.encodeWithSignature(
                "transfer(address,uint256)",
                msg.sender,
                amount
            )
        );
        require(success, "Transfer failed");

        emit Withdraw(msg.sender, vToken, amount);
    }

    /**
     * @dev Borrow assets from Venus Protocol
     * @param vToken Address of the VToken contract
     * @param amount Amount of underlying asset to borrow
     */
    function borrow(address vToken, uint amount) external {
        IVToken vTokenContract = IVToken(vToken);
        
        // Borrow assets
        uint result = vTokenContract.borrow(amount);
        require(result == 0, "Borrow failed");

        // Transfer borrowed asset to user
        address underlyingAsset = vTokenContract.underlying();
        (bool success, ) = underlyingAsset.call(
            abi.encodeWithSignature(
                "transfer(address,uint256)",
                msg.sender,
                amount
            )
        );
        require(success, "Transfer failed");

        emit Borrow(msg.sender, vToken, amount);
    }

    /**
     * @dev Repay borrowed assets to Venus Protocol
     * @param vToken Address of the VToken contract
     * @param amount Amount of underlying asset to repay
     */
    function repay(address vToken, uint amount) external {
        IVToken vTokenContract = IVToken(vToken);
        address underlyingAsset = vTokenContract.underlying();
        
        // Transfer underlying asset from user to this contract
        (bool success, ) = underlyingAsset.call(
            abi.encodeWithSignature(
                "transferFrom(address,address,uint256)",
                msg.sender,
                address(this),
                amount
            )
        );
        require(success, "Transfer failed");

        // Approve VToken to spend underlying asset
        (success, ) = underlyingAsset.call(
            abi.encodeWithSignature(
                "approve(address,uint256)",
                vToken,
                amount
            )
        );
        require(success, "Approval failed");

        // Repay borrow
        uint result = vTokenContract.repayBorrow(amount);
        require(result == 0, "Repayment failed");

        emit Repay(msg.sender, vToken, amount);
    }

    /**
     * @dev Get user's VToken balance
     * @param vToken Address of the VToken contract
     * @param user Address of the user
     * @return Balance of VTokens
     */
    function getVTokenBalance(address vToken, address user) external view returns (uint) {
        return IVToken(vToken).balanceOf(user);
    }

    /**
     * @dev Get user's borrow balance
     * @param vToken Address of the VToken contract
     * @param user Address of the user
     * @return Borrow balance
     */
    function getBorrowBalance(address vToken, address user) external returns (uint) {
        return IVToken(vToken).borrowBalanceCurrent(user);
    }

    /**
     * @dev Change the admin of the contract
     * @param newAdmin Address of the new admin
     */
    function changeAdmin(address newAdmin) external onlyAdmin {
        admin = newAdmin;
    }
}
```
