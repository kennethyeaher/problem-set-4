'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

OUT = './data/part3_plots'

def _save(name):
    plt.savefig(f'{OUT}/{name}.png', bbox_inches='tight')
    plt.close()

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def bar_fta(pred_universe):
    """Counts of failure to appear values."""
    plt.figure()
    sns.countplot(data=pred_universe, x='fta').set(title='Failure to Appear (FTA) Counts')
    _save('bar_fta')


# 2. Hue the previous barplot by sex
def bar_fta_by_sex(pred_universe):
    """FTA counts broken out by sex."""
    plt.figure()
    sns.countplot(data=pred_universe, x='fta', hue='sex').set(title='FTA Counts by Sex')
    _save('bar_fta_by_sex')


# 3. Plot a histogram of age_at_arrest
def hist_age(pred_universe):
    """Age-at-arrest distribution with default bins."""
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest').set(title='Age at Arrest')
    _save('hist_age')


# 4. Plot the same histogram, but create bins that represent the following age groups 
def hist_age_grouped(pred_universe):
    """Age-at-arrest distribution binned into 18-21, 21-30, 30-40, 40-100."""
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest',
                 bins=[18, 21, 30, 40, 100]).set(title='Age at Arrest (Grouped)')
    _save('hist_age_grouped')