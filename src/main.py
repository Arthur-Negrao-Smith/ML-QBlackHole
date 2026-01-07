import pandas as pd

RAW_DATA_PATH: str = "src/data/raw_data"
RAW_FILE: str = RAW_DATA_PATH + "/default_simulation.csv"


def main() -> None:
    all_df: pd.DataFrame = pd.read_csv(RAW_FILE)
    return


if __name__ == "__main__":
    main()
