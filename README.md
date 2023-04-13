# PhaGCN2_clean
The scripts were clean ver. of PhaGCN2, the database building ran only once. The database should download from PhaGCN2.

# Changes from [PhaGCN2](https://github.com/KennthShang/PhaGCN2.0)
- The python package scipy>=1.8+
- Simplify the scripts.
- The database was using `make_db/build_database.py` to build.
- The `make_db/split_contig.py` was isolated from `run_Speed_up.py`.
- The `run_Speed_up.py` was using `Split_files/` as input, the database should set in first use.
