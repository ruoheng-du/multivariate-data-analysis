import pandas as pd
path = r'/Users/duruoheng/desktop/1.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data)
a=[]
for i in range(0,len(df),60):##每隔60行取数据
    a.append(i)
file = df.iloc[a]
f = pd.DataFrame(file)
f.to_csv(r'/Users/duruoheng/desktop/2.csv', index=False,encoding='utf_8_sig')
