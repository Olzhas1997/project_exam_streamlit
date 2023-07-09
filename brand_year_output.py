import pandas as pd

df = pd.read_csv('autos.csv', encoding='ISO-8859-1')

brands: list[str] = df.brand.unique()

min_year: int = int(df.yearOfRegistration.min())
max_year: int = int(df.yearOfRegistration.max())

def get_auto(df: pd.DataFrame, brand: str, 
             min_year: int, max_year: int) -> pd.DataFrame:
    return df[(df.brand == brand) 
              & (df.yearOfRegistration >= min_year) 
              & (df.yearOfRegistration <= max_year)]