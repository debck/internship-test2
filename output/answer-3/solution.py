import pandas as pd

url = '../../input/question-3/main.csv'

data = pd.read_csv(url)
result=(data.sort_values(by=['Red Cards','Yellow Cards'],ascending=False))
print(result[['Team','Yellow Cards','Red Cards']])


# OUTPUT


#                    Team  Yellow Cards  Red Cards
# 6                Greece             9          1
# 9                Poland             7          1
# 11  Republic of Ireland             6          1
# 7                 Italy            16          0
# 10             Portugal            12          0
# 13                Spain            11          0
# 0               Croatia             9          0
# 1        Czech Republic             7          0
# 14               Sweden             7          0
# 4                France             6          0
# 12               Russia             6          0
# 3               England             5          0
# 8           Netherlands             5          0
# 15              Ukraine             5          0
# 2               Denmark             4          0
# 5               Germany             4          0