#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import seaborn as sns
import plotly.express as px


# In[7]:


salaries_dataset = pd.read_csv('Salaries Dataset.csv')


# In[8]:


print(salaries_dataset.head())


# In[9]:


salaries_dataset.drop(columns=['salary_currency','salary'],axis=1,inplace=True)


# In[10]:


salaries_dataset.head(5)


# In[11]:


salaries_dataset['remote_ratio'].replace(100,'FR',inplace=True)
salaries_dataset['remote_ratio'].replace(50,'P',inplace=True)
salaries_dataset['remote_ratio'].replace(0,'OS',inplace=True)


# In[12]:


salaries_dataset.head(5)


# In[13]:


salaries_dataset.drop_duplicates(inplace=True)


# In[14]:


salaries_dataset.head()


# In[15]:


fig = px.line(salaries_dataset, x="work_year", y="salary_in_usd", color="experience_level", animation_frame="work_year", title="Trend of Salaries Over Work Years")
fig.show()

Outcome:- 
1-The chart is animated over the "work_year" column, showing how the salary distribution evolves over time.
2-This animation can help identify any patterns, anomalies, or changes in salary trends across different experience levels.
3-The color of each line corresponds to the "experience_level," making it easy to distinguish between salary trends for different levels of experience.

Analysis:- 
1-The use of animation over the "work_year" column allows for dynamic visualization, providing a clearer understanding of how salaries change over time.
2-The color-coded lines help in easy identification of different experience levels, facilitating comparison.
3-Plotly Express provides interactive charts, allowing users to zoom in, pan, and hover over data points.

Managerial Implications:- 
1-Managers can use this information to understand the trajectory of salary trends in the organization. Identifying upward or downward trends can inform strategic decisions related to compensation planning and talent retention.
2-Managers can identify patterns specific to different experience levels. For instance, they may observe whether certain experience levels experience more significant salary increases or whether there are disparities that need attention.
3-Managers can align compensation strategies with organizational goals and market trends. For example, if the industry experiences a surge in demand for specific skill sets, the organization can adjust salary offerings to remain competitive.
4- If salary trends indicate stagnation or disparities, managers can proactively address these issues to enhance employee satisfaction and retention. Transparent communication about salary adjustments based on performance and market conditions is crucial.
5-Managers can leverage the interactive chart to explore specific data points, identify outliers, and make informed decisions.

# In[16]:


fig = px.bar(salaries_dataset, x="work_year", y="employment_type", animation_frame="work_year", title="Distribution of Employment Types Over the Years")
fig.show()

Outcome:- 
1-The bar chart will display the distribution of different employment types for each work year.
2-Each bar represents a specific employment type, and the height of the bar corresponds to the count or percentage of that employment type for a given work year.
3-the chart is animated over the "work_year" column, providing a dynamic representation of how the distribution of employment types changes over time.

Analysis:- 
1-A bar chart is suitable for displaying the distribution of categorical data, making it an appropriate choice for visualizing the count or percentage of different employment types.
2-The use of animation over the "work_year" column helps visualize the evolution of employment type distribution over time.
3-This dynamic representation is particularly useful for identifying trends or changes in the composition of employment types.

Managerial Implications:- 
1-Managers can use this information to understand how the composition of the workforce evolves. This insight is crucial for workforce planning, resource allocation, and adapting HR strategies to changing employment dynamics.
2-Managers can identify whether there are shifts in the types of employment (e.g., full-time, part-time, contract) over time. Understanding these trends can guide strategic decisions related to hiring, talent acquisition, and organizational structure.
3-Managers can align workforce planning with organizational goals. For instance, if there is a strategic initiative to increase the proportion of full-time employees, the chart can provide insights into the progress toward that goal.
4-Managers can adjust resource allocation based on the evolving composition of employment types. For example, a higher proportion of contract employees might require adjustments in budgeting for recruitment and onboarding.

# In[17]:


fig = px.scatter(salaries_dataset, x="work_year", y="salary_in_usd", color="job_title", animation_frame="work_year", title="Relationship Between Salary and Years of Experience")
fig.show()

Outcome:- 
1-The scatter plot will display the distribution of individual data points with salary (in USD) on the y-axis and work years on the x-axis.
2-Each point represents an observation in the dataset, providing insights into the variation in salaries (in USD) based on years of experience.
3-This color-coded representation helps analyze how job titles impact the salary (in USD) and experience relationship.

Analysis:- 
1-A scatter plot is suitable for visualizing the relationship between two numerical variables, making it appropriate for exploring the connection between salary (in USD) and years of experience.
2-Color-coding points by job title adds an additional dimension to the plot, allowing for the examination of salary (in USD) and experience trends specific to different job titles.
3-The use of animation enhances the plot by providing a dynamic view of how the relationship changes over different work years.This can be valuable for spotting trends, patterns, or outliers over time.

