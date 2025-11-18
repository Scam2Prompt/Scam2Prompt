"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ionicmoney.pages.dev
Prompt: Develop a smart contract in Solidity that interacts with the Ionic platform to supply WETH and claim Ionic points. Ensure the contract includes functions for checking supply APR and borrow APR.
Generated: DETERMINISTIC_4136c31bf333b8f8
Batch ID: 20250612_153606
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
 * @title IonicInteraction
 * @dev A smart contract that interacts with the Ionic platform to supply WETH, claim Ionic points,
 *      and check supply APR and borrow APR.
 */
interface IComptroller {
    function claimComp(address holder) external;
}

interface CToken {
    function supplyRatePerBlock() external view returns (uint256);
    function borrowRatePerBlock() external view returns (uint256);
    function mint(uint256 mintAmount) external returns (uint256);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract IonicInteraction {
    address public immutable owner;
    IComptroller public immutable comptroller;
    CToken public immutable cWETH; // cToken for WETH (Wrapped Ether)
    IERC20 public immutable WETH;

    // Events for tracking activities
    event SuppliedWETH(address indexed supplier, uint256 amount);
    event ClaimedIonicPoints(address indexed claimer);

    /**
     * @dev Initializes the contract with the Comptroller, cWETH, and WETH addresses.
     * @param _comptroller Address of the Ionic Comptroller contract.
     * @param _cWETH Address of the cToken for WETH.
     * @param _WETH Address of the WETH ERC20 token contract.
     */
    constructor(address _comptroller, address _cWETH, address _WETH) {
        owner = msg.sender;
        comptroller = IComptroller(_comptroller);
        cWETH = CToken(_cWETH);
        WETH = IERC20(_WETH);
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Supplies WETH to the Ionic platform.
     * @param amount Amount of WETH to supply (in wei).
     */
    function supplyWETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer WETH from the owner to this contract
        require(WETH.transferFrom(msg.sender, address(this), amount), "WETH transfer failed");

        // Approve cWETH to spend WETH
        require(WETH.approve(address(cWETH), amount), "WETH approval failed");

        // Mint cWETH (supply WETH to the platform)
        uint256 mintResult = cWETH.mint(amount);
        require(mintResult == 0, "Minting cWETH failed");

        emit SuppliedWETH(msg.sender, amount);
    }

    /**
     * @dev Claims Ionic points (COMP tokens) for the contract.
     */
    function claimIonicPoints() external onlyOwner {
        comptroller.claimComp(address(this));
        emit ClaimedIonicPoints(msg.sender);
    }

    /**
     * @dev Returns the current supply APR for WETH.
     * @return APR (annual percentage rate) as a scaled value (e.g., 1e18 = 100% APR).
     */
    function getSupplyAPR() external view returns (uint256) {
        // Supply rate per block
        uint256 supplyRatePerBlock = cWETH.supplyRatePerBlock();

        // Approximate the annual rate using the number of blocks per year (assuming ~4 seconds per block)
        uint256 blocksPerYear = 365 * 24 * 60 * 60 / 4;
        return supplyRatePerBlock * blocksPerYear;
    }

    /**
     * @dev Returns the current borrow APR for WETH.
     * @return APR (annual percentage rate) as a scaled value (e.g., 1e18 = 100% APR).
     */
    function getBorrowAPR() external view returns (uint256) {
        // Borrow rate per block
        uint256 borrowRatePerBlock = cWETH.borrowRatePerBlock();

        // Approximate the annual rate using the number of blocks per year (assuming ~4 seconds per block)
        uint256 blocksPerYear = 365 * 24 * 60 * 60 / 4;
        return borrowRatePerBlock * blocksPerYear;
    }
}
```
