from pytable import PyTable

table = PyTable()
table.alignmentDigits = 5
table.printHeader(variables=["ID", "NAME", "AGE"])

table.addRow([1, "Bernard", 3])
table.addRow([2, "Kalvin", 26])
table.addRow([3, "Lucas", 18])
table.addRow([4, "Albertom", 25])
table.addRow([5, "Thompson", 44])
table.addRow([6, "Augustus", 50])