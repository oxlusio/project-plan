"""
Cost of Living Index Streamlit Application

This application analyzes and visualizes cost of living data by country.
It provides interactive charts and insights into various cost factors
across different countries worldwide.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import json
import matplotlib.pyplot as plt
import os

# Page configuration
st.set_page_config(
    page_title="Cost of Living Index by Country",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("💰 Cost of Living Index by Country")
st.markdown("""
This application provides insights into the cost of living across different countries.
The data includes various indices such as Cost of Living, Rent, Groceries, Restaurant Prices, and Local Purchasing Power.
""")

@st.cache_data
def load_sample_data():
    """Load sample cost of living data"""
    countries = [
        'Switzerland', 'Norway', 'Iceland', 'Denmark', 'Luxembourg',
        'Singapore', 'United States', 'Ireland', 'Netherlands', 'Australia',
        'Germany', 'France', 'United Kingdom', 'Canada', 'Japan',
        'South Korea', 'Spain', 'Italy', 'Portugal', 'Poland',
        'Czech Republic', 'Hungary', 'Mexico', 'Brazil', 'India',
        'Thailand', 'Vietnam', 'Philippines', 'Indonesia', 'Malaysia'
    ]
    
    np.random.seed(42)  # For reproducible results
    
    data = {
        'Country': countries,
        'Cost of Living Index': np.random.uniform(20, 120, len(countries)),
        'Rent Index': np.random.uniform(10, 100, len(countries)),
        'Cost of Living Plus Rent Index': np.random.uniform(20, 110, len(countries)),
        'Groceries Index': np.random.uniform(15, 130, len(countries)),
        'Restaurant Price Index': np.random.uniform(10, 140, len(countries)),
        'Local Purchasing Power Index': np.random.uniform(30, 150, len(countries))
    }
    
    df = pd.DataFrame(data)
    
    # Make data more realistic
    df.loc[df['Country'] == 'Switzerland', 'Cost of Living Index'] = 115.2
    df.loc[df['Country'] == 'Norway', 'Cost of Living Index'] = 108.5
    df.loc[df['Country'] == 'India', 'Cost of Living Index'] = 22.1
    df.loc[df['Country'] == 'Vietnam', 'Cost of Living Index'] = 24.8
    
    return df

# --- NEW: Housing Costs Visualization Section ---
@st.cache_data
def load_housing_costs():
    """Load housing costs dataset from JSON file in data/ directory"""
    try:
        file_path = os.path.join("data", "housing_costs.json")
        with open(file_path) as f:
            data = json.load(f)
        return data
    except Exception as e:
        st.warning(f"Could not load housing costs dataset from {file_path}: {e}")
        return None

def show_housing_costs():
    st.header("🏠 Monthly Housing Cost Breakdown")

    data = load_housing_costs()
    if not data:
        st.info("No housing costs data found.")
        return

    categories = data["categories"]
    costs = data["costs"]
    expenses = data["expenses"]

    df_housing = pd.DataFrame({
        "Category": categories,
        "Cost": costs
    })

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Line Chart")
        fig = px.line(df_housing, x="Category", y="Cost", markers=True, title="Monthly Cost by Category")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("Pie Chart")
        fig = px.pie(df_housing, names="Category", values="Cost", title="Cost Distribution")
        st.plotly_chart(fig, use_container_width=True)
    with col3:
        st.subheader("Bar Chart")
        fig = px.bar(df_housing, x="Category", y="Cost", title="Monthly Cost by Category", color="Category")
        st.plotly_chart(fig, use_container_width=True)

    # Histogram
    st.subheader("Histogram of Monthly Expenses")
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(expenses, bins=10, color='skyblue', edgecolor='black')
    ax_hist.set_xlabel('Expense Amount (USD)')
    ax_hist.set_ylabel('Frequency')
    st.pyplot(fig_hist)

    # Raw Data
    st.subheader("Raw Housing Cost Data")
    st.dataframe(df_housing, use_container_width=True)

def main():
    """Main application function"""
    
    # Load data
    df = load_sample_data()
    
    # Sidebar
    st.sidebar.header("🔍 Filters and Options")
    
    # Country selection
    selected_countries = st.sidebar.multiselect(
        "Select Countries to Compare:",
        options=df['Country'].tolist(),
        default=df['Country'][:10].tolist(),
        key="country_multiselect"
    )
    
    # Index selection
    index_options = [col for col in df.columns if col != 'Country']
    selected_index = st.sidebar.selectbox(
        "Select Index to Display:",
        options=index_options,
        index=0,
        key="index_select"
    )
    
    # Filter data
    filtered_df = df[df['Country'].isin(selected_countries)]
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Bar chart
        st.subheader(f"📊 {selected_index} by Country")
        fig_bar = px.bar(
            filtered_df.sort_values(selected_index, ascending=False),
            x='Country',
            y=selected_index,
            title=f"{selected_index} Comparison",
            color=selected_index,
            color_continuous_scale='viridis'
        )
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Summary statistics
        st.subheader("📈 Summary Statistics")
        if not filtered_df.empty:
            st.metric("Average", f"{filtered_df[selected_index].mean():.1f}")
            st.metric("Highest", f"{filtered_df[selected_index].max():.1f}")
            st.metric("Lowest", f"{filtered_df[selected_index].min():.1f}")
            st.metric("Countries", len(filtered_df))
    
    # World map visualization
    st.subheader("🗺️ Global Cost of Living Map")
    fig_map = px.choropleth(
        df,
        locations='Country',
        locationmode='country names',
        color='Cost of Living Index',
        hover_name='Country',
        hover_data={'Cost of Living Index': ':.1f'},
        color_continuous_scale='RdYlBu_r',
        title="Cost of Living Index Worldwide"
    )
    fig_map.update_layout(height=500)
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Correlation matrix
    st.subheader("🔗 Index Correlations")
    correlation_data = df.select_dtypes(include=[np.number]).corr()
    fig_corr = px.imshow(
        correlation_data,
        title="Correlation Between Different Indices",
        color_continuous_scale='RdBu',
        aspect='auto'
    )
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Data table
    st.subheader("📋 Raw Data")
    st.dataframe(
        filtered_df.sort_values(selected_index, ascending=False),
        use_container_width=True,
        hide_index=True
    )
    
    # Download data
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Complete Dataset",
        data=csv,
        file_name=f"cost_of_living_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
    
    # Show housing costs visualizations
    show_housing_costs()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Data Note:** This application uses sample data for demonstration purposes. 
    In a production environment, this would connect to real cost of living data sources 
    such as Numbeo, World Bank, or other economic databases.
    """)

if __name__ == "__main__":
    main()
