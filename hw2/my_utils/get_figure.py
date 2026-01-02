import matplotlib.pyplot as plt
import pandas as pd
import argparse

# get CSVs' paths from command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--paths', nargs='+', required=True, help='Paths to the CSV files to compare')
parser.add_argument('--output', type=str, required=True, help='Path to save the output figure')
args = parser.parse_args()

# Read CSV files into DataFrames
dataframes = [pd.read_csv(path + '/parsed_scalars.csv') for path in args.paths]

label = 'Eval_AverageReturn'

# Create a figure
plt.figure(figsize=(10, 6))
for i, df in enumerate(dataframes):
    if label in df.columns:
        plt.plot(df['step'], df[label], label=f'Run {i+1}')
    else:
        print(f"Warning: '{label}' not found in {args.paths[i]}")

plt.xlabel('step')
plt.ylabel(label)
plt.legend()
plt.title('Comparison of Eval_AverageReturn across runs')
plt.grid(True)
plt.savefig(args.output)
print(f"Figure saved to {args.output}")