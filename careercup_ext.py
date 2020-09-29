import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.careercup.com/page?pid=amazon-interview-questions&job=sdet-interview-questions")

soup = BeautifulSoup(page.content, 'html.parser')
question_preview = soup.find(id='question_preview')
questions = question_preview.find_all('li')

x = [item.find('p').get_text().replace('\r', '\n').encode('utf-8') for item in questions]

final_questions = pd.DataFrame(
    {
        'Amazon SDET Questions': x
    })

final_questions.to_csv('Amazon SDET Questions.csv')