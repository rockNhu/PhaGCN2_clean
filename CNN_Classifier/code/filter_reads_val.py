import os
from Bio import SeqIO


def filter_reads(pos, file_name):
    with open(f"filtered_val/{file_name}", 'w') as f_out:
        for record in SeqIO.parse(pos+file_name, "fasta"):
            read = str(record.seq)
            flag = next(
                (1 for nucl in read if nucl not in ['A', 'C', 'G', 'T']), 0)
            if flag == 0:
                SeqIO.write(record, f_out, "fasta")


if __name__ == "__main__":
    load_path = "split_long_reads_val/"

    name_list = os.listdir(load_path)
    for name in name_list:
        filter_reads(load_path, name)
