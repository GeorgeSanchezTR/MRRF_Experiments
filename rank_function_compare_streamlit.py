import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def filter_zeroes_rank(rank):
    return rank[rank != 0]

def reciprocal_rank_fusion(rank, c):
    return 1/(c + rank)

def squared_rrf(rank):
    return 1/(rank**2)

def rank_value(rank, c):
    return 1/(rank + c)**2

def mandelbrot_rank(rank,c,n):
    denom = sum([rank_value(i, c) for i in range(1, n+1)])
    num = rank_value(rank, c)
    return num/denom

@st.cache_data
def generate_data():
    results_rrf=[]
    for i in range(1, 501):
        results_rrf.append((i,reciprocal_rank_fusion(i, 3), reciprocal_rank_fusion(i, 60), reciprocal_rank_fusion(i, 500), squared_rrf(i),mandelbrot_rank(i, 3, 10), mandelbrot_rank(i, 60, 10), mandelbrot_rank(i, 500, 10), mandelbrot_rank(i, 60, 5), mandelbrot_rank(i, 60, 30), mandelbrot_rank(i, 60, 50)))    
    df_rank_functions = pd.DataFrame(results_rrf, columns=['rank','rrf-3','rrf-60','rrf-500', 'srrf','mrrf-3-10', 'mrrf-60-10', 'mrrf-500-10','mrrf-60-5', 'mrrf-60-30', 'mrrf-60-50'])
    return df_rank_functions

data = generate_data()
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Rank Function Comparison')

df_compare_rrf_mrrf_srrf = data[['rank', 'rrf-60', 'srrf','mrrf-60-10']]
dfm = df_compare_rrf_mrrf_srrf.melt('rank', var_name='cols', value_name='score values')
# Plot the responses for different events and regions
st.line_chart(dfm,x="rank", y="score values", color="cols")

st.subheader('MRRF Different q values')

df_mrrf = data[['rank','mrrf-3-10','mrrf-60-10','mrrf-500-10']]
dfm2 = df_mrrf.melt('rank', var_name='cols', value_name='score values')
st.line_chart(dfm2,x="rank", y="score values", color="cols")


st.subheader('RRF Different K values')
df_rrf = data[['rank','rrf-3','rrf-60','rrf-500']]
dfm3 = df_rrf.melt('rank', var_name='cols', value_name='score values')
st.line_chart(dfm3,x="rank", y="score values", color="cols")

st.subheader('MRRF Different N values')
df_rrf = data[['rank','mrrf-60-5','mrrf-60-10','mrrf-60-30', 'mrrf-60-50']]
dfm4 = df_rrf.melt('rank', var_name='cols', value_name='score values')
st.line_chart(dfm4,x="rank", y="score values", color="cols")