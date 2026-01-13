import pandas as pd

from util.data_keys import Datakeys as dk

RAW_DATA_PATH: str = "data/raw"
RAW_FILE: str = RAW_DATA_PATH + "/default_simulation.csv"

MANIPULATED_DATA_PATH: str = "data/manipulated"

TARGETS: list[int] = [0, 1]
BLACK_HOLES_NUMBER: list[int] = [1, 3, 5]
ENTANGLEMENT_SWAPPING_PROB: float = 0.8
INTENSITIES: list[float] = [round(ENTANGLEMENT_SWAPPING_PROB - 0.1 * i, 1) for i in range(0, 8)]
print(INTENSITIES)
BHA_PROBS: list[float] = list(
    reversed([ENTANGLEMENT_SWAPPING_PROB - 0.1 * i for i in range(1, 9)])
)

FILE_NAMES: list[str] = []
for target in TARGETS:
    for bh_num in BLACK_HOLES_NUMBER:
        for intensity in INTENSITIES:
            file_name: str = MANIPULATED_DATA_PATH + "/"
            file_name = "without_target_" if target == 0 else "with_target-"
            file_name += f"{bh_num}_bha-"
            file_name += str(round(intensity, 1)).replace(".", "") + "_intensity.csv"
            FILE_NAMES.append(file_name)

def split_dataset() -> None:
    """
    Split all dataset by experiment
    """
    all_df: pd.DataFrame = pd.read_csv(RAW_FILE)
    df_filtered: dict[str, pd.DataFrame | pd.Series] = {}

    for target in TARGETS:
        for bh_num in BLACK_HOLES_NUMBER:
            intensity: int = 0
            for bha_prob in BHA_PROBS:
                tmp_df: pd.DataFrame | pd.Series = all_df.loc[
                    (all_df[dk.TARGETS_PER_BLACK_HOLE.value] == target)
                    & (all_df[dk.NUMBER_OF_BLACK_HOLES.value] == bh_num)
                    & (
                        all_df[dk.BLACK_HOLE_SWAP_PROB.value].round(1)
                        == round(bha_prob, 1)  # round the decimal points
                    )
                ]
                dict_key: str = "without_target_" if target == 0 else "with_target-"
                dict_key += f"{bh_num}_bha-"
                dict_key += str(INTENSITIES[intensity]).replace(".", "") + "_intensity.csv"

                df_filtered[dict_key] = tmp_df

                intensity += 1

    for csv_name, current_df in df_filtered.items():
        current_df.to_csv(
            MANIPULATED_DATA_PATH + "/" + csv_name, mode="w", encoding="utf-8", index=False
        )

    return

def load_dataset(path: str) -> pd.DataFrame:
    if not file_exists(path):
        raise FileExistsError("Dataset not found")

    df: pd.DataFrame = pd.read_csv(path, index_col=False)
    return df

def file_exists(path: str) -> bool:
    exists: bool = False
    try:
        with open(path, "r") as _:
            pass
        exists = True

    except:
        exists = False

    return exists

