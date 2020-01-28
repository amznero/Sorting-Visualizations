import argparse
from utils import generate_data, visulization
from sort import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    shell_sort,
    merge_cost,
    quick_sort,
)


def main(args):
    raise NotImplementedError


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sort",
        type=str,
        choices=["bubble", "selection", "insertion", "shell", "merge", "quick"],
    )

    args = parser.parse_args()
    main(args)
