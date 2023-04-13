import subprocess

try:
    make_diamond_cmd = 'diamond makedb --threads 128 --in database/ALL_protein.fasta -d database/database.dmnd'
    print("Creating Diamond database...")
    _ = subprocess.check_call(make_diamond_cmd, shell=True)

    diamond_cmd = 'diamond blastp --threads 128 --sensitive -d database/database.dmnd -q database/ALL_protein.fasta -o database/database.self-diamond.tab'
    print("Running Diamond...")
    _ = subprocess.check_call(diamond_cmd, shell=True)
    diamond_out_fp = "database/database.self-diamond.tab"
    database_abc_fp = "database/database.self-diamond.tab.abc"
    _ = subprocess.check_call("awk '$1!=$2 {{print $1,$2,$11}}' {0} > {1}".format(
        diamond_out_fp, database_abc_fp), shell=True)
except Exception:
    print("create database failed")
    exit(1)

def make_diamond_db(cpu: int=64):
    diamond_db_bp = "database/database.dmnd"
    aa_fp = "database/ALL_protein.fasta"

    make_diamond_cmd = ['diamond', 'makedb', '--threads', str(cpu), '--in', aa_fp, '-d', diamond_db_bp]
    print("Creating Diamond database...")
    res = subprocess.run(make_diamond_cmd, check=True, stdout=subprocess.PIPE)
    if res.returncode != 0:
        print('Error creating Diamond database')
        exit(1)
    return f'{diamond_db_bp}.dmnd'

_ = make_diamond_db()