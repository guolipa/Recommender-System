import numpy as np
import pandas as pd

def data_business(filename):
    business = pd.read_csv(filename, encoding='latin-1')