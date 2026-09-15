from collections import Counter

class Text:
    """
    Text class to explore columns with relevant data types E.g. string object.
    """
    
    def __init__(self, exp):
        """
        Initialize Text related data.

        Args:
            exp: Explore object which contain the data.
        """
        
        self.exp = exp
        
        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name, data type)) from dtypes attribute.
        2. Filter whether key (character code) belong to 'OST' (object, byte string, and StringDType).
        3. Getting val (column name) from vals (list of tuple(column name, data type)).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'OST' for val in vals]
        
        """
        Dict comprehension structure:
        1. Getting the length of every text from every column.
        """
        self.length = {key: self.exp.data[key].str.len() for key in self.columns}
        
        self.longest = self._longest()
        self.shortest = self._shortest()
        self.avg_length = self._avg_length()
        self.count_unique = self._count_unique()
        self.count_empty = self._count_empty()
        self.has_symbol = self._has_symbol()

    def count_occur(self):
        """
        Count occurence of every text in every column with string data.
        
        Returns:
            dict: column name and counter of text occurence.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Calculate total occurence of each text.
        """
        
        return {key: Counter(self.exp.data[key]) for key in self.columns}

    def count_symbol(self):
        """
        Count symbol occurence in every column with string data.

        Returns:
            dict: column name and boolean indicating if any text contains symbols.
        """
        
        """
        Dict comprehension structure:
        1. Getting key (column name) from every column.
        2. Check if any text contains symbols using regex.
        """
        
        return {key: self.exp.data[key].str.extractall(r'(?P<Symbol>[^a-zA-Z0-9])').groupby('Symbol').size() for key in self.columns}
        
    def _longest(self):
        """
        Retrieve the longest text by length for every row from every column with string data.
        
        Returns:
            dict: column name and list of text with the longest length.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting every val (text) with the longest text and put it in a set.
        """
        
        return {key: {val for val in self.exp.data[self.length[key] == self.length[key].max()][key]} for key in self.columns}

    def _shortest(self):
        """
        Retrieve the shortest text by length for every row from every column with string data.
        
        Returns:
            dict: column name and list of text with the shortest length.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting every val (text) with the shortest text and put it in a set.
        """
        
        return {key: {val for val in self.exp.data[self.length[key] == self.length[key].min()][key]} for key in self.columns}

    def _avg_length(self):
        """
        Retrieve the average text length for every row from every column with string data.
        
        Returns:
            dict: column name and average text length.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting average length of the text column.
        """
        
        return {key: self.exp.data[key].str.len().mean().round(2) for key in self.columns}

    def _count_unique(self):
        """
        Retrieve unique count of text for every row from every column with string data.
        
        Returns:
            dict: column name and count of unique text.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Counting unique text in the column.
        """
        
        return {key: self.exp.data[key].nunique() for key in self.columns}
    
    def _count_empty(self):
        """
        Count empty text in every column with string data.
        
        Returns:
            dict: column name and total count of row with empty text.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Calculate total number of empty text.
        """
        
        return {key: (self.exp.data[key] == '').sum() for key in self.columns}
        
    def _has_symbol(self):
        """
        Check if any text in every column with string data contains symbols.

        Returns:
            dict: column name and boolean indicating if any text contains symbols.
        """
        
        """
        Dict comprehension structure:
        1. Getting key (column name) from every column.
        2. Check if any text contains symbols using regex.
        """

        return {key: self.exp.data[key].str.contains('[^a-zA-Z0-9]', regex=True).any() for key in self.columns}

    def __str__(self):
        """
        String representation of the Text class.

        Returns:
            str: A string representation of the Text class.
        """
        return f"Columns with text values: {self.columns}\n\n" \
                f"shortest text: {self.shortest}\n\n" \
                f"longest text: {self.longest}\n\n" \
                f"Average text length: {self.avg_length}\n\n" \
                f"Count of Empty Text: {self.count_empty}\n\n" \
                f"Count of Text Occurrences: {self.count_occur}\n\n" \
                f"Has Symbols: {self.has_symbol}\n\n" \
                f"Count of Symbol Occurrences: {self.count_symbol}\n\n"