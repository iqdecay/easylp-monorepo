// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/LiquidityOptimization.sol";
import '../src/interfaces/INonfungiblePositionManager.sol';

contract ContractTest is Test {
    LiquidityOptimization public liquidityOptimization;
    address public constant DAI = 0x6B175474E89094C44Da98b954EedeAC495271d0F;
    address public constant USDC = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    INonfungiblePositionManager public nonfungiblePositionManager;

    function setUp() public {
        liquidityOptimization = new LiquidityOptimization(nonfungiblePositionManager);
    }

    function testMintingTokens() public {
        (uint256 tokenId, uint128 liquidity, uint256 amount0, uint256 amount1) = liquidityOptimization.mintNewPosition();
        if liquidity > 0:
            bool success = True;
        assertTrue(liquidity > 0);
    }
}
