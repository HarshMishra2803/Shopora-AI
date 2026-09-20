#  Shopora AI — SmartCart

### Customer Intelligence & Segmentation Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shopora-ai.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?logo=python\&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0?logo=python\&logoColor=white)](https://seaborn.pydata.org/)

**Shopora AI (SmartCart)** is a customer intelligence and segmentation platform that analyzes customer demographics, income, purchasing behavior, and shopping preferences to uncover meaningful customer patterns.

The project combines **data preprocessing, exploratory data analysis, customer segmentation, interactive visualizations, and a Streamlit dashboard** into a single platform.

### 🔗 Live Demo

**[🚀 Explore Shopora AI](https://shopora-ai.streamlit.app/)**

---

##  Project Overview

Retail businesses generate large amounts of customer data, but raw transaction data alone does not provide clear insights into customer behavior.

Shopora AI transforms this raw data into an interactive analytics dashboard where users can:

* Explore customer demographics
* Analyze income and spending patterns
* Identify customer segments
* Compare purchasing behavior
* Understand preferred shopping channels
* Filter customer groups dynamically
* Export filtered datasets for further analysis

---

##  Key Features

###  Customer Segmentation

Analyze customer groups based on characteristics such as:

* Education
* Living status
* Income
* Purchasing behavior

Interactive filters allow users to explore specific customer segments.

### 📊 Demographic Analysis

Visualize customer demographics through interactive charts, including:

* Age distribution
* Income distribution
* Education-level comparisons
* Customer population patterns

###  Spending Intelligence

Analyze customer spending behavior across multiple product categories:

*  Wines
*  Fruits
*  Meat
*  Sweets
*  Gold Products

The dashboard also allows users to examine relationships between **income and total spending**.

###  Shopping Channel Analysis

Understand customer purchasing preferences across different channels:

*  Web
*  Catalog
*  Store
*  Deals

###  Dynamic Filtering

Users can dynamically filter customers based on:

* Education
* Living status
* Income range
* Other available customer attributes

Charts and analytics update according to the selected filters.

##  Machine Learning / Data Science Workflow

The project follows a typical data analytics and ML workflow:

```text
Raw Customer Data
       ↓
Data Cleaning
       ↓
Missing Value Handling
       ↓
Feature Engineering
       ↓
Categorical Encoding
       ↓
Exploratory Data Analysis
       ↓
Customer Segmentation
       ↓
Visualization
       ↓
Interactive Streamlit Dashboard
```

---

## 🛠️ Tech Stack

| Technology       | Purpose                             |
| ---------------- | ----------------------------------- |
| **Python**       | Core programming language           |
| **Pandas**       | Data cleaning and manipulation      |
| **NumPy**        | Numerical operations                |
| **Scikit-learn** | Machine learning and preprocessing  |
| **Matplotlib**   | Data visualization                  |
| **Seaborn**      | Statistical visualization           |
| **Streamlit**    | Interactive web application         |
| **Git & GitHub** | Version control and project hosting |

---

## 📂 Project Structure

```text
Shopora-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── customer_data.csv
│
├── notebooks/
    └── analysis.ipynb
```
---

##  Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/HarshMishra2803/Shopora-AI.git
cd Shopora-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Dataset

The project uses customer-level retail data containing information related to:

* Demographics
* Income
* Education
* Household/living status
* Product purchases
* Shopping channels
* Customer activity

The dataset is processed and transformed before being used for analysis and segmentation.

---

##  Dashboard

Shopora AI uses a custom Streamlit interface with a dark-themed UI and interactive controls to make customer analytics easier to explore.

Users can modify filters and immediately observe changes in the visualizations and customer data.

---

## 📈 Potential Business Applications

The insights generated by Shopora AI can support:

* Customer segmentation
* Targeted marketing
* Product promotion analysis
* Shopping-channel optimization
* Customer behavior analysis
* Retail decision-making
* Personalized campaign planning

---


## Author

**Harsh Mishra**

### Connect

* GitHub: [@HarshMishra2803](https://github.com/HarshMishra2803)
* Project: [Shopora AI](https://shopora-ai.streamlit.app/)

---

##
