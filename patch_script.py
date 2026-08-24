import re

file_path = "/Users/young.h/.gemini/antigravity/brain/ba0228ef-f206-419d-9ba1-f3b54e36a634/scratch/generate_rich_maps_and_md.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# BUDAPEST
content = content.replace(
    '    ("Pater Marcus", 47.4986, 19.0399, "purple"),\n]',
    '    ("Pater Marcus", 47.4986, 19.0399, "purple"),\n    ("ALDI (마트)", 47.4930, 19.0558, "green"),\n    ("SPAR City", 47.4922, 19.0542, "green"),\n]'
)
bud_md_addition = """
## 🛒 호텔 주변 마트 & 쇼핑 (지도 내 초록색 번호)

* **[[18] ALDI (알디)](https://www.google.com/maps/search/?api=1&query=ALDI+Kossuth+Lajos+Budapest)**
  * **특징**: 호텔(파리시 우드버르)에서 도보 2~3분 거리에 위치한 대형 할인 마트. 저렴한 가격으로 생수, 간식, 신선 식품 등을 구매하기 좋습니다.
* **[[19] SPAR City (스파 시티)](https://www.google.com/maps/search/?api=1&query=SPAR+City+Ferenciek+tere)**
  * **특징**: 호텔 바로 근처(페렌치에크 광장)에 있는 마트로 접근성이 매우 뛰어납니다. 토카이 와인 등 간단한 기념품도 쉽게 구할 수 있습니다.

---"""
content = content.replace("## 🛍️ 필수 쇼핑 리스트", bud_md_addition + "\n\n## 🛍️ 필수 쇼핑 리스트", 1)

# VIENNA
content = content.replace(
    '    ("Mayer am Pfarrplatz", 48.2562, 16.3533, "purple"),\n]',
    '    ("Mayer am Pfarrplatz", 48.2562, 16.3533, "purple"),\n    ("BILLA Corso (마트)", 48.2105, 16.3725, "green"),\n    ("Julius Meinl", 48.2090, 16.3686, "green"),\n]'
)
vie_md_addition = """
## 🛒 호텔 주변 마트 & 쇼핑 (지도 내 초록색 번호)

* **[[13] BILLA Corso (빌라 코르소)](https://www.google.com/maps/search/?api=1&query=BILLA+Corso+Herrnhuterhaus)**
  * **특징**: 파크 하얏트 비엔나에서 도보 5분 거리에 있는 고급형 대형 마트. 와인, 치즈, 샐러드 등 퀄리티 높은 식료품이 많아 호텔에서 야식을 즐기기에 완벽합니다.
* **[[14] 율리어스 마인들 (Julius Meinl am Graben)](https://www.google.com/maps/search/?api=1&query=Julius+Meinl+am+Graben)**
  * **특징**: 호텔 근처 그라벤(Graben) 거리에 위치한 160년 전통의 프리미엄 식료품점. 최고급 커피 원두, 초콜릿 등 기념품 쇼핑의 성지입니다.

---"""
content = content.replace("## 🛍️ 필수 쇼핑 리스트", vie_md_addition + "\n\n## 🛍️ 필수 쇼핑 리스트", 1)

# SALZBURG
content = content.replace(
    '    ("Die Weisse", 47.8065, 13.0543, "purple"), # NEW\n]',
    '    ("Die Weisse", 47.8065, 13.0543, "purple"), # NEW\n    ("SPAR (마트)", 47.7888, 13.0305, "green"),\n    ("BILLA (마트)", 47.7963, 13.0326, "green"),\n]'
)
sal_md_addition = """
## 🛒 호텔 주변 마트 & 쇼핑 (지도 내 초록색 번호)

* **[[11] SPAR (스파)](https://www.google.com/maps/search/?api=1&query=SPAR+Sinnhubstraße+Salzburg)**
  * **특징**: 숙소(빌라 베르데) 바로 길 건너편 도보 2분 거리에 위치한 마트. 물, 맥주, 간단한 간식거리를 사서 숙소 정원에서 휴식하며 즐기기 좋습니다.
* **[[12] BILLA (빌라)](https://www.google.com/maps/search/?api=1&query=BILLA+Neutorstraße+Salzburg)**
  * **특징**: 숙소에서 구시가지로 걸어가거나 버스를 타고 나가는 길목(Neutorstraße)에 위치한 마트로, 이동 중에 들르기 좋습니다.

---"""
content = content.replace("## 🍺 수도원 맥주와 양조장 경험 (Bars & Drinks)", sal_md_addition + "\n\n## 🍺 수도원 맥주와 양조장 경험 (Bars & Drinks)")

# PRAGUE
content = content.replace(
    '    ("Hemingway Bar", 50.0839, 14.4150, "purple"),\n]',
    '    ("Hemingway Bar", 50.0839, 14.4150, "purple"),\n    ("Palladium (쇼핑몰)", 50.0894, 14.4293, "green"),\n    ("BILLA (마트)", 50.0886, 14.4312, "green"),\n]'
)
pra_md_addition = """
## 🛒 호텔 주변 마트 & 쇼핑 (지도 내 초록색 번호)

* **[[15] 팔라디움 (Palladium)](https://www.google.com/maps/search/?api=1&query=Palladium+Prague)**
  * **특징**: 안다즈 프라하 호텔에서 도보 4~5분 거리에 있는 프라하 최대 규모의 현대식 쇼핑몰. 의류, 잡화, 화장품(마누팍투라 포함) 매장이 빼곡히 입점해 있습니다.
* **[[16] BILLA (빌라 - 팔라디움 근처)](https://www.google.com/maps/search/?api=1&query=BILLA+V+Celnici+Prague)**
  * **특징**: 호텔 바로 근처에 위치한 대형 마트. 체코 전통 과자나 베체로브카(술), 코젤 맥주 등을 매우 저렴하게 구입할 수 있습니다.

---"""
content = content.replace("## 🛍️ 필수 쇼핑 리스트", pra_md_addition + "\n\n## 🛍️ 필수 쇼핑 리스트", 1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

