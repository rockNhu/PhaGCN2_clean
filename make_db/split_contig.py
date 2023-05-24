from Bio import SeqIO
import re
import argparse
import subprocess
import os
# The arguments parser setting
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--contigs', type=str, default='contigs.fa')
parser.add_argument('--len', type=int, default=5000)
args = parser.parse_args()


def check_folder(file_name):
    '''If folder is existed, clean it, else make new folder'''
    if not os.path.exists(file_name):
        os.makedirs(file_name)
    else:
        print("folder {0} exist... cleaning dictionary".format(file_name))
        if os.listdir(file_name):
            try:
                subprocess.check_call(
                    "rm -rf {0}".format(file_name), shell=True)
                os.makedirs(file_name)
                print("Dictionary cleaned")
            except Exception:
                print("Cannot clean your folder... permission denied")
                exit(1)


def special_match(strg, search=re.compile(r'[^ACGT]').search):
    '''Check the sequence is not empty.'''
    return not bool(search(strg))

# Env create
check_folder("Split_files")
# Some container and counter
file_id = 0
records = []
cnt = 0
# Using Biopython to parse and output.
for record in SeqIO.parse(args.contigs, 'fasta'):
    # Each FASTA take 1000 contigs.
    if cnt != 0 and cnt % 1000 == 0:
        SeqIO.write(records, f"Split_files/contig_{file_id}.fasta", "fasta")
        records = []
        file_id += 1
        cnt = 0
    seq = str(record.seq)
    seq = seq.upper()
    # Check sequence is long enough.
    if special_match(seq) and len(record.seq) > args.len:
        records.append(record)
        cnt += 1

# Remained collection
SeqIO.write(records, f"Split_files/contig_{file_id}.fasta", "fasta")
