# chb04: verified from disk — 01–19, 21–43 (no chb04_20)
train_files = [
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_01.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_02.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_03.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_04.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_05.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_06.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_07.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_08.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_09.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_10.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_11.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_12.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_13.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_14.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_15.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_16.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_17.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_18.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_19.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_21.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_22.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_23.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_24.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_25.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_26.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_27.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_28.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_29.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_30.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_31.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_32.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_33.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_34.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_35.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_36.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_37.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_38.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_39.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_40.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_41.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_42.edf"},
    {"path": "chb-mit-scalp-eeg-database-1.0.0/chb04/chb04_43.edf"},
]

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        from build_train_list import main as build_main
        build_main()
    else:
        print("Usage: python train_files_list.py <chbNN>   e.g.  train_files_list.py chb05")
        print("Generates train_files from actual .edf files on disk for that subject.")
        print("(Import this module to use the chb04 train_files list above.)")
