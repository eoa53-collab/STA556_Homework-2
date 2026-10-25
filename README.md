# STA 556 Homework 2

## Student Performance Factors

This project explores academic and behavioral factors associated with student exam performance.

## Data Source

The Student Performance Factors dataset was obtained from Kaggle:

Dataset:
lainguyn123/student-performance-factors

The data contain 6,607 student observations and 20 variables.

The dataset is retrieved using the Kaggle API and is therefore
not stored in the repository. To obtain the dataset, use the codes presented in the Preprocessing notebook.

You will need to install all the needed packages from the requirement.txt

## Project Structure

- notebooks/ contains notebooks used for the exploratory analysis.
- src/ contains reusable Python functions.
- data/ contains raw and processed data.
- figures/ contains plots produced by the analysis.

## Research Questions

1. Do average exam scores differ across motivation levels?
2. What is the relationship between hours studied and exam score? And how does this relationship vary across genders?
3. How does attendance impact student exam scores

## Main Findings

Students with higher motivation have slightly higher average exam scores, although the difference between motivation groups is small.

Hours studied has a moderate positive association with exam score across both genders

These results describe associations and should not be interpreted as causal effects since no formal regression model was run
