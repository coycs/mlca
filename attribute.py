import pandas as pd
import json

for index in range(5):
    index = index+1
    # 读取表格文件
    df = pd.read_csv("./{}.csv".format(index))
    # 初始化内容容器
    content = {
        "size": {
            "rows": df.shape[0],
            "columns": df.shape[1]
        },
        "features": {}
    }
    # 补充每列的feature
    for column in df.columns:
        feature = {
            "max": '%.3g' % df[column].max(),
            "min": '%.3g' % df[column].min(),
            "mean": '%.3g' % df[column].mean(),
            "median": '%.3g' % df[column].median(),
            "mode": '%.3g' % df[column].mode()[0],
            "var": '%.3g' % df[column].var(),
            "std": '%.3g' % df[column].std()
        }
        content["features"][column] = feature
    # 保存为json文件
    with open('{}_info.json'.format(index), 'w') as f:
        json.dump(content, f)
