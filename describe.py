import pandas as pd
import sys
import tkinter as tk
from tkinter import ttk

from mathFunctions.math import calculate_count, calculate_mean, calculate_std, \
     calculate_min, calculate_quarter, calculate_half, calculate_three_quarters, \
     calculate_max, calculate_sum

# Function to adjust column names
def adjust_column_names(df):
    # Make a copy of the DataFrame to avoid modifying the original
    df_adjusted = df.copy()
    # Limit the length of column names to 10 characters
    df_adjusted.columns = [col[:10] + ".." if len(col) > 10 else col for col in df.columns]
    return df_adjusted


# Function to check nb args
def nb_args(argv):
    if len(argv) < 2:
        print("\033[91musage: python describe.py [* .csv]")
        exit(1)

# Describe function
def ft_describe(df):
    for index, row in df.iterrows():
        for column in df.columns:
            value = row[column]
            if df[column].isna().any() or df[column].empty:
                print(f"Valeur à l'index {index}, colonne {column}: {value}")
            else:
                print("ERROR")

# Function to show descriptive statistics
def show_descriptive_stats(file):
    # Load the DataFrame from a CSV file
    df = pd.read_csv(file)
    
    # Adjust column names if necessary
    df = adjust_column_names(df)
    
    # Calculate descriptive statistics
    descriptive_stats = ft_describe(df)
    # descriptive_stats = df.describe()

    # Create a Tkinter window to display descriptive statistics
    # stats_window = tk.Tk()
    # stats_window.title("Descriptive Statistics")
    
    # Create a scrollable text area to display descriptive statistics
    # text_area = tk.Text(stats_window, wrap="none", width=1920, height=1280)
    # text_area.insert(tk.END, descriptive_stats.to_string())
    # text_area.pack(expand=True, fill="both")
    
    # Add a horizontal scrollbar
    # scrollbar_x = ttk.Scrollbar(stats_window, orient="horizontal", command=text_area.xview)
    # scrollbar_x.pack(side="bottom", fill="x")
    # text_area.config(xscrollcommand=scrollbar_x.set)
    
    # Launch the main Tkinter loop
    # stats_window.mainloop()

nb_args(sys.argv)

# Call the function to display descriptive statistics when the script is executed
show_descriptive_stats(sys.argv[1])