# main.py

from car_price_prediction.data.load_data import load_data
def main():
    # Laden der Daten
    data = load_data('CarPriceModelData.csv')
if __name__ == "__main__":
    main()
