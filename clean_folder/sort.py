import sys
from clean_folder import categorizer, mover, utils


def sorter(path_to_folder: str):
    file_paths = utils.get_files_from_folder(path_to_folder)

    categorize_result = categorizer.categorize_files(file_paths)

    for category, files in categorize_result["to_move"].items():
        for file in files:
            if category == "archives":
                mover.move_archive(file, path_to_folder)
            else:
                mover.move_file(file, category, path_to_folder)

    utils.remove_empty_folders(path_to_folder)
    print(
        f"Categories: {categorize_result['to_move']}\n"
        f"All extensions: {', '.join(categorize_result['all_extensions'])}\n"
        f"Unknown extensions: {', '.join(categorize_result['unknown_extensions'])}"
    )


def main():
    if len(sys.argv) < 2:
        print("You need to specify the folder name for sorting")
        sys.exit()

    path_to_folder = sys.argv[1]

    sorter(path_to_folder)


if __name__ == "__main__":
    main()
