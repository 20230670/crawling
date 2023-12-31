# 패키지 불러오기
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()

# 검색어 입력 및 검색
keyword = '서울 서점'    # 서울 서점 외에 원하는 장소,주소를 입력하면 카카오맵에 들어가서 자동으로 크롤링 해줌.
kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"

driver.get(kakao_map_search_url)
driver.get(kakao_map_search_url)

ind = 1  # 현재 복사한 순서
no = 1  # 1~5페이지 중 위치한 곳
page = 1  # 현재 페이지 번호
list1 = []  # 결과물이 저장되는 리스트

while 1:
    try:
        # 업체명, 주소
        title = driver.find_element(by='xpath',
                                    value=f'//*[@id="info.search.place.list"]/li[{ind}]/div[3]/strong/a[2]').text
        addr = driver.find_element(by='xpath',
                                   value=f'//*[@id="info.search.place.list"]/li[{ind}]/div[5]/div[2]/p[1]').text
        list1.append([title, addr])

        ind += 1

    except:
        # 더보기 버튼 찾기
        if driver.find_element(by='xpath', value=f'//*[@id="info.search.place.more"]').is_displayed():
            driver.find_element(by='xpath', value=f'//*[@id="info.search.place.more"]').click()
            no += 1
            ind = 1
            page += 1
            continue

        # 다음 페이지로 이동
        elif no >= 5:
            driver.find_element(by='xpath', value=f'//*[@id="info.search.page.next"]').click()
            no = 1
            ind = 1
            page += 1
            continue

        # 5페이지 단위마다 다음 페이지 버튼 누르기
        elif driver.find_element(by='xpath', value=f'//*[@id="info.search.page.no{no + 1}"]').is_displayed():
            no += 1
            driver.find_element(by='xpath', value=f'//*[@id="info.search.page.no{no}"]').click()
            ind = 1
            page += 1
            continue

        # 더이상 이동할수 없을 경우 종료
        else:
            break

print(pd.DataFrame(list1))
