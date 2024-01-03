import requests

url = "https://api.hypixel.net/v2/skyblock/bazaar"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    golden_plate_sell_price = data["products"]["GOLDEN_PLATE"]["quick_status"]["sellPrice"]
    print("Golden Plate Sell Price:", "{:,.1f}".format(golden_plate_sell_price), "coins")
    refined_diamond_buy_price = data["products"]["REFINED_DIAMOND"]["quick_status"]["buyPrice"]
    print("Refined Diamond Buy Price:", "{:,.1f}".format(refined_diamond_buy_price), "coins")
    enchanted_gold_block_buy_price = data["products"]["ENCHANTED_GOLD_BLOCK"]["quick_status"]["buyPrice"]
    print("Enchanted Gold Block Buy Price:", "{:,.1f}".format(enchanted_gold_block_buy_price), "coins")
    glacite_jewel_buy_price = data["products"]["GLACITE_JEWEL"]["quick_status"]["buyPrice"]
    print("Glacite Jewel Buy Price:", "{:,.1f}".format(glacite_jewel_buy_price), "coins")
    print("-----------------------------------------------------------------------------------------------")
    profit = golden_plate_sell_price - refined_diamond_buy_price - (enchanted_gold_block_buy_price * 2) - (glacite_jewel_buy_price * 5)
    if profit > 0:
        print("\033[92mProfit: +%s coins\033[0m" % "{:,.1f}".format(profit))
    else:
        print("\033[91mProfit: -%s coins\033[0m" % "{:,.1f}".format(profit))

else:
    print("Failed to fetch data from the API")

input("\nPress Enter to exit...")
