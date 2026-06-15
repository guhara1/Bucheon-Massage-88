#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙(Bing)·네이버(Naver)·얀덱스 등에 URL 변경을 알린다.

IndexNow는 한 번의 요청으로 참여 검색엔진 전체에 전달된다(구글은 미참여).
키 파일(/{KEY}.txt)은 build.py가 사이트 루트에 생성하므로, 배포가 끝난 뒤 실행해야
검색엔진이 키를 검증할 수 있다.

사용법:
    python3 tools/indexnow_submit.py                 # urls.txt 의 전체 URL 통보
    python3 tools/indexnow_submit.py https://.../a/   # 특정 URL만 통보(여러 개 가능)

의존성 없음(표준 라이브러리만 사용).
"""
import json
import os
import sys
import urllib.request
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ENDPOINT = "https://api.indexnow.org/indexnow"
BASE = BASE_URL.rstrip("/")
HOST = urlparse(BASE).netloc


def load_urls() -> list:
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    if args:
        return args
    path = os.path.join(ROOT, "urls.txt")
    if not os.path.exists(path):
        sys.exit("urls.txt 가 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]


def main() -> None:
    urls = load_urls()
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"IndexNow → {ENDPOINT}")
    print(f"  host={HOST}  urls={len(urls)}  keyLocation={BASE}/{INDEXNOW_KEY}.txt")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  HTTP {resp.status} {resp.reason}")
            # 200/202 = 정상 접수. 403 = 키 검증 실패(배포·키파일 확인). 422 = URL/호스트 불일치.
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} {e.reason}\n  {e.read().decode('utf-8', 'replace')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
