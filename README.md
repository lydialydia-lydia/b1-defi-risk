# b1-defi-risk

This repo is a small DeFi risk project focused on liquidation and bad-debt dynamics in a simple lending market: ETH collateral + USD-denominated debt.
The main idea is: under stress (price drops + oracle/execution delay), how many accounts cross HF < 1, and how much residual loss (bad debt) can form after liquidation frictions.
Because clean borrower-level position data is not always available publicly, the position book here is generated with reproducible distribution assumptions (fixed random seed), mainly to make stress testing and parameter comparisons easy.


- Build a synthetic position book (collateral sizes are heavy-tailed; borrowers cluster around a target LTV band)
- Compute Health Factor (HF) and the initial liquidatable rate under a chosen liquidation threshold (LT)
- Stress grid: price shock × delay (delay modeled as an “extra drop” proxy)
- One-step liquidation simulation with close factor / liquidation bonus / slippage → bad debt rate
- Parameter sweep on a few benchmark scenarios to compare protocol settings (“policy configs”)
- Time-path liquidation waterfall with oracle lag vs no lag (to show how lag can amplify losses)
