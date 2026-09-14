import numpy as np

# 2D array: rows = trial runs, columns = [concentration (mol/L), temperature (°C), yield (%)]
trials = np.array([
    [0.50, 25.0, 72.5],
    [0.75, 30.0, 81.2],
    [1.00, 35.0, 88.9],
    [0.60, 28.0, 76.4],
    [0.90, 40.0, 65.3],   # high temp, lower yield — worth noticing
    [1.10, 32.0, 91.7],
])

# Shape check
print(trials.shape)

# Column slicing
yield_pct = trials[:, 2]
print(f"yields of all trials: {yield_pct}")
temp_c = trials[:, 1]
print(f"temperature of all trials: {temp_c}")

# Vectorized unit conversion
temp_f = temp_c * 9/5 + 32
print(f"temperature converted to Fahrenheit: {temp_f}")

# Boolean-mask filtering
high_yield = trials[yield_pct > 80]
print(high_yield)

# Aggregate stats with reasoning
yield_mean = np.mean(yield_pct)
print(yield_mean)
yield_median = np.median(yield_pct)
print(yield_median)

# I would trust median more because mean is sensitive to outliers and median isn't.

# Correlation between temperature and yield
corr = np.corrcoef(temp_c, yield_pct)[0, 1]
print(corr)

# The correlation coefficient is negative but close to 0, suggesting temperature has little relationship with yield.
# However, the temperatures in trial 5 and 6 pull the yields in opposite ways. 

corr_trial_one_to_four = np.corrcoef(temp_c[:4], yield_pct[:4])[0, 1]
print(corr_trial_one_to_four)

# After taking trial 5 and 6 out, the correlation coefficient is close to 1, suggesting temperature has a positive correlation with yield.
# Hence, the full correlation is unstable depending on which trials you include. 