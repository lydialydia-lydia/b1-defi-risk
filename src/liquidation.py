import numpy as np
import pandas as pd

def simulate_one_step_liquidation(
    collateral_amount: pd.Series,
    debt_amount: pd.Series,
    price: float,
    liquidation_threshold: float,
    close_factor: float,
    liquidation_bonus: float,
    slippage: float
) -> pd.DataFrame:
    """
    One-step liquidation simulation (simplified).
    - Trigger: HF < 1
    - Liquidator repays up to close_factor * debt
    - Liquidator receives collateral with liquidation_bonus
    - Execution friction modeled as slippage haircut on collateral proceeds
    """


    #Convert collateral amount into USD value at the stressed/spot price
    collateral_value = collateral_amount * price

    hf = (collateral_value * liquidation_threshold) / debt_amount
    is_liq = hf < 1.0

    # Target repay amount (bounded by close factor)
    repay_amount = close_factor * debt_amount

    # Collateral value that can effectively be realized after frictions and bonus
    effective_collateral_value = collateral_value * (1.0 - slippage) / (1.0 + liquidation_bonus)

    # Actual repaid debt cannot exceed what collateral can cover
    actual_repaid = np.minimum(repay_amount, effective_collateral_value)

    remaining_debt = debt_amount - actual_repaid
    bad_debt = np.where(is_liq, np.maximum(remaining_debt, 0.0), 0.0)

    return pd.DataFrame({
        "hf": hf,
        "is_liquidatable": is_liq,
        "collateral_value": collateral_value,
        "effective_collateral_value": effective_collateral_value,
        "actual_repaid": actual_repaid,
        "bad_debt": bad_debt
    })
