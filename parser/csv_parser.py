from utils.normalize import normalize_column


def parse_csv_file(file_path: str):
    with open(file_path, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    header = lines[0].split(",")
    header = [normalize_column(h) for h in header]
    rows = []
    for line in lines[1:]:
        values = line.strip().split(",")
        row = dict(zip(header, values))
        rows.append(row)
    return rows
