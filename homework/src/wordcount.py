# ejemplo casos de uso
# python -m homework data/input data/output

import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder containing files to process.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def read_all_lines(input_folder):
    lines = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
