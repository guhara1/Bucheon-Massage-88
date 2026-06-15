# 메인 페이지 — 허브 역할. 행정구를 중간 허브로 세우고 대표 동·역세권으로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<meta name="naver-site-verification" content="d72b9347bb45636527b3fc7a291a8c7fe69e5925">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "부천 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 부천시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "부천 출장마사지·부천시 홈타이 지역별 안내",
  "url": "{BASE_URL}/",
  "description": "부천 출장마사지·홈타이 예약 전 원미구, 소사구, 오정구 생활권을 확인하세요."
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "부천 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 행정구별 안내에서 원미구, 소사구, 오정구 생활권을 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "부천역이나 상동역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "중1동과 중2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "숫자가 붙은 행정동은 중동, 상동, 송내동처럼 대표 동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이도 같은 곳에서 예약하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "네, 출장마사지와 홈타이는 같은 예약 전화로 안내합니다. 홈타이 안내 페이지에서 진행 방식을 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 부천 전지역</p>
    <h1>부천 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">원미구·소사구·오정구 생활권을 먼저 확인하고, 계신 곳에서 받는 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/bucheon/">행정구별 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>3개</strong><span>행정구</span></li>
      <li><strong>20개</strong><span>대표 동</span></li>
      <li><strong>13개</strong><span>역세권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="why">
<h2>부천시에서 출장마사지를 찾는 이유</h2>
<p>부천 출장마사지를 찾는 분들은 대부분 지금 계신 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 부천은 서울 서남권과 인천, 시흥, 광명과 맞닿아 있어 이동 수요가 꾸준한 도시입니다. 같은 부천 안에서도 원미구, 소사구, 오정구는 생활권이 서로 달라서, 한 페이지에 모든 내용을 몰아넣기보다 행정구와 대표 동, 지하철역을 나눠 안내하는 방식이 더 정확합니다. {BRAND}는 부천 전지역 방문 관리를 행정구 허브 중심으로 정리해, 처음 이용하시는 분도 본인 생활권을 빠르게 찾아 예약할 수 있도록 안내합니다. 출장마사지와 홈타이는 같은 예약 창구에서 함께 안내해 드립니다.</p>
</section>

<section id="districts">
<h2>원미구·소사구·오정구 생활권별 차이</h2>
<p>부천시는 행정구가 있는 도시이므로 행정구 페이지를 먼저 두고, 그 아래 대표 동과 역세권을 연결합니다. 원미구는 부천역, 신중동, 부천시청, 상동처럼 상권과 역세권 수요가 강한 지역입니다. 소사구는 소사역, 송내역, 옥길동, 범박동처럼 주거지와 교통 접근성이 함께 있는 지역이고, 오정구는 원종동, 고강동, 오정동처럼 차량 이동과 서해선 역세권을 함께 고려하는 생활권입니다. 본인이 속한 행정구를 먼저 고르시면 그 안에서 대표 동과 가까운 역을 따라가기 쉽습니다.</p>
<ul class="card-grid">
<li><a href="/bucheon/wonmi-gu-chuljangmassage/">원미구</a></li>
<li><a href="/bucheon/sosa-gu-chuljangmassage/">소사구</a></li>
<li><a href="/bucheon/ojeong-gu-chuljangmassage/">오정구</a></li>
</ul>
<p>부천 전체 지역 구조가 궁금하시면 <a href="/bucheon/">행정구별 안내</a>에서 세 개 구와 대표 동을 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="dongs">
<h2>대표 행정동별 방문 가능 지역</h2>
<p>부천시는 번호가 붙은 행정동이 많지만, 심곡1·2·3동을 각각 만들지 않고 심곡동 하나로 통합하듯 대표 행정동 단위로 안내합니다. 같은 생활권을 잘게 쪼개면 비슷한 내용이 반복되고, 검색하는 분께도 어느 페이지를 봐야 할지 혼란만 주기 때문입니다. 원미구는 심곡동·원미동·소사동·역곡동·춘의동·도당동·약대동·중동·상동, 소사구는 심곡본동·소사본동·범박동·옥길동·괴안동·송내동, 오정구는 성곡동·원종동·고강동·오정동·신흥동을 대표 동으로 안내합니다. 각 동 페이지에서 생활권 특징과 방문 조건을 동마다 다르게 설명합니다.</p>
</section>

