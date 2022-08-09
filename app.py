import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pip import main
import seaborn as sns

from Python.optimize_price import optimize_price
from Python.optimize_quantity import optimize_quantity


def load_data(path):
    data = pd.read_csv(path)
    return data


if __name__ == "__main__":

    df = load_data("Data/price.csv")
    # print(df.head())
    # print(df.describe())

    price_range = [150, 400]
    cost = 80

    optimize_price(df=df, price_range=price_range, cost=cost)
    # optimize_quantity(df)
