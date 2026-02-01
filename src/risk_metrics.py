import pandas as pd

def compute_health_factor(
    collateral_amount: pd.Series,
    debt_amount: pd.Series,
    price: float,
    liquidation_threshold: float
) -> pd.Series:
    """
    Compute Health Factor (HF).
    HF = (collateral_value * LT) / debt_value
    debt_value = debt_amount (assume debt price = 1.0).
    """
    collateral_value = collateral_amount * price
    hf = (collateral_value * liquidation_threshold) / debt_amount
    return hf
