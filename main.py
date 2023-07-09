import pandas as pd
import streamlit as st
import brand_year_output as byo

title: str = "Получить таблицу, содержащую машины указанного бренда (volkswagen, audi, …)" \
                + ", и указанным диапазоном года регистрации (с … и по …)."

st.title(title)
brand: str = st.selectbox('brands', byo.brands)

year: list[int] = st.slider('min_year', value=[byo.min_year, byo.max_year])

st.write(byo.get_auto(byo.df, brand, year[0], year[1]))