class Boolean:
    """
    Boolean class to explore columns with boolean data types.
    """
    
    def __init__(self, exp):
        """
        Initialize Boolean related data.

        Args:
            exp: Explore object which contain the data.
        """
        self.exp = exp

        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name and data type) from Explore class dtypes attribute.
        2. Filter whether key (character code) belong to 'b' (boolean).
        3. Getting val (column name) from vals (list of tuple(column name and data type)).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'b' for val in vals]
        
        self.false = self._false()
        self.true = self._true()
        
    def _false(self):
        """
        Count number of boolean False.

        Returns:
            dict: column name and number of row with boolean False data.
        """
        
        """
        Dict comprehension structure:
        1. Getting key (column name) from every column.
        2. Count the boolean False.
        """
        
        return {key: (~self.exp.data[key]).sum() for key in self.columns}
        
    def _true(self):
        """
        Count number of boolean True.

        Returns:
            dict: column name and number of row with boolean True data.
        """
        
        """
        Dict comprehension structure:
        1. Getting key (column name) from every column.
        2. Count the boolean True.
        """
        
        return {key: self.exp.data[key].sum() for key in self.columns}