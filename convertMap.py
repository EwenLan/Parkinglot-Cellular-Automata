import pandas as pd

if __name__ == '__main__':
    f = pd.read_excel('map.xlsx', header=None)
    f.to_csv('map.csv', header=False, index=False)
