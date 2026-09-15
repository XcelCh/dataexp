import pandas as pd

from .numeric import Numeric
from .text import Text
from .category import Category
from .date import Date
from .boolean import Boolean

class Dataexp:
    """
    A class to explore and analyze a pandas DataFrame.
    """
    
    def __init__(self, data):
        """
        Initialize explore with data to be analyzed.

        Args:
            data: pandas DataFrame to be analyzed.
        """
        
        self.data = data
        self.dtypes = self._pdtypes()
        
        self.null = data.isnull().sum()
        
        self.numeric = Numeric(self)
        self.text = Text(self)
        self.category = Category(self)
        self.date = Date(self)
        self.boolean = Boolean(self)

    def _pdtypes(self):
        """
        Parse data type of every column in the DataFrame.

        Returns:
            dict: key value object of Numpy character code and lists of tuple that includes column name, data type, and category values if exist.
        """

        """
        Keys: numpy character code identifying the general data type E.g. one of 'biufcmMOSTUV'.
        Vals: Every column that belongs to the general data type in a list of tuples structure, 
              the tuple will contain column name, data type, and if exist category values.

        val_detail list comprehension structure:
        1. Getting idx (column name) from data.dtypes.
        2. Forming value of list comprehension consisting (column name, data type, and category values if exist) in a tuple data type.

        return dict comprehension structure:
        1. Getting available key (character code) from data.dtypes.
        2. Getting val (list of tuple(column name, data type, and category values if exist)) from val_detail with the same key (character code).
        """
        dtypes = self.data.dtypes
        val_detail = [(idx, dtypes[idx].name, dtypes[idx].categories.to_list()) if dtypes[idx].name == 'category' else (idx, dtypes[idx].name) for idx in dtypes.index.to_list()]
        
        return {key.kind:[val for val in val_detail if dtypes[val[0]].kind == key.kind] for key in dtypes.unique().tolist()}

    def numeric_summary(self):
        """
        Generate summary of numeric columns in the data.
        
        Returns:
            pandas DataFrame: summary of numeric columns.
        """

        return pd.DataFrame({
            'Min': self.numeric.min,
            'Max': self.numeric.max,
            'Mean': self.numeric.mean,
            'Median': self.numeric.median,
            'Mode': self.numeric.mode,
            'Count Zero': self.numeric.count_zero,
            'Count Negative': self.numeric.count_negative,
            'Count Unique': self.numeric.count_unique
            })

    def text_summary(self):
        """
        Generate summary of text columns in the data.
        
        Returns:
            pandas DataFrame: summary of text columns.
        """

        return pd.DataFrame({
            'Longest': self.text.longest,
            'Shortest': self.text.shortest,
            'Average Length': self.text.avg_length,
            'Unique Count': self.text.count_unique,
            'Empty Count': self.text.count_empty,
            'Has Symbol': self.text.has_symbol
            })

    def category_summary(self):
        """
        Generate summary of category columns in the data.
        
        Returns:
            pandas DataFrame: summary of category columns.
        """

        return pd.DataFrame({
            'Most Common': self.category.common,
            'Rarest': self.category.rarest,
            'Occurrence': self.category.occur
            })

    def date_summary(self):
        """
        Generate summary of date columns in the data.
        
        Returns:
            pandas DataFrame: summary of date columns.
        """

        return pd.DataFrame({
            'Earliest': self.date.min,
            'Latest': self.date.max,
            'Range': self.date.range
            })
            
    def bool_summary(self):
        """
        Generate summary of boolean columns in the data.
        
        Returns:
            pandas DataFrame: summary of boolean columns.
        """

        return pd.DataFrame({
            'True': self.boolean.true,
            'False': self.boolean.false
            })