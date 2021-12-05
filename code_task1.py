# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:10:15 2021

@author: Shilpa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv"
score_data = pd.read_csv(url)
print("Successfully imported the Score data.")

score_data.head(10)

score_data.plot(x = 'Hours', y = 'Scores', style = 'o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()
