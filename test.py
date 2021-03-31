import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)
canadian_data=pd.read_csv("CAvideos.csv")
british_data=pd.read_csv("GBvideos.csv")


merge_data= pd.merge(canadian_data,british_data, on="video_id",how="outer")
print(canadian_data.shape,british_data.shape,merge_data.shape)
