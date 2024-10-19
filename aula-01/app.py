import pandas as pd
import site

valores1 = [10, 5, 23, 33, 55, 66, 77]
valores2 = [14, 5523, 335, 55]


def media(vlr: list) -> float:
    s = 0
    for item in vlr:
        s += item

    return (s / len(vlr))


print(media(valores1))
print(media(valores2))

print(site.getsitepackages())
