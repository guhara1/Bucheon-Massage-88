# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://bucheon-massage-88.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "G"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"
TAGLINE = "부천 전지역 방문 관리"
SERVICE_AREA = "경기도 부천시 전지역"

# IndexNow 키 — 빌드 시 루트에 {KEY}.txt 파일로 생성된다(빙·네이버 즉시 색인 통보용).
INDEXNOW_KEY = "e9b782a229a61379a7c0a9b2ee1604c5"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("출장마사지 안내", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("행정구별 방문 안내", "/massage/#coverage"),
        ("역세권 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("홈타이 안내", "/hometai/", []),
    ("행정구별 안내", "/bucheon/", [
        ("부천 전체", "/bucheon/"),
        ("원미구", "/bucheon/wonmi-gu-chuljangmassage/"),
        ("소사구", "/bucheon/sosa-gu-chuljangmassage/"),
        ("오정구", "/bucheon/ojeong-gu-chuljangmassage/"),
    ]),
    ("역세권별 안내", "/bucheon/stations/", [
        ("역 전체", "/bucheon/stations/"),
        ("부천역", "/bucheon/bucheon-station-chuljangmassage/"),
        ("역곡역", "/bucheon/yeokgok-station-chuljangmassage/"),
        ("소사역", "/bucheon/sosa-station-chuljangmassage/"),
        ("중동역", "/bucheon/jung-dong-station-chuljangmassage/"),
        ("송내역", "/bucheon/songnae-station-chuljangmassage/"),
        ("상동역", "/bucheon/sang-dong-station-chuljangmassage/"),
        ("부천시청역", "/bucheon/bucheon-cityhall-station-chuljangmassage/"),
        ("신중동역", "/bucheon/sinjung-dong-station-chuljangmassage/"),
        ("춘의역", "/bucheon/chunui-station-chuljangmassage/"),
        ("부천종합운동장역", "/bucheon/bucheon-stadium-station-chuljangmassage/"),
        ("까치울역", "/bucheon/kkachiul-station-chuljangmassage/"),
        ("소새울역", "/bucheon/sosaeul-station-chuljangmassage/"),
        ("원종역", "/bucheon/wonjong-station-chuljangmassage/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용 가이드", "/guide/", [
        ("이용 전 확인사항", "/guide/#prepare"),
        ("처음 이용하시는 분", "/guide/#first"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("홈타이 이용 가이드", "/hometai-guide/"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
        ("운영자 소개", "/about/"),
    ]),
]
