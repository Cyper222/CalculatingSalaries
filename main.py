import argparse
from parser.csv_parser import parse_csv_file
from report.payout import PayoutReport

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Paths to input CSV files")
    parser.add_argument("--report", required=True, help="Report type to generate")
    args = parser.parse_args()

    all_data = []
    for file in args.files:
        data = parse_csv_file(file)
        all_data.extend(data)

    if args.report == "payout":
        report = PayoutReport()
        print(report.generate(all_data))
    else:
        print(f"Unknown report type: {args.report}")

if __name__ == "__main__":
    main()