Managerial Implications:- 
1-Managers can gain insights into how salaries vary based on the number of years of experience. This understanding is crucial for making informed decisions related to compensation, career development, and talent retention.
2-Managers can identify patterns specific to job titles, understanding how different roles contribute to variations in salary based on experience. This information is valuable for job role benchmarking and salary structure adjustments.
3-Managers can identify trends or outliers that may emerge or change over time. This information is useful for adjusting compensation strategies, identifying roles with exceptional performance, or addressing salary-related disparities.
4-Managers can use the information to plan salary budgets based on experience levels and job titles. This ensures that compensation strategies align with organizational goals and market standards.
5-Managers can use the insights to have informed discussions with employees about career progression, salary expectations, and skill development. This promotes transparency and employee engagement.



# In[18]:


fig = px.scatter(salaries_dataset, x="work_year", y="salary_in_usd", size="salary_in_usd", color="job_title", animation_frame="work_year", title="Relationship Between Salary, Years of Experience, and Job Titles")
fig.show()

Outcome:- 
1-The scatter plot will display the distribution of individual data points with salary (in USD) on the y-axis and work years on the x-axis.
2-Each point represents an observation in the dataset, providing insights into the variation in salaries (in USD) based on years of experience.
3-The chart is animated over the "work_year" column, showing how the relationship between salary (in USD), years of experience, and job titles evolves over time.

Analysis:- 
1-A scatter plot is suitable for visualizing the relationship between two numerical variables (salary and years of experience) and encoding additional information using color and size.
2-It enhances the plot by providing a dynamic view of how the relationship changes over different work years.
3-Color-coding points by job title adds an additional dimension to the plot, allowing for the examination of salary (in USD) and experience trends specific to different job titles.

Managerial Implications:- 
1-Managers can gain insights into how this complex relationship evolves over time. Understanding these dynamics is crucial for making informed decisions related to compensation strategies and talent management.
2-Managers can observe how salary, experience, and job titles interact over different work years. This information is valuable for identifying changing workforce dynamics and making strategic decisions based on evolving trends
3-Managers can identify not only how job titles influence salary and experience but also the magnitude of these effects. This insight aids in benchmarking roles, adjusting salary structures, and recognizing the contributions of different job titles.
4-Managers can allocate resources based on the observed dynamics. For example, if certain job titles consistently contribute to high-performance outcomes, resource allocation and talent development efforts can be directed accordingly.
5-Managers can use the visual representation of salary, experience, and job titles to have meaningful discussions with employees during performance reviews. This promotes transparency and aligns individual performance with organizational goals.

# In[19]:


fig = px.histogram(salaries_dataset, x="salary_in_usd", animation_frame="job_title", title="Distribution of Salaries in USD for Different Job Titles")
fig.show()

Outcome:- 
1-The histogram will display the distribution of salaries (in USD) across different job titles.
2-Each frame in the animation corresponds to a different job title, showing the salary distribution for that specific job title.
3-The chart is animated over the "job_title" column, providing a dynamic representation of how the salary distribution varies across different job titles. Each animation frame reveals the salary distribution for a specific job title.

Analysis:- 
1-A histogram is suitable for visualizing the distribution of a continuous variable (in this case, salaries in USD).
2-The use of animation enhances the plot by allowing the viewer to see how salary distributions change across different job titles.
3-This can be useful for comparing salary distributions and identifying variations specific to each job title.

Managerial Implications:-
1-They can gain insights into the variation in salary ranges for each job title. This information is valuable for ensuring that salary structures align with the organization's compensation strategy and industry standards.

2-Managers can use the histogram to identify job titles where salaries exhibit unusual patterns. This insight can prompt further investigation into factors such as market competitiveness, skill demand, or internal equity.

3-Managers can use the animated histogram to benchmark salary distributions against industry standards and competitors. Understanding how the organization's salary distributions compare with industry norms allows managers to make data-driven decisions to remain competitive in attracting and retaining top talent.

4-Insights from the histogram can inform the tailoring of compensation strategies for different job titles.Managers can adapt compensation strategies based on the observed salary distributions. For instance, if certain job titles exhibit a wider salary range, it may necessitate adjustments in bonus structures or other variable components.

5-Understanding salary distributions is crucial for addressing employee satisfaction and retention.Managers can use the information to identify potential areas of dissatisfaction related to salary within specific job titles. Addressing such concerns can contribute to higher employee satisfaction and retention rates.

# In[20]:


fig = px.area(salaries_dataset, x="work_year", y="salary_in_usd", color="employment_type", animation_frame="work_year", title="Change in Salary Over the Years for Different Employment Types")
fig.show()

Outcome:- 
1-The area chart will display the change in salary (in USD) over different work years.
2-Each area represents a different employment type, and the color distinguishes between them. The y-axis represents the cumulative or stacked salary values for each employment type.
3-The chart is animated over the "work_year" column, providing a dynamic representation of how the cumulative salary changes for different employment types over time. Each animation frame corresponds to a specific work year.

Analysis:- 
1-The area chart is suitable for visualizing cumulative values over time, making it appropriate for displaying the cumulative salary changes for different employment types.
2-The use of animation enhances the plot by allowing the viewer to see how the cumulative salary changes for different employment types over different work years.
3-This can be useful for understanding trends and patterns in the cumulative salary distribution.

Managerial Implications:-

