import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def print_dataset_info(df, dataset_name):
    print(f"\n{'='*50}")
    print(f"{dataset_name} Dataset Metadata")
    print(f"{'='*50}")
    print("\n1. Basic Information:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\n2. Column Data Types:")
    print(df.dtypes)
    print("\n3. Missing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0] if any(missing > 0) else "No missing values found")
    print("\n4. Memory Usage:")
    print(df.memory_usage(deep=True).sum() / 1024**2, "MB")
    print("\n5. Sample Data (First 5 rows):")
    print(df.head())
    print("\n6. Descriptive Statistics:")
    print(df.describe())

def create_metadata_visualizations(df, dataset_name):
    # Create figure for metadata visualizations
    plt.figure(figsize=(15, 10))
    
    # 1. Missing Values Heatmap
    plt.subplot(2, 2, 1)
    sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
    plt.title(f'Missing Values in {dataset_name}')
    
    # 2. Data Types Distribution
    plt.subplot(2, 2, 2)
    dtype_counts = df.dtypes.value_counts()
    plt.pie(dtype_counts.values, labels=dtype_counts.index, autopct='%1.1f%%')
    plt.title(f'Data Types Distribution in {dataset_name}')
    
    # 3. Column-wise Non-Null Count
    plt.subplot(2, 2, 3)
    non_null_counts = df.count()
    sns.barplot(x=non_null_counts.values, y=non_null_counts.index)
    plt.title(f'Non-Null Counts per Column in {dataset_name}')
    plt.xlabel('Count')
    
    # 4. Memory Usage by Column
    plt.subplot(2, 2, 4)
    memory_usage = df.memory_usage(deep=True)[1:]  # Exclude index
    plt.barh(df.columns, memory_usage / 1024**2)
    plt.title(f'Memory Usage by Column in {dataset_name} (MB)')
    plt.xlabel('Memory Usage (MB)')
    
    plt.tight_layout()
    plt.savefig(f'{dataset_name.lower().replace(" ", "_")}_metadata.png', dpi=300, bbox_inches='tight')
    plt.close()

# Read the datasets
excel_file = 'Fabric_Business_Dataset_2025.xlsx'
orders_df = pd.read_excel(excel_file, sheet_name='Order Summary')
order_details_df = pd.read_excel(excel_file, sheet_name='Order Details')
monthly_summary_df = pd.read_excel(excel_file, sheet_name='Monthly Summary')

# Analyze Order Summary dataset
print_dataset_info(orders_df, "Order Summary")
create_metadata_visualizations(orders_df, "Order Summary")

# Analyze Order Details dataset
print_dataset_info(order_details_df, "Order Details")
create_metadata_visualizations(order_details_df, "Order Details")

# Analyze Monthly Summary dataset
print_dataset_info(monthly_summary_df, "Monthly Summary")
create_metadata_visualizations(monthly_summary_df, "Monthly Summary")

print("\nMetadata analysis completed!")
print("Generated visualization files:")
print("1. order_summary_metadata.png")
print("2. order_details_metadata.png")
print("3. monthly_summary_metadata.png") 