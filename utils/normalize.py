def normalize_column(col: str) -> str:
    aliases = {
        "rate": "hourly_rate",
        "salary": "hourly_rate",
    }
    return aliases.get(col.strip(), col.strip())
