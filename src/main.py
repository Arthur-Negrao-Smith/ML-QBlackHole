import pandas as pd

from util.data_keys import Datakeys as dk

RAW_DATA_PATH: str = "src/data/raw_data"
RAW_FILE: str = RAW_DATA_PATH + "/default_simulation.csv"

MANIPULATED_DATA_PATH: str = "src/data/manipulated_data"

TARGETS: list[int] = [0, 1]
BLACK_HOLES_NUMBER: list[int] = [1, 3, 5]
ENTANGLEMENT_SWAPPING_PROB: float = 0.8
INTENSITIES: list[float] = list(
    reversed([ENTANGLEMENT_SWAPPING_PROB - 0.1 * i for i in range(1, 9)])
)


def main() -> None:
    """
    Split all dataset by experiment
    """
    all_df: pd.DataFrame = pd.read_csv(RAW_FILE)
    df_filtered: dict[str, pd.DataFrame | pd.Series] = {}

    for target in TARGETS:
        for bh_num in BLACK_HOLES_NUMBER:
            for intensity in INTENSITIES:
                tmp_df: pd.DataFrame | pd.Series = all_df.loc[
                    (all_df[dk.TARGETS_PER_BLACK_HOLE.value] == target)
                    & (all_df[dk.NUMBER_OF_BLACK_HOLES.value] == bh_num)
                    & (
                        all_df[dk.BLACK_HOLE_SWAP_PROB.value].round(1)
                        == round(intensity, 1)  # round the decimal points
                    )
                ]
                dict_key: str = "without_target_" if target == 0 else "with_target-"
                dict_key += f"{bh_num}_bha-"
                dict_key += str(round(intensity, 1)).replace(".", "") + "_intensity.csv"

                df_filtered[dict_key] = tmp_df

    for csv_name, current_df in df_filtered.items():
        current_df.to_csv(
            MANIPULATED_DATA_PATH + "/" + csv_name, mode="w", encoding="utf-8"
        )

    return


if __name__ == "__main__":
    main()
