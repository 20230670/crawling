"""
1. 목표 사이트 - 예능 프로그램 시청률 순위
"""


"""
2. 크롤링에 대해 여러 곳을 돌아다니며 정보를 찾아보았는데, 
전부 beautifulsoup와 셀레니움을 이용한 웹크롤링이었습니다. 
그래서 파이참에서 beautifulsoup를 사용하여 웹 크롤링을 하는 방법을 공부했습니다.
아래 사이트를 보며 공부했습니다. 
"""


"""
3. 크롬드라이버와 셀레니움을 다운 받아 웹 크롤링을 하려 시도 해보았는데 크롬드라이버가 크롬 버전에 맞는 버전이 없어 
다른 방법을 이용하여 웹 크롤링을 시도 해보았습니다. 판다스를 이용하여 예능프로그램 순위를 크롤링 할 수 있다고 하여 시도해보았습니다. 


"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get(
    "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=9%EC%9B%9410%EC%9D%BC%EC%A3%BC%EC%98%88%EB%8A%A5%EC%8B%9C%EC%B2%AD%EB%A5%A0&oquery=9%EC%9B%9412%EC%9D%BC%EC%A3%BC%EC%98%88%EB%8A%A5%EC%8B%9C%EC%B2%AD%EB%A5%A0&tqi=idaojsprvOsssDX4MrdssssssZK-026498")
html_data = BeautifulSoup(response.text, 'html.parser')
program_names = html_data.select('td>p>a')
program_name = program_names[::2]

# 빈 리스트 만들기
rows = []

ranking = 0
for tag in program_name:
    ranking = ranking + 1
    name = tag.get_text()
    row = [ranking, name]
    rows.append(row)

df = pd.DataFrame(rows, columns=['순위', '프로그램명'])
print(rows)


print("2023년 9월 13일 시청률 순위")
print(df)
