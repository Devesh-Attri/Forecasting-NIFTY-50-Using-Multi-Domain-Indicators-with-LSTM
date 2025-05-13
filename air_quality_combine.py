import pdfplumber
import pandas as pd
import os

# Define input and output directories
pdf_files = [
    "Location_data_2017.pdf",
    "Location_data_2018.pdf",
    "Location_data_2019.pdf",
    "Location_data_2020.pdf",
    "Location_data_2021.pdf",
    "Location_data_2022.pdf",
    "Location_data_2023.pdf"
]
input_folder = "Dataset/Air Quality Data"
output_folder = "air_quality_extracted_csv"

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Function to extract tables and save as CSV
def extract_tables(pdf_path, output_csv):
    with pdfplumber.open(pdf_path) as pdf:
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                all_tables.append(df)
        
        if all_tables:
            final_df = pd.concat(all_tables, ignore_index=True)
            final_df.to_csv(output_csv, index=False)
            print(f"Extracted tables saved to: {output_csv}")
        else:
            print(f"No tables found in {pdf_path}")

# Process each PDF
for pdf_file in pdf_files:
    pdf_path = os.path.join(input_folder, pdf_file)
    output_csv = os.path.join(output_folder, f"{pdf_file.replace('.pdf', '.csv')}")
    extract_tables(pdf_path, output_csv)