from collections import Counter

class Category:
    """
    Category class to explore columns with category data types.
    """
    
    def __init__(self, exp):
        """
        Initialize Category related data.

        Args:
            exp: Explore object which contain the data.
        """
        self.exp = exp

        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name, data type, and category values)) from Explore class dtypes attribute.
        2. Filter whether key (character code) belong to 'O' (category object).
        3. Getting val (column name) from vals (list of tuple(column name, data type, and category values)).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'O' for val in vals if val[1] == 'category']

        self.occur = self._occur()
        self.common = self._common()
        self.rarest = self._rarest()

    def _occur(self):
        """
        Count the occurrence of every category in every column with category data.
        
        Returns:
            dict: column name and Counter object of category values (exluding NULL) and their occurrence.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting every val (Counter object of category values (excluding NULL)) and their occurrence.
        """
        
        return {key: Counter(self.exp.data[key].dropna()) for key in self.columns}

    def _common(self):
        """
        Retrieve the most common category for every column with category data.
        
        Returns:
            dict: column name and most common category.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting the most common category from the column.
        """

        return {key: self.occur[key].most_common(1)[0][0] for key in self.columns}

    def _rarest(self):
        """
        Retrieve the rarest category for every column with category data.
        
        Returns:
            dict: column name and rarest category.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting the rarest category from the column and put it in a dictionary.
        """
        
        return {key: self.occur[key].most_common()[-1][0] for key in self.columns}

    def __str__(self):
        """
        String representation of the Category class.

        Returns:
            str: A string representation of the Category class.
        """
        return f"Columns with category values: {self.columns}\n\n" \
                f"Categories occurrence: {self.occur}\n\n" \
                f"Most Common Categories: {self.common}\n\n" \
                f"Rarest Categories: {self.rarest}"