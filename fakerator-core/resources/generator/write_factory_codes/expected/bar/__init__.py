import datetime
from typing import TypedDict

import fakerator as f


class BarSchemaRecord(TypedDict):
    bar: int


def bar_schema_record(
    *,
    bar: int | f.Unset = f.UNSET,
) -> BarSchemaRecord:
    return {
        "bar": f.Unset.unwrap_or_else(bar, lambda: f.gen_int(ge=0, le=100)),
    }
