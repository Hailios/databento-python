import datetime

import databento as db
from databento.common.enums import Schema


if __name__ == "__main__":
    db.log = "debug"  # optional debug logging

    # Can load from file path (if exists)
    ts_start = datetime.datetime.utcnow()
    data = db.from_file(path="my_data.csv", schema=Schema.MBO)  # -> BentoDiskIO

    print(data.to_df())
    print(datetime.datetime.utcnow() - ts_start)
