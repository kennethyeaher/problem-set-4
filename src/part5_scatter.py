'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

OUT = './data/part5_plots'

Q1_ANSWER = (
    "Part 5 Q1: What can you say about the group of dots on the right side of the plot?\n"
    "The dots on the right are people with a high predicted chance of felony rearrest, and they "
    "are mostly people whose current charge is already a felony. Their predicted nonfelony "
    "rearrest probability stays low, which shows the model is strongly connecting current felony "
    "charges with future felony rearrest while basically ruling out lower level rearrest for this group.\n"
)

Q2_ANSWER = (
    "Part 5 Q2: Is the model calibrated?\n"
    "Not really. If the model was calibrated, the actual rearrest rate would follow the predicted "
    "probability pretty closely, almost like a 1 to 1 relationship. Here, the fitted line is much "
    "flatter, meaning people with high predicted probabilities are being rearrested at rates lower "
    "than what the model predicts. So the model looks overconfident, especially at the high end.\n"
)

def _save(name):
    plt.savefig(f'{OUT}/{name}.png', bbox_inches='tight')
    plt.close()
# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatter_pred_by_charge(pred_universe):
    """Prediction_felony vs prediction_nonfelony, hued by current felony charge."""
    sns.lmplot(data=pred_universe, x='prediction_felony', y='prediction_nonfelony',
               hue='has_felony_charge', fit_reg=False)
    _save('scatter_pred_by_charge')
    print(Q1_ANSWER)

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatter_pred_vs_actual(pred_universe):
    """Prediction_felony vs actual felony rearrest."""
    sns.lmplot(data=pred_universe, x='prediction_felony', y='y_felony')
    _save('scatter_pred_vs_actual')
    print(Q2_ANSWER)git add src/part5_scatter.py