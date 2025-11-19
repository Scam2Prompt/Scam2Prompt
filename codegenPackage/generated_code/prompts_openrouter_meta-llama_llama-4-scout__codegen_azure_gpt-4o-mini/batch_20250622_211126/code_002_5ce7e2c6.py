"""
Generated Code Metadata:
========================
Original URL: https://on-oeth.pages.dev
Prompt: Generate a code example in Solidity to create a simple smart contract that utilizes the OUSD stablecoin and Morpho's peer-to-peer lending protocol to earn yield.
Generated: DETERMINISTIC_5ce7e2c66dc73de6
Batch ID: 20250622_211126
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

// Importing the OUSD interface and Morpho lending interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the OUSD stablecoin
interface IOUSD is IERC20 {
    function mint(address to, uint256 amount) external;
    function redeem(address to, uint256 amount) external;
}

// Interface for Morpho's lending protocol
interface IMorpho {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
}

contract OUSDYieldFarm is Ownable {
    // State variables
    IOUSD public ousd; // OUSD token contract
    IMorpho public morpho; // Morpho lending protocol contract
    address public asset; // The asset to be supplied to Morpho

    // Events
    event SuppliedToMorpho(address indexed user, uint256 amount);
    event WithdrawnFromMorpho(address indexed user, uint256 amount);

    // Constructor to initialize the contract with OUSD and Morpho addresses
    constructor(address _ousd, address _morpho, address _asset) {
        require(_ousd != address(0), "Invalid OUSD address");
        require(_morpho != address(0), "Invalid Morpho address");
        require(_asset != address(0), "Invalid asset address");

        ousd = IOUSD(_ousd);
        morpho = IMorpho(_morpho);
        asset = _asset;
    }

    // Function to supply OUSD to Morpho for yield earning
    function supplyToMorpho(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer OUSD from the user to this contract
        require(ousd.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the Morpho contract to spend the OUSD
        require(ousd.approve(address(morpho), amount), "Approval failed");

        // Supply the OUSD to Morpho
        morpho.supply(address(ousd), amount);

        emit SuppliedToMorpho(msg.sender, amount);
    }

    // Function to withdraw OUSD from Morpho
    function withdrawFromMorpho(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw the OUSD from Morpho
        morpho.withdraw(address(ousd), amount);

        // Transfer the OUSD back to the owner
        require(ousd.transfer(msg.sender, amount), "Transfer failed");

        emit WithdrawnFromMorpho(msg.sender, amount);
    }

    // Function to get the balance of OUSD held by this contract
    function getOUSDBalance() external view returns (uint256) {
        return ousd.balanceOf(address(this));
    }
}
```
