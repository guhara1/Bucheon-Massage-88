# 간다GO — 부천 출장마사지·홈타이 안내 사이트

부천시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/WebPage/FAQPage JSON-LD)
  areas.py          # 행정구별: 부천 허브 + 원미구/소사구/오정구 집계
  areas_wonmi.py    # 원미구 허브 + 대표 동 9개
  areas_sosa.py     # 소사구 허브 + 대표 동 6개
  areas_ojeong.py   # 오정구 허브 + 대표 동 5개
  stations.py       # 역세권별: 허브 + 13개 역(1·7호선·서해선)
  info.py           # 출장마사지/홈타이 안내·예약·가이드·홈타이 가이드·고객센터·약관
  about.py          # 운영자 소개 (E-E-A-T)
  pricing.py        # 공용 요금 블록
assets/             # CSS, 모바일 내비 JS, 파비콘/OG
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 행정구는 원미구·소사구·오정구 3개 — 행정구 페이지를 먼저 두는 허브 구조
- 동은 대표 동 단위만 (심곡1·2·3동 → 심곡동 등) — 숫자 행정동 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역(소사역·부천종합운동장역)도 URL 하나, 출구별 페이지 없음
- 메타 디스크립션은 모두 80자 이내
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 불법·선정적 표현, 허위 후기, 과장 광고 금지

## URL 구조

```
/                                                  메인
/bucheon/                                          행정구 허브
/bucheon/wonmi-gu-chuljangmassage/                 원미구 허브 (소사구·오정구 동일)
/bucheon/wonmi/{dong}-dong-chuljangmassage/        원미구 대표 동
/bucheon/sosa/{dong}-dong-chuljangmassage/         소사구 대표 동
/bucheon/ojeong/{dong}-dong-chuljangmassage/       오정구 대표 동
/bucheon/stations/                                 역세권 허브
/bucheon/{station}-chuljangmassage/                역세권 페이지
/massage/ /hometai/ /reservation/ /guide/ /hometai-guide/
/support/ /support/privacy/ /support/terms/ /about/
```

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출, 네이버 서치어드바이저 동일
