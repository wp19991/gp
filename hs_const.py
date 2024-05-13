import json

import tushare as ts
from pandas import DataFrame

with open("tushare_token.txt", 'r', encoding='utf-8') as f:
    tushare_token = f.read()
ts.set_token(tushare_token)

pro = ts.pro_api()

data: DataFrame = pro.hs_const(hs_type='SH')
print(data)
with open("data/hs_const_SH.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data.to_dict(), ensure_ascii=False, indent=4))

data: DataFrame = pro.hs_const(hs_type='SZ')
print(data)
with open("data/hs_const_SZ.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data.to_dict(), ensure_ascii=False, indent=4))
