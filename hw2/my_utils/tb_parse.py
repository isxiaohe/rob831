from tbparse import SummaryReader
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--logdir', type=str, required=True, help='Path to the TensorBoard log directory')
args = parser.parse_args()
# breakpoint()
reader = SummaryReader(args.logdir)
df = reader.scalars

new_df = pd.DataFrame()   

for tag in df['tag'].unique():
    tag_df = df[df['tag'] == tag][['step', 'value']].copy()
    tag_df = tag_df.rename(columns={'value': tag})
    if new_df.empty:
        new_df = tag_df
    else:
        new_df = pd.merge(new_df, tag_df, on='step', how='outer')

new_df = new_df.sort_values(by='step').reset_index(drop=True)
output_path = args.logdir + '/parsed_scalars.csv'
new_df.to_csv(output_path, index=False)
print(f"Parsed scalars saved to {output_path}")