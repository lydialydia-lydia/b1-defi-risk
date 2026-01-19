import numpy as np
import pandas as pd

def generate_synthetic_positions(
    n_positions: int = 10_000,
    collateral_price_init: float = 2_500.0,
    ltv_center: float = 0.62,
    ltv_spread: float = 0.08,
    collateral_logn_mu: float = 0.0,
    collateral_logn_sigma: float = 1.0,
    seed: int = 42
) -> pd.DataFrame:
    """
    Generate synthetic lending positions for a single-collateral market.

    Assumptions:
    - Collateral: ETH
    - Debt: USD stablecoin (debt price = 1.0)
    - debt_amount = collateral_value_init * target_ltv
    """
    rng = np.random.default_rng(seed)

    # Collateral sizes follow a lognormal distribution (right tail / whales)
    collateral_amount = rng.lognormal(
        mean=collateral_logn_mu,
        sigma=collateral_logn_sigma,
        size=n_positions
    )

    # Target LTV follows a normal distribution, then clipped into a valid range
    target_ltv = rng.normal(loc=ltv_center, scale=ltv_spread, size=n_positions)
    target_ltv = np.clip(target_ltv, 0.05, 0.95)

    collateral_value_init = collateral_amount * collateral_price_init
    debt_amount = collateral_value_init * target_ltv

    return pd.DataFrame({
        "position_id": np.arange(1, n_positions + 1),
        "collateral_asset": "ETH",
        "debt_asset": "USD",
        "collateral_amount": collateral_amount,
        "debt_amount": debt_amount,
        "collateral_price_init": collateral_price_init,
        "collateral_value_init": collateral_value_init,
        "target_ltv": target_ltv,
    })
