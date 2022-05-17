# Notes about UniswapV3 smart contract architecture - 2022-05-17

Basically what the app needs to do is simply, for a given pair (asset0, asset1):

- Add liquidity inside of a range (minTick and maxTick)
- Determine the amount to provide (amount0, amount1)

### Sources:

- A full contract example that will be useful for us:

https://docs.uniswap.org/protocol/guides/providing-liquidity/the-full-contract

- The Periphery Contracts with the `NonFungiblePositionManager`:

https://docs.uniswap.org/protocol/reference/periphery/NonfungiblePositionManager#burn

> In `NonFungiblePositionManager`, there is no way to remove liquidity inside a range

- This means the only way to add/remove liquidity inside a range is to use the
  `NonFungiblePositionManager::mint` function with these parameters:

```solidity
  struct MintParams {
    address token0;
    address token1;
    uint24 fee;
    int24 tickLower;
    int24 tickUpper;
    uint256 amount0Desired;
    uint256 amount1Desired;
    uint256 amount0Min;
    uint256 amount1Min;
    address recipient;
    uint256 deadline;
}
```

and then use a `burn` function for removing liquidity inside a range: `UniswapV3Pool::burn`
with this signature:

```solidity
function burn(int24 tickLower, int24 tickUpper, uint128 amount)
```
