"""Suno AI音楽生成ラボ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Suno AI音楽生成ラボ"
BLOG_DESCRIPTION = "AI作曲ツールSunoの使い方・プロンプト術・Udio比較を毎日更新。1億人が使うAI音楽生成の全てを解説。"
BLOG_URL = "https://musclelove-777.github.io/suno-music-lab"
BLOG_TAGLINE = "AI作曲の全てがわかる日本語情報サイト"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/suno-music-lab"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Suno 使い方",
    "Suno 料金・プラン",
    "Suno vs Udio",
    "Suno 最新ニュース",
    "AI作曲テクニック",
    "Suno プロンプト術",
    "AI音楽生成比較",
    "Suno 活用事例",
]

THEME = {
    "primary": "#1DB954",
    "accent": "#191414",
    "gradient_start": "#1DB954",
    "gradient_end": "#1ed760",
    "dark_bg": "#0a0a0a",
    "dark_surface": "#191414",
    "light_bg": "#f0fff4",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Suno Pro": [
        {"service": "Suno", "url": "https://suno.com", "description": "Suno公式サイトで始める"},
    ],
    "Udio": [
        {"service": "Udio", "url": "https://www.udio.com", "description": "Udioで音楽を生成する"},
    ],
    "DTM機材": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでDTM機材を探す"},
        {"service": "楽天", "url": "https://www.rakuten.co.jp", "description": "楽天でDTM機材を探す"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "Udemyで音楽制作講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI音楽関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI音楽関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8097
