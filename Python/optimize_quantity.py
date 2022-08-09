from statsmodels.formula.api import ols


def optimize_quantity(df):
    print("\n\n############# in optimize_quantity #############\n")
    model = ols("Price ~ Quantity", data=df).fit()

    print(model.summary())
