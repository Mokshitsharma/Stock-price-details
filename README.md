# 📈 Stock Price Details — Indian Stock Fundamentals CLI

> **A colorful, auto-complete enabled command-line tool for fetching live stock fundamentals, today's price data, and shareholding patterns for Indian NSE stocks — all in your terminal.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![yfinance](https://img.shields.io/badge/yfinance-Live%20Data-green?style=flat-square)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

---

## 📌 Problem Statement

Most stock data tools require opening a browser, navigating to a website, searching for a stock, and clicking through multiple pages just to see basic fundamentals like PE ratio, EPS, Market Cap, and today's price. For developers, analysts, and investors who live in the terminal, there is no fast, keyboard-driven way to fetch live Indian stock fundamentals without leaving their workflow.

---

## 💡 My Solution

A lightweight Python CLI tool that fetches **live stock fundamentals, today's OHLCV data, and shareholding patterns** for 10 major NSE-listed stocks — directly in the terminal with:

- **Auto-complete** stock name suggestions as you type (powered by `prompt_toolkit`)
- **Color-coded output** for instant visual scanning (powered by `colorama`)
- **Human-readable number formatting** — Market Cap shown as `2.34T` not `2340000000000`
- **3 data sections** in one command: Fundamentals + Today's Stats + Shareholding Pattern

---

## 📊 Metrics & Output

| Section | Fields |
|---|---|
| **Fundamentals** | Company Name, Sector, Industry, Market Cap, Enterprise Value, 52-Week High, 52-Week Low, Dividend Yield, EPS, PE Ratio, PB Ratio, Beta |
| **Today's Stats** | Current Price (₹), Day High, Day Low, Volume |
| **Shareholding Pattern** | Major holders with percentage breakdown |

**Number formatting:**
- Values ≥ 1 Billion → shown as `XB` (e.g., `2.34B`)
- Values ≥ 1 Million → shown as `XM`
- Values ≥ 1 Thousand → shown as `XK`

---

## 🛠️ Skills & Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Market Data | yfinance (Yahoo Finance API) |
| CLI Autocomplete | prompt_toolkit (WordCompleter) |
| Terminal Colors | colorama (Fore, Style) |
| Data Formatting | Custom `format_value()` utility |
| Stocks Covered | 10 NSE large-caps (expandable) |

---

## 📂 Dataset Details

| Field | Details |
|---|---|
| **Data Source** | Yahoo Finance via yfinance (live, real-time) |
| **Exchange** | NSE (National Stock Exchange of India) |
| **Stocks Supported** | RELIANCE, TCS, INFY, HDFCBANK, ICICIBANK, HINDUNILVR, SBIN, AXISBANK, KOTAKBANK, ITC |
| **Data Type** | Live fundamentals + real-time OHLCV + major shareholding |
| **Latency** | Real-time (fetched on each run) |

---

## 🗂️ Folder Structure

```
Stock-price-details/
└── file.py          # Single-file CLI application (107 lines)
```

---

## ⚙️ System Architecture

```
Step 1 → User runs: python file.py
Step 2 → prompt_toolkit displays auto-complete suggestions as user types stock name
Step 3 → User selects / types a stock name (e.g., RELIANCE, TCS)
Step 4 → Stock name is mapped to NSE ticker symbol (e.g., RELIANCE → RELIANCE.NS)
Step 5 → yfinance fetches stock.info → fundamentals data (PE, EPS, Market Cap, Beta, etc.)
Step 6 → yfinance fetches stock.history(period="1d") → today's OHLCV data
Step 7 → yfinance fetches stock.major_holders → shareholding pattern
Step 8 → format_value() converts raw numbers to human-readable B/M/K format
Step 9 → colorama prints color-coded output: Cyan headers, Yellow labels, Green/Magenta sections
Step 10 → Full stock report displayed in terminal — no browser needed
```

---

## 🔍 Why This Tech Stack?

| Choice | Reason |
|---|---|
| **yfinance** | Free, reliable access to Yahoo Finance data for NSE/BSE stocks — no API key needed |
| **prompt_toolkit** | Industry-standard Python library for CLI UX — provides real autocomplete, not just argparse |
| **colorama** | Cross-platform terminal colors (works on Windows, Mac, Linux) — makes CLI output scannable |
| **Single file design** | Zero setup friction — clone and run; no complex package structure needed for a utility script |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
git clone https://github.com/Mokshitsharma/Stock-price-details.git
cd Stock-price-details
pip install yfinance prompt_toolkit colorama
```

### Run
```bash
python file.py
```

### Usage
```
Welcome to the Indian Stock Fundamentals Checker!
Enter stock name (e.g., RELIANCE, TCS). Auto-suggestions enabled.

Enter stock name: RELIANCE   ← type here, auto-suggestions appear

=== Fundamentals ===
Name:            Reliance Industries Limited
Sector:          Energy
Market Cap:      2.34T
PE Ratio:        28.4
EPS:             84.2
52-Week High:    ₹3,024
52-Week Low:     ₹2,220
...

=== Today's Stats ===
Current Price:   ₹2,856.30
High:            ₹2,871.00
Low:             ₹2,840.50
Volume:          4.23M

=== Shareholding Pattern ===
Promoters:       50.33%
Institutions:    29.17%
...
```

### Adding More Stocks
Open `file.py` and add to the `indian_stocks` dictionary:
```python
indian_stocks = {
    "WIPRO": "WIPRO.NS",
    "TATAMOTORS": "TATAMOTORS.NS",
    # add as many as you want
}
```

---

## 🔮 Future Improvements

1. **Expand stock universe** — cover all 50 Nifty stocks or allow any custom ticker input
2. **Historical price chart** — render ASCII price charts in terminal using `plotext` or `rich`
3. **Technical indicators** — add RSI, MACD, EMA directly in the CLI output
4. **Export to CSV** — save fetched data to a local file for record-keeping
5. **Web version** — wrap this into a Streamlit app for browser-based access
6. **Watchlist mode** — monitor multiple stocks simultaneously with auto-refresh

---

## 👤 Author

**Mokshit Sharma**
B.Tech + M.Tech (Dual Degree) — AI & Data Science | DAVV, Indore
📧 sharman48520@gmail.com | 🌐 [mokshitsharma27.vercel.app](https://mokshitsharma27.vercel.app)
🔗 [LinkedIn](https://linkedin.com/in/mokshit-sharma-75b5ab305) | 💻 [GitHub](https://github.com/Mokshitsharma)

---

⭐ Star this repo if you found it useful!
