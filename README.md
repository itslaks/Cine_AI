# 🎬 CineAI — One Stop for All Cinephiles

![CineAI Banner](https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&q=80&w=1200)

[![GitHub License](https://img.shields.io/github/license/itslaks/Cine_AI?style=flat-square&color=gold)](https://github.com/itslaks/Cine_AI/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/itslaks/Cine_AI?style=flat-square&color=teal)](https://github.com/itslaks/Cine_AI/stargazers)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-violet?style=flat-square)](https://www.python.org/)

**CineAI** is a premium, AI-powered movie discovery engine designed for those who don't just watch films—they live them. From underground Tamil masterpieces to Hollywood cult classics, CineAI understands the subtle nuances of your cinematic cravings.

---

## 🏗️ High-Level Architecture

CineAI is built on a distributed agentic architecture that prioritizes relevance and aesthetic precision.

```mermaid
graph TD
    User([Cinema Lover]) -->|Natural Language| UI[Glassmorphism Frontend]
    UI -->|Async Request| API[FastAPI Backend]
    API -->|LLM Reasoning| Groq[Groq LLaMA 3.1]
    API -->|Metadata| OMDb[OMDb API]
    API -->|Art & Trends| TMDB[TMDB API]
    API -->|Persistence| Cache[File System Cache]
    API -->|Watchlist| DB[(Local JSON DB)]
    Groq -->|Strategic Candidates| API
```

---

## ⚡ The Vibe & The Tech

CineAI merges a high-performance **FastAPI** backend with a sleek, glassmorphism-inspired **Vanilla JS** frontend.

### 🎭 Cinematic Features
- 🧠 **AI Recommendation Mode**: Describe your mood or a complex vibe. "Indie horror with 1980s synthwave aesthetics."
- 🔍 **Enriched Movie Lookup**: Beyond just a synopsis. Get 4-metric scores, streaming availability, and critical consensus.
- 🦸 **Character Archetype Mapping**: Find movies based on character tropes. Want another "stoic lone wolf"? We got you.
- 📅 **Decade Timelines**: Search specifically for eras. "90s grimy thrillers" or "Golden age Hollywood romance."
- ⚔️ **Metric Comparison Engine**: Side-by-side battle between two films using weighted analytics.

### 🔬 Advanced Metrics
Standard ratings are boring. CineAI uses a **Weighted Sentiment Index (WSI)**:
- **IMDb (35%)**: The global baseline.
- **Rotten Tomatoes (25%)**: Critical consensus.
- **Metacritic (20%)**: High-brow critical weighting.
- **Audience Score Proxy (20%)**: Derived via complex metadata parsing of vote density.

---

## 🚦 Quick Start for Cinephiles

### 1️⃣ Environment Setup
Clone the universe and install the logic:
```bash
git clone https://github.com/itslaks/Cine_AI.git
cd Cine_AI/main
pip install -r requirements.txt
```

### 2️⃣ Secret Sauce (API Keys)
Create a `.env` file in the `main` directory:
```env
GROQ_API_KEY=your_key
TMDB_API_KEY=your_key
OMDB_API_KEY=your_key
```

### 3️⃣ Action!
Launch the engine:
```bash
python main.py
```
Explore the cinematic multiverse at `http://127.0.0.1:8000`.

---

## 🤝 Contribution & Community
We're building the future of film discovery. Feel free to fork `itslaks/Cine_AI` and submit PRs for new discovery modes or aesthetic upgrades.

- **Architect**: [itslaks](https://github.com/itslaks)
- **Engine**: ⚡ LLaMA 3.1 
- **Soul**: 🍿 Cinema Enthusiasts

---

*Stay cinematic.* 🎥✨
