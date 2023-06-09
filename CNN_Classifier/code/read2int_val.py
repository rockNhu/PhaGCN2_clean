import numpy as np
import os

k_list = ["A", "C", "G", "T"]
nucl_list = ["A", "C", "G", "T"]


for _ in range(2):
    tmp = []
    for item in nucl_list:
        tmp.extend(nucl+item for nucl in k_list)
    k_list = tmp


int_to_vocab = dict(enumerate(k_list))
vocab_to_int = {word: ii for ii, word in int_to_vocab.items()}


def encode(file_name):
    file = open(f"stride50_val/{file_name}")
    data = file.readlines()
    feature = []
    for read in data:
        read = read[:-1]
        int_read = []
        for i in range(len(read)):
            if i + 3 > len(read):
                break

            int_read.append(vocab_to_int[read[i:i+3]])

        if len(int_read) != 1698:
            print("error length")
            print(file_name)
            print(read)

        feature.append(int_read)
    name = file_name.split(".fasta")[0]
    np.savetxt(f"int_val/{name}.csv", feature, delimiter=",", fmt='%d')


if __name__ == "__main__":
    Load_path = "stride50_val/"
    name_list = os.listdir(Load_path)
    for name in name_list:
        encode(name)
        # print(name + " finished")
