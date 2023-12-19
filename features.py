# Feature engineering
from sklearn.preprocessing import LabelEncoder
import pandas as pd


data = pd.read_csv("data.csv")


# columns = Index(['name', 'current_country', 'age', 'social_platform', 'job', 'interest'], dtype='object')

social_data = data[["interest", "name", "social_platform"]]

social_data.loc[:, "interest"] = LabelEncoder().fit_transform(data.loc[:, "interest"])
social_data.loc[:, "social_platform"] = LabelEncoder().fit_transform(
    data.loc[:, "social_platform"]
)

social_data_nums = social_data[["interest", "social_platform"]].values
