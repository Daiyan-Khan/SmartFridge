```markdown
# Fridge Inventory Analysis and Visualization

This Python script analyzes fridge inventory data and creates various visualizations to gain insights into fridge activity, item interactions, and hourly trends.

## Prerequisites

Before running the script, make sure you have the following libraries installed

- numpy
- pandas
- matplotlib
- scikit-learn (for LabelEncoder)

You can install these libraries using pip

```
pip install numpy pandas matplotlib scikit-learn
```

## Usage

1. Place your fridge inventory data in a CSV file named `fridge_inventory.csv`.

2. Run the script using Python

```
python fridge_inventory_analysis.py
```

The script will generate the following visualizations

- A scatter plot showing item interactions over time.
- A pie chart displaying interactions with each item.
- A bar chart depicting fridge activity by hour.
- A stacked bar chart illustrating interactions with items by hour.

## Data Format

Ensure that your CSV file has the following columns

- `Date` Date of the interaction.
- `Time` Time of the interaction.
- `Action` Action performed (e.g., Added or Removed).
- `Item` Name of the item.

## Output

The script will generate visualizations as PNG images in the current directory.

```

