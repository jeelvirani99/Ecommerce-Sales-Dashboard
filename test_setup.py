# Testing AI/ML Setup - No Emoji Version
print("="*50)
print("TESTING AI/ML ENVIRONMENT")
print("="*50)

# Test NumPy
try:
    import numpy as np
    print("[OK] NumPy installed - Version:", np.__version__)
except:
    print("[FAIL] NumPy NOT installed")

# Test Pandas
try:
    import pandas as pd
    print("[OK] Pandas installed - Version:", pd.__version__)
except:
    print("[FAIL] Pandas NOT installed")

# Test Matplotlib
try:
    import matplotlib
    print("[OK] Matplotlib installed - Version:", matplotlib.__version__)
except:
    print("[FAIL] Matplotlib NOT installed")

# Test Seaborn
try:
    import seaborn as sns
    print("[OK] Seaborn installed - Version:", sns.__version__)
except:
    print("[FAIL] Seaborn NOT installed")

# Test Scikit-learn
try:
    import sklearn
    print("[OK] Scikit-learn installed - Version:", sklearn.__version__)
except:
    print("[FAIL] Scikit-learn NOT installed")

# Test Jupyter
try:
    import jupyter
    print("[OK] Jupyter installed")
except:
    print("[FAIL] Jupyter NOT installed")

# Test Notebook
try:
    import notebook
    print("[OK] Notebook installed")
except:
    print("[FAIL] Notebook NOT installed")

# Simple calculation test
print("\n" + "="*50)
print("TESTING NUMPY CALCULATIONS")
print("="*50)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())

print("\n[SUCCESS] ALL SYSTEMS READY FOR AI/ML!")
print("="*50)