from threading import Thread, RLock
import os


class MyThread(Thread):
    def __init__(self, target, args=()):
        super().__init__(target=target, args=args)

        self.result = None

    def run(self):
        self.result = self._target(*self._args)


def get_files_from_folder(path: str) -> list:
    file_paths = []

    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
        else:
            th = MyThread(target=get_files_from_folder, args=(file_path,))
            th.start()
            th.join()
            file_paths += th.result

    return file_paths


if __name__ == "__main__":
    path = "C:\\Users\\PC\\Documents\\GitHub\\goit-homework-02\\clean_folder\\t"
    # result = []
    # for _ in range(5):
    #     th = FactorThread(target=get_files_from_folder, args=(path,))
    #     th.start()
    #     th.join()
    #     result.append(th.result)
    # print(result)
    res = get_files_from_folder(path)
    print(res)
