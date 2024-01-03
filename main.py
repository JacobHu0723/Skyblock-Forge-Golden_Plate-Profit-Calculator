import sys
from pathlib import Path

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

url = "https://api.hypixel.net/v2/skyblock/bazaar"

SRC_PATH = Path.absolute(Path(__file__)).parent  # Get temp path
icon_path = str(SRC_PATH / "icon.ico")  # Add to get icon path


class HypixelBazaar(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Skyblock Golden Plate Profit Calculator")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout(self)

        self.labels = []
        for i in range(4):
            label = QLabel(self)
            font = label.font()
            font.setPointSize(12)  # Set Font Size
            label.setFont(font)
            self.layout.addWidget(label)
            self.labels.append(label)

        self.profit_label = QLabel(self)
        font = self.profit_label.font()
        font.setPointSize(12)  # Set Font Size
        self.profit_label.setFont(font)
        self.layout.addWidget(self.profit_label)

        self.update_button = QPushButton("Update Prices", self)
        self.update_button.clicked.connect(self.fetch_and_update_prices)
        self.layout.addWidget(self.update_button)

        self.fetch_and_update_prices()

    def fetch_and_update_prices(self):
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            golden_plate_sell_price = data["products"]["GOLDEN_PLATE"]["quick_status"]["sellPrice"]
            refined_diamond_buy_price = data["products"]["REFINED_DIAMOND"]["quick_status"]["buyPrice"]
            enchanted_gold_block_buy_price = data["products"]["ENCHANTED_GOLD_BLOCK"]["quick_status"]["buyPrice"]
            glacite_jewel_buy_price = data["products"]["GLACITE_JEWEL"]["quick_status"]["buyPrice"]

            self.labels[0].setText(f"Golden Plate Sell Price: {golden_plate_sell_price:,.1f} coins")
            self.labels[1].setText(f"Refined Diamond Buy Price: {refined_diamond_buy_price:,.1f} coins")
            self.labels[2].setText(f"Enchanted Gold Block Buy Price: {enchanted_gold_block_buy_price:,.1f} coins")
            self.labels[3].setText(f"Glacite Jewel Buy Price: {glacite_jewel_buy_price:,.1f} coins")

            profit = golden_plate_sell_price - refined_diamond_buy_price - (enchanted_gold_block_buy_price * 2) - (
                    glacite_jewel_buy_price * 5)
            if profit > 0:
                self.profit_label.setText(f"Profit: +{profit:,.1f} coins")
                self.profit_label.setTextFormat(Qt.RichText)
                self.profit_label.setStyleSheet("color: green;")
            else:
                self.profit_label.setText(f"Profit: -{profit:,.1f} coins")
                self.profit_label.setTextFormat(Qt.RichText)
                self.profit_label.setStyleSheet("color: red;")
        else:
            self.profit_label.setText("Failed to fetch data from the API")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HypixelBazaar()
    window.setWindowIcon(QIcon(icon_path))
    window.show()
    sys.exit(app.exec_())
