import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Shopora AI | Customer Intelligence",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for Dark Black & Orange Minimalist Theme ---
st.markdown(
    """
    <style>
    /* Global App Background */
    .stApp {
        background-color: #0b0b0b;
        color: #e5e5e5;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #121212;
        border-right: 1px solid #222222;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: #d4d4d4;
    }

    /* Project Banner / Expressive Header */
    .project-banner {
        background-color: #141414;
        border: 1px solid #222222;
        border-left: 4px solid #ff7700;
        padding: 2rem;
        border-radius: 6px;
        margin-bottom: 2rem;
    }
    .project-banner h1 {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        letter-spacing: -0.02em;
    }
    .project-banner p {
        color: #a3a3a3;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 0;
    }

    /* Metric Box Styling */
    .metric-card {
        background-color: #141414;
        border: 1px solid #222222;
        border-top: 2px solid #ff7700;
        padding: 1.25rem;
        border-radius: 6px;
    }
    .metric-card p {
        color: #888888;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.3rem;
    }
    .metric-card h3 {
        color: #ffffff;
        font-size: 1.6rem;
        font-weight: 600;
        margin: 0;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #141414;
        border: 1px solid #222222;
        color: #a3a3a3;
        border-radius: 4px;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff7700 !important;
        color: #000000 !important;
        font-weight: 600;
        border-color: #ff7700 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# --- Load and Preprocess Data ---
@st.cache_data
def load_and_preprocess_data():
  df = pd.read_csv("smartcart_customers.csv")

  # Handle Missing Values
  df["Income"] = df["Income"].fillna(df["Income"].median())

  # Feature Engineering
  df["Age"] = 2026 - df["Year_Birth"]
  df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True)
  reference_date = df["Dt_Customer"].max()
  df["Customer_Tenure_Days"] = (reference_date - df["Dt_Customer"]).dt.days

  df["Total_Spending"] = (
      df["MntWines"]
      + df["MntFruits"]
      + df["MntMeatProducts"]
      + df["MntFishProducts"]
      + df["MntSweetProducts"]
      + df["MntGoldProds"]
  )
  df["Total_Children"] = df["Kidhome"] + df["Teenhome"]

  df["Education"] = df["Education"].replace({
      "Basic": "Undergraduate",
      "2n Cycle": "Undergraduate",
      "Graduation": "Graduate",
      "Master": "Postgraduate",
      "PhD": "Postgraduate",
  })

  df["Living_With"] = df["Marital_Status"].replace({
      "Married": "Partner",
      "Together": "Partner",
      "Single": "Alone",
      "Divorced": "Alone",
      "Widow": "Alone",
      "Absurd": "Alone",
      "YOLO": "Alone",
  })

  return df


try:
  df = load_and_preprocess_data()
except Exception as e:
  st.error(
      f"Error loading 'smartcart_customers.csv'. Ensure the file is in the"
      f" same directory. Details: {e}"
  )
  st.stop()

# --- Sidebar Controls ---
st.sidebar.markdown("### 🎛️ Data Filters")
st.sidebar.markdown(
    "<p style='color: #737373; font-size: 0.85rem;'>Refine customer segments"
    " for targeted analysis.</p>",
    unsafe_allow_html=True,
)

selected_education = st.sidebar.multiselect(
    "Education Level",
    options=df["Education"].unique(),
    default=df["Education"].unique(),
)

selected_living = st.sidebar.multiselect(
    "Living Status",
    options=df["Living_With"].unique(),
    default=df["Living_With"].unique(),
)

min_income, max_income = int(df["Income"].min()), int(df["Income"].max())
income_range = st.sidebar.slider(
    "Income Range ($)", min_income, max_income, (min_income, max_income)
)

# Apply Filter Logic
filtered_df = df[
    (df["Education"].isin(selected_education))
    & (df["Living_With"].isin(selected_living))
    & (df["Income"] >= income_range[0])
    & (df["Income"] <= income_range[1])
]

# --- Expressive Project Overview Banner ---
st.markdown(
    """
    <div class="project-banner">
        <h1>SmartCart: Customer Segmentation & Analytics</h1>
        <p>A machine learning-driven analytics platform designed to analyze consumer purchasing behaviors, demographic profiles, and product preferences to optimize retail targeting and recommendation systems.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Top Metrics Row ---
col1, col2, col3, col4 = st.columns(4)

with col1:
  st.markdown(
      f"""
        <div class="metric-card">
            <p>Total Customers</p>
            <h3>{len(filtered_df):,}</h3>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col2:
  avg_income = (
      filtered_df["Income"].mean() if not filtered_df.empty else 0
  )
  st.markdown(
      f"""
        <div class="metric-card">
            <p>Average Income</p>
            <h3>${avg_income:,.0f}</h3>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col3:
  avg_spend = (
      filtered_df["Total_Spending"].mean() if not filtered_df.empty else 0
  )
  st.markdown(
      f"""
        <div class="metric-card">
            <p>Avg Total Spending</p>
            <h3>${avg_spend:,.0f}</h3>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col4:
  avg_age = filtered_df["Age"].mean() if not filtered_df.empty else 0
  st.markdown(
      f"""
        <div class="metric-card">
            <p>Average Age</p>
            <h3>{avg_age:.1f} yrs</h3>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)

# --- Clean Tab Structure ---
tab1, tab2, tab3, tab4 = st.tabs([
    "Demographics",
    "Spending Habits",
    "Purchase Channels",
    "Dataset Explorer",
]
)

# Helper function for matching plot themes with dark-black/orange
def apply_dark_theme(fig, ax):
  fig.patch.set_facecolor("#141414")
  ax.set_facecolor("#141414")
  ax.tick_params(colors="#a3a3a3")
  ax.xaxis.label.set_color("#d4d4d4")
  ax.yaxis.label.set_color("#d4d4d4")
  for spine in ax.spines.values():
    spine.set_edgecolor("#262626")


with tab1:
  st.markdown(
      "### Customer Demographics Overview",
  )
  c1, c2 = st.columns(2)

  with c1:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.histplot(
        filtered_df["Age"],
        kde=True,
        color="#ff7700",
        ax=ax,
        bins=20,
        element="step",
    )
    ax.set_title("Age Distribution", color="#ffffff", fontsize=12, pad=12)
    apply_dark_theme(fig, ax)
    st.pyplot(fig)

  with c2:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.boxplot(
        x="Education",
        y="Income",
        data=filtered_df,
        color="#ff7700",
        ax=ax,
        boxprops=dict(alpha=0.8),
    )
    ax.set_title("Income by Education Level", color="#ffffff", fontsize=12, pad=12)
    apply_dark_theme(fig, ax)
    plt.xticks(rotation=0)
    st.pyplot(fig)

with tab2:
  st.markdown(
      "### Spending Patterns vs Income",
  )
  sc1, sc2 = st.columns(2)

  with sc1:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.scatterplot(
        x="Income",
        y="Total_Spending",
        data=filtered_df,
        color="#ff7700",
        alpha=0.7,
        ax=ax,
    )
    ax.set_title(
        "Total Spending against Income", color="#ffffff", fontsize=12, pad=12
    )
    apply_dark_theme(fig, ax)
    st.pyplot(fig)

  with sc2:
    categories = [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds",
    ]
    avg_spend_vals = [df[col].mean() for col in categories if col in df.columns]
    cat_names = [col.replace("Mnt", "") for col in categories if col in df.columns]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.barplot(
        x=cat_names,
        y=avg_spend_vals,
        color="#ff7700",
        ax=ax,
        saturation=0.85,
    )
    ax.set_title(
        "Average Spend per Product Category", color="#ffffff", fontsize=12, pad=12
    )
    apply_dark_theme(fig, ax)
    plt.xticks(rotation=20)
    st.pyplot(fig)

with tab3:
  st.markdown(
      "### Preferred Acquisition & Purchase Channels",
  )
  channels = [
      "NumWebPurchases",
      "NumCatalogPurchases",
      "NumStorePurchases",
      "NumDealsPurchases",
  ]
  channel_means = [df[c].mean() for c in channels if c in df.columns]
  channel_labels = ["Web", "Catalog", "Store", "Deals"]

  fig, ax = plt.subplots(figsize=(9, 4.5))
  sns.barplot(
      x=channel_labels,
      y=channel_means,
      color="#ff7700",
      ax=ax,
      saturation=0.85,
  )
  ax.set_title(
      "Mean Transactions across Distribution Channels",
      color="#ffffff",
      fontsize=12,
      pad=12,
  )
  apply_dark_theme(fig, ax)
  st.pyplot(fig)

with tab4:
  st.markdown(
      "### Filtered Dataset Inspection",
  )
  st.dataframe(filtered_df, use_container_width=True)

  csv_data = filtered_df.to_csv(index=False).encode("utf-8")
  st.download_button(
      label="📥 Export Filtered Data (CSV)",
      data=csv_data,
      file_name="smartcart_filtered_customers.csv",
      mime="text/csv",
  )