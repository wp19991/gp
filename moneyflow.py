import json
import os

import tushare as ts
from pandas import DataFrame

with open("tushare_token.txt", 'r', encoding='utf-8') as f:
    tushare_token = f.read()
ts.set_token(tushare_token)

pro = ts.pro_api()

with open("data/trade_cal.json", "r", encoding="utf-8") as f:
    trade_cal_data = json.loads(''.join(f.readlines()))
i = 0
trade_cal = [i for i in trade_cal_data.get('cal_date').values()][::-1][i:]
trade_cal_is_open = [i for i in trade_cal_data.get('is_open').values()][::-1][i:]

for trade_date in zip(trade_cal, trade_cal_is_open):
    if trade_date[1] == 0 or os.path.exists(r"C:\Users\wp\Desktop\gp\data\moneyflow\moneyflow_{}.json".format(trade_date[0])) \
            or int(trade_date[0]) < 20100000:
        i += 1
        continue
    data: DataFrame = pro.moneyflow(trade_date=trade_date[0])
    log_str = "[{}/{}] date:{} data.shape:{}".format(i, len(trade_cal), trade_date[0], str(data.shape))
    print(log_str)
    with open("moneyflow_log.txt", "a", encoding="utf-8") as f:
        f.write('\n')
        f.write(log_str)
    with open(r"C:\Users\wp\Desktop\gp\data\moneyflow\moneyflow_{}.json".format(trade_date[0]), "w", encoding="utf-8") as f:
        f.write(json.dumps(data.to_dict(), ensure_ascii=False, indent=4).replace('NaN', 'null'))
    i += 1
