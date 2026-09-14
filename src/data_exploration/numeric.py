from pandas import qcut

class Numeric:
    """
    Numeric class to explore columns with relevant data types E.g. int, float.
    """

    def __init__(self, exp):
        """
        Initialize numeric related data.

        Args:
            exp: Explore object which contain the data.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the minimum value as value.
        """
        
        self.exp = exp

        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name, data type)) from dtypes attribute.
        2. Filter whether key (character code) belong to 'iuf' (int and float).
        3. Getting val (column name) from vals (list of tuple(column name, data type)).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'iuf' for val in vals]

        self.min = self._min()
        self.max = self._max()
        self.mean = self._mean()
        self.median = self._median()
        self.mode = self._mode()
        self.count_zero = self._count_zero()
        self.count_negative = self._count_negative()
        self.count_unique = self._count_unique()

    def count_quartile(self):
        """
        Count the size of each quartile from column with relevant data types E.g. int, float.
        
        Returns:
            list: Quartile count of every numeric column.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and count the quartile group size.
        """
        
        return [qcut(self.exp.data[val], 4, duplicates='drop').value_counts().sort_index() for val in self.columns]

    def _min(self):
        """
        Parse minimum value of column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and minimum value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the minimum value as value.
        """
        return {val: self.exp.data[val].min().round(2) for val in self.columns}

    def _max(self):
        """
        Parse maximum value of column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and maximum value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the maximum value as value.
        """
        return {val: self.exp.data[val].max().round(2) for val in self.columns}

    def _median(self):
        """
        Parse median value of column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and median value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the median value as value.
        """
        return {val: self.exp.data[val].median().round(2) for val in self.columns}

    def _mean(self):
        """
        Parse mean value of column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and mean value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the mean value as value.
        """
        return {val: self.exp.data[val].mean().round(2) for val in self.columns}

    def _mode(self):
        """
        Parse mode value of column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and mode value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the mode value as value.
        """
        
        return {val: self.exp.data[val].mode()[0] for val in self.columns}

    def _count_zero(self):
        """
        Count 0 values in column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and count of zero values parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to check whether it has zero value as value.
        """
        return {val: (self.exp.data[val] == 0).sum() for val in self.columns}

    def _count_negative(self):
        """
        Count negative values in column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and count of negative values parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to check whether it has negative value as value.
        """
        return {val: (self.exp.data[val] < 0).sum() for val in self.columns}

    def _count_unique(self):
        """
        Count unique values in column with relevant data types E.g. int, float.
        
        Returns:
            dict: Column name and count of unique values parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the count of unique values as value.
        """
        return {val: self.exp.data[val].nunique() for val in self.columns}

    def __str__(self):
        """
        String representation of the Numeric class.

        Returns:
            str: A string representation of the Numeric class.
        """
        return f"Columns with numeric values: {self.columns}\n\n" \
                f"Minimum Values: {self.min}\n\n" \
                f"Maximum Values: {self.max}\n\n" \
                f"Median Values: {self.median}\n\n" \
                f"Mean Values: {self.mean}\n\n" \
                f"Mode Values: {self.mode}\n\n" \
                f"Count of Zero Values: {self.count_zero}\n\n" \
                f"Count of Negative Values: {self.count_negative}\n\n" \
                f"Count of Unique Values: {self.count_unique}"