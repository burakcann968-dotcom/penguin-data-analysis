
# Penguin Dataset Analysis

## 1. Project Overview

This project explores the Penguins dataset using Python and Pandas. The goal is to understand the dataset's structure, check data quality, calculate summary statistics, and identify interesting patterns.

## 2. Dataset

The dataset contains 344 rows and 7 columns.

It includes information about penguin species, islands, bill measurements, flipper length, body mass, and sex.

## 3. Project Setup

### Requirements

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Installation

1. Download or extract the project folder.
2. Open the project folder in VS Code.
3. Create a virtual environment:

```powershell
py -m venv .venv
```

4. Activate the virtual environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install the required libraries:

```powershell
python -m pip install -r requirements.txt
```

6. Run the Python script:

```powershell
python Penguinn.py
```

## 4. Data Analysis

The analysis includes:

- Exploring the dataset structure and data types
- Identifying missing values
- Checking for duplicate rows
- Calculating summary statistics
- Counting penguin species
- Comparing average body mass by species
- Visualizing average body mass

## 5. Key Findings

- The dataset contains 344 rows and 7 columns.
- All columns contain missing values.
- The sex column has the most missing values (33).
- There are no completely duplicated rows.
- Adelie is the most common species with 145 observations.
- Gentoo penguins have the highest average body mass, approximately 5106 grams.
- Adelie and Chinstrap penguins have similar average body masses.

## 6. Visualization

A bar chart compares the average body mass of Adelie, Chinstrap, and Gentoo penguins.

The visualization shows that Gentoo penguins are noticeably heavier on average than the other two species.

## 7. Author

Burak Can

MDH University of Applied Sciences

