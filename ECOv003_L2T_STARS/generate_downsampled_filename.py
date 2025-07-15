from os import makedirs
from os.path import join, dirname
from dateutil import parser
from datetime import date

from typing import Union

def generate_downsampled_filename(directory: str, variable: str, date_UTC: Union[date, str], tile: str, cell_size: int) -> str:
    if isinstance(date_UTC, str):
        date_UTC = parser.parse(date_UTC).date()

    variable = str(variable)
    year = str(date_UTC.year)
    timestamp = date_UTC.strftime("%Y-%m-%d")
    tile = str(tile)
    cell_size = int(cell_size)
    filename = join(directory, year, timestamp, tile, f"STARS_{variable}_{tile}_{cell_size}m.tif")
    makedirs(dirname(filename), exist_ok=True)

    return filename
