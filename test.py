import customized_table
print(customized_table.__version__)
from customized_table import *
import numpy as np

data = [
    ["The Shawshank Redemption", 1994, 9.3],
    ["The Dark Knight", 2008, 9.0],
    ["Batman Begins", 2005, 8.2],
    ["The Light Between Oceans", 2016, 7.2],
    ["The Empire Strikes Back", 1980, 8.7],
]

t = CustomizedTable(["Title", "Year", "Rating"], subheader_style={"background": "#eef", "color": "green"})
t.column_style(2, {"color": "value"})
t.column_style(1, {"color": "red"})

for r in data:
    t.add_row(r)
t.add_subheader(["Mean:", "", np.mean([x[2] for x in data])])

t.display_terminal(darkmode=True)
