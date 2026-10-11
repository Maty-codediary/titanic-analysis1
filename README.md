Titanic Survival Analysis — Python

A data analysis of the Titanic dataset built using only Python’s built-in csv module — no pandas, no external libraries. Just pure Python logic.

What I analysed

Overall survival rate
Survival rate by gender
Survival rate by passenger class
Survival rate by age group (children, adults, elders)

What I found

Overall survival rate: 38.4%
Women: 74.2% | Men: 18.9%
1st class: 63.0% | 2nd class: 47.3% | 3rd class: 24.2%
Children: 54.0% | Adults: 38.6% | Elders: 26.9%

The data brings the phrase “women and children first” to life — women survived at nearly 4× the rate of men, and children had the highest survival rate of any age group. Perhaps most striking is the class divide: a 1st class passenger was more than twice as likely to survive as someone in 3rd class. Wealth, it seems, bought more than comfort on the Titanic.

How to run it

bash
git clone https://github.com/YOUR_USERNAME/titanic-analysis
cd titanic-analysis
python titanic.py

Download the dataset from Kaggle and place train.csv in the same folder.

Why I built this

This is my first data analysis project, built during my exchange semester in China as part of teaching myself AI engineering from scratch. No shortcuts — pure Python before touching any libraries.