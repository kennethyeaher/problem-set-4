# Visualizing Arrest Data and Model Predictions

![Python](docs/readme/badges/python-3776AB.svg)
![Seaborn](docs/readme/badges/seaborn.svg)
![Matplotlib](docs/readme/badges/matplotlib.svg)
![pandas](docs/readme/badges/pandas-150458.svg)

A coursework exploration of distributions, group comparisons, and model calibration using pandas, Seaborn, and Matplotlib. The plots put predicted rearrest probabilities beside observed outcomes so their relationship can be examined.

## My contribution

I extended the [course starter](https://github.com/gi11ikin/problem-set-4) with bar charts, histograms, categorical comparisons, scatter plots, and written interpretations. The repository retains the instructor's plotting examples and assignment instructions.

![Saved scatter plot of predicted felony rearrest probability against the observed binary outcome, with a fitted line.](data/part5_plots/scatter_pred_vs_actual.png)

This is an existing committed output from the exercise. It is not a new evaluation, and the fitted line alone does not establish model calibration or fairness.

## Reading the plot collection

| Collection | Question |
| --- | --- |
| [Bar charts and histograms](data/part3_plots/) | How are failure to appear and age distributed in the sample? |
| [Categorical comparisons](data/part4_plots/) | How do predicted probabilities vary with current charge type and observed outcomes? |
| [Scatter plots](data/part5_plots/) | How do predictions relate to one another and to recorded rearrest? |

The source keeps plot creation and written interpretation in separate functions. Read the interpretations as coursework observations about this dataset, with particular care around causal or fairness conclusions.

## Explore or run

Browse [saved plots](data/) or start with [the main program](main.py). To reproduce them, create a fresh Python environment, install `requirements.txt`, and run `python main.py` from the repository root. The ETL stage downloads the course datasets from Dropbox; it needs network access even though plot images are already included.

These analyses concern recorded arrest data and classroom predictions. They are not validated for decisions about individuals.

<details>
<summary>Original course assignment</summary>

PROBLEM SET #2: PLOTS

Instructions:
- Clone the Problem Set code package from GitHub:
- Remember to spend some time to get to know the data before you start on pre-processing and analysis
- Run `pip install -r requirements.txt`
- Run main.py and then work through each of the five PARTS of the Problem Set

Before you start:
- Make sure to setup a virtual environment as discussed in the Course Tech Setup lecture. Here's a short article as an additional resource: https://www.freecodecamp.org/news/python-requirementstxt-explained/
- Don't forget to set your requirements.txt file using pip freeze > requirements.txt

When you're done:
- Commit and push this code package to your GitHub account
    - A good practice is to use simple commit comments and commit code after you've finished each feature. Commit and push often.

Submission: You will submit the GitHub URL for this repo in ELMS

Grading: We will look to make sure you've output the correct PNGs and print statements. We will only run main.py, so make sure to stucture this correctly. Credit will be given for adhering to the course's Code Standards and Data Standards, using GitHub correctly, and producing the correct output, among other considerations.

</details>

---

## Author

**Kenneth Yeaher**  
Master of Information Management  
University of Maryland, College Park  
[![LinkedIn: Kenneth Yeaher](https://img.shields.io/badge/LinkedIn-Kenneth_Yeaher-0A66C2?style=flat)](https://www.linkedin.com/in/kennethyeaher/)

`Python` · `Data Visualization`
