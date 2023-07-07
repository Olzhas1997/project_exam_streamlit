import pandas as pd
import streamlit as st

df = pd.read_csv('autos.csv', encoding='ISO-8859-1')

def get_auto(df, brand, min_year, max_year):
    return df[(df['brand'] == brand) & (df['yearOfRegistration'] >= min_year) & (df['yearOfRegistration'] <= max_year)]


print(df.yearOfRegistration.max())

brands = df.brand.unique()


title: str = "Получить таблицу, содержащую машины указанного бренда (volkswagen, audi, …)" \
                + ", и указанным диапазоном года регистрации (с … и по …)."

st.title(title)
brand = st.selectbox('brands', brands)
min_year = st.number_input('min_year', 1000, 9999)
max_year = st.number_input('max_year', min_year, 9999)
df1 = get_auto(df, brand, min_year, max_year)
st.write(df1)
