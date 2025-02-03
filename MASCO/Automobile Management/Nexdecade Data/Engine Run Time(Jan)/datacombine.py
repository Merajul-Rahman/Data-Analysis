import os
import pandas as pd

folder_path = r"E:\OneDrive - Masco Group\Desktop\VTS\Nexdecade data\Engine Run Time(Jan)"  # Folder path
excel_files = [file for file in os.listdir(folder_path) if file.endswith(".xls")]

all_data = []

for file in excel_files:
    file_path = os.path.join(folder_path, file)

    try:
        # Read HTML table
        tables = pd.read_html(file_path, skiprows=8, header=0)
        for table in tables:
            # Keep only relevant columns if available
            if set(["Vehicle", "Date", "Duration"]).issubset(table.columns):
                filtered_table = table[
                    ~table["Vehicle"].str.contains("Total Number of Engine Run Time", na=False)
                    & ~table["Vehicle"].str.contains("Total Duration", na=False)
                ]
                all_data.append(filtered_table[["Vehicle", "Date", "Duration"]])
    except Exception as e:
        print(f"Error reading file {file}: {e}")
        continue

# Combine all data
if all_data:
    final_data = pd.concat(all_data, ignore_index=True)
    print(final_data)
    output_file = "combined_data_jan.xlsx"  # Change this to your desired output file name
    final_data.to_excel(output_file, index=False)

    print(f"All data combined and saved to {output_file}")
else:
    print("No valid data found.")
