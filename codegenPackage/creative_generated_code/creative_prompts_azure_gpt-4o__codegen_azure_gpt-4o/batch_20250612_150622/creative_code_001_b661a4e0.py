"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-route.pages.dev
Prompt: Generate an example of an Ethereum smart contract that interacts with the Origin vault to mint OUSD using DAI, USDC, or USDT as collateral.
Generated: DETERMINISTIC_b661a4e08de5df25
Batch ID: 20250612_150622
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

// Import interfaces for interacting with ERC20 tokens and the Origin Vault
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IOriginVault {
    function mint(address asset, uint256 amount, uint256 minOusdAmount) external;
}

// Smart contract to interact with the Origin Vault and mint OUSD using stablecoins
contract OUSDMinter {
    // Address of the Origin Vault contract
    address public originVault;

    // Supported stablecoin addresses
    address public dai;
    address public usdc;
    address public usdt;

    // Event emitted when OUSD is minted
    event OUSDMinted(address indexed user, address indexed stablecoin, uint256 stablecoinAmount, uint256 ousdAmount);

    // Constructor to initialize the Origin Vault and stablecoin addresses
    constructor(address _originVault, address _dai, address _usdc, address _usdt) {
        require(_originVault != address(0), "Invalid Origin Vault address");
        require(_dai != address(0), "Invalid DAI address");
        require(_usdc != address(0), "Invalid USDC address");
        require(_usdt != address(0), "Invalid USDT address");

        originVault = _originVault;
        dai = _dai;
        usdc = _usdc;
        usdt = _usdt;
    }

    /**
     * @dev Mint OUSD using a specified stablecoin as collateral.
     * @param stablecoin Address of the stablecoin (DAI, USDC, or USDT).
     * @param amount Amount of stablecoin to deposit.
     * @param minOusdAmount Minimum OUSD amount expected from the minting process.
     */
    function mintOUSD(address stablecoin, uint256 amount, uint256 minOusdAmount) external {
        // Ensure the provided stablecoin is supported
        require(stablecoin == dai || stablecoin == usdc || stablecoin == usdt, "Unsupported stablecoin");

        // Transfer the specified stablecoin from the caller to this contract
        IERC20(stablecoin).transferFrom(msg.sender, address(this), amount);

        // Approve the Origin Vault to spend the stablecoin
        IERC20(stablecoin).approve(originVault, amount);

        // Mint OUSD by interacting with the Origin Vault
        IOriginVault(originVault).mint(stablecoin, amount, minOusdAmount);

        // Emit an event indicating successful minting
        emit OUSDMinted(msg.sender, stablecoin, amount, minOusdAmount);
    }

    /**
     * @dev Withdraw accidentally sent tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param to Address to send the tokens to.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(IERC20(token).transfer(to, amount), "Token transfer failed");
    }
}
```
