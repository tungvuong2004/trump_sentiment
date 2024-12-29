import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\vuong\OneDrive\Desktop\trump_sentiment_analysis\sentiment_trump_tweets_vader.csv"
df = pd.read_csv(file_path)

# Check if necessary columns exist
if "Sentiment" not in df.columns or "VADER_Sentiment" not in df.columns:
    print("Error: One or both sentiment columns are missing.")
    exit()

# Compare TextBlob and VADER sentiments
comparison = df[["Sentiment", "VADER_Sentiment"]].value_counts()
print("Comparison between TextBlob and VADER Sentiments:")
print(comparison)

# Calculate agreement rate
df["Agreement"] = df["Sentiment"] == df["VADER_Sentiment"]
agreement_rate = df["Agreement"].mean() * 100
print(f"Agreement Rate: {agreement_rate:.2f}%")

# Generate a confusion matrix for visualization
confusion_matrix = df.groupby(["Sentiment", "VADER_Sentiment"]).size().unstack(fill_value=0)

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Comparison of TextBlob and VADER Sentiments")
plt.xlabel("VADER Sentiment")
plt.ylabel("TextBlob Sentiment")
plt.show()

# Save the comparison results to a CSV file
comparison.to_csv(r"C:\Users\vuong\OneDrive\Desktop\trump_sentiment_analysis\sentiment_comparison.csv")
print("Comparison results saved to 'sentiment_comparison.csv'")



