import pandas as pd

url = '../../input/question-2/main.csv'

data =pd.read_csv(url)
result = data.groupby('occupation').agg({'age':['min','max']})
print(result)



# OUTPUT



#               age
#               min max
# occupation
# administrator  21  70
# artist         19  48
# doctor         28  64
# educator       23  63
# engineer       22  70
# entertainment  15  50
# executive      22  69
# healthcare     22  62
# homemaker      20  50
# lawyer         21  53
# librarian      23  69
# marketing      24  55
# none           11  55
# other          13  64
# programmer     20  63
# retired        51  73
# salesman       18  66
# scientist      23  55
# student         7  42
# technician     21  55
# writer         18  60