<section id="stations">
<h2>부천 주요 역세권 출장마사지 안내</h2>
<p>역을 기준으로 위치를 설명하는 것이 편하시다면 역세권 안내를 참고하세요. 1호선·7호선·서해선이 지나는 부천의 13개 역을 역마다 한 페이지씩 안내합니다. 소사역과 부천종합운동장역처럼 두 노선이 만나는 환승역도 노선별로 나누지 않고 한 페이지로만 운영하며, 본문에서 환승 특징을 설명합니다.</p>
<ul class="card-grid">
<li><a href="/bucheon/bucheon-station-chuljangmassage/">부천역</a></li>
<li><a href="/bucheon/yeokgok-station-chuljangmassage/">역곡역</a></li>
<li><a href="/bucheon/sosa-station-chuljangmassage/">소사역</a></li>
<li><a href="/bucheon/jung-dong-station-chuljangmassage/">중동역</a></li>
<li><a href="/bucheon/songnae-station-chuljangmassage/">송내역</a></li>
<li><a href="/bucheon/sang-dong-station-chuljangmassage/">상동역</a></li>
<li><a href="/bucheon/bucheon-cityhall-station-chuljangmassage/">부천시청역</a></li>
<li><a href="/bucheon/sinjung-dong-station-chuljangmassage/">신중동역</a></li>
<li><a href="/bucheon/chunui-station-chuljangmassage/">춘의역</a></li>
<li><a href="/bucheon/bucheon-stadium-station-chuljangmassage/">부천종합운동장역</a></li>
<li><a href="/bucheon/kkachiul-station-chuljangmassage/">까치울역</a></li>
<li><a href="/bucheon/sosaeul-station-chuljangmassage/">소새울역</a></li>
<li><a href="/bucheon/wonjong-station-chuljangmassage/">원종역</a></li>
</ul>
</section>

<section id="hometai">
<h2>부천 홈타이 예약 전 확인사항</h2>
<p>부천 홈타이는 자택, 숙소, 사무실 인근에서 방문 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 오일 없이 편한 옷차림으로 받는 구성이라 처음 이용하는 분도 부담이 적습니다. 예약 전에는 방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 결제 방식, 취소 기준, 서비스 범위를 함께 확인하시는 것이 좋습니다. 홈타이 진행 방식은 <a href="/hometai/">홈타이 안내</a>와 <a href="/hometai-guide/">홈타이 이용 가이드</a>에서, 예약 절차는 <a href="/reservation/">예약 안내</a>에서 자세히 다룹니다.</p>
</section>

<section id="seo">
<h2>구글 기준에 맞는 부천 지역 페이지 구성</h2>
<p>이 사이트는 페이지 수를 무리하게 늘리기보다 페이지마다 고유한 정보를 담는 방향으로 구성했습니다. 번호 행정동을 각각 만들지 않고 대표 동으로 통합하며, 환승역은 한 URL만 사용하고, 같은 본문에서 지역명만 바꾸는 방식을 쓰지 않습니다. 불법·선정적 표현이나 허위 후기, 과장 광고는 사용하지 않으며, 방문 가능 지역과 예약 절차, 이용 전 확인사항, 개인정보 처리 기준을 분명히 안내합니다. 정보 중심으로 운영하는 부천 출장마사지·홈타이 안내 사이트입니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>부천 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. <a href="/bucheon/">행정구별 안내</a>에서 원미구, 소사구, 오정구 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>부천역이나 상동역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>중1동, 상1동처럼 번호 동은 왜 따로 없나요?</h3>
<p>숫자가 붙은 행정동은 중동, 상동, 송내동처럼 대표 동 페이지에서 통합 안내합니다. 방문은 행정동이 아니라 실제 주소 기준으로 진행됩니다.</p>
</div>
<div class="faq-item">
<h3>홈타이와 출장마사지는 어떻게 다른가요?</h3>
<p>홈타이는 집에서 받는 타이마사지를 가리키는 말로, 출장마사지의 대표 형태입니다. 두 가지 모두 같은 예약 전화로 안내해 드립니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>부천 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "부천 출장마사지｜원미구·소사구·오정구 홈타이 지역 안내",
    "desc": "부천 출장마사지·홈타이 예약 전 원미구, 소사구, 오정구 생활권을 확인하세요.",
    "h1": "부천 출장마사지 · 부천시 홈타이 지역별 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