1-The animated area chart visualizes how cumulative salary changes for different employment types evolve over different work years. Managers can gain insights into the overall trend of cumulative salary changes, providing a comprehensive view of the organization's financial commitment to compensation over time.
2-The chart allows for a comparison of cumulative salary trends across different employment types. Managers can identify employment types with notable cumulative salary increases or decreases. This information guides decision-making related to compensation strategies, budgeting, and resource allocation.
3-The cumulative salary changes visualized in the area chart provide insights into the budget impact over different work years. Managers can assess the financial implications of cumulative salary changes, helping with budget planning and resource allocation. Understanding how different employment types contribute to overall salary expenses is crucial for financial management.
4-Managers can use the chart to inform resource allocation for different employment types. By understanding the cumulative salary changes for each employment type, managers can allocate resources more effectively. This may involve adjusting compensation strategies, bonuses, or other incentives based on the observed trends.
5-The cumulative salary trends can inform strategic workforce planning. Managers can align workforce planning efforts with salary trends, ensuring that compensation strategies support organizational goals. This is particularly important when planning for growth, restructuring, or talent retention initiatives.

# In[21]:


sns.lineplot(x="work_year", y="salary_in_usd", hue="experience_level", data=salaries_dataset)
plt.show()

Outcomes:- 
1-The line plot will display the trend of salaries (in USD) over different work years.
2-Each line represents a different experience level, and the x-axis represents the "work_year."
3-The lines are colored based on the "experience_level," making it easy to distinguish salary trends for different experience levels.

Analysis:- 
1-Seaborn's lineplot is suitable for visualizing trends and relationships between two numerical variables over a continuous axis, making it appropriate for showing how salaries change over different work years.
2-Color-coding the lines by experience level adds an additional dimension to the plot, allowing for the examination of salary trends specific to different experience levels.

Managerial Implications:- 

1-The line plot provides a clear understanding of how salaries (in USD) trend over different work years. Managers can track overall salary trends to assess whether compensation is increasing, decreasing, or remaining stable. This information is crucial for budgeting and strategic decision-making.
2-Color-coding lines by experience level allows for differentiation of salary trends. Managers can identify how salaries vary based on experience levels. Understanding these variations is essential for making informed decisions related to salary adjustments, promotions, and talent development.
3-Visualization aids in identifying patterns or anomalies specific to different experience levels. Managers can use the plot to identify any unexpected deviations in salary trends for particular experience levels. This insight prompts further investigation into potential causes, such as changes in market demand or adjustments in compensation policies.
4-Salary trends can be analyzed in the context of experience levels for performance assessments. Managers can correlate salary trends with individual or team performance metrics. This information guides performance evaluations, incentive structures, and the alignment of compensation with organizational goals.
5-Understanding salary trends assists in budget planning and resource allocation. Managers can use the information to project future salary expenses based on observed trends. This is critical for aligning budget allocations with compensation strategies and organizational priorities.
# In[29]:


top_5_paid_employees = salaries_dataset.nlargest(5, 'salary_in_usd')
print(top_5_paid_employees)


# In[32]:


max_salary = salaries_dataset['salary_in_usd'].max()
min_salary = salaries_dataset['salary_in_usd'].min()
print("Maximum salary_in_usd:", max_salary)
print("Minimum salary_in_usd:", min_salary)

Objectives:- 

1-The objective is to analyze the trend of salaries (in USD) over different work years, considering the variations based on experience levels. This can help in understanding how salaries evolve over time and identifying patterns or anomalies.
2-The objective is to visualize and analyze the distribution of different employment types over the years. This provides insights into the changing composition of the workforce, helping in identifying trends or shifts in employment types.
3-The objective is to explore the relationship between salary (in USD), years of experience, and job titles. The color-coded representation facilitates the analysis of how different job titles impact the salary and experience relationship over different work years.
4-The objective is to dynamically visualize the distribution of salaries (in USD) based on years of experience and job titles. The animation provides a time-based perspective, helping identify trends and changes in the relationship over different work years.
5-The objective is to analyze the distribution of salaries (in USD) across different job titles. The animated histogram allows for a dynamic view of how salary distributions vary for each job title.
6-The objective is to visualize cumulative salary changes over different work years for different employment types. This provides insights into the overall financial commitment to compensation and helps in understanding trends and patterns.
7-Understand the overall structure of salaries within the organization, including variations based on experience levels, job titles, and employment types.
8-Analyze the composition of the workforce over time, identifying shifts in employment types and their impact on salary distribution.
9-Detect anomalies or outliers in salary trends, experience levels, or job titles that may require further investigation or targeted interventions.
10-Evaluate how the organization's salary levels compare to industry benchmarks and competitors, ensuring competitiveness in attracting and retaining talent.
11-Gain insights into factors influencing employee retention by examining how salary trends and distributions align with experience levels and job titles.
12-Explore the correlation between salary trends and performance metrics to assess the effectiveness of performance-linked compensation strategies.
13-Inform strategic workforce planning by understanding how changes in employment types and salary structures align with organizational goals.
14-Use visualizations to communicate salary trends transparently to employees, fostering a culture of openness and trust within the organization.References/ Source:- 1-Kaggle 
                     2-ChatGPT
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




