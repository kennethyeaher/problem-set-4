'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

OUT = './data/part4_plots'

Q2_ANSWER = (
    "Part 4 Q2: What might explain the difference between the plots?\n"
    "People with a current felony charge have a higher predicted chance of felony rearrest "
    "and a lower predicted chance of nonfelony rearrest. This is probably because the model "
    "is treating the current charge degree as a major predictor of future offense type. In other "
    "words, felony charges are pushing the prediction more toward felony rearrest and away from "
    "nonfelony rearrest.\n"
)

Q3_ANSWER = (
    "Part 4 Q3: Why do current felony/no actual rearrest arrestees score higher than "
    "current misdemeanor/actual rearrest arrestees?\n"
    "This suggests the model is putting too much weight on current charge degree compared to "
    "actual reoffense risk. Because of that, some people with felony charges get high scores "
    "even when they are not rearrested, while some people with misdemeanor charges get lower "
    "scores even when they are rearrested. That creates a calibration and fairness issue because "
    "the score is being driven more by the current charge than the person's actual risk.\n"
)

def _save(name):
    plt.savefig(f'{OUT}/{name}.png', bbox_inches='tight')
    plt.close()

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def cat_pred_felony(pred_universe):
    """Predicted felony rearrest by current charge type."""
    (sns.catplot(data=pred_universe, x='has_felony_charge',
                 y='prediction_felony', kind='bar')
        .set_axis_labels('Has felony charge', 'Predicted P(felony rearrest)'))
    _save('cat_pred_felony')


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?
def cat_pred_nonfelony(pred_universe):
    """Predicted non-felony rearrest by current charge type."""
    (sns.catplot(data=pred_universe, x='has_felony_charge',
                 y='prediction_nonfelony', kind='bar')
        .set_axis_labels('Has felony charge', 'Predicted P(nonfelony rearrest)'))
    _save('cat_pred_nonfelony')
    print(Q2_ANSWER)

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
def cat_pred_felony_by_actual(pred_universe):
    """Predicted felony rearrest by current charge, hued by actual felony rearrest."""
    (sns.catplot(data=pred_universe, x='has_felony_charge',
                 y='prediction_felony', hue='y_felony', kind='bar')
        .set_axis_labels('Has felony charge', 'Predicted P(felony rearrest)'))
    _save('cat_pred_felony_by_actual')
    print(Q3_ANSWER)
