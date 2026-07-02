import sys
import json
from webullsdkcore.client import ApiClient

def get_quote(app_key, app_secret, symbol, region="jp"):
    try:
        api_client = ApiClient(app_key=app_key, app_secret=app_secret, region_id=region)
        quote = api_client.quote.get_brief_quote(symbol)
        
        current_price = quote.get('last')
        ath = quote.get('high52week')
        
        return {
            "symbol": symbol,
            "currentPrice": current_price,
            "allTimeHigh": ath,
            "percentFromATH": round(((current_price - ath) / ath * 100), 2) if ath and current_price else None
        }
    except Exception as e:
        return {"error": str(e), "symbol": symbol}

if __name__ == "__main__":
    app_key = sys.argv[1]
    app_secret = sys.argv[2]
    symbol = sys.argv[3]
    
    result = get_quote(app_key, app_secret, symbol)
    print(json.dumps(result))
