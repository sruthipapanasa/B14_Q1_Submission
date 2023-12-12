# DSC180A Quarter 1 Code
## Project Description
The modern world divides people based on political ideals and beliefs, so this model of
learning the different personas of different people’s opinions answers political questions that help
us efficiently gain a better understanding of people’s responses. In past approaches, others have
not been able to properly solve the problem at hand while also taking cultural stereotypes and
everyday social behaviors into account in order to result in more accurate answers. We are
specifically evaluating people’s opinions on presidential candidates, so by taking the sentiments
of people’s opinions in Twitter data and creating “personas” using LangChain Agents, we believe
this will take more factors into account that have previously been neglected. As a result of this
model, we are expecting accurate responses to questions regarding political ideals, current
political issues, and presidential candidates.

## Data Description
Link to the data: https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets

Our data consists of two separate CSV files. The first dataset contains all of the tweets
from the 2020 election that included the hashtag #biden in it. The second dataset contained all
the tweets that included the hashtag #trump. Neither dataset was exclusively partisan to either
candidate. Rather, they consisted of opinions and sentiments from voters who held various
perspectives on the two candidates, irrespective of their stance. It included any tweet that had the
corresponding hashtag, regardless of whether that hashtag was used to express support or
opposition for the tagged candidate. We cleaned the dataset, removing all of the unnecessary
punctuation, emojis, hashtags, and stop words. This allowed us to plug in all of the tweets from
users that tweeted more than 20 times into a Langchain agent. We then asked the agent to adopt
and imitate the “personas” extracted from the language of the tweets. That allowed us to further
interrogate these personas to get answers about their political views, stances of pressing topics,
and thoughts on candidates.

The most important thing to note about our data is that the raw data is too large to be uploaded to Github. To be able to run our code, 
you need to follow the link (https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets), download the two csv files, and store them in the data folder. They should be saved as hashtag_donaldtrump.csv and hashtag_joebiden.csv

## Installations --> todo
```pip install openai``` 

```pip install langchain```

## Running The Code
### Downloading the data 
The most important thing to note about our data is that the raw data is too large to be uploaded to Github. To be able to run our code, 
you need to follow the link (https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets), download the two csv files, and store them in the data folder. They should be saved as hashtag_donaldtrump.csv and hashtag_joebiden.csv
### API Key
Replace all areas with "INSERT_API_KEY" with your own Open AI API key before running the notebook. You can make an API key here: https://platform.openai.com/api-keys
### File Descriptions
#### run.py
### Opening visualization files
A key part of understanding our project's purpose and analysis includes seeing the plots and graphs in our .ipynb files. Although running
run.py will run all of the .ipynb files, for the graphs to be visible, you must manually open each file. Please take a look at the following 
ipynb files to understand our visualizations: 'exploratory_visualizations.ipynb', 'agent_response_visualizations.ipynb',  'final_bias_visualizations.ipynb'.
