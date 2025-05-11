import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the style for better visualizations
plt.style.use('default')
sns.set_theme(style="whitegrid")
sns.set_palette("husl")

# Load the dataset
df = pd.read_csv("Rajput_travels_dataset.csv")

# Create a figure with multiple subplots
plt.figure(figsize=(20, 15))

# 1. Distribution of Total Amount
plt.subplot(2, 2, 1)
sns.histplot(data=df, x="Total_Amount", bins=30, kde=True)
plt.title("Distribution of Total Amount", fontsize=12, pad=15)
plt.xlabel("Total Amount (₹)", fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.xticks(rotation=45)

# 2. Average Total Amount by Season
plt.subplot(2, 2, 2)
season_avg = df.groupby('Season')['Total_Amount'].mean().sort_values(ascending=False)
sns.barplot(x=season_avg.index, y=season_avg.values)
plt.title("Average Total Amount by Season", fontsize=12, pad=15)
plt.xlabel("Season", fontsize=10)
plt.ylabel("Average Total Amount (₹)", fontsize=10)
plt.xticks(rotation=45)

# 3. Total Amount vs Distance
plt.subplot(2, 2, 3)
sns.scatterplot(data=df, x="Distance_km", y="Total_Amount", hue="Season", alpha=0.6)
plt.title("Total Amount vs Distance", fontsize=12, pad=15)
plt.xlabel("Distance (km)", fontsize=10)
plt.ylabel("Total Amount (₹)", fontsize=10)

# 4. Profit Distribution
plt.subplot(2, 2, 4)
sns.boxplot(data=df, y="Total_Profit")
plt.title("Distribution of Total Profit", fontsize=12, pad=15)
plt.ylabel("Total Profit (₹)", fontsize=10)

# Adjust layout and save
plt.tight_layout()
plt.savefig('comprehensive_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# Create a second figure for additional insights
plt.figure(figsize=(20, 15))

# 5. Customer Segment Analysis
plt.subplot(2, 2, 1)
segment_avg = df.groupby('Customer_Segment')['Total_Amount'].mean().sort_values(ascending=False)
sns.barplot(x=segment_avg.index, y=segment_avg.values)
plt.title("Average Total Amount by Customer Segment", fontsize=12, pad=15)
plt.xlabel("Customer Segment", fontsize=10)
plt.ylabel("Average Total Amount (₹)", fontsize=10)
plt.xticks(rotation=45)

# 6. Day of Week Analysis
plt.subplot(2, 2, 2)
day_avg = df.groupby('Day_of_Week')['Total_Amount'].mean()
sns.barplot(x=day_avg.index, y=day_avg.values)
plt.title("Average Total Amount by Day of Week", fontsize=12, pad=15)
plt.xlabel("Day of Week", fontsize=10)
plt.ylabel("Average Total Amount (₹)", fontsize=10)
plt.xticks(rotation=45)

# 7. Payment Mode Analysis
plt.subplot(2, 2, 3)
payment_counts = df['Mode_of_Payment'].value_counts()
plt.pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%')
plt.title("Distribution of Payment Modes", fontsize=12, pad=15)

# 8. Car Name Analysis
plt.subplot(2, 2, 4)
car_avg = df.groupby('Car_Name')['Total_Amount'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=car_avg.values, y=car_avg.index)
plt.title("Top 10 Cars by Average Total Amount", fontsize=12, pad=15)
plt.xlabel("Average Total Amount (₹)", fontsize=10)

# Adjust layout and save
plt.tight_layout()
plt.savefig('additional_insights.png', dpi=300, bbox_inches='tight')
plt.close()

# Print key findings
print("\n=== KEY FINDINGS AND INSIGHTS ===")
print("\n1. Revenue Analysis:")
print(f"   - Total Revenue: ₹{df['Total_Amount'].sum():,.2f}")
print(f"   - Average Transaction Value: ₹{df['Total_Amount'].mean():,.2f}")
print(f"   - Total Profit: ₹{df['Total_Profit'].sum():,.2f}")
print(f"   - Average Profit Margin: {(df['Total_Profit'].sum() / df['Total_Amount'].sum() * 100):.1f}%")

print("\n2. Seasonal Trends:")
season_stats = df.groupby('Season').agg({
    'Total_Amount': ['mean', 'count'],
    'Total_Profit': 'mean'
}).round(2)
print(season_stats)

print("\n3. Customer Segment Analysis:")
segment_stats = df.groupby('Customer_Segment').agg({
    'Total_Amount': ['mean', 'count'],
    'Total_Profit': 'mean'
}).round(2)
print(segment_stats)

print("\n4. Distance Analysis:")
print(f"   - Average Trip Distance: {df['Distance_km'].mean():.1f} km")
print(f"   - Longest Trip: {df['Distance_km'].max():.1f} km")
print(f"   - Shortest Trip: {df['Distance_km'].min():.1f} km")

print("\n5. Popular Destinations:")
print(df['Destination'].value_counts().head())

print("\n6. Payment Mode Distribution:")
print(df['Mode_of_Payment'].value_counts())

# Save the findings to a text file
with open('analysis_findings.txt', 'w') as f:
    f.write("=== RAJPUT TRAVELS DATA ANALYSIS FINDINGS ===\n\n")
    f.write("1. Revenue Analysis:\n")
    f.write(f"   - Total Revenue: ₹{df['Total_Amount'].sum():,.2f}\n")
    f.write(f"   - Average Transaction Value: ₹{df['Total_Amount'].mean():,.2f}\n")
    f.write(f"   - Total Profit: ₹{df['Total_Profit'].sum():,.2f}\n")
    f.write(f"   - Average Profit Margin: {(df['Total_Profit'].sum() / df['Total_Amount'].sum() * 100):.1f}%\n\n")
    
    f.write("2. Seasonal Trends:\n")
    f.write(season_stats.to_string())
    f.write("\n\n3. Customer Segment Analysis:\n")
    f.write(segment_stats.to_string())
    f.write("\n\n4. Distance Analysis:\n")
    f.write(f"   - Average Trip Distance: {df['Distance_km'].mean():.1f} km\n")
    f.write(f"   - Longest Trip: {df['Distance_km'].max():.1f} km\n")
    f.write(f"   - Shortest Trip: {df['Distance_km'].min():.1f} km\n\n")
    
    f.write("5. Popular Destinations:\n")
    f.write(df['Destination'].value_counts().head().to_string())
    f.write("\n\n6. Payment Mode Distribution:\n")
    f.write(df['Mode_of_Payment'].value_counts().to_string()) 