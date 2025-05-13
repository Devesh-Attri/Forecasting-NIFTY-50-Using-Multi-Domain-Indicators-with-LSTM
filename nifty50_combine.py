import pandas as pd
import os

def combine_nifty50_data(data_directory="Dataset/Nifty 50 Raw Data/", output_file="combined_nifty50_data.csv"):
    """
    Combines Nifty 50 CSV files into a single time series CSV.

    Args:
        data_directory (str): The directory containing the Nifty 50 CSV files.
        output_file (str): The name of the output CSV file.
    """

    all_files = sorted([f for f in os.listdir(data_directory) if f.startswith("NIFTY 50-") and f.endswith(".csv")])
    dfs = []

    for file in all_files:
        file_path = os.path.join(data_directory, file)
        try:
            df = pd.read_csv(file_path)

            # Normalize column names (remove spaces and convert to lowercase for consistency)
            df.columns = df.columns.str.strip()  

            dfs.append(df)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except pd.errors.EmptyDataError:
            print(f"Empty data file: {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)

        # Ensure 'Date' column exists and convert it to datetime format
        if 'Date' in combined_df.columns:
            combined_df['Date'] = pd.to_datetime(combined_df['Date'], errors='coerce')
            combined_df = combined_df.sort_values(by='Date')

            # Save the combined DataFrame to a CSV file
            combined_df.to_csv(output_file, index=False)
            print(f"Combined data saved to {output_file}")
        else:
            print("No 'Date' column found in the dataframes. Unable to combine.")
    else:
        print("No valid data files found.")

# Execute the function
combine_nifty50_data()