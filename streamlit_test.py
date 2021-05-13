import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Hello Streamlit! This is my first app.")

st.write("Here's my first attempt at using data to create a table:")
st.write(pd.DataFrame({
	'first column': [1,2,3,4],
	'second column': [10,20,30,40]
	}))

df = pd.DataFrame({
	'first column': [1,2,3,4],
	'second column': [10,20,30,40]
	})

df

array = np.array([1,2,3,4,5])
array


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
