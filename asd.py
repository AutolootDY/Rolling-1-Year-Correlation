# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go

# # Streamlit App Title
# st.title("Bitcoin and S&P 500: Rolling 1-Year Correlation Coefficient")

# # File uploader for CSV data
# btc_file = st.file_uploader("Upload Bitcoin CSV file", type=["csv"])
# sp500_file = st.file_uploader("Upload S&P 500 CSV file", type=["csv"])

# if btc_file and sp500_file:
#     # Load data from uploaded files
#     btc = pd.read_csv(btc_file, parse_dates=["Date"], index_col="Date")
#     sp500 = pd.read_csv(sp500_file, parse_dates=["Date"], index_col="Date")
    
#     # Ensure necessary columns exist
#     btc = btc[["Close"]].rename(columns={"Close": "BTC"})
#     sp500 = sp500[["Close"]].rename(columns={"Close": "SP500"})
    
#     # Merge data by date
#     merged = btc.join(sp500, how="inner")
    
#     # Convert to numeric to avoid errors
#     merged = merged.apply(pd.to_numeric, errors='coerce')
    
#     # Calculate log returns
#     merged["BTC_Return"] = np.log(merged["BTC"] / merged["BTC"].shift(1))
#     merged["SP500_Return"] = np.log(merged["SP500"] / merged["SP500"].shift(1))
    
#     # Remove NaN and infinite values
#     merged = merged.replace([np.inf, -np.inf], np.nan).dropna()
    
#     # Compute Rolling 1-Year Correlation (252 trading days)
#     merged["Rolling_Corr"] = merged["BTC_Return"].rolling(window=252).corr(merged["SP500_Return"])
    
#     # Streamlit Plot with Plotly
#     st.subheader("Rolling 1-Year Correlation between Bitcoin and S&P 500")
#     fig = go.Figure()
    
#     # Line chart for correlation
#     fig.add_trace(go.Scatter(x=merged.index, y=merged["Rolling_Corr"], mode='lines', name='BTC vs S&P 500', line=dict(color='blue')))
    
#     # Fill negative correlation area
#     negative_corr = merged["Rolling_Corr"].copy()
#     negative_corr[negative_corr >= 0] = np.nan  # Keep only negative values
    
#     fig.add_trace(go.Scatter(
#         x=merged.index,
#         y=negative_corr,
#         mode='lines',
#         fill='tozeroy',
#         fillcolor='rgba(255, 0, 0, 0.3)',
#         name='Negative Correlation',
#         showlegend=True,
#     ))
    
#     # Customize layout
#     fig.update_layout(
#         title="Bitcoin and S&P 500: Rolling 1-Year Correlation Coefficient",
#         xaxis_title="Year",
#         yaxis_title="Correlation",
#         xaxis=dict(showgrid=True),
#         yaxis=dict(showgrid=True, zeroline=True, zerolinecolor='black', zerolinewidth=1),
#         template="plotly_white"
#     )
    
#     # Display Plotly chart
#     st.plotly_chart(fig)
# else:
#     st.warning("Please upload both Bitcoin and S&P 500 CSV files.")


import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Streamlit App Title
st.title("Bitcoin and S&P 500: Rolling 1-Year Correlation Coefficient")

# Load data from existing CSV files
btc = pd.read_csv("btc.csv", parse_dates=["Date"], index_col="Date")
sp500 = pd.read_csv("spx500.csv", parse_dates=["Date"], index_col="Date")

# Ensure necessary columns exist
btc = btc[["Close"]].rename(columns={"Close": "BTC"})
sp500 = sp500[["Close"]].rename(columns={"Close": "SP500"})

# Merge data by date
merged = btc.join(sp500, how="inner")

# Convert to numeric to avoid errors
merged = merged.apply(pd.to_numeric, errors='coerce')

# Calculate log returns
merged["BTC_Return"] = np.log(merged["BTC"] / merged["BTC"].shift(1))
merged["SP500_Return"] = np.log(merged["SP500"] / merged["SP500"].shift(1))

# Remove NaN and infinite values
merged = merged.replace([np.inf, -np.inf], np.nan).dropna()

# Compute Rolling 1-Year Correlation (252 trading days)
merged["Rolling_Corr"] = merged["BTC_Return"].rolling(window=252).corr(merged["SP500_Return"])

# Streamlit Plot with Plotly
st.subheader("Rolling 1-Year Correlation between Bitcoin and S&P 500")
fig = go.Figure()

# Line chart for correlation
fig.add_trace(go.Scatter(x=merged.index, y=merged["Rolling_Corr"], mode='lines', name='BTC vs S&P 500', line=dict(color='blue')))

# Fill negative correlation area
negative_corr = merged["Rolling_Corr"].copy()
negative_corr[negative_corr >= 0] = np.nan  # Keep only negative values

fig.add_trace(go.Scatter(
    x=merged.index,
    y=negative_corr,
    mode='lines',
    fill='tozeroy',
    fillcolor='rgba(255, 0, 0, 0.3)',
    name='Negative Correlation',
    showlegend=True,
))

# Customize layout
fig.update_layout(
    title="Bitcoin and S&P 500: Rolling 1-Year Correlation Coefficient",
    xaxis_title="Year",
    yaxis_title="Correlation",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True, zeroline=True, zerolinecolor='black', zerolinewidth=1),
    template="plotly_white"
)

# Display Plotly chart
st.plotly_chart(fig)
