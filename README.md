# Excel Data Processing

This repository contains a Python script for processing Excel datasets, calculating probabilities for categorical data, and normalizing numerical data.
It is very useful for those who are using numerical datasets for Intrusion Detection systems. 
So, If your dataset contains non-numerical variables/features (string, category, ...), you can use this code and customise it to generate only numerical dataset. 
Please see the attached Excel sheet sample dataset (from KDD)

## Features

- Reads data from an Excel file.
- Calculates probabilities for protocol types, flags, and services.
- Replaces nominal values with their respective probabilities.
- Normalizes numerical data using Min-Max normalization.
- Outputs the results to CSV files.

## Requirements

- Python 3.x
- pandas
- openpyxl
- numpy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maherjas/data_processing_ids.git
   
