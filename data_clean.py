def data_clean(x):
    x = x.dropna(axis=0, subset=['fwci_2020', 'oitjp_10_2020', 'pub_2020'])
    return x