from ctypes import alignment
from msilib.schema import AdvtExecuteSequence
from turtle import color
from matplotlib import style
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def optimize_price(df, price_range, cost):

    # fit OLS model
    print("\n\n############# in optimize_price #############")
    model = ols("Quantity ~ Price", data=df).fit()

    price = list(range(price_range[0], price_range[1], 5))
    quantity = []
    revenue = []
    for p in price:
        demand = model.params[0] + model.params[1]*p
        quantity.append(demand)
        revenue.append((p-cost)*demand)

    profit = pd.DataFrame(
        {"Price": price, "Revenue": revenue, "Quantity": quantity})

    max_value = profit.loc[(profit["Revenue"] == profit["Revenue"].max())]
    min_value = profit.loc[(profit["Revenue"] == profit["Revenue"].min())]

    print(
        f"Maximum Revenue {round(max_value['Revenue'].values[0])} at Price {round(max_value['Price'].values[0])}")

    fig, axs = plt.subplots(1, 2, figsize=(8, 5))
    fig.suptitle("Price Optimization", fontsize=16, fontweight='bold')

    sns.scatterplot(ax=axs[0], data=df, x='Price', y='Quantity')
    axs[0].plot(price, quantity, c='black', linestyle='dashed')
    axs[0].set_title("Price vs Demand", fontsize=12)

    x = profit['Price']
    y = profit['Revenue']
    sns.lineplot(ax=axs[1], x=x, y=y)
    axs[1].axvline(x[np.argmax(y)], c='red', linestyle='dotted')
    axs[1].axhline(y[np.argmax(y)], c='red', linestyle='dotted')
    axs[1].set_title("Maximizing Revenue", fontsize=12)

    plt.tight_layout()
    plt.show()
