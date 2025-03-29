import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.graph_objects as go

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("apnews_summary.csv")

data = load_data()

# Dashboard Header
st.title("Assignment 2 - Webscraping and text analysis")
st.subheader("Course: CSIS4260 - Special Topics in Data Analytics| Student: Roberto Escalante Gafau")

# Sidebar navigation
st.sidebar.title("News Scraping Dashboard")
page = st.sidebar.radio("Select a page", ["Overview", "Articles", "Visualizations"])

if page == "Overview":
    st.title("Scraping Overview")
    st.write(f"Total Articles Scraped: {len(data)}")
    
    # Load benchmark data
    bs4_time = 15.2  # Replace with actual values
    playwright_time = 8.4  # Replace with actual values
    st.write("### Benchmarking")
    st.write(f"**BeautifulSoup Execution Time:** {bs4_time} sec")
    st.write(f"**Playwright Execution Time:** {playwright_time} sec")

    # Benchmark bar chart
    fig, ax = plt.subplots()
    sns.barplot(x=["BeautifulSoup", "Playwright"], y=[bs4_time, playwright_time], palette="viridis", ax=ax, hue=None, legend=False)
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Benchmarking Execution Time")
    st.pyplot(fig)
    
elif page == "Articles":
    st.title("Scraped Articles")
    sentiment_filter = st.selectbox("Filter by Sentiment", ["All", "Positive", "Negative"])
    
    filtered_data = data if sentiment_filter == "All" else data[data["Sentiment Direction"] == sentiment_filter]
    st.dataframe(filtered_data)
    
elif page == "Visualizations":
    st.title("Sentiment Analysis")
    
    # Sentiment Distribution
    st.write("### Sentiment Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x=data["Sentiment Direction"], palette="viridis", ax=ax, hue=None, legend=False)
    st.pyplot(fig)

    # Average Sentiment Score Gauge
    avg_sentiment = data["Sentiment Score"].mean()
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_sentiment,
        title={"text": "Average Sentiment Score"},
        gauge={"axis": {"range": [-1, 1]}, "bar": {"color": "blue"}}
    ))
    st.plotly_chart(fig)
    
    # Word Cloud
    st.write("### Word Cloud of Summaries")
    text = " ".join(data["Summary"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

st.sidebar.info("Data sourced from AP News")
