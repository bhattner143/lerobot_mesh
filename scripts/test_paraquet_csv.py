

import pandas as pd

df = pd.read_parquet('/home/dips/Documents/datasets_lerobot/so100_test_2025_05_15/data/chunk-000/episode_000000.parquet')
print(df.head())


df.to_csv('/home/dips/Documents/datasets_lerobot/so100_test_2025_05_15/data/chunk-000/episode_000000.csv', index=False)