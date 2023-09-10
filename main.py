"""
1. 목표 사이트 - 기상청
"""


"""
2. 크롤링에 대해 여러 곳을 돌아다니며 정보를 찾아보았는데, 
전부 beautifulsoup와 셀레니움을 이용한 웹크롤링이었습니다. 
그래서 파이참에서 beautifulsoup를 사용하여 웹 크롤링을 하는 방법을 공부했습니다.
아래 사이트를 보며 공부했습니다. 

https://charimlab.tistory.com/
entry/ep01%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81
-11-%EB%8F%99%EC%A0%81-%ED%8E%98%EC%9D%B4%EC%A7%80%EC%9B%B9-
%EB%8F%99%EC%9E%91-%EC%9E%90%EB%8F%99%ED%99%94Selenium-with-
%ED%8C%8C%EC%9D%B4%EC%8D%AC

https://yogyui.tistory.com/entry/BeautifulSoup-
%EA%B8%B0%EC%83%81%EC%B2%AD-%EB%8F%84%EC%8B%9C%EB%B3%84-
%ED%98%84%EC%9E%AC%EB%82%A0%EC%94%A8-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0

"""


"""
3. 크롬드라이버와 셀레니움을 다운 받아 웹 크롤링을 하려 시도 해보았는데 크롬드라이버가 크롬 버전에 맞는 버전이 없어 
다른 방법을 이용하여 웹 크롤링을 시도 해보았습니다. 판다스를 이용하여 기상청을 크롤링 할 수 있다고 하여 시도해보았습니다. 
기상청 사이트에서 과거관측 페이지 부분을 크롤링 해보았습니다.

"""
import requests
from bs4 import BeautifulSoup

url = "https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
print(soup)