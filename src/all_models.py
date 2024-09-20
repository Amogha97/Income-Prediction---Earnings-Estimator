import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dict1 ={
    "Model" : ["Decision Tree", "Random Forest", "KNN", "SVM", "Logistic Regression", "Neural Networks"],
    "Accuracy" : [0.84, 0.85, 0.85, 0.87, 0.85, 0.86],
    "Precision" : [0.61, 0.61, 0.62, 0.69, 0.58, 0.65],
    "Recall" : [0.46, 0.68, 0.53, 0.55, 0.72, 0.56],
    "F1 Score" : [0.53, 0.64, 0.57, 0.61, 0.65, 0.60],
    "AUC" : [0.82, 0.89, 0.73, 0.89, 0.89, 0.88]
}

df= pd.DataFrame(dict1)
print(pd.DataFrame(dict1))

# Create bar chart
plt.figure(figsize=(10, 8))

# Create bar chart using Seaborn
sns.barplot(x=df.loc[:,'Model'], y=df.loc[:,'Recall'], palette='viridis')
# Add labels and title
plt.xlabel('Model', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Values', fontsize=12, fontweight='bold', color='gray')
plt.title('Recall of All the Models', fontsize=14, fontweight='bold', color='black')

# Customize ticks
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels by 45 degrees and align them to the right
plt.yticks(fontsize=10, color='black')  # Customize y-axis ticks font size and color

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add value labels on top of each bar
for i, value in enumerate(df.loc[:,'Recall'].to_list()):
    plt.text(i, value - 0.1, str(value), ha='center', fontsize=10)

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()