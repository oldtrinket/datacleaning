#Data Cleaning Repository! 

Each folder contains:

- **Raw Data**: Stored in `.xlsx` file;
- **Data Cleaning**: Utilizes Python scripts to clean the data.
- **Cleaned Data**: Outputs are converted to `.csv` file.

## Repository Structure

- **Raw Data**: Contains the original, unprocessed Excel files (.xlsx).
  - *Example: `sales_data_2023.xlsx`*
  
- **scripts/**: Python scripts used for data cleaning.
  - *Example: `dataclean1.py`*
  
- **clean_data/**: Cleaned data saved as CSV files after processing.
  - *Example: `data_cleaned1.csv`*


### Dependencies

- Python 3.x
- pandas
- openpyxl (for reading Excel files)

Please install these dependencies using pip:

```bash
pip install pandas openpyxl
