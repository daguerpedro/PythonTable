from pytable import PyTable

# Init the table
table = PyTable()

table.alignmentDigits = 12 # Digits per word
table.printHeader(['REAL', 'SAMPLE', 'SAMPLE ERROR'])  # Table HEADER

# EXAMPLE DATA
real = [45.8, 72.3, 90.2, 141.8, 191.4, 205.9, 306.0]
sample = [38.7, 66.6, 86.0, 137.6, 188.1, 203.2, 305.3]

# PRINT EACH VALUE
for i in range(len(real)):
    _real = real[i] 
    _analog = sample[i] 

    eanalog = round(abs(_real - _analog)/_real * 100, 2)

    # PRINT TO THE TABLE
    table.addRow([_real, _analog, str(eanalog) + '%']) 
