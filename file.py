import yfinance as yf
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import Fore, Style, init

# colour of the particular keyword
init(autoreset=True)

# isme aur jyada bhi add kr skte h, jitne mrzi ho utne 
indian_stocks = {
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "INFY": "INFY.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "HINDUNILVR": "HINDUNILVR.NS",
    "SBIN": "SBIN.NS",
    "AXISBANK": "AXISBANK.NS",
    "KOTAKBANK": "KOTAKBANK.NS",
    "ITC": "ITC.NS",
}

# dropdown/suggestion
stock_completer = WordCompleter(indian_stocks.keys(), ignore_case=True)

def format_value(value):
    """Format large numbers to human-readable format."""
    try:
        if value >= 1e9:
            return f"{value / 1e9:.2f}B"
        elif value >= 1e6:
            return f"{value / 1e6:.2f}M"
        elif value >= 1e3:
            return f"{value / 1e3:.2f}K"
        else:
            return f"{value}"
    except:
        return "N/A"

def display_fundamentals(info):
    print(Fore.CYAN + "\n=== Fundamentals ===")
    print(f"{Fore.YELLOW}Name:{Style.RESET_ALL} {info.get('longName', 'N/A')}")
    print(f"{Fore.YELLOW}Sector:{Style.RESET_ALL} {info.get('sector', 'N/A')}")
    print(f"{Fore.YELLOW}Industry:{Style.RESET_ALL} {info.get('industry', 'N/A')}")
    print(f"{Fore.YELLOW}Market Cap:{Style.RESET_ALL} {format_value(info.get('marketCap', 0))}")
    print(f"{Fore.YELLOW}Enterprise Value:{Style.RESET_ALL} {format_value(info.get('enterpriseValue', 0))}")
    print(f"{Fore.YELLOW}52-Week High:{Style.RESET_ALL} {info.get('fiftyTwoWeekHigh', 'N/A')}")
    print(f"{Fore.YELLOW}52-Week Low:{Style.RESET_ALL} {info.get('fiftyTwoWeekLow', 'N/A')}")
    print(f"{Fore.YELLOW}Dividend Yield:{Style.RESET_ALL} {info.get('dividendYield', 'N/A')}")
    print(f"{Fore.YELLOW}EPS:{Style.RESET_ALL} {info.get('trailingEps', 'N/A')}")
    print(f"{Fore.YELLOW}PE Ratio:{Style.RESET_ALL} {info.get('trailingPE', 'N/A')}")
    print(f"{Fore.YELLOW}PB Ratio:{Style.RESET_ALL} {info.get('priceToBook', 'N/A')}")
    print(f"{Fore.YELLOW}Beta:{Style.RESET_ALL} {info.get('beta', 'N/A')}")

def display_live_data(history):
    print(Fore.GREEN + "\n=== Today's Stats ===")
    try:
        current_price = history["Close"].iloc[-1]
        high = history["High"].iloc[-1]
        low = history["Low"].iloc[-1]
        volume = history["Volume"].iloc[-1]

        print(f"{Fore.YELLOW}Current Price:{Style.RESET_ALL} ₹{current_price:.2f}")
        print(f"{Fore.YELLOW}High:{Style.RESET_ALL} ₹{high:.2f}")
        print(f"{Fore.YELLOW}Low:{Style.RESET_ALL} ₹{low:.2f}")
        print(f"{Fore.YELLOW}Volume:{Style.RESET_ALL} {format_value(volume)}")
    except:
        print("Unable to fetch today's data.")

def display_shareholding(stock):
    print(Fore.MAGENTA + "\n=== Shareholding Pattern ===")
    try:
        holders = stock.major_holders
        if not holders.empty:
            for i, row in holders.iterrows():
                print(f"{row[1]}: {row[0]:.2f}%")
        else:
            print("Shareholding data not available.")
    except:
        print("Error fetching shareholding data.")

def fetch_fundamentals(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        todays_data = stock.history(period="1d")

        display_fundamentals(info)
        display_live_data(todays_data)
        display_shareholding(stock)

    except Exception as e:
        print(Fore.RED + f"Error fetching data: {e}")

def main():
    print(Fore.BLUE + "Welcome to the Indian Stock Fundamentals Checker!")
    print("Enter stock name (e.g., RELIANCE, TCS). Auto-suggestions enabled.\n")

    stock_name = prompt("Enter stock name: ", completer=stock_completer).strip().upper()

    if stock_name in indian_stocks:
        fetch_fundamentals(indian_stocks[stock_name])
    else:
        print(Fore.RED + "Stock not found in the list. Please try again.")

if __name__ == "__main__":
    main()
