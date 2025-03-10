import pandas as pd

url = '../../input/question-1/main.csv'


crime = pd.read_csv(url)
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
crime.set_index('Year', drop=True, inplace=True)
crime.drop(columns='Total')
crimes = crime.resample('10AS').sum()
crimes['Population'] = crime['Population'].resample('10AS').max()
print(crimes)




#OUTPUT


#       Population      Total   Violent   Property  Murder  Forcible_Rape  Robbery  Aggravated_assault  Burglary  Larceny_Theft  Vehicle_Theft
# Year
# 1960   201385000   49295900   4134930   45160900  106180         236720  1633510             2158520  13321100       26547700        5292100
# 1970   220099000  100991600   9607930   91383800  192230         554570  4159020             4702120  28486000       53157800        9739900
# 1980   248239000  131123369  14074328  117048900  206439         865639  5383109             7619130  33073494       72040253       11935411
# 1990   272690813  136582146  17527048  119053499  211664         998827  5748930            10568963  26750015       77679366       14624418
# 2000   307006550  115012044  13968056  100944369  163068         922499  4230366             8652124  21565176       67970291       11412834
# 2010   318857056   50167967   6072017   44095950   72867         421059  1749809             3764142  10125170       30401698        3569080