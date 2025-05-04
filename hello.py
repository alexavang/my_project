from preswald import connect, get_df, table, text, plotly, sidebar
import pandas as pd
import plotly.express as px

#5. Customize the Branding
sb = sidebar()

# 1. Load the dataset
connect()  # Initialize connection to preswald.toml data sources
df = get_df('data/Google_Daily_News.csv')  # Load data

text("# Structured Labs Online Assessment")
text("Google Daily News")

# 2. Query or manipulate the data
if df is not None and not df.empty:
    table(df, title="All Data")

    # Filter for SeekingAlpha articles
    filtered_df = df[df['source'].str.contains('SeekingAlpha', case=False, na=False)]
    table(filtered_df, title="Only SeekingAlpha Articles" if not filtered_df.empty else "No results for SeekingAlpha in dataset")

# 3. Build an interactive UI
# The bar chart allows interaction by clicking on sources

text("# Visualization")

# 4. Create a visualization
try:
    company_counts = df['source'].value_counts().reset_index()
    company_counts.columns = ['company', 'count']

    fig = px.bar(company_counts, x="company", y="count", title="Top Sources by Article Count", color="company")
    fig.update_xaxes(title="Company")
    fig.update_yaxes(title="Number of Articles")
    plotly(fig)
except Exception as e:
    text(f"Plot error: {e}")
    