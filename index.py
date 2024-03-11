from os import getcwd, listdir
from time import sleep

from loguru import logger
from requests import post

PATH_TO_WORKING_ENV = getcwd()
logger.debug(f"{PATH_TO_WORKING_ENV=}")

LIST_OF_FILES = listdir(PATH_TO_WORKING_ENV)
logger.debug(f"{LIST_OF_FILES=}")

URL = ""
SECURITY_KEY = ""


def get_full_files_names_from_working_env() -> dict | None:
    list_of_files = listdir(path=PATH_TO_WORKING_ENV)
    result = {}

    for file_name in list_of_files:
        if "import" in file_name:
            result["import"] = file_name
        if "offers" in file_name:
            result["offers"] = file_name

    if len(result) == 2:
        return result
    else:
        return None


if __name__ == "__main__":
    while True:
        files_for_work = get_full_files_names_from_working_env()
        if not files_for_work:
            logger.debug("Files not found in working env")
        else:
            logger.debug(f"{files_for_work=}")

            import_file = open(file=files_for_work["import"], mode="rb")
            offers_file = open(file=files_for_work["offers"], mode="rb")

            post(
                url=URL,
                files={
                    "import.xml": import_file,
                    "offers.xml": offers_file,
                },
                headers={"security_key": SECURITY_KEY},
            )

            import_file.close()
            offers_file.close()

        sleep(3600 * 1.5)
