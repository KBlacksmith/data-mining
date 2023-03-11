import pandas as pd

def data_adquisition(dataset: str): 
    df = pd.read_csv(dataset+".csv")
    print("Raw")
    print(df)
    df = df.drop(labels="Rank", axis="columns")
    df = df.dropna(axis="index")
    df.to_csv(dataset+"_clean.csv")


if __name__=="__main__":
    dataset = "vgsales"
    data_adquisition(dataset)
