from Bio import SeqIO
import re
import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--contigs', type=str, default='contigs.fa')
parser.add_argument('--len', type=int, default=5000)
args = parser.parse_args()


def check_folder(file_name):
    if not os.path.exists(file_name):
        _ = os.makedirs(file_name)
    else:
        print("folder {0} exist... cleaning dictionary".format(file_name))
        if os.listdir(file_name):
            try:
                _ = subprocess.check_call(
                    "rm -rf {0}".format(file_name), shell=True)
                _ = os.makedirs(file_name)
                print("Dictionary cleaned")
            except Exception:
                print("Cannot clean your folder... permission denied")
                exit(1)


def special_match(strg, search=re.compile(r'[^ACGT]').search):
    return not bool(search(strg))


file_id = 0
records = []
cnt = 0
for record in SeqIO.parse(args.contigs, 'fasta'):
    if cnt != 0 and cnt % 1000 == 0:
        SeqIO.write(
            records, f"Split_files/contig_{str(file_id)}.fasta", "fasta")
        records = []
        file_id += 1
        cnt = 0
    seq = str(record.seq)
    seq = seq.upper()
    if special_match(seq) and len(record.seq) > args.len:
        records.append(record)
        cnt += 1

check_folder("Split_files")
SeqIO.write(records, f"Split_files/contig_{str(file_id)}.fasta", "fasta")
file_id += 1
