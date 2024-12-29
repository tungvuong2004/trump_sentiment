import pandas as pd
import re

# Set the correct file path
file_path = r"C:\Users\vuong\OneDrive\Desktop\trump_sentiment_analysis\trump_tweets.csv"

# Load the Trump tweets data
df = pd.read_csv(file_path)

# Define a function to clean tweet text
def clean_tweet_text(text):
    """
    Clean tweet text by removing URLs, mentions, hashtags, and special characters.
    """
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)    # Remove mentions
    text = re.sub(r"#\w+", "", text)    # Remove hashtags
    text = re.sub(r"[^\w\s]", "", text) # Remove special characters
    text = text.lower()                 # Convert to lowercase
    return text.strip()

# Apply the cleaning function to the "Tweet" column
if "Tweet" in df.columns:
    df["Cleaned_Tweet"] = df["Tweet"].apply(clean_tweet_text)

# Save the cleaned data to a new CSV file
output_path = r"C:\Users\vuong\OneDrive\Desktop\trump_sentiment_analysis\cleaned_trump_tweets.csv"
df.to_csv(output_path, index=False)

print(f"Cleaned tweets saved to {output_path}")

