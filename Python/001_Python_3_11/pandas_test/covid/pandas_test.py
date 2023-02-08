import pandas as pd

if __name__ == '__main__':
    data_frame = pd.read_csv("usa_county_wise.csv")
    print(data_frame['Date'].unique())