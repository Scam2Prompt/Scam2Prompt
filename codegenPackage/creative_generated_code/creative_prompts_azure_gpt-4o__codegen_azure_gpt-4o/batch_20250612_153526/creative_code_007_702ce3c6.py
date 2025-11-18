"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Develop a function in Solidity to redeem OUSD for its underlying stablecoins (DAI, USDC, USDT) at a 1:1 ratio, factoring in the 0.25% redemption fee.
Generated: DETERMINISTIC_702ce3c65e0bdfe4
Batch ID: 20250612_153526
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
 * @title OUSD Redemption Contract
 * @dev This contract allows users to redeem OUSD for its underlying stablecoins
 * (DAI, USDC, USDT) at a 1:1 ratio, factoring in a 0.25% redemption fee.
 */
contract OUSDRedemption {
    IERC20 public ousdToken; // OUSD token interface
    IERC20 public daiToken;  // DAI token interface
    IERC20 public usdcToken; // USDC token interface
    IERC20 public usdtToken; // USDT token interface

    uint256 public constant FEE_DENOMINATOR = 100000; // Used for fee calculations
    uint256 public constant REDEMPTION_FEE = 250;    // 0.25% fee (250/100000)

    address public owner; // Contract owner for administration

    event Redeemed(address indexed user, uint256 ousdAmount, uint256 daiAmount, uint256 usdcAmount, uint256 usdtAmount, uint256 fee);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token addresses.
     * @param _ousdToken Address of the OUSD token contract.
     * @param _daiToken Address of the DAI token contract.
     * @param _usdcToken Address of the USDC token contract.
     * @param _usdtToken Address of the USDT token contract.
     */
    constructor(
        address _ousdToken,
        address _daiToken,
        address _usdcToken,
        address _usdtToken
    ) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        require(_daiToken != address(0), "Invalid DAI token address");
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_usdtToken != address(0), "Invalid USDT token address");

        ousdToken = IERC20(_ousdToken);
        daiToken = IERC20(_daiToken);
        usdcToken = IERC20(_usdcToken);
        usdtToken = IERC20(_usdtToken);
        owner = msg.sender;
    }

    /**
     * @dev Redeems OUSD for its underlying stablecoins (DAI, USDC, USDT).
     * @param _ousdAmount Amount of OUSD to redeem.
     */
    function redeem(uint256 _ousdAmount) external {
        require(_ousdAmount > 0, "Redeem amount must be greater than zero");

        // Calculate redemption fee
        uint256 fee = (_ousdAmount * REDEMPTION_FEE) / FEE_DENOMINATOR;

        // Calculate net amount to redeem after fee
        uint256 netAmount = _ousdAmount - fee;

        // Ensure contract has enough stablecoins to fulfill redemption
        require(daiToken.balanceOf(address(this)) >= netAmount / 3, "Insufficient DAI liquidity");
        require(usdcToken.balanceOf(address(this)) >= netAmount / 3, "Insufficient USDC liquidity");
        require(usdtToken.balanceOf(address(this)) >= netAmount / 3, "Insufficient USDT liquidity");

        // Transfer OUSD tokens from user to contract
        require(ousdToken.transferFrom(msg.sender, address(this), _ousdAmount), "OUSD transfer failed");

        // Transfer stablecoins to user at 1:1 ratio (split evenly)
        uint256 stablecoinShare = netAmount / 3;
        require(daiToken.transfer(msg.sender, stablecoinShare), "DAI transfer failed");
        require(usdcToken.transfer(msg.sender, stablecoinShare), "USDC transfer failed");
        require(usdtToken.transfer(msg.sender, stablecoinShare), "USDT transfer failed");

        emit Redeemed(msg.sender, _ousdAmount, stablecoinShare, stablecoinShare, stablecoinShare, fee);
    }

    /**
     * @dev Allows the owner to withdraw excess stablecoins from the contract.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawExcessStablecoins(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Withdraw amount must be greater than zero");

        IERC20 token = IERC20(_token);
        require(token.transfer(owner, _amount), "Token transfer failed");
    }
}

/**
 * @dev ERC20 Interface
 * Minimal interface to interact with ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
