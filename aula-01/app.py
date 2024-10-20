import pandas as pd
import site

# valores1 = [10, 5, 23, 33, 55, 66, 77]
# valores2 = [14, 5523, 335, 55]

# ps1 = pd.Series(valores1)
# ps2 = pd.Series(valores2)


def media(vlr: list) -> float:
    s = 0
    for item in vlr:
        s += item

    return (s / len(vlr))


# print(media(valores1))
# print(media(valores2))

print(site.getsitepackages())

# print(ps1.mode())
# # print(ps1.median())
# # print(ps1.mean())
# print(ps1.describe())


# Leitura do arquivo CSV
df = pd.read_csv("vendas.csv")
# df = pd.read_csv("vendas.csv")

# Salvando o DataFrame como arquivo Parquet
df.to_parquet('vendas.parquet')
