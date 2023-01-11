import datetime

import databento as db
from databento import Bento


if __name__ == "__main__":
    db.log = "debug"  # optional debug logging
    ts_start = datetime.datetime.utcnow()

    # Can load from file path (if exists)
    data = Bento.from_file(path="my_data.dbn")

    print(data.to_df())
    print(datetime.datetime.utcnow() - ts_start)
