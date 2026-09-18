# dataexp

`dataexp` is a lightweight Python library for quickly exploring a pandas DataFrame. Point it at your data and get instant summary statistics broken down by column type — numeric, text, category, date, and boolean — without writing repetitive `.describe()` / `.value_counts()` boilerplate every time.

## Features

- **Automatic column type detection** — columns are grouped by their underlying dtype (numeric, text, category, date, boolean) as soon as you create a `Dataexp` object.
- **One-line summaries** per data type:
  - `numeric_summary()` — min, max, mean, median, mode, count of zeros, count of negatives, count of unique values
  - `text_summary()` — longest/shortest string, average length, unique count, empty count, whether a column contains symbols
  - `category_summary()` — most common value, rarest value, occurrence counts
  - `date_summary()` — earliest date, latest date, date range
  - `bool_summary()` — count of `True` / `False` values
- **Deeper, on-demand inspection** for specific types, e.g. quartile counts for numeric columns or value occurrence counts for text columns.
- **Null count** for every column, available out of the box (`.null`).

## Installation

`dataexp` is available on [PyPI](https://pypi.org/project/dataexp/). Install it with [uv](https://docs.astral.sh/uv/) (recommended) or pip:

```bash
# with uv
uv add dataexp

# with pip
pip install dataexp
```

Or clone the repo and install it in editable mode for local development:

```bash
git clone https://github.com/<your-username>/dataexp.git
cd dataexp
uv sync
```

### Requirements

- Python >= 3.11
- pandas >= 3.0.5
- python-dateutil >= 2.9.0

## Quick start

```python
import seaborn as sns
from dataexp import Dataexp

df = sns.load_dataset('titanic')
exp = Dataexp(df)

print(exp.numeric_summary())
print(exp.text_summary())
print(exp.category_summary())
print(exp.date_summary())
print(exp.bool_summary())
```

Each `*_summary()` method returns a pandas DataFrame indexed by column name, so it prints and slices just like any other DataFrame:

```python
>>> exp.numeric_summary()
          Min    Max   Mean  Median  Mode  Count Zero  Count Negative  Count Unique
survived  0.0    1.0   0.38  0.0     0.0   549         0               2
pclass    1.0    3.0   2.31  3.0     3.0   0           0               3
age       0.42   80.0  29.7  28.0    24.0  0           0               88
...
```

## Usage

### Checking for missing values

```python
exp.null
```

Returns a pandas Series with the count of missing values per column.

### Working with a specific data type

Each type also has its own object (`.numeric`, `.text`, `.category`, `.date`, `.boolean`) if you want more detail than the summary table provides, or want to print a readable text report:

```python
print(exp.numeric)   # detailed __str__ report of every numeric metric
print(exp.text)
print(exp.date)
```

### Numeric quartile counts

```python
exp.numeric.count_quartile()
```

Returns a list of value counts (one per numeric column), showing how many rows fall into each quartile.

### Text occurrence and symbol counts

```python
exp.text.count_occur()   # dict: column name -> Counter of value occurrences
exp.text.count_symbol()  # dict: column name -> count of values containing symbols
```

## License

Licensed under the MIT License — see [LICENSE](LICENSE) for details. Includes third-party license notices for [pandas](LICENSES/PANDAS_LICENSE) and [python-dateutil](LICENSES/DATEUTIL_LICENSE).
